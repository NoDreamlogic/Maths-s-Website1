@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo ============================================
echo   Hugo 文章编辑器
echo ============================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo [错误] 没找到 Python，请确认已安装 Python 并加入了 PATH。
    pause
    exit /b 1
)

python -c "import flask" >nul 2>&1
if errorlevel 1 (
    echo 首次运行，正在安装 Flask，请稍等……
    python -m pip install flask
    echo.
)

echo 启动中……浏览器会自动打开 http://127.0.0.1:5000
echo 关闭本窗口即可停止服务。
echo.

start "" /min powershell -NoProfile -Command "Start-Sleep -Seconds 2; Start-Process 'http://127.0.0.1:5000'"
python server.py

pause