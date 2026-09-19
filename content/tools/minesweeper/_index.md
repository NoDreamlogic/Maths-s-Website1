---
title: "扫雷"
---

<style>
    #minesweeper-page {
        max-width: 700px;
        margin: 0 auto;
        padding: 40px 20px;
        text-align: center;
    }
    #mine-settings {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        justify-content: center;
        align-items: flex-end;
        margin: 20px 0;
    }
    #mine-settings label {
        display: flex;
        flex-direction: column;
        font-size: 0.85em;
        color: #666;
        gap: 4px;
    }
    #mine-settings input {
        width: 80px;
        box-sizing: border-box;
        padding: 6px 8px;
        border: 1px solid #ddd;
        border-radius: 6px;
        font-size: 0.95em;
        text-align: center;
        font-family: inherit;
    }
    #mine-settings button {
        background: #333;
        color: #fff;
        border: 1px solid #333;
        border-radius: 6px;
        padding: 8px 20px;
        font-size: 0.95em;
        cursor: pointer;
        font-family: inherit;
        transition: background 0.2s;
    }
    #mine-settings button:hover {
        background: #000;
    }
    #minesweeper-info {
        display: flex;
        justify-content: center;
        gap: 24px;
        align-items: center;
        margin: 16px 0;
        font-size: 0.95em;
        color: #666;
    }
    #mine-status { font-weight: 600; color: #333; }
    #minesweeper-board {
        display: grid;
        gap: 2px;
        justify-content: center;
        margin: 20px auto 0;
        user-select: none;
    }
    .mine-cell {
        background: #e8e8e8;
        border-radius: 4px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 600;
        cursor: pointer;
        transition: background 0.15s;
        font-size: 0.85em;
    }
    .mine-cell:hover { background: #dcdcdc; }
    .mine-cell.revealed {
        background: #f5f5f5;
        cursor: default;
    }
    .mine-cell.revealed:hover { background: #f5f5f5; }
    .mine-cell.mine { background: #ffdddd; }
    .mine-cell.n1 { color: #1976d2; }
    .mine-cell.n2 { color: #388e3c; }
    .mine-cell.n3 { color: #d32f2f; }
    .mine-cell.n4 { color: #7b1fa2; }
    .mine-cell.n5 { color: #f57c00; }
    .mine-cell.n6 { color: #0097a7; }
    .mine-cell.n7 { color: #5d4037; }
    .mine-cell.n8 { color: #455a64; }
    .mine-help {
        margin-top: 20px;
        font-size: 0.85em;
        color: #999;
    }
</style>

<div id="minesweeper-page">
<h1>扫雷</h1>

<div id="mine-settings">
<label>
行数
<input type="number" id="mine-rows" value="9" min="5" max="30">
</label>
<label>
列数
<input type="number" id="mine-cols" value="9" min="5" max="30">
</label>
<label>
雷数
<input type="number" id="mine-mines" value="10" min="1">
</label>
<button id="mine-start">开始新游戏</button>
</div>

<div id="minesweeper-info">
<span>剩余雷数：<span id="mine-flag-count">10</span></span>
<span>状态：<span id="mine-status">进行中</span></span>
</div>

<div id="minesweeper-board"></div>

<p class="mine-help">左键翻开，右键标记旗子。翻开所有非雷格子即胜利。</p>
</div>

<script>
(function() {
    let ROWS = 9;
    let COLS = 9;
    let MINES = 10;

    const CELL_SIZE = 34;

    let board = [];
    let revealed = [];
    let flagged = [];
    let gameOver = false;
    let firstClick = true;
    let flagsUsed = 0;

    const boardEl = document.getElementById('minesweeper-board');
    const flagCountEl = document.getElementById('mine-flag-count');
    const statusEl = document.getElementById('mine-status');
    const rowsInput = document.getElementById('mine-rows');
    const colsInput = document.getElementById('mine-cols');
    const minesInput = document.getElementById('mine-mines');

    function readSettings() {
        let r = parseInt(rowsInput.value, 10);
        let c = parseInt(colsInput.value, 10);
        let m = parseInt(minesInput.value, 10);

        if (isNaN(r) || r < 5) r = 5;
        if (isNaN(c) || c < 5) c = 5;
        if (r > 30) r = 30;
        if (c > 30) c = 30;

        const maxMines = r * c - 9;
        if (isNaN(m) || m < 1) m = 1;
        if (m > maxMines) m = maxMines;

        rowsInput.value = r;
        colsInput.value = c;
        minesInput.value = m;

        ROWS = r;
        COLS = c;
        MINES = m;
    }

    function init() {
        readSettings();

        board = Array.from({ length: ROWS }, () => Array(COLS).fill(0));
        revealed = Array.from({ length: ROWS }, () => Array(COLS).fill(false));
        flagged = Array.from({ length: ROWS }, () => Array(COLS).fill(false));
        gameOver = false;
        firstClick = true;
        flagsUsed = 0;
        flagCountEl.textContent = MINES;
        statusEl.textContent = '进行中';

        boardEl.style.gridTemplateColumns = `repeat(${COLS}, ${CELL_SIZE}px)`;
        render();
    }

    function placeMines(sr, sc) {
        let placed = 0;
        while (placed < MINES) {
            const r = Math.floor(Math.random() * ROWS);
            const c = Math.floor(Math.random() * COLS);
            if (board[r][c] === -1) continue;
            if (Math.abs(r - sr) <= 1 && Math.abs(c - sc) <= 1) continue;
            board[r][c] = -1;
            placed++;
        }
        for (let r = 0; r < ROWS; r++) {
            for (let c = 0; c < COLS; c++) {
                if (board[r][c] === -1) continue;
                let count = 0;
                for (let dr = -1; dr <= 1; dr++) {
                    for (let dc = -1; dc <= 1; dc++) {
                        if (dr === 0 && dc === 0) continue;
                        const nr = r + dr, nc = c + dc;
                        if (nr >= 0 && nr < ROWS && nc >= 0 && nc < COLS && board[nr][nc] === -1) count++;
                    }
                }
                board[r][c] = count;
            }
        }
    }

    function reveal(r, c) {
        if (gameOver) return;
        if (r < 0 || r >= ROWS || c < 0 || c >= COLS) return;
        if (revealed[r][c] || flagged[r][c]) return;
        revealed[r][c] = true;
        if (board[r][c] === -1) {
            gameOver = true;
            statusEl.textContent = '踩到雷了';
            for (let rr = 0; rr < ROWS; rr++) {
                for (let cc = 0; cc < COLS; cc++) {
                    if (board[rr][cc] === -1) revealed[rr][cc] = true;
                }
            }
            return;
        }
        if (board[r][c] === 0) {
            for (let dr = -1; dr <= 1; dr++) {
                for (let dc = -1; dc <= 1; dc++) {
                    if (dr === 0 && dc === 0) continue;
                    reveal(r + dr, c + dc);
                }
            }
        }
    }

    function checkWin() {
        for (let r = 0; r < ROWS; r++) {
            for (let c = 0; c < COLS; c++) {
                if (board[r][c] !== -1 && !revealed[r][c]) return false;
            }
        }
        return true;
    }

    function handleClick(r, c) {
        if (gameOver || flagged[r][c]) return;
        if (firstClick) {
            firstClick = false;
            placeMines(r, c);
        }
        reveal(r, c);
        if (!gameOver && checkWin()) {
            gameOver = true;
            statusEl.textContent = '胜利！';
        }
        render();
    }

    function handleRightClick(r, c) {
        if (gameOver || revealed[r][c]) return;
        flagged[r][c] = !flagged[r][c];
        flagsUsed += flagged[r][c] ? 1 : -1;
        flagCountEl.textContent = MINES - flagsUsed;
        render();
    }

    function render() {
        boardEl.innerHTML = '';
        for (let r = 0; r < ROWS; r++) {
            for (let c = 0; c < COLS; c++) {
                const cell = document.createElement('div');
                cell.className = 'mine-cell';
                cell.style.width = CELL_SIZE + 'px';
                cell.style.height = CELL_SIZE + 'px';
                if (revealed[r][c]) {
                    cell.classList.add('revealed');
                    if (board[r][c] === -1) {
                        cell.classList.add('mine');
                        cell.textContent = '💣';
                    } else if (board[r][c] > 0) {
                        cell.textContent = board[r][c];
                        cell.classList.add('n' + board[r][c]);
                    }
                } else if (flagged[r][c]) {
                    cell.textContent = '🚩';
                }
                cell.addEventListener('click', () => handleClick(r, c));
                cell.addEventListener('contextmenu', (e) => {
                    e.preventDefault();
                    handleRightClick(r, c);
                });
                boardEl.appendChild(cell);
            }
        }
    }

    document.getElementById('mine-start').addEventListener('click', init);
    init();
})();
</script>