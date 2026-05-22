@echo off
setlocal enabledelayedexpansion

echo.
echo  ╔══════════════════════════════════════════════════════════════╗
echo  ║       INFOU PINECONE VECTOR DB INJECTOR                      ║
echo  ╚══════════════════════════════════════════════════════════════╝
echo.

set SCRIPT_DIR=%~dp0
set VENV_PYTHON="%SCRIPT_DIR%.venv\Scripts\python.exe"

if not exist %VENV_PYTHON% (
    echo  [ERROR] Virtual environment not found at .venv\
    pause & exit /b 1
)

echo  Scanning for the most recent pipeline run...
echo.

%VENV_PYTHON% -m src.scheme_scraper.pipeline.vectorstore_ingest

echo.
pause
