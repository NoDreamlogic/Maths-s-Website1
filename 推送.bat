@echo off
cd /d "D:\MyFun\World\NoDreamLogic.com\my-website"

echo === In the update file. ===
git add .

echo === Uploading. ===
git commit -m "update site"

echo === Refreshing. ===
git push

echo === Over. ===
pause