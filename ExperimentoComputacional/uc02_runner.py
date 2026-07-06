import os, sys, time, subprocess
from datetime import datetime
import generate_reports

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENVS = ["E-commerce", "E-commerce-controles"]

VUS_LIST = [1, 2, 3, 5, 8]
RUNS = 3

def restart_env_full(env_path):
    print(f"\n[+] Full Restart de {env_path}...")
    subprocess.run(["docker-compose", "down", "--remove-orphans"], cwd=os.path.join(BASE_DIR, "E-commerce"), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=60)
    subprocess.run(["docker-compose", "down", "--remove-orphans"], cwd=os.path.join(BASE_DIR, "E-commerce-controles"), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=60)
    for _retry in range(3):
        try:
            subprocess.run(["docker-compose", "down", "--remove-orphans"], cwd=env_path, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=60)
            # Nuke ALL containers before EVERY attempt (catches partially-created leftovers)
            subprocess.run(["docker", "rm", "-f", "api-gateway", "mongo-db", "postgres-db", "ms-usuarios", "ms-ordenes", "ms-catalogo", "ms-resenas", "mongo-init"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            time.sleep(5)
            result = subprocess.run(["docker-compose", "up", "-d"], cwd=env_path, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, timeout=180)
            if result.returncode == 0:
                break
            print(f"[WARN] docker-compose up falló (intento {_retry+1}/3). Reintentando...")
            subprocess.run(["docker-compose", "down", "--remove-orphans"], cwd=env_path, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=60)
        except subprocess.TimeoutExpired:
            print("[WARN] docker-compose operación colgada. Forzando continue.")
        time.sleep(5)
    print("[+] Entorno listo.")

def run_uc02():
    uc_name = "UC-02_Profundidad_Moderada"
    uc_script = "UC02_profundidad_moderada/uc02_profundidad_nivel.js"
    levels = list(range(1, 8))
    
    for level in levels:
        full_data = {"Vulnerable": {}, "Protegido": {}}
        avg_data = {"Vulnerable": {}, "Protegido": {}}
        
        print(f"\n\n{'='*60}\n=== PROCESANDO NIVEL {level} ===\n{'='*60}")
        
        for env in ENVS:
            env_path = os.path.join(BASE_DIR, env)
            env_key = "Vulnerable" if "controles" not in env else "Protegido"
            
            print(f"\n---> [{env_key}] Iniciando entorno...")
            restart_env_full(env_path)
            run_script = os.path.join(env_path, "load_tests", "run_multiple_experiments.py")
            
            for vus in VUS_LIST:
                print(f"\n    [>] Nivel {level} | {env_key} | VUs: {vus}")
                
                cmd = [sys.executable, run_script, "--test-script", uc_script, "--vus", str(vus), "--runs", str(RUNS)]
                env_vars = os.environ.copy()
                env_vars["LEVEL"] = str(level)
                    
                p = subprocess.Popen(cmd, cwd=env_path, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, env=env_vars)
                for line in p.stdout:
                    print(line.rstrip())
                p.wait()
                
                # Cargar el markdown recién generado
                md_path = os.path.join(env_path, "load_tests", "UC02_profundidad_moderada", "resultados", f"reporte_consolidado_{RUNS}runs_vus{vus}_nivel{level}.md")
                if os.path.exists(md_path):
                    res = generate_reports.parse_md_full_result(md_path)
                    full_data[env_key][vus] = res
                    avg_data[env_key][vus] = res.get("avg", {})
                else:
                    print(f"[ERROR] No se genero el archivo {md_path}")
        
        # Una vez completado ambos entornos para este nivel, generar reportes
        print(f"\n[+] Generando reportes Excel y Graficos para el NIVEL {level}...")
        
        import matplotlib.pyplot as plt
        
        out_excel = os.path.join(generate_reports.PRUEBAS_DIR, f"{uc_name}_Nivel_{level}_Comparativa.xlsx")
        generate_reports.export_to_excel(uc_name, level, full_data, avg_data, VUS_LIST, out_excel)
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        fig.suptitle(f"{uc_name} - Nivel {level}", fontsize=14, fontweight="bold")
        
        vuln_p = [avg_data["Vulnerable"].get(v, {}).get("peticiones", 0) for v in VUS_LIST]
        prot_p = [avg_data["Protegido"].get(v, {}).get("peticiones", 0) for v in VUS_LIST]
        vuln_l = [avg_data["Vulnerable"].get(v, {}).get("latencia", 0) for v in VUS_LIST]
        prot_l = [avg_data["Protegido"].get(v, {}).get("latencia", 0) for v in VUS_LIST]
        
        x = range(len(VUS_LIST))
        ax1.plot(x, vuln_p, marker='o', color='#E74C3C', label='Vulnerable')
        ax1.plot(x, prot_p, marker='s', color='#2ECC71', label='Protegido')
        ax1.set_xticks(x); ax1.set_xticklabels(VUS_LIST)
        ax1.set_title("Throughput (Peticiones/s)"); ax1.legend()
        
        ax2.plot(x, vuln_l, marker='o', color='#E74C3C', label='Vulnerable')
        ax2.plot(x, prot_l, marker='s', color='#2ECC71', label='Protegido')
        ax2.set_xticks(x); ax2.set_xticklabels(VUS_LIST)
        ax2.set_title("Latencia (ms)"); ax2.legend()
        
        plt.tight_layout()
        out_png = os.path.join(generate_reports.PRUEBAS_DIR, f"{uc_name}_Nivel_{level}_Comparativa_Grafico.png")
        fig.savefig(out_png)
        plt.close(fig)
        
        print(f"[EXITO] Nivel {level} finalizado y exportado en carpeta pruebas.")

if __name__ == "__main__":
    start_time = datetime.now()
    try:
        run_uc02()
    except Exception as e:
        print(f"ERROR: {e}")
    finally:
        end_time = datetime.now()
        print(f"[{end_time}] EJECUCION UC02 FINALIZADA")
