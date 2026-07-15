<#
    ============================================================================
     INSTALADOR DE REQUISITOS - Experimento GraphQL + ISO/IEC 27001
    ============================================================================
     Verifica e instala TODO lo necesario en una PC desde cero:

        Git  |  Python 3.12  |  k6 (Grafana k6)  |  Docker Desktop

     Luego instala las librerias de Python, enciende el motor de Docker
     y abre el preparador del entorno (contenedores + sembrado de datos).

     ---------------------------------------------------------------------
     COMO USARLO
     ---------------------------------------------------------------------
        Clic derecho sobre el archivo  ->  "Ejecutar con PowerShell"

     o desde una terminal, dentro de la carpeta del proyecto:

        powershell -ExecutionPolicy Bypass -File .\instalar_requisitos.ps1

     Solo revisar que tienes, sin instalar nada:

        powershell -ExecutionPolicy Bypass -File .\instalar_requisitos.ps1 -SoloVerificar

     ---------------------------------------------------------------------
     NOTAS
     ---------------------------------------------------------------------
     * Se eleva a Administrador solo (Docker Desktop lo necesita).
     * Es re-ejecutable: no repite lo que ya esta instalado.
     * Refresca el PATH sin cerrar la ventana. Por eso funciona a la primera,
       a diferencia de correr los "winget install" sueltos a mano.
     * Escrito en ASCII a proposito: PowerShell 5.1 lee los .ps1 sin BOM como
       Windows-1252 y los acentos romperian el script.
    ============================================================================
#>

param(
    [switch]$SoloVerificar   # revisa e informa, pero no instala ni eleva permisos
)

$ErrorActionPreference = "Continue"
$PY_MIN = [version]"3.10.0"     # version minima de Python que usa el proyecto

# ----------------------------- Salida -----------------------------
function Titulo($t) {
    Write-Host ""
    Write-Host ("=" * 74) -ForegroundColor DarkCyan
    Write-Host "  $t" -ForegroundColor Cyan
    Write-Host ("=" * 74) -ForegroundColor DarkCyan
}
function Paso($t)  { Write-Host "`n>> $t" -ForegroundColor White }
function Ok($t)    { Write-Host "   [ OK ]  $t" -ForegroundColor Green }
function Aviso($t) { Write-Host "   [ .. ]  $t" -ForegroundColor Yellow }
function Malo($t)  { Write-Host "   [ X  ]  $t" -ForegroundColor Red }
function Pausa($t) { if (-not $SoloVerificar) { Read-Host "`n$t" | Out-Null } }

# --------------- Refrescar el PATH en esta misma ventana ---------------
# Sin esto, despues de un "winget install" la terminal actual NO ve el comando
# nuevo y parece que la instalacion fallo. Es el problema clasico.
function Refrescar-Path {
    $m = [System.Environment]::GetEnvironmentVariable("Path", "Machine")
    $u = [System.Environment]::GetEnvironmentVariable("Path", "User")
    $env:Path = "$m;$u"
}

function Existe-Cmd($cmd) {
    Refrescar-Path
    return ($null -ne (Get-Command $cmd -ErrorAction SilentlyContinue))
}

# Version de un programa (primera linea util). Devuelve $null si no responde.
function Version-De($cmd, $arg) {
    if (-not (Existe-Cmd $cmd)) { return $null }
    try {
        $out = & $cmd $arg 2>$null | Select-Object -First 1
        if ([string]::IsNullOrWhiteSpace($out)) { return $null }
        return $out.ToString().Trim()
    } catch { return $null }
}

# ---------------------- Elevar a Administrador ----------------------
if (-not $SoloVerificar) {
    $ident = [Security.Principal.WindowsIdentity]::GetCurrent()
    $prin  = New-Object Security.Principal.WindowsPrincipal($ident)
    $esAdmin = $prin.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
    if (-not $esAdmin) {
        Write-Host "Se necesita Administrador (Docker lo exige). Relanzando..." -ForegroundColor Yellow
        Start-Process powershell -Verb RunAs -ArgumentList "-ExecutionPolicy Bypass -NoExit -File `"$PSCommandPath`""
        exit
    }
}

Titulo "REQUISITOS DEL EXPERIMENTO - GraphQL / ISO 27001"
if ($SoloVerificar) {
    Write-Host "  Modo revision: solo informa, no instala nada." -ForegroundColor Gray
} else {
    Write-Host "  Revisa lo que ya tienes e instala unicamente lo que falte." -ForegroundColor Gray
}

# ------------------------------ winget ------------------------------
Paso "winget (el instalador de Windows)"
if (Existe-Cmd "winget") {
    Ok ("disponible  ->  " + (Version-De "winget" "--version"))
} else {
    Malo "winget no esta disponible en esta PC."
    if (-not $SoloVerificar) {
        Write-Host "   Instala 'Instalador de aplicaciones' desde Microsoft Store y re-ejecuta." -ForegroundColor Yellow
        Write-Host "   ms-windows-store://pdp/?ProductId=9NBLGGH4NNS1" -ForegroundColor Gray
        Pausa "Enter para salir"
        exit 1
    }
}

# ------------------- Instalar / verificar un programa -------------------
function Asegurar-Programa($nombre, $wingetId, $cmd, $verArg) {
    Paso $nombre
    $v = Version-De $cmd $verArg
    if ($v) { Ok "ya instalado  ->  $v"; return $true }

    if ($SoloVerificar) {
        Malo "FALTA  (se instalaria con: winget install -e --id $wingetId)"
        return $false
    }

    Aviso "no esta instalado. Instalando  ->  $wingetId"
    winget install -e --id $wingetId --accept-source-agreements --accept-package-agreements --disable-interactivity
    Refrescar-Path

    $v = Version-De $cmd $verArg
    if ($v) { Ok "instalado  ->  $v"; return $true }

    Malo "$nombre quedo instalado pero todavia no aparece en el PATH."
    Write-Host "   Cierra esta ventana, abre PowerShell otra vez y re-ejecuta el script." -ForegroundColor Yellow
    return $false
}

# =============================== 1) Git ===============================
Asegurar-Programa "Git" "Git.Git" "git" "--version" | Out-Null

# ============================= 2) Python =============================
Paso "Python (se necesita $PY_MIN o superior)"
$pyOk  = $false
$pyRaw = Version-De "python" "--version"     # $null si es el atajo falso de Microsoft Store
if ($pyRaw -and ($pyRaw -match "(\d+\.\d+\.\d+)")) {
    $ver = [version]$Matches[1]
    if ($ver -ge $PY_MIN) {
        Ok "ya instalado  ->  Python $ver"
        $pyOk = $true
    } else {
        Aviso "tienes Python $ver, pero el proyecto necesita $PY_MIN o superior"
    }
} elseif (Existe-Cmd "python") {
    Aviso "'python' existe pero no responde: es el atajo de Microsoft Store, no Python real"
} else {
    Aviso "no esta instalado"
}

if (-not $pyOk) {
    if ($SoloVerificar) {
        Malo "FALTA  (se instalaria con: winget install -e --id Python.Python.3.12)"
    } else {
        Aviso "Instalando Python 3.12  ->  Python.Python.3.12"
        winget install -e --id Python.Python.3.12 --accept-source-agreements --accept-package-agreements --disable-interactivity
        Refrescar-Path
        $pyRaw = Version-De "python" "--version"
        if ($pyRaw) {
            Ok "instalado  ->  $pyRaw"
            $pyOk = $true
        } else {
            Malo "Python no aparece en el PATH. Cierra y reabre PowerShell, y re-ejecuta."
        }
    }
}

# =============================== 3) k6 ===============================
# El ID correcto en winget es GrafanaLabs.k6   (NO "Grafana.k6")
Asegurar-Programa "k6 (inyector de carga de Grafana)" "GrafanaLabs.k6" "k6" "version" | Out-Null

# ========================= 4) Docker Desktop =========================
Paso "Docker Desktop"
$dockerNuevo = $false
$dv = Version-De "docker" "--version"
if ($dv) {
    Ok "ya instalado  ->  $dv"
} elseif ($SoloVerificar) {
    Malo "FALTA  (se instalaria con: winget install -e --id Docker.DockerDesktop)"
} else {
    Aviso "no esta instalado. Instalando  ->  Docker.DockerDesktop  (tarda varios minutos)"
    winget install -e --id Docker.DockerDesktop --accept-source-agreements --accept-package-agreements --disable-interactivity
    Refrescar-Path
    $dockerNuevo = $true
}

if ($dockerNuevo) {
    Titulo "HAY QUE REINICIAR LA COMPUTADORA"
    Write-Host "  Docker Desktop se acaba de instalar y necesita reiniciar Windows" -ForegroundColor Yellow
    Write-Host "  para activar WSL2. Despues del reinicio:" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "     1. Abre Docker Desktop y espera la ballena VERDE abajo a la izquierda." -ForegroundColor White
    Write-Host "     2. Vuelve a ejecutar este mismo script." -ForegroundColor White
    Write-Host ""
    Write-Host "  Continuara donde quedo: no repite lo que ya instalo." -ForegroundColor Gray
    Pausa "Enter para salir"
    exit 0
}

# --------------- Encender el motor de Docker y esperarlo ---------------
Paso "Motor de Docker"
docker info 2>$null | Out-Null
$motorOk = ($LASTEXITCODE -eq 0)

if ($motorOk) {
    Ok "motor ya estaba corriendo"
} elseif ($SoloVerificar) {
    Aviso "instalado pero apagado (habria que abrir Docker Desktop)"
} else {
    $exe = Join-Path $env:ProgramFiles "Docker\Docker\Docker Desktop.exe"
    if (Test-Path $exe) {
        Aviso "abriendo Docker Desktop..."
        Start-Process $exe
    } else {
        Aviso "abre Docker Desktop manualmente desde el menu Inicio"
    }

    Aviso "esperando a que arranque el motor (hasta 4 minutos)..."
    $fin = (Get-Date).AddMinutes(4)
    while ((Get-Date) -lt $fin) {
        Start-Sleep -Seconds 6
        docker info 2>$null | Out-Null
        if ($LASTEXITCODE -eq 0) { $motorOk = $true; break }
        Write-Host "." -NoNewline -ForegroundColor DarkGray
    }
    Write-Host ""
    if ($motorOk) {
        Ok "motor corriendo"
    } else {
        Malo "Docker no arranco a tiempo."
        Write-Host "   Abrelo a mano, espera la ballena verde y re-ejecuta este script." -ForegroundColor Yellow
        Pausa "Enter para salir"
        exit 1
    }
}

# --------------- Librerias de Python del proyecto ---------------
Paso "Librerias de Python (openpyxl, matplotlib, numpy, scipy)"
$req = Join-Path $PSScriptRoot "requirements.txt"
if (-not (Test-Path $req)) {
    Malo "no se encontro requirements.txt junto al script"
    Write-Host "   Ejecuta el script DENTRO de la carpeta del proyecto." -ForegroundColor Yellow
} elseif (-not $pyOk) {
    Malo "no se pueden instalar: falta Python"
} elseif ($SoloVerificar) {
    $falt = @()
    foreach ($m in @("openpyxl", "matplotlib", "numpy", "scipy")) {
        python -c "import $m" 2>$null
        if ($LASTEXITCODE -ne 0) { $falt += $m }
    }
    if ($falt.Count -eq 0) {
        Ok "todas instaladas"
    } else {
        Malo ("FALTAN: " + ($falt -join ", ") + "   (se instalarian con: pip install -r requirements.txt)")
    }
} else {
    python -m pip install --upgrade pip --quiet
    python -m pip install -r $req --quiet
    if ($?) { Ok "librerias instaladas" } else { Malo "fallo pip; revisa el mensaje de arriba" }
}

# ----------------------------- Resumen -----------------------------
Titulo "RESUMEN"
$todo = $true
foreach ($p in @(@("git", "--version"), @("python", "--version"), @("k6", "version"), @("docker", "--version"))) {
    $v = Version-De $p[0] $p[1]
    if ($v) {
        Ok ("{0,-8} {1}" -f $p[0], $v)
    } else {
        Malo ("{0,-8} NO disponible" -f $p[0])
        $todo = $false
    }
}

if ($SoloVerificar) {
    Write-Host ""
    if ($todo) {
        Write-Host "  Tienes todo lo necesario." -ForegroundColor Green
    } else {
        Write-Host "  Falta algo. Ejecuta el script SIN -SoloVerificar para instalarlo." -ForegroundColor Yellow
    }
    return
}

if (-not $todo) {
    Write-Host "`n  Falta algo de la lista. Cierra PowerShell, abrelo de nuevo y re-ejecuta." -ForegroundColor Yellow
    Pausa "Enter para cerrar"
    exit 1
}

# --------------- Abrir el preparador del entorno ---------------
$prep = Join-Path $PSScriptRoot "preparar_entorno.py"
if (Test-Path $prep) {
    Write-Host ""
    $r = Read-Host "Abrir ahora el preparador del entorno (construye contenedores y siembra datos)? [S/n]"
    if ($r -eq "" -or $r -match "^[sSyY]") {
        Paso "abriendo preparar_entorno.py ..."
        Start-Process python -ArgumentList "`"$prep`"" -WorkingDirectory $PSScriptRoot
        Write-Host "   En esa ventana pulsa el boton grande:  Preparar TODO" -ForegroundColor Cyan
        Write-Host "   La primera vez tarda entre 20 y 45 minutos. Es normal." -ForegroundColor Gray
    } else {
        Write-Host "   Cuando quieras:  python preparar_entorno.py" -ForegroundColor Gray
    }
} else {
    Write-Host "`n   Siguiente paso:  python preparar_entorno.py" -ForegroundColor Cyan
}

Pausa "Enter para cerrar"
