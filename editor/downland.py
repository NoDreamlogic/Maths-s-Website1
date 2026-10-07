# -*- coding: utf-8 -*-
"""自动从多个镜像下载前端依赖到 static/ 目录"""
import urllib.request
from pathlib import Path

STATIC = Path(__file__).parent / "static"
STATIC.mkdir(exist_ok=True)

FILES = {
    "easymde.min.css": [
        "https://cdn.staticfile.org/easymde/2.18.0/easymde.min.css",
        "https://cdn.bootcdn.net/ajax/libs/easymde/2.18.0/easymde.min.css",
        "https://unpkg.com/easymde@2.18.0/dist/easymde.min.css",
        "https://cdn.jsdelivr.net/npm/easymde@2.18.0/dist/easymde.min.css",
    ],
    "easymde.min.js": [
        "https://cdn.staticfile.org/easymde/2.18.0/easymde.min.js",
        "https://cdn.bootcdn.net/ajax/libs/easymde/2.18.0/easymde.min.js",
        "https://unpkg.com/easymde@2.18.0/dist/easymde.min.js",
        "https://cdn.jsdelivr.net/npm/easymde@2.18.0/dist/easymde.min.js",
    ],
    "marked.min.js": [
        "https://cdn.staticfile.org/marked/12.0.0/marked.min.js",
        "https://cdn.bootcdn.net/ajax/libs/marked/12.0.0/marked.min.js",
        "https://unpkg.com/marked@12.0.0/marked.min.js",
        "https://cdn.jsdelivr.net/npm/marked@12.0.0/marked.min.js",
    ],
}

print("=" * 50)
for name, urls in FILES.items():
    dest = STATIC / name
    ok = False
    for url in urls:
        print(f"[{name}] 尝试 {url}")
        try:
            with urllib.request.urlopen(url, timeout=15) as r:
                data = r.read()
            if len(data) < 200:
                print(f"   太小（{len(data)} 字节），换下一个")
                continue
            dest.write_bytes(data)
            print(f"   成功，{len(data):,} 字节")
            ok = True
            break
        except Exception as e:
            print(f"   失败：{e}")
    if not ok:
        print(f"   ×× 无法下载 {name}")
print("=" * 50)
print("检查 static 目录，正常情况下应看到 3 个文件。")
input("按回车键退出……")