# -*- coding: utf-8 -*-
"""
Hugo 本地文章编辑器 —— 后端服务（Flask）

用法：
    cd D:\\MyFun\\World\\NoDreamLogic.com\\my-website\\editor
    python server.py
然后浏览器打开 http://127.0.0.1:5000

也可以直接双击 editor 目录里的「启动编辑器.bat」。
"""

import re
import tomllib
import unicodedata
from datetime import datetime, timedelta, timezone
from pathlib import Path

from flask import Flask, abort, jsonify, render_template, request

# ============================================================ 基础配置

EDITOR_DIR = Path(__file__).resolve().parent
PROJECT_DIR = EDITOR_DIR.parent          # Hugo 项目根目录
POSTS_DIR = PROJECT_DIR / "content" / "posts"

HOST = "127.0.0.1"
PORT = 5000
TIMEZONE = timezone(timedelta(hours=8))  # 北京时间（东八区）

# 允许的文件名：字母/数字/中文开头，之后是字母数字中文和 . _ -
FILENAME_RE = re.compile(r"^[A-Za-z0-9\u4e00-\u9fff][A-Za-z0-9\u4e00-\u9fff._-]*\.md$")

app = Flask(__name__)
try:
    app.json.ensure_ascii = False        # 让接口返回的中文可读
except Exception:
    pass


# ============================================================ 工具函数

def ensure_posts_dir() -> None:
    POSTS_DIR.mkdir(parents=True, exist_ok=True)


def resolve_post_path(filename: str) -> Path:
    """校验文件名并返回绝对路径，防止越权读写目录外的文件。"""
    if not FILENAME_RE.match(filename or ""):
        abort(400, description="文件名不合法")
    path = (POSTS_DIR / filename).resolve()
    if path.parent != POSTS_DIR.resolve():
        abort(400, description="路径不合法")
    return path


def split_front_matter(text: str):
    """把文件拆成 (front matter 原文, 正文)。没有 front matter 时返回 (None, 全文)。"""
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    if not normalized.startswith("+++"):
        return None, normalized
    lines = normalized.split("\n")
    if lines[0].strip() != "+++":
        return None, normalized
    for i in range(1, len(lines)):
        if lines[i].strip() == "+++":
            raw = "\n".join(lines[1:i])
            body = "\n".join(lines[i + 1:])
            return raw, body.lstrip("\n")
    return None, normalized


def parse_post(text: str):
    """返回 (meta 字典, 正文)"""
    raw, body = split_front_matter(text)
    data = {}
    if raw:
        try:
            data = tomllib.loads(raw)
        except tomllib.TOMLDecodeError:
            data = {}

    title = data.get("title", "")
    title = str(title) if title is not None else ""

    date_value = data.get("date", "")
    date = date_value.isoformat() if isinstance(date_value, datetime) else str(date_value or "")

    draft = bool(data.get("draft", False))

    tags = data.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    elif not isinstance(tags, (list, tuple)):
        tags = [tags] if tags else []
    tags = [str(t) for t in tags if str(t).strip()]

    return {"title": title, "date": date, "draft": draft, "tags": tags}, body


def toml_quote(value) -> str:
    """把字符串安全地写成 TOML 的双引号字符串。"""
    text = str(value)
    text = text.replace("\\", "\\\\").replace('"', '\\"')
    text = text.replace("\n", "\\n").replace("\r", "\\r").replace("\t", "\\t")
    return '"' + text + '"'


def normalize_date(value) -> str:
    """把各种日期写法统一成 2026-10-06T12:00:00+08:00 这种格式。"""
    text = str(value or "").strip()
    dt = None
    if text:
        try:
            dt = datetime.fromisoformat(text.replace("Z", "+00:00"))
        except ValueError:
            for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M", "%Y-%m-%d"):
                try:
                    dt = datetime.strptime(text, fmt)
                    break
                except ValueError:
                    continue
    if dt is None:
        dt = datetime.now(TIMEZONE)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=TIMEZONE)
    return dt.replace(microsecond=0).isoformat()


def parse_tags(value) -> list:
    """把 "a, b, c" 或 ["a","b"] 统一成 ["a","b","c"]"""
    if value is None:
        return []
    if isinstance(value, str):
        raw = [value]
    elif isinstance(value, (list, tuple)):
        raw = [str(v) for v in value]
    else:
        raw = [str(value)]
    parts = []
    for item in raw:
        parts.extend(re.split(r"[,，;；]", item))
    return [p.strip() for p in parts if p.strip()]


def make_slug(title: str) -> str:
    """从标题里提取英文/数字，生成 URL 友好的短名。中文标题会返回空串。"""
    text = unicodedata.normalize("NFKD", str(title or ""))
    text = text.encode("ascii", "ignore").decode("ascii").lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text[:60].strip("-")


def build_filename(title: str, date_iso: str, existing: set) -> str:
    """生成不重复的文件名，形如 2026-10-06-hello-world.md"""
    slug = make_slug(title)
    if not slug:
        slug = "post-" + datetime.now(TIMEZONE).strftime("%Y%m%d-%H%M%S")
    day = (date_iso or "")[:10]
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", day):
        day = datetime.now(TIMEZONE).strftime("%Y-%m-%d")
    base = f"{day}-{slug}"
    name = base + ".md"
    n = 2
    while name in existing:
        name = f"{base}-{n}.md"
        n += 1
    return name


def build_post_text(meta: dict, body: str) -> str:
    """按照 Hugo 的 TOML front matter 格式拼出整个文件内容。"""
    lines = [
        "+++",
        "title = " + toml_quote(meta["title"]),
        "date = " + meta["date"],
        "draft = " + ("true" if meta["draft"] else "false"),
        "tags = [" + ", ".join(toml_quote(t) for t in meta["tags"]) + "]",
        "+++",
        "",
    ]
    text = "\n".join(lines)
    body = (body or "").strip()
    if body:
        text += body + "\n"
    return text


def payload_to_meta(data: dict) -> dict:
    title = str(data.get("title", "") or "").strip() or "未命名文章"
    return {
        "title": title,
        "date": normalize_date(data.get("date")),
        "draft": bool(data.get("draft", False)),
        "tags": parse_tags(data.get("tags")),
    }


# ============================================================ 路由

@app.get("/")
def index():
    return render_template("index.html")


@app.get("/api/posts")
def api_list_posts():
    """列出 content/posts 下所有 .md 文件。"""
    ensure_posts_dir()
    items = []
    for path in POSTS_DIR.glob("*.md"):
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            text = path.read_text(encoding="utf-8", errors="replace")
        meta, _ = parse_post(text)
        items.append({
            "filename": path.name,
            "title": meta["title"] or path.stem,
            "date": meta["date"],
            "draft": meta["draft"],
            "tags": meta["tags"],
        })
    items.sort(key=lambda x: (x["date"] or "", x["filename"]), reverse=True)
    return jsonify(items)


@app.get("/api/posts/<filename>")
def api_get_post(filename):
    """读取一篇文章。"""
    path = resolve_post_path(filename)
    if not path.exists():
        abort(404, description="文章不存在：" + filename)
    text = path.read_text(encoding="utf-8")
    meta, body = parse_post(text)
    return jsonify({
        "filename": path.name,
        "title": meta["title"],
        "date": meta["date"],
        "draft": meta["draft"],
        "tags": meta["tags"],
        "body": body,
    })


@app.post("/api/posts")
def api_create_post():
    """新建文章。"""
    data = request.get_json(silent=True) or {}
    meta = payload_to_meta(data)
    body = str(data.get("body", "") or "")

    ensure_posts_dir()
    existing = {p.name for p in POSTS_DIR.glob("*.md")}
    filename = build_filename(meta["title"], meta["date"], existing)

    path = POSTS_DIR / filename
    path.write_text(build_post_text(meta, body), encoding="utf-8")
    return jsonify({"filename": filename, "ok": True}), 201


@app.put("/api/posts/<filename>")
def api_update_post(filename):
    """保存（覆盖）一篇文章。"""
    path = resolve_post_path(filename)
    if not path.exists():
        abort(404, description="文章不存在：" + filename)

    data = request.get_json(silent=True) or {}
    meta = payload_to_meta(data)
    body = str(data.get("body", "") or "")

    path.write_text(build_post_text(meta, body), encoding="utf-8")
    return jsonify({"filename": path.name, "ok": True})


@app.errorhandler(400)
@app.errorhandler(404)
@app.errorhandler(500)
def handle_error(err):
    return jsonify({"error": getattr(err, "description", str(err))}), getattr(err, "code", 500)


# ============================================================ 启动

if __name__ == "__main__":
    ensure_posts_dir()
    print("=" * 62)
    print("  Hugo 文章编辑器")
    print("-" * 62)
    print(f"  项目根目录 : {PROJECT_DIR}")
    print(f"  文章目录   : {POSTS_DIR}")
    print(f"  访问地址   : http://{HOST}:{PORT}")
    print("-" * 62)
    print("  关闭这个窗口（或按 Ctrl+C）即可停止服务。")
    print("=" * 62)
    app.run(host=HOST, port=PORT, debug=False)