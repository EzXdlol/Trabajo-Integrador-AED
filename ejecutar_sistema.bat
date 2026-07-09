@echo off
setlocal EnableExtensions

title Sistema de alquiler de bicicletas

set "SCRIPT_NAME=main_alquiler_bicicletas.py"
set "BASE_DIR=%~dp0"
set "PYFILE="

echo Buscando %SCRIPT_NAME%...

REM Buscar primero en la misma carpeta del .bat
if exist "%BASE_DIR%%SCRIPT_NAME%" (
    set "PYFILE=%BASE_DIR%%SCRIPT_NAME%"
    goto archivo_encontrado
)

REM Buscar en subcarpetas desde donde esta el .bat
for /r "%BASE_DIR%" %%F in (*) do (
    if /I "%%~nxF"=="%SCRIPT_NAME%" (
        set "PYFILE=%%~fF"
        goto archivo_encontrado
    )
)

echo.
echo ERROR: No se encontro %SCRIPT_NAME%.
echo Pone este archivo .bat en la misma carpeta que el .py o en una carpeta superior.
echo.
pause
exit /b 1

:archivo_encontrado
echo Archivo encontrado:
echo "%PYFILE%"
echo.

REM Buscar Python
where py >nul 2>nul
if %errorlevel%==0 (
    echo Ejecutando con: py
    echo.
    py "%PYFILE%"
    echo.
    pause
    exit /b 0
)

where python >nul 2>nul
if %errorlevel%==0 (
    echo Ejecutando con: python
    echo.
    python "%PYFILE%"
    echo.
    pause
    exit /b 0
)

where python3 >nul 2>nul
if %errorlevel%==0 (
    echo Ejecutando con: python3
    echo.
    python3 "%PYFILE%"
    echo.
    pause
    exit /b 0
)

echo.
echo ERROR: No se encontro Python instalado.
echo Instala Python 3 y volve a intentar.
echo.
pause
exit /b 1