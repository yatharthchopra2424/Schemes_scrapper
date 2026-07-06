@echo off
setlocal enabledelayedexpansion

:: ================================================================
::   INFOU - SMART RESUME: LLM DOCUMENT GENERATION
::   - Schemes with evidence: generates 9 .md docs (no crawl)
::   - Schemes with NO evidence: runs full crawl + LLM + docs
::   Safe to Ctrl+C and re-run - already done schemes are skipped.
:: ================================================================

echo.
echo  +============================================================+
echo  ^|     INFOU - SMART RESUME: LLM DOCUMENT GENERATION         ^|
echo  +============================================================+
echo.

:: ================================================================
::   CONFIGURATION
:: ================================================================
set SCRIPT_DIR=%~dp0
set VENV_PYTHON="%SCRIPT_DIR%.venv\Scripts\python.exe"
set CONFIG=config/settings.yaml
set INPUT_CSV=data/input/sample_schemes.csv

:: ----------------------------------------------------------------
::  TARGET RUN: set to the run_id you want to resume.
::  Leave blank to auto-detect the LATEST run in runs\ folder.
:: ----------------------------------------------------------------
set TARGET_RUN_ID=run_20260623_0022

:: ----------------------------------------------------------------
::  WORKERS: parallel Chrome workers for the crawl phase.
::  Default is from config. Override here if needed (e.g. 3).
:: ----------------------------------------------------------------
set WORKERS=

:: Python / encoding settings
set PYTHON_GIL=0
set PYTHONWARNINGS=ignore::RuntimeWarning
set PYTHONIOENCODING=utf-8
set PYTHONUTF8=1

:: ================================================================
::   PRE-FLIGHT CHECKS
:: ================================================================
echo  [CHECK 1/3] Verifying virtual environment...
if not exist "%SCRIPT_DIR%.venv\Scripts\python.exe" (
    echo  [ERROR] Virtual environment not found at .venv\
    echo          Please run:  python -m venv .venv
    echo          Then:        .venv\Scripts\pip install -e .
    pause & exit /b 1
)
echo           OK - .venv found

echo  [CHECK 2/3] Verifying NVIDIA API key...
%VENV_PYTHON% -c "import os; from dotenv import load_dotenv; load_dotenv(); k=os.environ.get('NVIDIA_API_KEY',''); exit(0 if k else 1)" 2>nul
if errorlevel 1 (
    echo  [ERROR] NVIDIA_API_KEY is not set in .env file
    echo          Please add to .env:  NVIDIA_API_KEY=nvapi-...
    pause & exit /b 1
)
echo           OK - API key found

echo  [CHECK 3/3] Verifying input CSV...
if not exist "%SCRIPT_DIR%%INPUT_CSV%" (
    echo  [ERROR] Input CSV not found: %INPUT_CSV%
    echo          This is needed to match no-evidence schemes.
    pause & exit /b 1
)
echo           OK - Input CSV found

:: ================================================================
::   SHOW WHAT WE WILL DO
:: ================================================================
echo.
if "%TARGET_RUN_ID%"=="" (
    echo  Target run : AUTO-DETECT latest run in runs\
) else (
    echo  Target run : %TARGET_RUN_ID%
    if not exist "%SCRIPT_DIR%runs\%TARGET_RUN_ID%\artifacts" (
        echo  [ERROR] Artifacts folder not found: runs\%TARGET_RUN_ID%\artifacts
        echo          Check the run ID is correct.
        pause & exit /b 1
    )
)
echo.
echo  What this script does:
echo    - Schemes with evidence (ai_summary.json / docs): generates 9 .md docs ONLY
echo    - Schemes with NO evidence (empty dirs): runs FULL crawl + LLM + doc gen
echo    - Already complete schemes (9 docs exist): SKIPPED
echo.
echo  Starting... (Press Ctrl+C to pause - safe to re-run any time)
echo.

:: ================================================================
::   RUN
:: ================================================================
if "%TARGET_RUN_ID%"=="" (
    if "%WORKERS%"=="" (
        %VENV_PYTHON% resume_llm_docs.py --config %CONFIG% --input %INPUT_CSV%
    ) else (
        %VENV_PYTHON% resume_llm_docs.py --config %CONFIG% --input %INPUT_CSV% --workers %WORKERS%
    )
) else (
    if "%WORKERS%"=="" (
        %VENV_PYTHON% resume_llm_docs.py --run-id %TARGET_RUN_ID% --config %CONFIG% --input %INPUT_CSV%
    ) else (
        %VENV_PYTHON% resume_llm_docs.py --run-id %TARGET_RUN_ID% --config %CONFIG% --input %INPUT_CSV% --workers %WORKERS%
    )
)

set EXIT_CODE=%errorlevel%

:: ================================================================
::   RESULT
:: ================================================================
echo.
if %EXIT_CODE% == 0 (
    echo  +============================================================+
    echo  ^|  COMPLETE - All documents generated successfully           ^|
    echo  +============================================================+
    echo.
    if "%TARGET_RUN_ID%"=="" (
        echo  Check your latest run folder in: runs\
    ) else (
        echo  Check output in: runs\%TARGET_RUN_ID%\artifacts\
    )
) else if %EXIT_CODE% == 1 (
    echo  +============================================================+
    echo  ^|  INTERRUPTED - Progress saved. Re-run to continue.        ^|
    echo  +============================================================+
) else (
    echo  +============================================================+
    echo  ^|  FAILED - Exit code: %EXIT_CODE%                                  ^|
    echo  +============================================================+
    echo  Check pipeline.log for details.
    if "%TARGET_RUN_ID%"=="" (
        echo  Log: runs\^<latest^>\pipeline.log
    ) else (
        echo  Log: runs\%TARGET_RUN_ID%\pipeline.log
    )
)
echo.
pause
