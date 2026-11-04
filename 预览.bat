@echo off
cd /d "D:\MyFun\World\NoDreamLogic.com\my-website"
start "Hugo Server" cmd /k "hugo server --buildDrafts=false --buildFuture=false"
timeout /t 3 /nobreak >nul
start "" "http://localhost:1313"
