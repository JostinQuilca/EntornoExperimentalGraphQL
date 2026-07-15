# -*- coding: utf-8 -*-
"""
Preparación del Entorno — Bootstrap para una máquina NUEVA.
==========================================================
Deja lista una PC desde cero para reproducir el experimento GraphQL + ISO 27001:

  0) Verifica prerequisitos (Docker, Compose, k6, dependencias Python).
  1) Construye las imágenes Docker de los dos entornos.
  2) Siembra los datos (~227 000 registros) en ambos entornos  [idempotente].
  3) Verifica que cada entorno responda con datos reales.

Es idempotente: si algo ya está hecho, lo detecta y lo salta (marcadores .seeded_ok).
Uso:
    python preparar_entorno.py            # interfaz gráfica
    python preparar_entorno.py --cli      # modo consola (todo el pipeline)
    python preparar_entorno.py --cli --force-seed   # re-sembrar aunque exista marcador
"""
import os, sys, subprocess, threading, queue, time, json, urllib.request, urllib.error

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENVS = [
    ("Vulnerable", os.path.join(BASE_DIR, "E-commerce"),           "#f85149"),
    ("Protegido",  os.path.join(BASE_DIR, "E-commerce-controles"), "#3fb950"),
]
GATEWAY_URL = "http://localhost:4000/graphql"
PY = sys.executable
NO_WINDOW = 0x08000000 if os.name == "nt" else 0   # evita ventanas de consola en Windows

# ─────────────────────────────────────────────────────────────
#  Lógica de setup (sin GUI — reutilizable y testeable por consola)
# ─────────────────────────────────────────────────────────────
_COMPOSE = None
def compose_cmd():
    """Detecta 'docker compose' (v2) o 'docker-compose' (v1). Cachea el resultado."""
    global _COMPOSE
    if _COMPOSE is not None:
        return _COMPOSE
    for cand in (["docker", "compose"], ["docker-compose"]):
        try:
            r = subprocess.run(cand + ["version"], capture_output=True, text=True,
                               timeout=20, creationflags=NO_WINDOW)
            if r.returncode == 0:
                _COMPOSE = cand
                return cand
        except Exception:
            continue
    _COMPOSE = ["docker-compose"]
    return _COMPOSE


def run_stream(cmd, cwd, log, env=None, timeout=None):
    """Ejecuta un comando y envía su salida línea a línea a log(). Devuelve returncode."""
    log(f"$ {' '.join(cmd)}", "cmd")
    try:
        p = subprocess.Popen(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                             text=True, encoding="utf-8", errors="replace", bufsize=1,
                             env=env, creationflags=NO_WINDOW)
    except FileNotFoundError:
        log(f"  [!] No se encontró el ejecutable: {cmd[0]}", "err")
        return 127
    start = time.time()
    for line in p.stdout:
        log("  " + line.rstrip(), "out")
        if timeout and time.time() - start > timeout:
            p.kill(); log("  [!] Tiempo agotado.", "err"); return 1
    p.wait()
    return p.returncode


# ── Genera los .env que docker-compose necesita (no se versionan) ──
_PROJECTS = {"E-commerce": "exp-vulnerable", "E-commerce-controles": "exp-protegido"}
def ensure_env_files(log):
    for _, path, _ in ENVS:
        base = os.path.basename(path)
        proj = _PROJECTS.get(base)
        envf = os.path.join(path, ".env")
        if proj and not os.path.isfile(envf):
            with open(envf, "w", encoding="utf-8") as f:
                f.write("# Generado por preparar_entorno.py (aislamiento de red/volúmenes)\n")
                f.write(f"COMPOSE_PROJECT_NAME={proj}\n")
            log(f"  [OK] Generado {base}/.env (COMPOSE_PROJECT_NAME={proj})", "ok")
    return True


# ── Paso 0: prerequisitos ────────────────────────────────────
def check_prereqs(log):
    ok = True
    # Docker corriendo
    try:
        r = subprocess.run(["docker", "info"], capture_output=True, text=True,
                           timeout=25, creationflags=NO_WINDOW)
        if r.returncode == 0:
            log("  [OK] Docker está corriendo.", "ok")
        else:
            log("  [X] Docker NO está corriendo. Abre Docker Desktop y espera a que inicie.", "err"); ok = False
    except Exception:
        log("  [X] Docker no está instalado o no responde. Instala Docker Desktop.", "err"); ok = False
    # Compose
    c = compose_cmd()
    try:
        r = subprocess.run(c + ["version"], capture_output=True, text=True, timeout=20, creationflags=NO_WINDOW)
        log(f"  [OK] Docker Compose disponible ({' '.join(c)}).", "ok") if r.returncode == 0 else None
        if r.returncode != 0:
            log("  [X] Docker Compose no disponible.", "err"); ok = False
    except Exception:
        log("  [X] Docker Compose no disponible.", "err"); ok = False
    # k6
    try:
        r = subprocess.run(["k6", "version"], capture_output=True, text=True, timeout=20, creationflags=NO_WINDOW)
        if r.returncode == 0:
            log(f"  [OK] k6 instalado: {r.stdout.strip().splitlines()[0]}", "ok")
        else:
            log("  [X] k6 no responde. Instálalo desde https://k6.io/docs/get-started/installation/", "err"); ok = False
    except Exception:
        log("  [X] k6 no está en el PATH. Instálalo (https://k6.io).", "err"); ok = False
    # Dependencias Python
    faltan = [m for m in ("openpyxl", "matplotlib", "numpy", "scipy") if _missing(m)]
    if faltan:
        log(f"  [X] Faltan paquetes Python: {', '.join(faltan)}  ->  pip install -r requirements.txt", "err"); ok = False
    else:
        log("  [OK] Dependencias Python presentes (openpyxl, matplotlib, numpy, scipy).", "ok")
    log(("  Prerequisitos COMPLETOS." if ok else "  Faltan prerequisitos (revisa lo marcado con [X])."),
        "hdr" if ok else "err")
    return ok

def _missing(mod):
    try:
        __import__(mod); return False
    except Exception:
        return True


# ── Paso 1: construir imágenes ───────────────────────────────
def build_all(log):
    ensure_env_files(log)
    c = compose_cmd(); ok = True
    for name, path, _ in ENVS:
        if not os.path.isdir(path):
            log(f"  [X] No existe el directorio de {name}: {path}", "err"); ok = False; continue
        log(f"  Construyendo imágenes de {name}...", "hdr")
        rc = run_stream(c + ["build"], cwd=path, log=log)
        if rc == 0:
            log(f"  [OK] Imágenes de {name} construidas.", "ok")
        else:
            log(f"  [X] Falló la construcción de {name} (código {rc}).", "err"); ok = False
    return ok


# ── Paso 2: sembrar datos (idempotente) ──────────────────────
def is_seeded(path):
    return os.path.isfile(os.path.join(path, ".seeded_ok"))

def seed_all(log, force=False):
    ensure_env_files(log)
    pendientes = [n for n, p, _ in ENVS if force or not is_seeded(p)]
    if not pendientes:
        log("  Ambos entornos ya estaban sembrados (marcador .seeded_ok). Se omite la siembra.", "ok")
        return True
    log(f"  Sembrando datos (~227 000 registros). Esto puede tardar bastante. Entornos: {', '.join(pendientes)}", "hdr")
    seeder = os.path.join(BASE_DIR, "prepare_mock_data.py")
    if not os.path.isfile(seeder):
        log(f"  [X] No se encontró el sembrador: {seeder}", "err"); return False
    rc = run_stream([PY, seeder], cwd=BASE_DIR, log=log)
    if rc != 0:
        log(f"  [X] La siembra terminó con código {rc}. Revisa el log de arriba.", "err"); return False
    # marcar como sembrados
    for name, path, _ in ENVS:
        try:
            with open(os.path.join(path, ".seeded_ok"), "w", encoding="utf-8") as f:
                f.write(time.strftime("%Y-%m-%d %H:%M:%S"))
        except Exception:
            pass
    log("  [OK] Siembra completada y marcada.", "ok")
    return True


# ── Paso 3: verificar que respondan con datos ────────────────
def _graphql(query):
    """Devuelve (codigo_http, respuesta_json). Un 400 de GraphQL trae el error en el cuerpo,
    así que hay que leerlo en vez de tratarlo como 'no respondió'."""
    data = json.dumps({"query": query}).encode()
    req = urllib.request.Request(GATEWAY_URL, data=data, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            return r.status, json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        try:
            return e.code, json.loads(body)
        except Exception:
            return e.code, {"raw": body[:200]}

def verify_all(log):
    ensure_env_files(log)
    c = compose_cmd(); ok = True
    for name, path, _ in ENVS:
        log(f"  Verificando {name}...", "hdr")
        # bajar los demás para liberar el puerto 4000
        for _, p2, _ in ENVS:
            subprocess.run(c + ["down", "--remove-orphans"], cwd=p2, capture_output=True,
                           timeout=90, creationflags=NO_WINDOW)
        rc = run_stream(c + ["up", "-d", "--wait", "--wait-timeout", "240"], cwd=path, log=log)
        if rc != 0:
            log(f"  [X] {name} no levantó correctamente.", "err"); ok = False; continue
        time.sleep(8)
        try:
            # Consulta ligera y válida en ambos entornos: solo 10 categorías.
            code, res = _graphql("query { listarCategorias { id } }")
            items = (res.get("data") or {}).get("listarCategorias")
            if items:
                log(f"  [OK] {name} responde con datos reales ({len(items)} categorías).", "ok")
            elif res.get("errors"):
                msg = (res["errors"][0].get("message") or "")[:130]
                log(f"  [X] {name} respondió (HTTP {code}) pero con error de GraphQL: {msg}", "err"); ok = False
            elif items == []:
                log(f"  [~] {name} responde pero la base está vacía. Falta sembrar (Paso 2).", "warn")
            else:
                log(f"  [~] {name} respondió HTTP {code} sin datos: {str(res)[:120]}", "warn")
        except Exception as e:
            log(f"  [X] {name} no respondió en {GATEWAY_URL}: {e}", "err"); ok = False
        subprocess.run(c + ["down", "--remove-orphans"], cwd=path, capture_output=True,
                       timeout=90, creationflags=NO_WINDOW)
    return ok


def run_all(log, force_seed=False):
    log("========== PREPARACIÓN DE LA MÁQUINA (COMPU NUEVA) ==========", "hdr")
    if not check_prereqs(log):
        log(">> Corrige los prerequisitos y vuelve a intentar.", "err"); return False
    if not build_all(log):    return False
    if not seed_all(log, force=force_seed): return False
    if not verify_all(log):   return False
    log("========== ¡LISTO! El entorno quedó preparado. ==========", "hdr")
    log(">> Ahora puedes abrir el Panel de Ataques (panel_control.py) y correr los UC-01 a UC-05.", "ok")
    return True


# ─────────────────────────────────────────────────────────────
#  Interfaz gráfica (Tkinter) — tema oscuro igual que el panel
# ─────────────────────────────────────────────────────────────
def launch_gui():
    import tkinter as tk
    from tkinter import scrolledtext
    BG, BG2, BG3, BORD, FG, MUTED = "#0d1117", "#161b22", "#21262d", "#30363d", "#c9d1d9", "#8b949e"
    ACC, GREEN, RED, ORG, BLUE = "#6e40c9", "#3fb950", "#f85149", "#d29922", "#58a6ff"
    TAGS = {"ok": GREEN, "err": RED, "warn": ORG, "hdr": BLUE, "cmd": ACC, "out": FG, "info": MUTED}
    UI = ("Segoe UI", 10); UI_B = ("Segoe UI", 10, "bold")

    root = tk.Tk()
    root.title("Preparación del Entorno — Experimento GraphQL / ISO 27001")
    root.geometry("1080x760"); root.minsize(900, 620); root.configure(bg=BG)
    q = queue.Queue(); running = {"on": False}

    def log(text, tag="out"):
        q.put((text, tag))
    def drain():
        try:
            while True:
                text, tag = q.get_nowait()
                logw.config(state="normal")
                logw.insert("end", text + "\n", tag)
                logw.see("end"); logw.config(state="disabled")
        except queue.Empty:
            pass
        root.after(80, drain)

    def in_thread(fn):
        if running["on"]:
            return
        def wrap():
            running["on"] = True
            _set_busy(True)
            try:
                fn()
            except Exception as e:
                log(f"  [!] Error inesperado: {e}", "err")
            finally:
                running["on"] = False
                _set_busy(False)
        threading.Thread(target=wrap, daemon=True).start()

    def _set_busy(b):
        st = "disabled" if b else "normal"
        for btn in botones: btn.config(state=st)
        status.config(text=("● Trabajando..." if b else "● Listo"), fg=(ORG if b else GREEN))

    # Topbar
    top = tk.Frame(root, bg=BG2, height=52); top.pack(fill="x"); top.pack_propagate(False)
    tk.Label(top, text="  ⬡  Preparación del Entorno", bg=BG2, fg=FG, font=("Segoe UI", 13, "bold")).pack(side="left", padx=10)
    status = tk.Label(top, text="● Listo", bg=BG2, fg=GREEN, font=UI); status.pack(side="right", padx=16)
    tk.Frame(root, bg=BORD, height=1).pack(fill="x")

    body = tk.Frame(root, bg=BG); body.pack(fill="both", expand=True)
    left = tk.Frame(body, bg=BG, width=340); left.pack(side="left", fill="y"); left.pack_propagate(False)

    tk.Label(left, text="Para una máquina NUEVA, corre los pasos en orden\n(o pulsa «Preparar TODO»).",
             bg=BG, fg=MUTED, font=UI, justify="left", wraplength=310).pack(anchor="w", padx=16, pady=(14, 8))

    botones = []
    def add_btn(text, color, cmd, big=False):
        b = tk.Button(left, text=text, bg=color, fg="#fff", font=("Segoe UI", 11, "bold") if big else UI_B,
                      relief="flat", bd=0, cursor="hand2", activebackground=color,
                      command=cmd, pady=(12 if big else 8))
        b.pack(fill="x", padx=16, pady=(10 if big else 5))
        botones.append(b); return b

    add_btn("⚡  Preparar TODO (compu nueva)", GREEN, lambda: in_thread(lambda: run_all(log, force_seed=force.get())), big=True)
    tk.Frame(left, bg=BORD, height=1).pack(fill="x", padx=16, pady=8)
    add_btn("0 · Verificar prerequisitos", BG3, lambda: in_thread(lambda: check_prereqs(log)))
    add_btn("1 · Construir imágenes Docker", BG3, lambda: in_thread(lambda: build_all(log)))
    add_btn("2 · Sembrar datos (~227k)", BG3, lambda: in_thread(lambda: seed_all(log, force=force.get())))
    add_btn("3 · Verificar que responda", BG3, lambda: in_thread(lambda: verify_all(log)))
    force = tk.BooleanVar(value=False)
    tk.Checkbutton(left, text="Forzar re-siembra (borra datos)", variable=force, bg=BG, fg=MUTED,
                   selectcolor=BG2, activebackground=BG, font=UI, anchor="w").pack(fill="x", padx=16, pady=(6, 0))
    tk.Frame(left, bg=BORD, height=1).pack(fill="x", padx=16, pady=10)

    def abrir_panel():
        panel = os.path.join(BASE_DIR, "panel_control.py")
        if os.path.isfile(panel):
            subprocess.Popen([PY, panel], cwd=BASE_DIR)
            log("  Abriendo panel_control.py ...", "info")
        else:
            log("  [X] No se encontró panel_control.py", "err")
    add_btn("▶  Abrir Panel de Ataques", ACC, abrir_panel)

    # Log
    rightf = tk.Frame(body, bg=BG); rightf.pack(side="left", fill="both", expand=True, padx=(0, 8), pady=8)
    tk.Label(rightf, text="Registro de ejecución", bg=BG, fg=MUTED, font=UI_B).pack(anchor="w", padx=6, pady=(4, 2))
    logw = scrolledtext.ScrolledText(rightf, bg="#010409", fg=FG, insertbackground=FG,
                                     font=("Cascadia Mono", 9), relief="flat", wrap="word", state="disabled")
    logw.pack(fill="both", expand=True)
    for tag, col in TAGS.items():
        logw.tag_config(tag, foreground=col)
    log("Bienvenido. Si esta PC es nueva, pulsa «Preparar TODO (compu nueva)».", "hdr")
    log("Requiere Docker Desktop abierto, k6 en el PATH y las dependencias de requirements.txt.", "info")

    drain()
    root.mainloop()


# ─────────────────────────────────────────────────────────────
def main():
    if "--cli" in sys.argv:
        force = "--force-seed" in sys.argv
        def clog(text, tag="out"):
            print(text)
        ok = run_all(clog, force_seed=force)
        sys.exit(0 if ok else 1)
    else:
        launch_gui()

if __name__ == "__main__":
    main()
