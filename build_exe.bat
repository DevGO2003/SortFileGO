@echo off
REM ============================================
REM Script: Build FileSorter.exe
REM Tự động đóng gói ứng dụng Python thành .exe
REM ============================================

echo ========================================
echo     FILE SORTER - BUILD EXE
echo ========================================
echo.

REM Kiểm tra Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python chua duoc cai dat!
    echo Vui long tai Python tai: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [OK] Python da duoc cai dat
echo.

REM Kiểm tra PyInstaller
pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo [INFO] Dang cai dat PyInstaller...
    pip install pyinstaller
    if errorlevel 1 (
        echo [ERROR] Khong the cai dat PyInstaller!
        pause
        exit /b 1
    )
)

echo [OK] PyInstaller da san sang
echo.

REM Xóa thư mục build cũ
if exist build (
    echo [INFO] Xoa thu muc build cu...
    rmdir /s /q build
)

if exist dist (
    echo [INFO] Xoa thu muc dist cu...
    rmdir /s /q dist
)

if exist FileSorter.spec (
    echo [INFO] Xoa file spec cu...
    del FileSorter.spec
)

echo.
echo ========================================
echo     DANG DONG GOI FILE .EXE...
echo ========================================
echo.

REM Đóng gói
pyinstaller --onefile --noconsole --name "FileSorter" file_sorter.py

if errorlevel 1 (
    echo.
    echo [ERROR] Loi khi dong goi!
    pause
    exit /b 1
)

echo.
echo ========================================
echo     HOAN THANH!
echo ========================================
echo.
echo File .exe da duoc tao tai:
echo %CD%\dist\FileSorter.exe
echo.
echo Ban co the:
echo 1. Chay file .exe truc tiep
echo 2. Copy file .exe di bat ky dau
echo 3. Chia se cho nguoi khac (khong can Python)
echo.

REM Mở thư mục dist
explorer dist

pause
