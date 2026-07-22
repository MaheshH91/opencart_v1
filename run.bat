@echo off
:: Ensure the batch script executes from its own root directory
cd /d "%~dp0"

:: Activate your virtual environment
call .venv\Scripts\activate.bat

:: Execute pytest using 'call'
call pytest -s -v testCases/ -m "sanity" --browser=edge --capture=tee-sys

:: Keep the terminal window open after completion to inspect results
pause