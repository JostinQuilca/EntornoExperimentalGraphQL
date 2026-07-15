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

Calcula **1 hora** la primera vez. Casi todo es esperar descargas y el sembrado de datos.

---

## PARTE 1 — Descargar el proyecto

No necesitas tener nada instalado para este paso.

1. Entra a
   <https://github.com/JostinQuilca/EntornoExperimentalGraphQL/tree/experimento-computacional>
2. Pulsa el botón verde **«Code» → «Download ZIP»**.
3. **Descomprime** el ZIP donde quieras (por ejemplo, el Escritorio).
4. Entra a la carpeta descomprimida.

> 💡 **¿Ya tienes Git?** Entonces es más rápido así:
> ```powershell
> cd $HOME\Desktop
> git clone -b experimento-computacional https://github.com/JostinQuilca/EntornoExperimentalGraphQL.git
> cd EntornoExperimentalGraphQL
> ```

---

## PARTE 2 — Instalar todo (un solo doble clic)

Dentro de la carpeta del proyecto vas a ver el archivo **`INSTALAR.bat`**.

1. **Doble clic** en `INSTALAR.bat`.
2. Windows pedirá permiso de **Administrador** → dale **«Sí»** (Docker lo exige).
3. Espera. El script solo:
   - 🔍 revisa qué tienes ya instalado y qué falta,
   - 📥 instala lo que falte: **Git**, **Python 3.12**, **k6** y **Docker Desktop**,
   - 📚 instala las librerías de Python (openpyxl, matplotlib, numpy, scipy),
   - 🐳 enciende el motor de Docker y espera a que esté listo.

> 🔁 **Si instaló Docker Desktop, te pedirá reiniciar la computadora.** Reinicia, abre Docker
> Desktop, espera la ballena verde y **vuelve a dar doble clic en `INSTALAR.bat`**.
> El script continúa donde quedó: no repite lo que ya instaló.

Al final te muestra un resumen con las versiones y te ofrece abrir el preparador del entorno.

> 🔍 **¿Solo quieres ver qué te falta, sin instalar nada?** En PowerShell:
> ```powershell
> powershell -ExecutionPolicy Bypass -File .\instalar_requisitos.ps1 -SoloVerificar
> ```

### 🔵 Plan B — Instalar a mano (si el script falla)

<details>
<summary>Desplegar los pasos manuales</summary>

En **PowerShell como administrador**:

```powershell
winget install -e --id Git.Git
winget install -e --id Python.Python.3.12
winget install -e --id GrafanaLabs.k6
winget install -e --id Docker.DockerDesktop
```

⚠️ Después de cada instalación, **cierra y vuelve a abrir PowerShell**. Si no, la ventana
sigue sin reconocer el comando nuevo y parece que falló. (El script hace esto solo.)

O descargando cada instalador:

1. **Docker Desktop** → <https://www.docker.com/products/docker-desktop/> · instala y **reinicia**. Si pide **WSL2**, acepta.
2. **Git** → <https://git-scm.com/download/win> · todo por defecto («Next» hasta el final).
3. **Python 3.12** → <https://www.python.org/downloads/> · **MUY IMPORTANTE**: marca ☑️ **«Add python.exe to PATH»** antes de «Install Now».
4. **k6** → <https://grafana.com/docs/k6/latest/set-up/install-k6/> · descarga el `.msi` de Windows.

Y luego, en la carpeta del proyecto: `pip install -r requirements.txt`

</details>

---

## PARTE 3 — Darle RAM a Docker

1. Abre **Docker Desktop** y espera la **ballena verde** abajo a la izquierda («Engine running»).
2. Ve a **⚙️ Settings → Resources → Advanced**.
3. Sube **Memory (RAM)** a **6 GB** mínimo (8 GB si la PC tiene 16). Dale **«Apply & restart»**.

> 💡 Deja Docker Desktop **abierto** todo el tiempo que uses el experimento.

---

## PARTE 4 — Preparar el entorno (¡lo hace todo solo!)

Si dijiste que sí al final del `INSTALAR.bat`, esta ventana ya está abierta. Si no:

```powershell
python preparar_entorno.py
```

1. Pulsa el botón grande **«⚡ Preparar TODO»**.
2. Verás en el registro cómo:
   - ✔️ verifica que todo esté instalado,
   - 🔨 construye los contenedores,
   - 🌱 siembra ~227 000 registros de prueba,
   - ✅ verifica que los dos entornos respondan.

> ⏳ **La primera vez tarda entre 20 y 45 minutos** (descarga imágenes + siembra). Es normal.
> No cierres la ventana. Si quieres verlo sin ventana: `python preparar_entorno.py --cli`.

Cuando diga **«¡LISTO!»**, ya está todo preparado.

---

## PARTE 5 — Correr los ataques

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
| **`INSTALAR.bat` se abre y cierra al instante** | Ejecútalo desde PowerShell para ver el error: `powershell -ExecutionPolicy Bypass -File .\instalar_requisitos.ps1` |
| **«winget no está disponible»** | Instala «Instalador de aplicaciones» desde Microsoft Store, o usa el **Plan B** de la Parte 2. |
| **«Docker no está corriendo»** | Abre Docker Desktop y espera la ballena verde. |
| **«k6 no está en el PATH»** | Cierra y vuelve a abrir PowerShell. Si sigue, re-ejecuta `INSTALAR.bat`. |
| **«python no se reconoce…»** | Reinstala Python marcando ☑️ «Add to PATH» y reabre PowerShell. |
| **`python` abre Microsoft Store** | Es el atajo falso de Windows. El script lo detecta e instala el Python real. |
| **El sembrado falla o se congela** | Falta RAM. Cierra programas, sube la memoria de Docker (Parte 3) y reintenta con **«Forzar re-siembra»**. |
| **«port 4000 is already in use»** | Algo está usando ese puerto. Cierra el otro programa (o reinicia la PC). |
| **Error de WSL2 al abrir Docker** | Abre PowerShell como admin, ejecuta `wsl --install` y reinicia. |
| **La ventana no abre pero no hay error** | Usa el modo consola: `python preparar_entorno.py --cli`. |

---

## ✔️ Lista de verificación rápida

- [ ] Proyecto descargado y entré a la carpeta.
- [ ] `INSTALAR.bat` terminó con el resumen en verde (git, python, k6, docker).
- [ ] Docker Desktop **abierto**, en **verde** y con **6 GB o más** de RAM.
- [ ] `python preparar_entorno.py` → «⚡ Preparar TODO» → terminó en «¡LISTO!».
- [ ] Abrí el panel y corrí un ataque de prueba (UC-01).

Si todos están marcados, el experimento está corriendo en esa PC. 🎉

---

*Nota: los números de latencia y CPU dependen del hardware, así que en otra PC saldrán distintos.
Las conclusiones (bloqueo de introspección, control de profundidad/complejidad, etc.) y el consumo
de RAM (topes fijos de los contenedores) se mantienen igual.*
