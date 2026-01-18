@echo off
echo ================================================
echo   Shopee Retur Automation - Instalasi
echo ================================================
echo.
echo Mengecek instalasi Python...
python --version
if %errorlevel% neq 0 (
    echo.
    echo ERROR: Python tidak ditemukan!
    echo Silakan install Python terlebih dahulu dari https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo.
echo Menginstal dependencies...
echo.

pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo.
    echo ERROR: Instalasi gagal!
    echo.
    pause
    exit /b 1
)

echo.
echo ================================================
echo   Instalasi berhasil!
echo ================================================
echo.
echo Untuk menjalankan aplikasi, double-click file: run_app.bat
echo.
pause
