@echo off
cd /d "D:\MyFun\World\NoDreamLogic.com\my-website"

echo === 正在添加文件 ===
git add .

echo === 正在提交 ===
git commit -m "update %date% %time%"

echo === 正在推送 ===
git push

echo === 完成 ===
pause