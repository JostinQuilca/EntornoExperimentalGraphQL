@echo off
REM ===========================================================================
REM  Experimento GraphQL + ISO/IEC 27001 - Instalador de requisitos
REM  Doble clic aqui para instalar y preparar TODO en una PC desde cero.
REM
REM  Lanza instalar_requisitos.ps1 saltando la politica de ejecucion de
REM  PowerShell, que por defecto bloquea los .ps1 en Windows.
REM ===========================================================================
title Experimento GraphQL - Instalador de requisitos
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0instalar_requisitos.ps1"
if errorlevel 1 pause
