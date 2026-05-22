@echo off
setlocal enabledelayedexpansion

echo.
echo  ╔══════════════════════════════════════════════════════════════╗
echo  ║       INFOU LLM DIAGNOSTIC TOOL                             ║
echo  ╚══════════════════════════════════════════════════════════════╝
echo.

set SCRIPT_DIR=%~dp0
set VENV_PYTHON="%SCRIPT_DIR%.venv\Scripts\python.exe"

if not exist %VENV_PYTHON% (
    echo  [ERROR] Virtual environment not found at .venv\
    pause & exit /b 1
)

:: Verify API Key
%VENV_PYTHON% -c "import os; from dotenv import load_dotenv; load_dotenv(); k=os.environ.get('NVIDIA_API_KEY',''); exit(0 if k else 1)" 2>nul
if errorlevel 1 (
    echo  [ERROR] NVIDIA_API_KEY is not set in .env file
    pause & exit /b 1
)

echo  Running isolated LLM Diagnostic Test...
echo.

%VENV_PYTHON% test_llm.py

echo.
pause
