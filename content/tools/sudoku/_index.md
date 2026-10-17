---
title: "数独"
---

<style>
    /* ===== 暗色模式 ===== */
    html.dark .sudoku-btn,
    html.night .sudoku-btn,
    html.dark-mode .sudoku-btn,
    html[data-theme="dark"] .sudoku-btn,
    body.dark .sudoku-btn,
    body.night .sudoku-btn,
    body.dark-mode .sudoku-btn {
        color: #bbb;
        border-color: #444;
    }
    html.dark .sudoku-btn:hover,
    html.night .sudoku-btn:hover,
    html.dark-mode .sudoku-btn:hover,
    html[data-theme="dark"] .sudoku-btn:hover,
    body.dark .sudoku-btn:hover,
    body.night .sudoku-btn:hover,
    body.dark-mode .sudoku-btn:hover {
        color: #fff;
        border-color: #888;
    }
    html.dark .sudoku-btn.active,
    html.night .sudoku-btn.active,
    html.dark-mode .sudoku-btn.active,
    html[data-theme="dark"] .sudoku-btn.active,
    body.dark .sudoku-btn.active,
    body.night .sudoku-btn.active,
    body.dark-mode .sudoku-btn.active {
        background: #eee;
        color: #222;
        border-color: #eee;
    }

    html.dark #sudoku-board,
    html.night #sudoku-board,
    html.dark-mode #sudoku-board,
    html[data-theme="dark"] #sudoku-board,
    body.dark #sudoku-board,
    body.night #sudoku-board,
    body.dark-mode #sudoku-board {
        border-color: #888;
    }
    html.dark .sudoku-cell,
    html.night .sudoku-cell,
    html.dark-mode .sudoku-cell,
    html[data-theme="dark"] .sudoku-cell,
    body.dark .sudoku-cell,
    body.night .sudoku-cell,
    body.dark-mode .sudoku-cell {
        border-right-color: #3a3a3a;
        border-bottom-color: #3a3a3a;
        color: #7aa7ff;
    }
    html.dark .sudoku-cell.br,
    html.night .sudoku-cell.br,
    html.dark-mode .sudoku-cell.br,
    html[data-theme="dark"] .sudoku-cell.br,
    body.dark .sudoku-cell.br,
    body.night .sudoku-cell.br,
    body.dark-mode .sudoku-cell.br {
        border-right-color: #888;
    }
    html.dark .sudoku-cell.bb,
    html.night .sudoku-cell.bb,
    html.dark-mode .sudoku-cell.bb,
    html[data-theme="dark"] .sudoku-cell.bb,
    body.dark .sudoku-cell.bb,
    body.night .sudoku-cell.bb,
    body.dark-mode .sudoku-cell.bb {
        border-bottom-color: #888;
    }
    html.dark .sudoku-cell.given,
    html.night .sudoku-cell.given,
    html.dark-mode .sudoku-cell.given,
    html[data-theme="dark"] .sudoku-cell.given,
    body.dark .sudoku-cell.given,
    body.night .sudoku-cell.given,
    body.dark-mode .sudoku-cell.given {
        color: #eee;
    }
    html.dark .sudoku-cell.selected,
    html.night .sudoku-cell.selected,
    html.dark-mode .sudoku-cell.selected,
    html[data-theme="dark"] .sudoku-cell.selected,
    body.dark .sudoku-cell.selected,
    body.night .sudoku-cell.selected,
    body.dark-mode .sudoku-cell.selected {
        background: #3a4a6a;
    }
    html.dark .sudoku-cell.highlighted,
    html.night .sudoku-cell.highlighted,
    html.dark-mode .sudoku-cell.highlighted,
    html[data-theme="dark"] .sudoku-cell.highlighted,
    body.dark .sudoku-cell.highlighted,
    body.night .sudoku-cell.highlighted,
    body.dark-mode .sudoku-cell.highlighted {
        background: #2a2a2a;
    }
    html.dark .sudoku-cell.selected.highlighted,
    html.night .sudoku-cell.selected.highlighted,
    html.dark-mode .sudoku-cell.selected.highlighted,
    html[data-theme="dark"] .sudoku-cell.selected.highlighted,
    body.dark .sudoku-cell.selected.highlighted,
    body.night .sudoku-cell.selected.highlighted,
    body.dark-mode .sudoku-cell.selected.highlighted {
        background: #3a4a6a;
    }
    html.dark .sudoku-cell.conflict,
    html.night .sudoku-cell.conflict,
    html.dark-mode .sudoku-cell.conflict,
    html[data-theme="dark"] .sudoku-cell.conflict,
    body.dark .sudoku-cell.conflict,
    body.night .sudoku-cell.conflict,
    body.dark-mode .sudoku-cell.conflict {
        color: #ff6b6b;
    }

    html.dark .sudoku-num,
    html.night .sudoku-num,
    html.dark-mode .sudoku-num,
    html[data-theme="dark"] .sudoku-num,
    body.dark .sudoku-num,
    body.night .sudoku-num,
    body.dark-mode .sudoku-num {
        color: #ddd;
        border-color: #444;
    }
    html.dark .sudoku-num:hover,
    html.night .sudoku-num:hover,
    html.dark-mode .sudoku-num:hover,
    html[data-theme="dark"] .sudoku-num:hover,
    body.dark .sudoku-num:hover,
    body.night .sudoku-num:hover,
    body.dark-mode .sudoku-num:hover {
        border-color: #888;
        background: #2a2a2a;
    }

    html.dark #sudoku-status,
    html.night #sudoku-status,
    html.dark-mode #sudoku-status,
    html[data-theme="dark"] #sudoku-status,
    body.dark #sudoku-status,
    body.night #sudoku-status,
    body.dark-mode #sudoku-status {
        color: #888;
    }
    #sudoku-page {
        max-width: 560px;
        margin: 0 auto;
        padding: 40px 20px;
        text-align: center;
    }
    #sudoku-controls {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        justify-content: center;
        margin-bottom: 20px;
    }
    .sudoku-btn {
        background: none;
        border: 1px solid #ddd;
        border-radius: 6px;
        padding: 6px 14px;
        font-size: 0.9em;
        color: #666;
        cursor: pointer;
        font-family: inherit;
        transition: all 0.2s;
    }
    .sudoku-btn:hover {
        color: #222;
        border-color: #aaa;
    }
    .sudoku-btn.active {
        background: #333;
        color: #fff;
        border-color: #333;
    }
    #sudoku-board {
        display: grid;
        grid-template-columns: repeat(9, 44px);
        grid-template-rows: repeat(9, 44px);
        width: fit-content;
        margin: 0 auto 20px;
        border: 2px solid #333;
        user-select: none;
    }
    .sudoku-cell {
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.15em;
        border-right: 1px solid #ddd;
        border-bottom: 1px solid #ddd;
        cursor: pointer;
        transition: background 0.15s;
        color: #2a5db0;
        font-weight: 600;
    }
    .sudoku-cell:nth-child(9n) {
        border-right: none;
    }
    .sudoku-cell:nth-child(n+73) {
        border-bottom: none;
    }
    .sudoku-cell.br {
        border-right: 2px solid #333;
    }
    .sudoku-cell.bb {
        border-bottom: 2px solid #333;
    }
    .sudoku-cell.given {
        color: #222;
        font-weight: 700;
    }
    .sudoku-cell.selected {
        background: #d6e4ff;
    }
    .sudoku-cell.highlighted {
        background: #f0f0f0;
    }
    .sudoku-cell.selected.highlighted {
        background: #d6e4ff;
    }
    .sudoku-cell.conflict {
        color: #d32f2f;
    }
    #sudoku-numbers {
        display: grid;
        grid-template-columns: repeat(5, 48px);
        gap: 6px;
        justify-content: center;
        margin-bottom: 20px;
    }
    .sudoku-num {
        height: 48px;
        background: none;
        border: 1px solid #ddd;
        border-radius: 8px;
        font-size: 1.1em;
        color: #333;
        cursor: pointer;
        font-family: inherit;
        transition: all 0.2s;
    }
    .sudoku-num:hover {
        border-color: #999;
        background: #fafafa;
    }
    #sudoku-status {
        font-size: 0.9em;
        color: #888;
        min-height: 1.5em;
    }
    @media (max-width: 480px) {
        #sudoku-board {
            grid-template-columns: repeat(9, 34px);
            grid-template-rows: repeat(9, 34px);
        }
        .sudoku-cell {
            font-size: 0.95em;
        }
        #sudoku-numbers {
            grid-template-columns: repeat(5, 40px);
        }
        .sudoku-num {
            height: 40px;
        }
    }
</style>

<div id="sudoku-page">
<h1>数独</h1>

<div id="sudoku-controls">
<button class="sudoku-btn active" data-diff="easy">简单</button>
<button class="sudoku-btn" data-diff="medium">中等</button>
<button class="sudoku-btn" data-diff="hard">困难</button>
<button class="sudoku-btn" id="sudoku-check">检查</button>
<button class="sudoku-btn" id="sudoku-reveal">显示答案</button>
</div>

<div id="sudoku-board"></div>

<div id="sudoku-numbers">
<button class="sudoku-num" data-num="1">1</button>
<button class="sudoku-num" data-num="2">2</button>
<button class="sudoku-num" data-num="3">3</button>
<button class="sudoku-num" data-num="4">4</button>
<button class="sudoku-num" data-num="5">5</button>
<button class="sudoku-num" data-num="6">6</button>
<button class="sudoku-num" data-num="7">7</button>
<button class="sudoku-num" data-num="8">8</button>
<button class="sudoku-num" data-num="9">9</button>
<button class="sudoku-num" id="sudoku-clear">×</button>
</div>

<div id="sudoku-status"></div>
</div>

<script>
(function() {
    // ===== 工具函数 =====
    function shuffle(arr) {
        for (let i = arr.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [arr[i], arr[j]] = [arr[j], arr[i]];
        }
        return arr;
    }

    function isValid(grid, r, c, n) {
        for (let i = 0; i < 9; i++) {
            if (grid[r][i] === n) return false;
            if (grid[i][c] === n) return false;
        }
        const br = Math.floor(r / 3) * 3;
        const bc = Math.floor(c / 3) * 3;
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 3; j++) {
                if (grid[br + i][bc + j] === n) return false;
            }
        }
        return true;
    }

    function fillGrid(grid) {
        for (let r = 0; r < 9; r++) {
            for (let c = 0; c < 9; c++) {
                if (grid[r][c] === 0) {
                    const nums = shuffle([1,2,3,4,5,6,7,8,9]);
                    for (const n of nums) {
                        if (isValid(grid, r, c, n)) {
                            grid[r][c] = n;
                            if (fillGrid(grid)) return true;
                            grid[r][c] = 0;
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }

    function generateSolution() {
        const grid = Array.from({length: 9}, () => Array(9).fill(0));
        fillGrid(grid);
        return grid;
    }

    function digHoles(solution, holes) {
        const puzzle = solution.map(row => [...row]);
        const positions = shuffle([...Array(81).keys()]);
        for (let i = 0; i < holes && i < positions.length; i++) {
            const idx = positions[i];
            const r = Math.floor(idx / 9);
            const c = idx % 9;
            puzzle[r][c] = 0;
        }
        return puzzle;
    }

    // ===== 状态 =====
    let solution = null;
    let puzzle = null;
    let userGrid = null;
    let selected = { r: -1, c: -1 };

    const boardEl = document.getElementById('sudoku-board');
    const statusEl = document.getElementById('sudoku-status');

    // ===== 渲染 =====
    function render() {
        boardEl.innerHTML = '';
        for (let r = 0; r < 9; r++) {
            for (let c = 0; c < 9; c++) {
                const cell = document.createElement('div');
                cell.className = 'sudoku-cell';
                cell.dataset.r = r;
                cell.dataset.c = c;

                if (c === 2 || c === 5) cell.classList.add('br');
                if (r === 2 || r === 5) cell.classList.add('bb');

                const val = puzzle[r][c] !== 0 ? puzzle[r][c] : userGrid[r][c];
                if (puzzle[r][c] !== 0) {
                    cell.classList.add('given');
                    cell.textContent = puzzle[r][c];
                } else if (val !== 0) {
                    cell.textContent = val;
                }

                if (selected.r === r && selected.c === c) {
                    cell.classList.add('selected');
                } else if (selected.r >= 0) {
                    const sameRow = selected.r === r;
                    const sameCol = selected.c === c;
                    const sameBox = Math.floor(selected.r / 3) === Math.floor(r / 3) &&
                                    Math.floor(selected.c / 3) === Math.floor(c / 3);
                    if (sameRow || sameCol || sameBox) {
                        cell.classList.add('highlighted');
                    }
                }

                if (userGrid[r][c] !== 0 && hasConflict(r, c)) {
                    cell.classList.add('conflict');
                }

                cell.addEventListener('click', () => {
                    selected = { r, c };
                    render();
                });

                boardEl.appendChild(cell);
            }
        }
    }

    function hasConflict(r, c) {
        const n = userGrid[r][c];
        if (n === 0) return false;
        for (let i = 0; i < 9; i++) {
            if (i !== c && userGrid[r][i] === n) return true;
            if (i !== r && userGrid[i][c] === n) return true;
        }
        const br = Math.floor(r / 3) * 3;
        const bc = Math.floor(c / 3) * 3;
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 3; j++) {
                const rr = br + i, cc = bc + j;
                if ((rr !== r || cc !== c) && userGrid[rr][cc] === n) return true;
            }
        }
        return false;
    }

    // ===== 交互 =====
    function inputNumber(n) {
        if (selected.r < 0 || selected.c < 0) return;
        if (puzzle[selected.r][selected.c] !== 0) return;
        userGrid[selected.r][selected.c] = n;
        render();
    }

    function clearCell() {
        if (selected.r < 0 || selected.c < 0) return;
        if (puzzle[selected.r][selected.c] !== 0) return;
        userGrid[selected.r][selected.c] = 0;
        render();
    }

    // ===== 游戏流程 =====
    function newGame(difficulty) {
        statusEl.textContent = '生成中…';
        boardEl.innerHTML = '';

        setTimeout(() => {
            solution = generateSolution();
            const holes = {
                easy: 35,
                medium: 45,
                hard: 52
            }[difficulty] || 35;
            puzzle = digHoles(solution, holes);
            userGrid = Array.from({length: 9}, () => Array(9).fill(0));
            selected = { r: -1, c: -1 };
            statusEl.textContent = '';
            render();
        }, 30);
    }

    function checkAnswers() {
        let empty = 0;
        let conflict = 0;
        for (let r = 0; r < 9; r++) {
            for (let c = 0; c < 9; c++) {
                if (puzzle[r][c] !== 0) continue;
                const v = userGrid[r][c];
                if (v === 0) {
                    empty++;
                } else if (hasConflict(r, c)) {
                    conflict++;
                }
            }
        }
        if (empty === 0 && conflict === 0) {
            statusEl.textContent = '全部填满，没有冲突。';
        } else if (conflict > 0) {
            statusEl.textContent = `还有 ${empty} 个空格，${conflict} 处冲突。`;
        } else {
            statusEl.textContent = `还有 ${empty} 个空格。`;
        }
    }

    function revealSolution() {
        for (let r = 0; r < 9; r++) {
            for (let c = 0; c < 9; c++) {
                if (puzzle[r][c] === 0) {
                    userGrid[r][c] = solution[r][c];
                }
            }
        }
        statusEl.textContent = '已显示答案。';
        render();
    }

    // ===== 绑定 =====
    document.querySelectorAll('.sudoku-btn[data-diff]').forEach(btn => {
        btn.addEventListener('click', () => {
            document.querySelectorAll('.sudoku-btn[data-diff]').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            newGame(btn.dataset.diff);
        });
    });

    document.querySelectorAll('.sudoku-num[data-num]').forEach(btn => {
        btn.addEventListener('click', () => inputNumber(parseInt(btn.dataset.num, 10)));
    });

    document.getElementById('sudoku-clear').addEventListener('click', clearCell);
    document.getElementById('sudoku-check').addEventListener('click', checkAnswers);
    document.getElementById('sudoku-reveal').addEventListener('click', revealSolution);

    document.addEventListener('keydown', (e) => {
        if (e.key >= '1' && e.key <= '9') {
            inputNumber(parseInt(e.key, 10));
        } else if (e.key === 'Backspace' || e.key === 'Delete') {
            clearCell();
        } else if (e.key === 'ArrowUp' && selected.r > 0) {
            selected.r--; render();
        } else if (e.key === 'ArrowDown' && selected.r < 8) {
            selected.r++; render();
        } else if (e.key === 'ArrowLeft' && selected.c > 0) {
            selected.c--; render();
        } else if (e.key === 'ArrowRight' && selected.c < 8) {
            selected.c++; render();
        }
    });

    // 启动
    newGame('easy');
})();
</script>