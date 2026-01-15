@echo off
REM Setup Database Script untuk Command Prompt/CMD
echo === Quiz Pengupil - Database Setup ===
echo.

set DB_NAME=quiz_pengupil
set DB_USER=root
set /p DB_PASSWORD="Masukkan password MySQL untuk user 'root': "

echo.
echo Membuat database dan tabel...
echo.

mysql -u %DB_USER% -p%DB_PASSWORD% < db\setup_database.sql

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================
    echo Database berhasil dibuat!
    echo ========================================
    echo.
    echo Database: %DB_NAME%
    echo Default Users:
    echo   1. Username: irul     Password: 123456
    echo   2. Username: ahmad    Password: 123456
    echo.
    echo Next Steps:
    echo   1. Jalankan: php -S localhost:8000
    echo   2. Buka browser: http://localhost:8000/login.php
    echo   3. Atau run tests: python tests\run_tests.py
    echo.
) else (
    echo Error saat membuat database!
    pause
    exit /b 1
)

pause
