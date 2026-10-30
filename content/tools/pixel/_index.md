---
title: "像素画板"
---

<style>
    #pixel-page {
        max-width: 720px;
        margin: 0 auto;
        padding: 40px 20px;
    }
    #pixel-page h1 {
        text-align: center;
        margin: 0 0 20px;
        font-size: 1.3em;
        color: #333;
    }
    #pixel-toolbar {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        justify-content: center;
        align-items: center;
        margin-bottom: 12px;
    }
    .px-btn {
        background: none;
        border: 1px solid #ddd;
        border-radius: 6px;
        padding: 8px 14px;
        font-size: 0.9em;
        color: #666;
        cursor: pointer;
        font-family: inherit;
        transition: all 0.2s;
        min-height: 40px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 4px;
    }
    .px-btn:hover {
        color: #222;
        border-color: #aaa;
    }
    .px-btn.active {
        background: #333;
        color: #fff;
        border-color: #333;
    }
    .px-btn:disabled {
        opacity: 0.35;
        cursor: not-allowed;
    }
    .px-btn.primary {
        background: #333;
        color: #fff;
        border-color: #333;
    }
    .px-btn.primary:hover {
        background: #000;
    }
    .px-toggle {
        cursor: pointer;
        gap: 6px;
    }
    .px-toggle input {
        margin: 0;
    }
    .px-color-wrap {
        position: relative;
        width: 40px;
        height: 40px;
        border-radius: 6px;
        border: 1px solid #ddd;
        overflow: hidden;
        cursor: pointer;
        flex-shrink: 0;
    }
    #pixel-color {
        position: absolute;
        inset: -8px;
        width: calc(100% + 16px);
        height: calc(100% + 16px);
        border: none;
        padding: 0;
        cursor: pointer;
        opacity: 0;
    }
    #pixel-color-preview {
        position: absolute;
        inset: 0;
        pointer-events: none;
        background: #000;
    }
    .px-color-wrap:hover {
        border-color: #999;
    }
    #pixel-swatches {
        display: flex;
        flex-wrap: wrap;
        gap: 4px;
        justify-content: center;
        margin-bottom: 16px;
    }
    .px-swatch {
        width: 24px;
        height: 24px;
        border-radius: 4px;
        border: 1px solid rgba(0,0,0,0.15);
        cursor: pointer;
        padding: 0;
        transition: transform 0.15s;
    }
    .px-swatch:hover {
        transform: scale(1.15);
    }
    .px-canvas-wrap {
        position: relative;
        width: 100%;
        max-width: 512px;
        aspect-ratio: 1 / 1;
        margin: 0 auto 16px;
        border: 1px solid #ddd;
        border-radius: 8px;
        overflow: hidden;
        background-color: #fff;
        background-image:
            linear-gradient(45deg, #ececec 25%, transparent 25%),
            linear-gradient(-45deg, #ececec 25%, transparent 25%),
            linear-gradient(45deg, transparent 75%, #ececec 75%),
            linear-gradient(-45deg, transparent 75%, #ececec 75%);
        background-size: 16px 16px;
        background-position: 0 0, 0 8px, 8px -8px, -8px 0px;
    }
    #pixel-canvas {
        display: block;
        width: 100%;
        height: 100%;
        image-rendering: pixelated;
        image-rendering: crisp-edges;
        touch-action: none;
        cursor: crosshair;
        -webkit-touch-callout: none;
        -webkit-user-select: none;
        user-select: none;
        position: relative;
        z-index: 1;
    }
    .px-grid {
        position: absolute;
        inset: 0;
        pointer-events: none;
        z-index: 2;
        display: none;
        background-image:
            repeating-linear-gradient(to right, rgba(0,0,0,0.12) 0 1px, transparent 1px calc(100%/32)),
            repeating-linear-gradient(to bottom, rgba(0,0,0,0.12) 0 1px, transparent 1px calc(100%/32));
    }
    .px-grid.visible {
        display: block;
    }
    #pixel-actions {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        justify-content: center;
        align-items: center;
    }
    .px-export-row {
        display: flex;
        gap: 8px;
        align-items: center;
    }
    #pixel-export-size {
        padding: 8px 10px;
        border: 1px solid #ddd;
        border-radius: 6px;
        font-family: inherit;
        font-size: 0.9em;
        color: #333;
        background: #fff;
        min-height: 40px;
        cursor: pointer;
    }
    #pixel-status {
        text-align: center;
        font-size: 0.85em;
        color: #999;
        min-height: 1.5em;
        margin-top: 12px;
    }
    @media (max-width: 480px) {
        .px-btn {
            padding: 6px 10px;
            font-size: 0.85em;
        }
        .px-swatch {
            width: 22px;
            height: 22px;
        }
    }
</style>

<div id="pixel-page">
<h1>像素画板</h1>

<div id="pixel-toolbar">
    <button class="px-btn active" data-tool="pencil" title="铅笔 (B)">✏️ 铅笔</button>
    <button class="px-btn" data-tool="eraser" title="橡皮 (E)">🧽 橡皮</button>
    <button class="px-btn" data-tool="bucket" title="油漆桶 (G)">🪣 填充</button>
    <button class="px-btn" data-tool="picker" title="取色器 (I)">💧 取色</button>
    <div class="px-color-wrap">
        <input type="color" id="pixel-color" value="#000000">
        <div id="pixel-color-preview"></div>
    </div>
</div>

<div id="pixel-swatches"></div>

<div class="px-canvas-wrap">
    <canvas id="pixel-canvas" width="32" height="32"></canvas>
    <div class="px-grid visible" id="pixel-grid"></div>
</div>

<div id="pixel-actions">
    <button class="px-btn" id="pixel-undo" title="撤销 (Ctrl+Z)" disabled>↶ 撤销</button>
    <button class="px-btn" id="pixel-redo" title="重做 (Ctrl+Y)" disabled>↷ 重做</button>
    <button class="px-btn" id="pixel-clear">🗑 清空</button>
    <label class="px-btn px-toggle">
        <input type="checkbox" id="pixel-grid-toggle" checked> 网格
    </label>
    <div class="px-export-row">
        <select id="pixel-export-size">
            <option value="1">64 × 64</option>
            <option value="2">128 × 128</option>
            <option value="4" selected>256 × 256</option>
            <option value="8">512 × 512</option>
            <option value="16">1024 × 1024</option>
        </select>
        <button class="px-btn primary" id="pixel-export">导出 PNG</button>
    </div>
</div>

<div id="pixel-status"></div>
</div>

<script>
(function() {
    const SIZE = 32;
    const STORAGE_KEY = 'pixel-art-32';
    const PICO8 = [
        '#000000','#1D2B53','#7E2553','#008751',
        '#AB5236','#5F574F','#C2C3C7','#FFF1E8',
        '#FF004D','#FFA300','#FFEC27','#00E436',
        '#29ADFF','#83769C','#FF77A8','#FFCCAA'
    ];

    const canvas = document.getElementById('pixel-canvas');
    const ctx = canvas.getContext('2d');
    const imgData = ctx.createImageData(SIZE, SIZE);
    const pixels = imgData.data;

    let currentTool = 'pencil';
    let currentColor = '#000000';
    let isDrawing = false;
    let lastPixel = null;
    const undoStack = [];
    const redoStack = [];
    const UNDO_MAX = 50;

    const statusEl = document.getElementById('pixel-status');
    const undoBtn = document.getElementById('pixel-undo');
    const redoBtn = document.getElementById('pixel-redo');
    const colorInput = document.getElementById('pixel-color');
    const colorPreview = document.getElementById('pixel-color-preview');
    const gridEl = document.getElementById('pixel-grid');
    const gridToggle = document.getElementById('pixel-grid-toggle');

    function hexToRgb(hex) {
        const m = /^#?([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})$/i.exec(hex);
        if (!m) return { r: 0, g: 0, b: 0 };
        return { r: parseInt(m[1], 16), g: parseInt(m[2], 16), b: parseInt(m[3], 16) };
    }
    function rgbToHex(r, g, b) {
        return '#' + [r, g, b].map(v => v.toString(16).padStart(2, '0')).join('');
    }

    function setPixel(x, y, rgba) {
        if (x < 0 || x >= SIZE || y < 0 || y >= SIZE) return false;
        const i = (y * SIZE + x) * 4;
        if (pixels[i] === rgba[0] && pixels[i+1] === rgba[1] && pixels[i+2] === rgba[2] && pixels[i+3] === rgba[3]) return false;
        pixels[i] = rgba[0];
        pixels[i+1] = rgba[1];
        pixels[i+2] = rgba[2];
        pixels[i+3] = rgba[3];
        return true;
    }
    function getPixel(x, y) {
        const i = (y * SIZE + x) * 4;
        return [pixels[i], pixels[i+1], pixels[i+2], pixels[i+3]];
    }

    function render() {
        ctx.putImageData(imgData, 0, 0);
    }

    function setColor(hex) {
        currentColor = hex;
        colorInput.value = hex;
        colorPreview.style.background = hex;
    }

    function setTool(tool) {
        currentTool = tool;
        document.querySelectorAll('#pixel-toolbar .px-btn[data-tool]').forEach(b => {
            b.classList.toggle('active', b.dataset.tool === tool);
        });
    }

    function updateButtons() {
        undoBtn.disabled = undoStack.length === 0;
        redoBtn.disabled = redoStack.length === 0;
    }

    function snapshot() {
        return new Uint8ClampedArray(pixels);
    }
    function pushUndo() {
        undoStack.push(snapshot());
        if (undoStack.length > UNDO_MAX) undoStack.shift();
        redoStack.length = 0;
        updateButtons();
    }
    function undo() {
        if (!undoStack.length) return;
        redoStack.push(snapshot());
        pixels.set(undoStack.pop());
        render();
        save();
        updateButtons();
    }
    function redo() {
        if (!redoStack.length) return;
        undoStack.push(snapshot());
        pixels.set(redoStack.pop());
        render();
        save();
        updateButtons();
    }

    function drawLine(x0, y0, x1, y1, fn) {
        let dx = Math.abs(x1 - x0), sx = x0 < x1 ? 1 : -1;
        let dy = -Math.abs(y1 - y0), sy = y0 < y1 ? 1 : -1;
        let err = dx + dy;
        while (true) {
            fn(x0, y0);
            if (x0 === x1 && y0 === y1) break;
            const e2 = 2 * err;
            if (e2 >= dy) { err += dy; x0 += sx; }
            if (e2 <= dx) { err += dx; y0 += sy; }
        }
    }

    function floodFill(x, y) {
        const target = getPixel(x, y);
        const c = hexToRgb(currentColor);
        const fill = [c.r, c.g, c.b, 255];
        if (target[0] === fill[0] && target[1] === fill[1] && target[2] === fill[2] && target[3] === fill[3]) return;
        const stack = [[x, y]];
        while (stack.length) {
            const [cx, cy] = stack.pop();
            if (cx < 0 || cx >= SIZE || cy < 0 || cy >= SIZE) continue;
            const p = getPixel(cx, cy);
            if (p[0] !== target[0] || p[1] !== target[1] || p[2] !== target[2] || p[3] !== target[3]) continue;
            setPixel(cx, cy, fill);
            stack.push([cx+1, cy], [cx-1, cy], [cx, cy+1], [cx, cy-1]);
        }
    }

    function applyTool(x, y) {
        if (currentTool === 'pencil') {
            const c = hexToRgb(currentColor);
            return setPixel(x, y, [c.r, c.g, c.b, 255]);
        }
        if (currentTool === 'eraser') {
            return setPixel(x, y, [0, 0, 0, 0]);
        }
        if (currentTool === 'picker') {
            const p = getPixel(x, y);
            if (p[3] > 0) {
                setColor(rgbToHex(p[0], p[1], p[2]));
                statusEl.textContent = `已取色 ${currentColor}`;
            }
            return false;
        }
        if (currentTool === 'bucket') {
            floodFill(x, y);
            return true;
        }
        return false;
    }

    function getPixelCoords(e) {
        const rect = canvas.getBoundingClientRect();
        const x = Math.floor((e.clientX - rect.left) / rect.width * SIZE);
        const y = Math.floor((e.clientY - rect.top) / rect.height * SIZE);
        return {
            x: Math.max(0, Math.min(SIZE - 1, x)),
            y: Math.max(0, Math.min(SIZE - 1, y))
        };
    }

    let saveTimer = null;
    function save() {
        clearTimeout(saveTimer);
        saveTimer = setTimeout(() => {
            try {
                localStorage.setItem(STORAGE_KEY, canvas.toDataURL('image/png'));
            } catch (e) {}
        }, 400);
    }

    function load() {
        try {
            const dataUrl = localStorage.getItem(STORAGE_KEY);
            if (!dataUrl) return;
            const img = new Image();
            img.onload = () => {
                const tmp = document.createElement('canvas');
                tmp.width = tmp.height = SIZE;
                const tctx = tmp.getContext('2d');
                tctx.drawImage(img, 0, 0);
                const data = tctx.getImageData(0, 0, SIZE, SIZE);
                pixels.set(data.data);
                render();
            };
            img.src = dataUrl;
        } catch (e) {}
    }

    // ===== 事件 =====
    canvas.addEventListener('pointerdown', (e) => {
        e.preventDefault();
        try { canvas.setPointerCapture(e.pointerId); } catch (err) {}
        const { x, y } = getPixelCoords(e);
        if (currentTool === 'picker') {
            applyTool(x, y);
            return;
        }
        pushUndo();
        if (currentTool === 'bucket') {
            applyTool(x, y);
            render();
            save();
            return;
        }
        isDrawing = true;
        lastPixel = { x, y };
        if (applyTool(x, y)) render();
    });

    canvas.addEventListener('pointermove', (e) => {
        if (!isDrawing) return;
        e.preventDefault();
        const { x, y } = getPixelCoords(e);
        if (lastPixel && (lastPixel.x !== x || lastPixel.y !== y)) {
            drawLine(lastPixel.x, lastPixel.y, x, y, (px, py) => applyTool(px, py));
            lastPixel = { x, y };
            render();
        }
    });

    function endDraw(e) {
        if (!isDrawing) return;
        isDrawing = false;
        lastPixel = null;
        save();
    }
    canvas.addEventListener('pointerup', endDraw);
    canvas.addEventListener('pointercancel', endDraw);
    canvas.addEventListener('contextmenu', (e) => e.preventDefault());

    document.querySelectorAll('#pixel-toolbar .px-btn[data-tool]').forEach(btn => {
        btn.addEventListener('click', () => setTool(btn.dataset.tool));
    });

    colorInput.addEventListener('input', (e) => setColor(e.target.value));

    // 色块
    const swatchEl = document.getElementById('pixel-swatches');
    PICO8.forEach(c => {
        const b = document.createElement('button');
        b.className = 'px-swatch';
        b.type = 'button';
        b.style.background = c;
        b.title = c;
        b.addEventListener('click', () => setColor(c));
        swatchEl.appendChild(b);
    });

    undoBtn.addEventListener('click', undo);
    redoBtn.addEventListener('click', redo);

    document.getElementById('pixel-clear').addEventListener('click', () => {
        pushUndo();
        pixels.fill(0);
        render();
        save();
    });

    gridToggle.addEventListener('change', () => {
        gridEl.classList.toggle('visible', gridToggle.checked);
    });

    document.getElementById('pixel-export').addEventListener('click', () => {
        const scale = parseInt(document.getElementById('pixel-export-size').value, 10);
        const out = document.createElement('canvas');
        out.width = out.height = SIZE * scale;
        const octx = out.getContext('2d');
        octx.imageSmoothingEnabled = false;
        octx.drawImage(canvas, 0, 0, SIZE * scale, SIZE * scale);
        out.toBlob(blob => {
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `pixel-art-${SIZE}x${SIZE}-x${scale}.png`;
            document.body.appendChild(a);
            a.click();
            a.remove();
            setTimeout(() => URL.revokeObjectURL(url), 1000);
            statusEl.textContent = `已导出 ${SIZE * scale} × ${SIZE * scale}`;
        }, 'image/png');
    });

    document.addEventListener('keydown', (e) => {
        if (e.target && (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA' || e.target.tagName === 'SELECT')) return;
        if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'z') {
            e.preventDefault();
            if (e.shiftKey) redo(); else undo();
        } else if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'y') {
            e.preventDefault();
            redo();
        } else if (e.key === 'b' || e.key === 'B') setTool('pencil');
        else if (e.key === 'e' || e.key === 'E') setTool('eraser');
        else if (e.key === 'g' || e.key === 'G') setTool('bucket');
        else if (e.key === 'i' || e.key === 'I') setTool('picker');
    });

    // 启动
    setColor(currentColor);
    setTool('pencil');
    updateButtons();
    render();
    load();
})();
</script>