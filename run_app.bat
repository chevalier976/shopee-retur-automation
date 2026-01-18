@echo off
echo ================================================
echo   Shopee Retur Automation - Web Application
echo ================================================
echo.
echo Memulai aplikasi web...
echo.
echo Browser akan terbuka otomatis di http://localhost:8501
echo.
echo Tekan Ctrl+C untuk menghentikan aplikasi
echo ================================================
echo.

streamlit run app.py --server.port 8501 --server.address localhost

pause
