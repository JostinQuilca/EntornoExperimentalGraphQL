# 📘 Manual: correr el experimento en una PC desde cero

> Guía para poner en marcha el experimento en una computadora **que no tiene nada instalado**
> (ni Docker, ni Python, ni nada). Pensada para seguirse paso a paso, sin conocimientos previos.
> Sistema: **Windows 10 u 11 (64 bits)**.

---

## ✅ Antes de empezar: requisitos de la PC

| Requisito | Mínimo | Recomendado |
| :--- | :---: | :---: |
| **Memoria RAM** | 8 GB | 16 GB |
| **Espacio libre en disco** | 10 GB | 20 GB |
| **Internet** | Sí (para descargar todo) | — |
| **Virtualización** | Activada en BIOS (casi siempre lo está por defecto) | — |

> ⚠️ **Con menos de 8 GB de RAM el experimento NO va a correr** (los contenedores no caben y el
> sembrado de datos falla). Si la PC tiene 8 GB, cierra los demás programas mientras corre.

Vas a instalar **4 programas** (una sola vez) y luego correr el experimento. Calcula
**1 hora** la primera vez (la mayor parte es esperar descargas y el sembrado de datos).

---

## PARTE 1 — Instalar los 4 programas

Tienes dos caminos. **La Opción A es la más fácil.**

### 🟢 Opción A — Automática (con `winget`, ya viene en Windows 11)

1. Pulsa el botón **Inicio**, escribe `PowerShell`, haz **clic derecho → «Ejecutar como administrador»**.
2. Copia y pega estos comandos, uno por uno (Enter después de cada uno):

   ```powershell
   winget install -e --id Docker.DockerDesktop
   winget install -e --id Git.Git
   winget install -e --id Python.Python.3.12
   winget install -e --id Grafana.k6
   ```

3. **Reinicia la computadora** cuando termine (Docker lo necesita).

Si algún comando falla, instala ese programa con la **Opción B**.

### 🔵 Opción B — Manual (descargando cada uno)

1. **Docker Desktop** → <https://www.docker.com/products/docker-desktop/>
   Descarga, instala, **reinicia**. Al abrirlo puede pedir instalar **WSL2**: acepta.
2. **Git** → <https://git-scm.com/download/win>
   Instala con todas las opciones por defecto (solo dale «Next»).
3. **Python 3.12** → <https://www.python.org/downloads/>
   Descarga e instala, pero **MUY IMPORTANTE**: en la primera pantalla marca la casilla
   ☑️ **«Add python.exe to PATH»** antes de darle «Install Now».
4. **k6** → <https://grafana.com/docs/k6/latest/set-up/install-k6/>
   En la sección de Windows, descarga el instalador `.msi` y ejecútalo.

---

## PARTE 2 — Configurar Docker Desktop

1. Abre **Docker Desktop** (búscalo en Inicio).
2. Espera a que abajo a la izquierda aparezca la **ballena en verde** («Engine running»).
   La primera vez puede tardar unos minutos.
3. Ve a **⚙️ Settings → Resources → Advanced** y sube **Memory (RAM)** a **6 GB** como mínimo
   (8 GB si tu PC tiene 16). Dale **«Apply & restart»**.

> 💡 Deja Docker Desktop **abierto** todo el tiempo que uses el experimento.

---

## PARTE 3 — Descargar el proyecto

1. Abre **PowerShell** (normal, no hace falta administrador).
2. Ubícate donde quieras guardar el proyecto, por ejemplo el escritorio:

   ```powershell
   cd $HOME\Desktop
   ```

3. Descarga el proyecto desde GitHub:

   ```powershell
   git clone -b experimento-computacional https://github.com/JostinQuilca/EntornoExperimentalGraphQL.git
   cd EntornoExperimentalGraphQL
   ```

> **¿No quieres usar Git?** Entra a
> <https://github.com/JostinQuilca/EntornoExperimentalGraphQL/tree/experimento-computacional>,
> pulsa el botón verde **«Code» → «Download ZIP»**, descomprime y entra a la carpeta.

---

## PARTE 4 — Instalar las librerías de Python

Dentro de la carpeta del proyecto (en PowerShell), ejecuta:

```powershell
pip install -r requirements.txt
```

Instala openpyxl, matplotlib, numpy y scipy (para los gráficos y la estadística).

---

## PARTE 5 — Preparar el entorno (¡lo hace todo solo!)

1. Verifica que **Docker Desktop esté abierto y en verde**.
2. En PowerShell, dentro de la carpeta del proyecto, ejecuta:

   ```powershell
   python preparar_entorno.py
   ```

3. Se abre una ventana. Pulsa el botón grande **«⚡ Preparar TODO (compu nueva)»**.
4. Verás en el registro cómo:
   - ✔️ verifica que todo esté instalado,
   - 🔨 construye los contenedores,
   - 🌱 siembra ~227 000 registros de prueba,
   - ✅ verifica que los dos entornos respondan.

> ⏳ **La primera vez tarda entre 20 y 45 minutos** (descarga imágenes + siembra). Es normal.
> No cierres la ventana. Si quieres verlo sin ventana: `python preparar_entorno.py --cli`.

Cuando diga **«¡LISTO!»**, ya está todo preparado.

---

## PARTE 6 — Correr los ataques

1. En la misma ventana, pulsa **«▶ Abrir Panel de Ataques»** (o ejecuta `python panel_control.py`).
2. En el panel:
   - Elige el caso de uso (**UC-01** a **UC-05**).
   - Elige entorno **Vulnerable** o **Protegido**, o usa la pestaña **Comparativa** para verlos lado a lado.
   - Pulsa **Ejecutar**.
3. Al terminar puedes ver **gráficos**, exportar a **Excel** y ver el **análisis estadístico**.

---

## 🔧 Solución de problemas

| Mensaje / síntoma | Qué hacer |
| :--- | :--- |
| **«Docker no está corriendo»** | Abre Docker Desktop y espera a la ballena verde. |
| **«k6 no está en el PATH»** | Reinstala k6 y **cierra y vuelve a abrir** PowerShell. |
| **«python no se reconoce…»** | Reinstala Python marcando ☑️ «Add to PATH» y reabre PowerShell. |
| **El sembrado falla o se congela** | Falta RAM. Cierra programas, sube la memoria de Docker (Parte 2) y reintenta con **«Forzar re-siembra»**. |
| **«port 4000 is already in use»** | Algo está usando ese puerto. Cierra el otro programa (o reinicia la PC). |
| **Error de WSL2 al abrir Docker** | Abre PowerShell como admin y ejecuta `wsl --install`, reinicia. |
| **La ventana no abre pero no hay error** | Usa el modo consola: `python preparar_entorno.py --cli`. |

---

## ✔️ Lista de verificación rápida

- [ ] Docker Desktop instalado, **abierto** y en **verde**.
- [ ] Git, Python (con PATH) y k6 instalados.
- [ ] Proyecto descargado y entré a la carpeta.
- [ ] `pip install -r requirements.txt` sin errores.
- [ ] `python preparar_entorno.py` → «⚡ Preparar TODO» → terminó en «¡LISTO!».
- [ ] Abrí el panel y corrí un ataque de prueba (UC-01).

Si todos están marcados, el experimento está corriendo en esa PC. 🎉

---

*Nota: los números de latencia y CPU dependen del hardware, así que en otra PC saldrán distintos.
Las conclusiones (bloqueo de introspección, control de profundidad/complejidad, etc.) y el consumo
de RAM (topes fijos de los contenedores) se mantienen igual.*
