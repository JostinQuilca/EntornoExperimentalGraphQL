# -*- coding: utf-8 -*-
"""
CORRER TODO — un solo comando, de git pull hasta el Excel.
==========================================================
Pensado para la otra PC (proyecto ya clonado, solo hace falta un pull). Encadena:

  1) git pull de la rama del experimento (guardando cambios locales si los hay).
  2) preparar_entorno.py: verifica Docker/k6/Python, construye y siembra.
  3) experimento_completo.py: la corrida de 90 escenarios, reanudable.
  4) Al llegar a 90/90 exporta el Excel (Registro_Datos) automaticamente.

Esta hecho para aguantar los tropiezos de Docker que dieron problemas:
  - Si Docker no responde, espera a que arranque en vez de fallar.
  - Si la corrida se cae a mitad (Docker colgado, un up que no levanta), la
    relanza sola: como es reanudable, cada reintento continua donde se quedo.
  - Antes de cada intento baja los dos entornos para liberar el puerto 4000.
  - Evita que Windows suspenda la maquina mientras corre.
  - Un candado impide que se ejecuten dos copias a la vez (el fallo de origen).

Uso en la otra PC:
    python correr_todo.py                 # todo el proceso, de principio a fin
    python correr_todo.py --verificar     # solo revisa que todo este listo, no corre nada
    python correr_todo.py --reiniciar     # empieza campana nueva desde cero (archiva lo previo)
    python correr_todo.py --no-pull       # salta el git pull (si no hay internet)
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
import threading
import time
from datetime import datetime

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAMA = "experimento-computacional"
PY = sys.executable
LOCK = os.path.join(BASE_DIR, ".correr_todo.lock")
ESTADO = os.path.join(BASE_DIR, ".campania_estado.json")
MAX_INTENTOS = 6          # reintentos de la corrida ante caidas de Docker
ES_PREP_TIMEOUT = 3600    # tope para el paso de preparacion (build + seed)
STALL_MIN = 15            # minutos sin un reporte nuevo => se considera colgada
STALL_CHECK_SEG = 60      # cada cuanto revisa el vigilante si hubo avance

import uc_base
from experimento_completo import DISENO, REPLICAS, plan, ruta_reporte, fmt_dur

_t0 = time.time()


def log(msg, tipo="info"):
    marca = {"ok": "[OK] ", "err": "[X] ", "warn": "[!] ", "paso": "\n=> ", "hdr": ""}.get(tipo, "    ")
    t = time.strftime("%H:%M:%S")
    print(f"{t} {marca}{msg}", flush=True)


# ─────────────────────────────────────────────────────────────
# Antisuspension (mantiene la PC despierta SOLO mientras corre; no cambia
# ninguna configuracion guardada de Windows).
# ─────────────────────────────────────────────────────────────
def evitar_suspension(activar):
    if os.name != "nt":
        return
    try:
        import ctypes
        ES_CONTINUOUS = 0x80000000
        ES_SYSTEM_REQUIRED = 0x00000001
        flags = (ES_CONTINUOUS | ES_SYSTEM_REQUIRED) if activar else ES_CONTINUOUS
        ctypes.windll.kernel32.SetThreadExecutionState(flags)
    except Exception:
        pass


# ─────────────────────────────────────────────────────────────
# Candado: una sola instancia de este orquestador.
# ─────────────────────────────────────────────────────────────
def tomar_candado():
    if os.path.isfile(LOCK):
        try:
            info = json.load(open(LOCK, encoding="utf-8"))
            log(f"Ya hay una corrida en marcha (PID {info.get('pid')}, desde {info.get('inicio')}).", "err")
        except Exception:
            log("Existe un candado de otra corrida.", "err")
        log(f"Si estas seguro de que no hay ninguna, borra el archivo:\n      {LOCK}", "warn")
        return False
    json.dump({"pid": os.getpid(), "inicio": datetime.now().strftime("%d/%m %H:%M:%S")},
              open(LOCK, "w", encoding="utf-8"))
    return True


def soltar_candado():
    try:
        os.remove(LOCK)
    except OSError:
        pass


# ─────────────────────────────────────────────────────────────
# Utilidad para lanzar comandos mostrando su salida en vivo.
# ─────────────────────────────────────────────────────────────
def correr(cmd, cwd=BASE_DIR, prefijo="    ", timeout=None):
    # Sin esto, el proceso hijo bloquea su stdout al estar canalizado y su salida
    # no aparece en pantalla hasta que se llena el buffer: la ventana se ve muda
    # aunque por debajo este trabajando. PYTHONUNBUFFERED fuerza salida inmediata,
    # y se propaga a los subprocesos que este hijo lance (hereda el entorno).
    entorno = os.environ.copy()
    entorno["PYTHONUNBUFFERED"] = "1"
    try:
        p = subprocess.Popen(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                             text=True, encoding="utf-8", errors="replace", bufsize=1,
                             env=entorno)
    except FileNotFoundError:
        log(f"No se encontro el ejecutable: {cmd[0]}", "err")
        return 127
    ini = time.time()
    for linea in p.stdout:
        print(prefijo + linea.rstrip(), flush=True)
        if timeout and time.time() - ini > timeout:
            p.kill()
            log("Tiempo agotado; proceso terminado.", "err")
            return 1
    p.wait()
    return p.returncode


def _reporte_mas_nuevo(replicas):
    """Marca de tiempo del reporte mas reciente de toda la rejilla."""
    nuevo = 0.0
    for env_name in ("Vulnerable", "Protegido"):
        for uc in DISENO.values():
            for vus, nivel in uc["escenarios"]:
                r = ruta_reporte(env_name, uc, vus, nivel, replicas)
                try:
                    if os.path.isfile(r):
                        nuevo = max(nuevo, os.path.getmtime(r))
                except OSError:
                    pass
    return nuevo


def correr_vigilado(cmd, replicas, cwd=BASE_DIR, prefijo="    "):
    """Como correr(), pero con un vigilante que corta la corrida si deja de
    escribir reportes por STALL_MIN minutos. Un cuelgue de Docker o de k6 no
    dispara ningun timeout interno y congela todo en silencio; el vigilante lo
    detecta por la falta de avance, mata el arbol de procesos y deja que el bucle
    de reintentos reanude desde el ultimo escenario guardado."""
    entorno = os.environ.copy()
    entorno["PYTHONUNBUFFERED"] = "1"
    try:
        p = subprocess.Popen(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                             text=True, encoding="utf-8", errors="replace", bufsize=1, env=entorno)
    except FileNotFoundError:
        log(f"No se encontro el ejecutable: {cmd[0]}", "err")
        return 127

    parar = threading.Event()
    estado = {"colgada": False}

    def vigilar():
        base = _reporte_mas_nuevo(replicas)
        ultimo_avance = time.time()   # se cuenta desde ahora, no desde el reporte viejo
        while not parar.wait(STALL_CHECK_SEG):
            actual = _reporte_mas_nuevo(replicas)
            if actual > base:
                base = actual
                ultimo_avance = time.time()
            if time.time() - ultimo_avance > STALL_MIN * 60:
                estado["colgada"] = True
                log(f"Sin reportes nuevos en {STALL_MIN} min: la corrida se colgo. "
                    "Cortando para reanudar...", "warn")
                try:
                    if os.name == "nt":
                        subprocess.run(["taskkill", "/F", "/T", "/PID", str(p.pid)],
                                      capture_output=True)
                    else:
                        p.kill()
                except Exception:
                    pass
                return

    hilo = threading.Thread(target=vigilar, daemon=True)
    hilo.start()
    try:
        for linea in p.stdout:
            print(prefijo + linea.rstrip(), flush=True)
    except Exception:
        pass
    p.wait()
    parar.set()
    return -999 if estado["colgada"] else p.returncode


# ─────────────────────────────────────────────────────────────
# Paso 1: git pull robusto.
# ─────────────────────────────────────────────────────────────
def git_pull():
    log("Actualizando el codigo (git pull)...", "paso")
    if not os.path.isdir(os.path.join(BASE_DIR, ".git")):
        log("Esta carpeta no es un repositorio git. Se continua con el codigo actual.", "warn")
        return
    subprocess.run(["git", "fetch", "origin", RAMA], cwd=BASE_DIR, capture_output=True, text=True)

    sucio = subprocess.run(["git", "status", "--porcelain"], cwd=BASE_DIR,
                          capture_output=True, text=True).stdout
    # Solo cuentan los cambios en archivos versionados (los ?? son datos, se quedan).
    modificados = [l for l in sucio.splitlines() if l and not l.startswith("??")]
    if modificados:
        etiqueta = f"auto-correr_todo {datetime.now():%Y%m%d_%H%M%S}"
        log(f"Hay cambios locales en {len(modificados)} archivo(s); se guardan en un stash.", "warn")
        r = subprocess.run(["git", "stash", "push", "-m", etiqueta], cwd=BASE_DIR,
                          capture_output=True, text=True)
        if r.returncode == 0:
            log(f"Guardados con: git stash list  (etiqueta '{etiqueta}')", "ok")

    subprocess.run(["git", "checkout", RAMA], cwd=BASE_DIR, capture_output=True, text=True)
    r = subprocess.run(["git", "pull", "--ff-only", "origin", RAMA], cwd=BASE_DIR,
                      capture_output=True, text=True)
    if r.returncode == 0:
        log("Codigo actualizado a la ultima version.", "ok")
    else:
        log("No se pudo hacer fast-forward; se sigue con el codigo actual.", "warn")
        if r.stderr.strip():
            print("    " + r.stderr.strip())


# ─────────────────────────────────────────────────────────────
# Docker listo (espera a que responda en vez de fallar).
# ─────────────────────────────────────────────────────────────
def docker_listo(espera=180):
    fin = time.time() + espera
    aviso = False
    while time.time() < fin:
        r = subprocess.run(["docker", "info"], capture_output=True, text=True)
        if r.returncode == 0:
            return True
        if not aviso:
            log("Docker no responde. Abre Docker Desktop y espera a que termine de iniciar...", "warn")
            aviso = True
        time.sleep(5)
    return False


def bajar_entornos():
    """Baja los dos entornos para dejar libre el puerto 4000 antes de empezar."""
    try:
        from preparar_entorno import compose_cmd
        c = compose_cmd()
    except Exception:
        c = ["docker-compose"]
    for nombre, ruta in uc_base.ENVS.items():
        if os.path.isdir(ruta):
            try:
                subprocess.run(c + ["down", "--remove-orphans"], cwd=ruta,
                              capture_output=True, timeout=120)
            except Exception:
                pass  # si docker-compose se cuelga aqui, no debe tumbar la corrida


# ─────────────────────────────────────────────────────────────
# Paso 2: preparar entorno (verifica, construye, siembra).
# ─────────────────────────────────────────────────────────────
def preparar():
    log("Preparando entornos (verificar + construir + sembrar)...", "paso")
    log("La primera vez tarda: construye imagenes y siembra ~227k datos.", "info")
    rc = correr([PY, "preparar_entorno.py", "--cli"], timeout=ES_PREP_TIMEOUT)
    if rc == 0:
        log("Entornos listos y verificados.", "ok")
        return True
    log("La preparacion no termino bien. Revisa los [X] de arriba "
        "(Docker parado, k6 sin instalar, etc.).", "err")
    return False


# ─────────────────────────────────────────────────────────────
# Campana: nueva vs reanudar.
# ─────────────────────────────────────────────────────────────
def es_campania_nueva():
    return not os.path.isfile(ESTADO)


def archivar_reportes_previos(replicas):
    """Aparta (no borra) reportes previos de esta rejilla, para partir limpio."""
    movidos = 0
    sello = datetime.now().strftime("%Y%m%d_%H%M%S")
    for env_name in ("Vulnerable", "Protegido"):
        for uc_id, uc in DISENO.items():
            for vus, nivel in uc["escenarios"]:
                p = ruta_reporte(env_name, uc, vus, nivel, replicas)
                if os.path.isfile(p):
                    destino = os.path.join(os.path.dirname(p), f"_respaldo_{sello}")
                    os.makedirs(destino, exist_ok=True)
                    shutil.move(p, os.path.join(destino, os.path.basename(p)))
                    movidos += 1
    return movidos


def marcar_inicio(replicas):
    json.dump({"inicio": datetime.now().isoformat(), "replicas": replicas},
              open(ESTADO, "w", encoding="utf-8"))


def marcar_fin():
    try:
        os.replace(ESTADO, os.path.join(BASE_DIR, ".campania_completada.json"))
    except OSError:
        pass


# ─────────────────────────────────────────────────────────────
# Exportar Excel.
# ─────────────────────────────────────────────────────────────
def exportar_excel(replicas):
    from generar_registro_datos import escribir, recolectar
    filas, faltantes = recolectar(replicas)
    salida = os.path.join(BASE_DIR, f"Registro_Datos_{datetime.now():%Y%m%d_%H%M%S}.xlsx")
    escribir(filas, salida, replicas)

    invalidas = sum(1 for f in filas if f[28])
    log(f"Excel generado: {os.path.basename(salida)}", "ok")
    log(f"Filas: {len(filas)}  |  replicas sin respuesta: {invalidas}", "info")
    if invalidas:
        log("Hay replicas marcadas en la columna Observaciones; revisalas.", "warn")
    return salida


# ─────────────────────────────────────────────────────────────
# Orquestacion.
# ─────────────────────────────────────────────────────────────
def mostrar_plan(replicas, solo):
    pend, hechos = plan(["Vulnerable", "Protegido"], solo, replicas)
    total = len(pend) + len(hechos)
    log(f"Escenarios: {total}  ({len(hechos)} ya en disco, {len(pend)} por ejecutar)", "hdr")
    est = len(pend) * replicas * 124
    log(f"Estimado de lo pendiente: {fmt_dur(est)} (~{est/3600:.1f} h)", "hdr")
    return pend


def main():
    ap = argparse.ArgumentParser(description="Corre todo el experimento de principio a fin")
    ap.add_argument("--verificar", action="store_true", help="revisa que todo este listo y muestra el plan, sin correr")
    ap.add_argument("--reiniciar", action="store_true", help="campana nueva desde cero (archiva los reportes previos)")
    ap.add_argument("--no-pull", action="store_true", help="no hacer git pull")
    ap.add_argument("--no-preparar", action="store_true", help="saltar el paso de construir/sembrar")
    ap.add_argument("--solo", default=None, metavar="UC-0N", help="un unico caso de uso")
    ap.add_argument("--replicas", type=int, default=REPLICAS)
    args = ap.parse_args()

    print("=" * 72)
    print("  CORRER TODO — experimento GraphQL + ISO 27001")
    print("=" * 72)
    print("  Mientras corre:")
    print("    - NO abras el panel de control.")
    print("    - Deja la PC enchufada (la suspension se desactiva sola aqui).")
    print("    - Si se corta, vuelve a ejecutar este mismo comando: continua donde iba.")
    print("=" * 72)

    # --- Modo verificacion: no toca nada ---
    if args.verificar:
        log("VERIFICACION (no se corre nada)", "paso")
        if docker_listo(espera=15):
            log("Docker responde.", "ok")
        else:
            log("Docker no responde (abre Docker Desktop).", "err")
        try:
            from preparar_entorno import check_prereqs
            check_prereqs(lambda m, t=None: print("   " + m))
        except Exception as e:
            log(f"No se pudo verificar prerequisitos: {e}", "warn")
        mostrar_plan(args.replicas, args.solo)
        return

    if not tomar_candado():
        sys.exit(1)

    evitar_suspension(True)
    try:
        if not args.no_pull:
            git_pull()

        if not docker_listo():
            log("Docker sigue sin responder. Abre Docker Desktop y vuelve a ejecutar.", "err")
            sys.exit(1)

        if not args.no_preparar:
            if not preparar():
                sys.exit(1)

        # Campana nueva o reanudacion
        if args.reiniciar or es_campania_nueva():
            n = archivar_reportes_previos(args.replicas)
            log(f"Campana nueva: {n} reporte(s) previo(s) apartado(s) a carpetas _respaldo_*.", "paso")
            marcar_inicio(args.replicas)
        else:
            log("Reanudando la campana en curso (se salta lo ya hecho).", "paso")

        # Corrida con reintentos ante caidas de Docker
        entornos = ["Vulnerable", "Protegido"]
        intentos = 0
        sin_progreso = 0
        while True:
            pend, _ = plan(entornos, args.solo, args.replicas)
            if not pend:
                break
            if intentos >= MAX_INTENTOS:
                log(f"Se alcanzo el maximo de {MAX_INTENTOS} intentos.", "warn")
                break
            if sin_progreso >= 2:
                log("Dos intentos seguidos sin avanzar; algo falla de fondo. Se detiene.", "err")
                break

            intentos += 1
            log(f"Intento {intentos}/{MAX_INTENTOS} — quedan {len(pend)} escenarios.", "paso")
            if not docker_listo():
                log("Docker no responde antes del intento; esperando mas...", "warn")
                continue
            bajar_entornos()

            cmd = [PY, "experimento_completo.py", "--replicas", str(args.replicas)]
            if args.solo:
                cmd += ["--solo", args.solo]
            rc = correr_vigilado(cmd, args.replicas)
            if rc == -999:
                log("Corrida colgada cortada por el vigilante; se reanudara en el siguiente intento.", "warn")

            despues, _ = plan(entornos, args.solo, args.replicas)
            if len(despues) >= len(pend):
                sin_progreso += 1
                log(f"Intento sin avanzar (rc={rc}). Se reintentara tras revisar Docker.", "warn")
            else:
                sin_progreso = 0

        # Cierre
        pend, hechos = plan(entornos, args.solo, args.replicas)
        total = len(pend) + len(hechos)
        print("\n" + "=" * 72)
        if not pend:
            log(f"CORRIDA COMPLETA: {len(hechos)}/{total} escenarios. Exportando Excel...", "ok")
            exportar_excel(args.replicas)
            marcar_fin()
            log(f"Listo. Tiempo total: {fmt_dur(time.time() - _t0)}", "ok")
        else:
            log(f"Faltan {len(pend)} de {total} escenarios. NO se exporta todavia.", "warn")
            log("Vuelve a ejecutar 'python correr_todo.py' para reanudar y completar.", "warn")
            for env_n, uc_id, uc, vus, nivel in pend[:15]:
                print(f"      - {env_n} | {uc_id} | VUs={vus} Nivel={nivel}")
            if len(pend) > 15:
                print(f"      ... y {len(pend) - 15} mas")
        print("=" * 72)

    finally:
        evitar_suspension(False)
        soltar_candado()


if __name__ == "__main__":
    main()
