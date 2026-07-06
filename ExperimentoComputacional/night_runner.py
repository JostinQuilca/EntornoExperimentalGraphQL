import os, sys, time, subprocess
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENVS = [
    "E-commerce",           # Vulnerable
    "E-commerce-controles"  # Protegido
]

# Casos de uso
CASES = [
    {
        "name": "UC-01",
        "script": "UC01_introspeccion/uc01_stress_introspeccion.js",
        "levels": [None]
    },
    {
        "name": "UC-02",
        "script": "UC02_profundidad_moderada/uc02_profundidad_nivel.js",
        "levels": list(range(1, 8))
    },
    {
        "name": "UC-03",
        "script": "UC03_recursividad_circular/uc03_recursividad_nivel.js",
        "levels": list(range(1, 6))
    },
    {
        "name": "UC-04",
        "script": "UC04_abuso_alias/uc04_alias_nivel.js",
        "levels": list(range(1, 10))
    },
    {
        "name": "UC-05",
        "script": "UC05_bomba_fragmentos/uc05_fragmentos_nivel.js",
        "levels": list(range(1, 6))
    }
]

VUS_LIST = [1, 2, 3, 5, 8]
RUNS = 3

def restart_env_full(env_path):
    print(f"\n[+] Full Restart de {env_path}...")
    subprocess.run(["docker-compose", "down", "-v"], cwd=env_path, capture_output=True, shell=True)
    subprocess.run(["docker-compose", "up", "-d", "--build"], cwd=env_path, capture_output=True, shell=True)
    time.sleep(25) # Esperar a que inicie
    print("[+] Entorno listo.")

def run_tests():
    for env in ENVS:
        env_path = os.path.join(BASE_DIR, env)
        print(f"\n\n{'='*60}\nINICIANDO ENTORNO: {env}\n{'='*60}")
        restart_env_full(env_path)
        
        run_script = os.path.join(env_path, "load_tests", "run_multiple_experiments.py")
        
        for case in CASES:
            for level in case["levels"]:
                for vus in VUS_LIST:
                    print(f"\n---> [{env}] Caso: {case['name']} | Nivel: {level} | VUs: {vus} | Runs: {RUNS}")
                    
                    # Restart rapido entre configuraciones (K6 script handlea el restart de replicas)
                    subprocess.run(["docker-compose", "restart"], cwd=env_path, capture_output=True, shell=True)
                    time.sleep(15)
                    
                    cmd = [sys.executable, run_script, "--test-script", case["script"], "--vus", str(vus), "--runs", str(RUNS)]
                    
                    env_vars = os.environ.copy()
                    if level is not None:
                        env_vars["LEVEL"] = str(level)
                        
                    p = subprocess.Popen(cmd, cwd=env_path, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, env=env_vars)
                    for line in p.stdout:
                        print(line.rstrip())
                    p.wait()
                    
if __name__ == "__main__":
    start_time = datetime.now()
    print(f"[{start_time}] INICIANDO EJECUCIÓN NOCTURNA")
    try:
        run_tests()
        print("\n\n[+] GENERANDO REPORTES EXCEL Y GRAFICOS...")
        import generate_reports
        generate_reports.generate_all()
        print("[+] TODO COMPLETADO CON EXITO.")
    except Exception as e:
        print(f"ERROR: {e}")
    finally:
        end_time = datetime.now()
        print(f"[{end_time}] EJECUCIÓN NOCTURNA FINALIZADA (Tomó {end_time - start_time})")
