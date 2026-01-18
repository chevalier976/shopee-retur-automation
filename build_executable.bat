@echo off
echo ================================================
echo   Shopee Retur Automation - Build Executable
echo ================================================
echo.
echo Membuat file .exe yang bisa dijalankan tanpa Python...
echo Proses ini membutuhkan waktu 3-5 menit.
echo.

REM Install PyInstaller jika belum ada
echo [1/3] Memastikan PyInstaller terinstall...
pip install pyinstaller>=6.0.0

if %errorlevel% neq 0 (
    echo.
    echo ERROR: Gagal install PyInstaller!
    pause
    exit /b 1
)

echo.
echo [2/3] Membuat executable...
echo.

REM Build dengan PyInstaller
pyinstaller --name "ShopeeReturAutomation" ^
    --onefile ^
    --add-data "config;config" ^
    --add-data "utils;utils" ^
    --add-data "data;data" ^
    --add-data ".streamlit;.streamlit" ^
    --hidden-import streamlit ^
    --hidden-import pandas ^
    --hidden-import openpyxl ^
    --hidden-import plotly ^
    --hidden-import plotly.express ^
    --hidden-import plotly.graph_objects ^
    --collect-all streamlit ^
    --noconfirm ^
    app.py

if %errorlevel% neq 0 (
    echo.
    echo ERROR: Build gagal!
    pause
    exit /b 1
)

echo.
echo [3/3] Membuat script untuk menjalankan executable...

REM Buat batch file untuk menjalankan executable
echo @echo off > dist\run_ShopeeReturAutomation.bat
echo echo ================================================ >> dist\run_ShopeeReturAutomation.bat
echo echo   Shopee Retur Automation >> dist\run_ShopeeReturAutomation.bat
echo echo ================================================ >> dist\run_ShopeeReturAutomation.bat
echo echo. >> dist\run_ShopeeReturAutomation.bat
echo echo Memulai aplikasi... >> dist\run_ShopeeReturAutomation.bat
echo echo Browser akan terbuka di http://localhost:8501 >> dist\run_ShopeeReturAutomation.bat
echo echo. >> dist\run_ShopeeReturAutomation.bat
echo echo Tekan Ctrl+C untuk menghentikan aplikasi >> dist\run_ShopeeReturAutomation.bat
echo echo ================================================ >> dist\run_ShopeeReturAutomation.bat
echo echo. >> dist\run_ShopeeReturAutomation.bat
echo start http://localhost:8501 >> dist\run_ShopeeReturAutomation.bat
echo ShopeeReturAutomation.exe >> dist\run_ShopeeReturAutomation.bat
echo pause >> dist\run_ShopeeReturAutomation.bat

REM Copy folder yang diperlukan ke dist
echo.
echo Menyalin file pendukung...
xcopy /E /I /Y .streamlit dist\.streamlit >nul 2>&1
xcopy /E /I /Y config dist\config >nul 2>&1
xcopy /E /I /Y utils dist\utils >nul 2>&1
xcopy /E /I /Y data dist\data >nul 2>&1
if not exist "dist\output" mkdir dist\output

echo.
echo ================================================
echo   BUILD BERHASIL!
echo ================================================
echo.
echo File executable tersimpan di folder: dist\
echo.
echo File yang perlu di-copy ke laptop lain:
echo   - ShopeeReturAutomation.exe
echo   - run_ShopeeReturAutomation.bat
echo   - folder: .streamlit, config, utils, data, output
echo.
echo ATAU copy seluruh folder 'dist\' ke laptop lain
echo.
echo Cara menjalankan di laptop lain:
echo   Double-click: run_ShopeeReturAutomation.bat
echo.
echo CATATAN: Tidak perlu Python di laptop lain!
echo.
pause
