@echo off
REM run_billboard.bat
REM Double-click this file to run the Billboard fetch script.
REM It automatically activates your venv and runs fetch_billboard.py -
REM no need to open a terminal or type any commands yourself.

REM Move into the same folder this .bat file is sitting in
cd /d "%~dp0"

REM Activate the virtual environment
call venv\Scripts\activate.bat

REM Run the script
python fetch_billboard.py

REM Keep the window open after it finishes so you can read the output
echo.
echo Press any key to close this window...
pause >nul