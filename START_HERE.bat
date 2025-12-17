@echo off
echo ==========================================
echo Student Performance Predictor
echo File Structure Check
echo ==========================================
echo.

REM Check if app.py exists
if not exist "app.py" (
    echo ERROR: app.py not found!
    echo Please make sure you are in the correct folder.
    echo.
    pause
    exit /b 1
)

REM Check if templates folder exists
if not exist "templates" (
    echo ERROR: templates folder not found!
    echo Please create a folder named "templates" in this directory.
    echo.
    pause
    exit /b 1
)

REM Check if index.html exists in templates
if not exist "templates\index.html" (
    echo ERROR: templates\index.html not found!
    echo Please make sure index.html is inside the templates folder.
    echo.
    pause
    exit /b 1
)

echo All required files found!
echo.
echo Starting Flask server...
echo Access the app at: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo ==========================================
echo.

python app.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ==========================================
    echo ERROR: Failed to start the application
    echo ==========================================
    echo.
    echo Possible issues:
    echo 1. Python is not installed or not in PATH
    echo 2. Flask is not installed
    echo.
    echo To install Flask, run:
    echo    pip install Flask
    echo.
    pause
)
