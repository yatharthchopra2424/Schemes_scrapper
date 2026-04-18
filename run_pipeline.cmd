@echo off
setlocal enabledelayedexpansion

:: ═══════════════════════════════════════════════════════════════════
::   INFOU SCHEME INTELLIGENCE SCRAPER
::   Industry-Grade Pipeline Runner
:: ═══════════════════════════════════════════════════════════════════

echo.
echo  ╔══════════════════════════════════════════════════════════════╗
echo  ║       INFOU SCHEME INTELLIGENCE PIPELINE v2.0               ║
echo  ╚══════════════════════════════════════════════════════════════╝
echo.

:: ══ CONFIGURATION ══════════════════════════════════════════════════
set SCRIPT_DIR=%~dp0
set VENV_PYTHON="%SCRIPT_DIR%.venv\Scripts\python.exe"
set INPUT_CSV=data/input/sample_schemes.csv
set CONFIG=config/settings.yaml
set OUTPUT_ROOT=runs

:: Auto-generate timestamped run ID to avoid overwriting previous runs
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set DATETIME=%%a
set RUN_ID=run_%DATETIME:~0,8%_%DATETIME:~8,4%

:: Optional flags (edit here or pass as arguments)
:: To resume a previous run:    set RESUME=--resume
:: To skip LLM (crawl only):    set SKIP_LLM=--skip-llm
:: To test with 1 scheme:       set MAX_SCHEMES=--max-schemes 1
:: To use 3 parallel workers:   set WORKERS=--workers 3
set RESUME=
set SKIP_LLM=
set MAX_SCHEMES=
set WORKERS=--workers 2

:: GIL settings for Python 3.14 free-threading
set PYTHON_GIL=0
set PYTHONWARNINGS=ignore::RuntimeWarning
set PYTHONIOENCODING=utf-8
set PYTHONUTF8=1

:: ══ PRE-FLIGHT CHECKS ══════════════════════════════════════════════
echo  [CHECK 1/4] Verifying virtual environment...
if not exist "%SCRIPT_DIR%.venv\Scripts\python.exe" (
    echo  [ERROR] Virtual environment not found at .venv\
    echo          Please run:  python -m venv .venv
    echo          Then:        .venv\Scripts\pip install -e .
    pause & exit /b 1
)
echo           OK — .venv found

echo  [CHECK 2/4] Verifying NVIDIA API key...
%VENV_PYTHON% -c "import os; from dotenv import load_dotenv; load_dotenv(); k=os.environ.get('NVIDIA_API_KEY',''); exit(0 if k else 1)" 2>nul
if errorlevel 1 (
    echo  [ERROR] NVIDIA_API_KEY is not set in .env file
    echo          Please add to .env:  NVIDIA_API_KEY=nvapi-...
    pause & exit /b 1
)
echo           OK — API key found

echo  [CHECK 3/4] Verifying input CSV...
if not exist "%SCRIPT_DIR%%INPUT_CSV%" (
    echo  [ERROR] Input CSV not found: %INPUT_CSV%
    echo          Please create: data\input\sample_schemes.csv
    pause & exit /b 1
)
echo           OK — Input CSV found

echo  [CHECK 4/4] Verifying browser configuration...
echo           OK — Selenium Manager will natively handle ChromeDriver

:: ══ PIPELINE LAUNCH ════════════════════════════════════════════════
echo.
echo  ┌──────────────────────────────────────────────────────────────┐
echo  │  Run ID: %RUN_ID%
echo  │  Output: %OUTPUT_ROOT%\%RUN_ID%\
echo  └──────────────────────────────────────────────────────────────┘
echo.
echo  Starting pipeline...
echo  (Press Ctrl+C to interrupt — partial results will be saved)
echo.

%VENV_PYTHON% -m scheme_scraper.main ^
    --input %INPUT_CSV% ^
    --config %CONFIG% ^
    --output-root %OUTPUT_ROOT% ^
    --run-id %RUN_ID% ^
    %RESUME% ^
    %SKIP_LLM% ^
    %MAX_SCHEMES% ^
    %WORKERS%

set PIPELINE_EXIT=%errorlevel%

:: ══ POST-RUN SUMMARY ════════════════════════════════════════════════
echo.
if %PIPELINE_EXIT% == 0 (
    echo  ╔══════════════════════════════════════════════════════════════╗
    echo  ║  PIPELINE FINISHED SUCCESSFULLY                              ║
    echo  ╚══════════════════════════════════════════════════════════════╝
    echo.
    echo  Generating run health dashboard...
    %VENV_PYTHON% -m scheme_scraper.pipeline.pipeline_summary --run-dir %OUTPUT_ROOT%\%RUN_ID%
) else (
    echo  ╔══════════════════════════════════════════════════════════════╗
    echo  ║  PIPELINE EXITED WITH CODE: %PIPELINE_EXIT%                          ║
    echo  ╚══════════════════════════════════════════════════════════════╝
)

echo.
echo  Results are in: %OUTPUT_ROOT%\%RUN_ID%\
echo  Full log:       %OUTPUT_ROOT%\%RUN_ID%\pipeline.log
echo.
pause
