---
title: "小工具们"
---

<style>
    #tools-page {
        max-width: 1200px;
        margin: 0 auto;
        padding: 40px 20px;
    }
    .tool-grid {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 16px;
        margin-top: 24px;
    }
    @media (max-width: 900px) {
        .tool-grid { grid-template-columns: repeat(3, 1fr); }
    }
    @media (max-width: 600px) {
        .tool-grid { grid-template-columns: repeat(2, 1fr); }
    }
    .tool-card {
        display: flex;
        align-items: center;
        justify-content: center;
        aspect-ratio: 1 / 1;
        padding: 16px;
        background-color: #fafafa;
        background-size: cover;
        background-position: center;
        border: 1px solid #eee;
        border-radius: 12px;
        text-align: center;
        color: #fff;
        text-shadow: 0 1px 3px rgba(0, 0, 0, .6);
        text-decoration: none;
        cursor: pointer;
        transition: all 0.2s;
        font-size: 1em;
        letter-spacing: 0.05em;
        position: relative;
    }

    /* 半透明遮罩，让文字可读 */
    .tool-card::before {
        content: "";
        position: absolute;
        inset: 0;
        background: rgba(0, 0, 0, 0.5);
        border-radius: 12px;
        z-index: 0;
    }
    .tool-card > * {
        position: relative;
        z-index: 1;
    }
    .tool-card:hover::before {
        background: rgba(0, 0, 0, 0.35);
    }
    .tool-card:hover {
        border-color: #ccc;
        transform: translateY(-2px);
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
    }

    /* 每张卡片各自的背景图 */
    .tool-card[data-tool="oracle"] {
        background-image: url('/images/tools/oracle.jpg');
    }
    .tool-card[data-tool="random"] {
        background-image: url('/images/tools/random.jpg');
    }
    .tool-card[data-tool="guess"] {
        background-image: url('/images/tools/guess.jpg');
    }
    .tool-card[data-bg="minesweeper"] {
        background-image: url('/images/tools/minesweeper.jpg');
    }
    .tool-card[data-bg="ruogelike"] {
        background-image: url('/images/tools/ruogelike.jpg');
    }
    .tool-card[data-bg="sudoku"] {
        background-image: url('/images/tools/sudoku.jpg');
    }
    .tool-card[data-bg="pixel"] {
        background-image: url('/images/tools/pixel.jpg');
    }

    /* 弹窗通用 */
    .tool-modal {
        display: none;
        position: fixed;
        inset: 0;
        background: rgba(0, 0, 0, 0.7);
        z-index: 100;
        align-items: center;
        justify-content: center;
    }
    .tool-modal.active { display: flex; }
    .tool-panel {
        background: #fff;
        border-radius: 16px;
        padding: 36px 32px;
        max-width: 500px;
        width: 90%;
        text-align: center;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
    }

    /* 占卜 */
    #oracle-hint { margin: 0 0 24px; color: #888; font-size: 0.95em; }
    #oracle-cards { display: flex; justify-content: center; margin-bottom: 20px; padding-top: 10px; padding-bottom: 60px; }
    .oracle-card { width: 60px; height: 90px; perspective: 600px; cursor: pointer; transition: transform 0.4s ease, opacity 0.4s ease; margin-left: -25px; position: relative; }
    .oracle-card:first-child { margin-left: 0; }
    .oracle-card:hover:not(.disabled) { transform: translateY(12px); z-index: 5; }
    .oracle-card.drawn { transform: translateY(35px); z-index: 10; }
    .oracle-card.disabled { pointer-events: none; }
    .oracle-card.dimmed { opacity: 0.15; }
    .oracle-card-inner { position: relative; width: 100%; height: 100%; transition: transform 0.6s ease; transform-style: preserve-3d; }
    .oracle-card.flipped .oracle-card-inner { transform: rotateY(180deg); }
    .oracle-card-front, .oracle-card-back { position: absolute; inset: 0; backface-visibility: hidden; border-radius: 8px; display: flex; align-items: center; justify-content: center; }
    .oracle-card-back { background-image: url('/images/back.png'); background-size: cover; background-position: center; background-color: #2a2a2a; }
    .oracle-card-front { background: #fff; border: 1px solid #ddd; transform: rotateY(180deg); font-size: 0.75em; padding: 6px; text-align: center; color: #333; line-height: 1.3; overflow: hidden; word-break: break-all; }
    #oracle-result { opacity: 0; transition: opacity 0.5s; margin-bottom: 20px; }
    #oracle-result.show { opacity: 1; }
    #oracle-result-level { font-size: 0.8em; letter-spacing: 0.3em; color: #999; margin-bottom: 12px; min-height: 1.2em; }
    #oracle-result-text { font-size: 1.05em; line-height: 1.8; color: #333; margin: 0; }

    /* 骰子 */
    #random-panel { max-width: 520px; }
    .dice-quick-row { display: flex; flex-wrap: wrap; gap: 6px; justify-content: center; margin-bottom: 14px; }
    .dice-quick { padding: 6px 12px; border: 1px solid #ddd; border-radius: 6px; background: #fafafa; color: #333; cursor: pointer; font-family: inherit; font-size: 0.9em; transition: all 0.2s; }
    .dice-quick:hover { background: #f0f0f0; border-color: #aaa; }
    .dice-input-row { display: flex; gap: 8px; margin-bottom: 12px; }
    #dice-expression { flex: 1; padding: 8px 10px; border: 1px solid #ddd; border-radius: 6px; font-size: 1em; font-family: inherit; text-align: center; min-width: 0; }
    .dice-extra-row { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; justify-content: center; margin-bottom: 12px; }
    .dice-times-label { font-size: 0.85em; color: #888; display: flex; align-items: center; gap: 4px; }
    #dice-times { width: 56px; padding: 6px; border: 1px solid #ddd; border-radius: 6px; font-family: inherit; text-align: center; }
    .dice-target-row { margin-bottom: 14px; font-size: 0.85em; color: #888; }
    #dice-target { width: 100px; padding: 6px; border: 1px solid #ddd; border-radius: 6px; font-family: inherit; text-align: center; margin-left: 4px; }
    #dice-result { min-height: 60px; margin-bottom: 14px; }
    .dice-formula { font-size: 0.85em; color: #999; margin-bottom: 8px; }
    .dice-rolls { display: flex; flex-wrap: wrap; gap: 4px; justify-content: center; margin-bottom: 8px; }
    .dice-chip { min-width: 32px; height: 32px; padding: 0 6px; border: 1px solid #ddd; border-radius: 6px; background: #fafafa; display: flex; align-items: center; justify-content: center; font-weight: 600; font-size: 0.95em; }
    .dice-chip.discarded { opacity: 0.35; text-decoration: line-through; }
    .dice-chip.kept { border-color: #333; background: #333; color: #fff; }
    .dice-modifier { font-size: 0.9em; color: #666; margin-bottom: 4px; }
    .dice-total { font-size: 2.2em; font-weight: 700; color: #222; line-height: 1.1; }
    .dice-total-inline { font-weight: 700; color: #222; }
    .dice-multi-row { padding: 4px 0; border-bottom: 1px dashed #eee; font-size: 0.95em; color: #666; }
    .dice-multi-row:last-child { border-bottom: none; }
    .dice-target.success { color: #2e7d32; font-weight: 600; margin-top: 6px; }
    .dice-target.fail { color: #c62828; font-weight: 600; margin-top: 6px; }
    .dice-error { color: #c62828; font-size: 0.9em; }
    #dice-history { max-height: 120px; overflow-y: auto; border-top: 1px dashed #eee; padding-top: 8px; margin-bottom: 14px; font-size: 0.8em; color: #999; text-align: left; }
    .dice-history-item { padding: 3px 0; }

    /* 猜数字 */
    #guess-input-row { display: flex; gap: 10px; justify-content: center; margin: 16px 0; }
    #guess-input { width: 120px; box-sizing: border-box; padding: 8px 10px; border: 1px solid #ddd; border-radius: 6px; font-size: 1em; text-align: center; font-family: inherit; }
    #guess-input:disabled { opacity: 0.5; }
    #guess-feedback { min-height: 1.6em; color: #333; font-size: 0.95em; margin: 0 0 16px; }

    /* 按钮 */
    .tool-actions { display: flex; gap: 10px; justify-content: center; }
    .tool-btn { background: none; border: 1px solid #ddd; border-radius: 6px; padding: 8px 24px; font-size: 0.95em; color: #888; cursor: pointer; font-family: inherit; transition: all 0.2s; }
    .tool-btn:hover { color: #333; border-color: #aaa; }
    .tool-btn.primary { background: #333; color: #fff; border-color: #333; }
    .tool-btn.primary:hover { background: #000; }
</style>

<div id="tools-page">
<h1>小工具们</h1>
<p>选择进入你喜欢的工具。</p>

<div class="tool-grid">
<div class="tool-card" data-tool="oracle">未知的命运</div>
<div class="tool-card" data-tool="random">遵从骰子之意</div>
<div class="tool-card" data-tool="guess">猜数字</div>
<a href="/tools/minesweeper/" class="tool-card" data-bg="minesweeper">雷区扫荡</a>
<a href="/tools/ruogelike/" class="tool-card" data-bg="ruogelike">我爱打牌</a>
<a href="/tools/sudoku/" class="tool-card" data-bg="sudoku">益智数学</a>
<a href="/tools/pixel/" class="tool-card" data-bg="pixel">像素画板</a>
</div>
</div>

<div id="oracle-modal" class="tool-modal" role="dialog" aria-modal="true" aria-labelledby="oracle-hint">
<div class="tool-panel">
<p id="oracle-hint">选择一个观测的视角。</p>
<div id="oracle-cards"></div>
<div id="oracle-result">
<div id="oracle-result-level"></div>
<p id="oracle-result-text"></p>
</div>
<div class="tool-actions">
<button class="tool-btn" id="oracle-close">关闭</button>
</div>
</div>
</div>

<div id="random-modal" class="tool-modal" role="dialog" aria-modal="true" aria-labelledby="random-panel-title">
<div class="tool-panel" id="random-panel">
<h3 id="random-panel-title">骰子的意愿</h3>
<div class="dice-quick-row">
<button class="dice-quick" data-sides="4">d4</button>
<button class="dice-quick" data-sides="6">d6</button>
<button class="dice-quick" data-sides="8">d8</button>
<button class="dice-quick" data-sides="10">d10</button>
<button class="dice-quick" data-sides="12">d12</button>
<button class="dice-quick" data-sides="20">d20</button>
<button class="dice-quick" data-sides="100">d100</button>
</div>
<div class="dice-input-row">
<input type="text" id="dice-expression" value="1d20" placeholder="如 2d6+3、1d20、2d20kh1" autocomplete="off">
<button class="tool-btn primary" id="dice-roll">掷骰</button>
</div>
<div class="dice-extra-row">
<button class="tool-btn" id="dice-adv">优势 d20</button>
<button class="tool-btn" id="dice-dis">劣势 d20</button>
<label class="dice-times-label">次数 <input type="number" id="dice-times" value="1" min="1" max="20"></label>
<button class="tool-btn" id="dice-roll-times">掷 N 次</button>
</div>
<div class="dice-target-row">
成功判定（可选）目标值 <input type="number" id="dice-target" placeholder="留空不判定">
</div>
<div id="dice-result"></div>
<div id="dice-history"></div>
<div class="tool-actions">
<button class="tool-btn" id="random-close">关闭</button>
</div>
</div>
</div>

<div id="guess-modal" class="tool-modal" role="dialog" aria-modal="true" aria-labelledby="guess-hint">
<div class="tool-panel">
<h3 id="guess-hint">猜数字</h3>
<p id="guess-hint-text">我想了一个 1 到 100 之间的数字。</p>
<div id="guess-input-row">
<input type="number" id="guess-input" min="1" max="100" placeholder="输入数字">
<button class="tool-btn primary" id="guess-submit">猜</button>
</div>
<p id="guess-feedback"></p>
<div class="tool-actions">
<button class="tool-btn" id="guess-restart">重新开始</button>
<button class="tool-btn" id="guess-close">关闭</button>
</div>
</div>
</div>

<script>
let oracleItems = [];

fetch('/data/oracle.json')
    .then(res => res.json())
    .then(data => { oracleItems = Array.isArray(data) ? data : []; })
    .catch(err => console.error('占卜数据加载失败', err));

const oracleModal = document.getElementById('oracle-modal');
const oracleCardsEl = document.getElementById('oracle-cards');
const oracleResult = document.getElementById('oracle-result');
const oracleResultLevel = document.getElementById('oracle-result-level');
const oracleResultText = document.getElementById('oracle-result-text');
const oracleHint = document.getElementById('oracle-hint');

function lockScroll(lock) {
    document.body.style.overflow = lock ? 'hidden' : '';
}

function openOracle() {
    if (oracleItems.length === 0) return;
    oracleResult.classList.remove('show');
    oracleResultLevel.textContent = '';
    oracleResultText.textContent = '';
    oracleHint.textContent = '选择一个观测的视角。';
    oracleHint.style.display = '';

    oracleCardsEl.innerHTML = '';
    for (let i = 0; i < 5; i++) {
        const card = document.createElement('div');
        card.className = 'oracle-card';
        card.setAttribute('role', 'button');
        card.setAttribute('tabindex', '0');
        card.innerHTML = '<div class="oracle-card-inner"><div class="oracle-card-back"></div><div class="oracle-card-front"></div></div>';
        card.addEventListener('click', () => pickCard(card));
        card.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); pickCard(card); }
        });
        oracleCardsEl.appendChild(card);
    }
    oracleModal.classList.add('active');
    lockScroll(true);
}

function pickCard(card) {
    if (card.classList.contains('flipped') || card.classList.contains('drawn')) return;
    const allCards = oracleCardsEl.querySelectorAll('.oracle-card');
    allCards.forEach(c => c.classList.add('disabled'));

    const item = oracleItems[Math.floor(Math.random() * oracleItems.length)];
    const front = card.querySelector('.oracle-card-front');
    if (front) front.textContent = item.name;

    card.classList.add('drawn');
    allCards.forEach(c => { if (c !== card) c.classList.add('dimmed'); });

    setTimeout(() => {
        if (!card.isConnected) return;
        card.classList.add('flipped');
    }, 400);
    setTimeout(() => {
        if (!card.isConnected) return;
        oracleHint.style.display = 'none';
        oracleResultLevel.textContent = item.name || '';
        oracleResultText.textContent = item.text;
        oracleResult.classList.add('show');
    }, 1000);
}

/* ===== 骰子 ===== */
const randomModal = document.getElementById('random-modal');
const diceExpression = document.getElementById('dice-expression');
const diceResult = document.getElementById('dice-result');
const diceHistory = document.getElementById('dice-history');
const diceTarget = document.getElementById('dice-target');
const diceTimes = document.getElementById('dice-times');
const diceHistoryList = [];

const DICE_MAX = 100;

function rollDie(sides) {
    return Math.floor(Math.random() * sides) + 1;
}

function parseExpression(expr) {
    expr = String(expr || '').trim().toLowerCase().replace(/\s+/g, '');
    if (!expr) return null;
    if (/^\d+$/.test(expr)) {
        const n = parseInt(expr, 10);
        return { count: 0, sides: 0, modifier: n, keep: null };
    }
    const m = expr.match(/^(\d*)d(\d+)(kh1|kl1)?([+-]\d+)?$/);
    if (!m) return null;
    let count = m[1] ? parseInt(m[1], 10) : 1;
    const sides = parseInt(m[2], 10);
    const keep = m[3] || null;
    const modifier = m[4] ? parseInt(m[4], 10) : 0;
    if (count < 1) count = 1;
    if (count > DICE_MAX) count = DICE_MAX;
    if (sides < 2 || sides > 1000) return null;
    return { count, sides, modifier, keep };
}

function rollExpression(parsed) {
    if (!parsed) return null;
    if (parsed.sides === 0) {
        return { parsed, rolls: [], kept: [], total: parsed.modifier, modifier: parsed.modifier };
    }
    const rolls = [];
    for (let i = 0; i < parsed.count; i++) rolls.push(rollDie(parsed.sides));
    let kept;
    if (parsed.keep === 'kh1') {
        const max = Math.max(...rolls);
        let found = false;
        kept = rolls.map((v, i) => {
            if (!found && v === max) { found = true; return { value: v, index: i, keep: true }; }
            return { value: v, index: i, keep: false };
        });
    } else if (parsed.keep === 'kl1') {
        const min = Math.min(...rolls);
        let found = false;
        kept = rolls.map((v, i) => {
            if (!found && v === min) { found = true; return { value: v, index: i, keep: true }; }
            return { value: v, index: i, keep: false };
        });
    } else {
        kept = rolls.map((v, i) => ({ value: v, index: i }));
    }
    const keptSum = kept.filter(x => x.keep !== false).reduce((s, x) => s + x.value, 0);
    return { parsed, rolls, kept, total: keptSum + parsed.modifier, modifier: parsed.modifier };
}

function diceLabel(parsed) {
    if (parsed.sides === 0) return String(parsed.modifier);
    let s = `${parsed.count}d${parsed.sides}`;
    if (parsed.keep) s += parsed.keep;
    if (parsed.modifier) s += (parsed.modifier > 0 ? '+' : '') + parsed.modifier;
    return s;
}

function renderDiceResult(result) {
    if (!result) { diceResult.innerHTML = '<div class="dice-error">表达式无效</div>'; return; }
    const { parsed, kept, total } = result;
    const target = parseInt(diceTarget.value, 10);
    let html = '';
    if (parsed.sides === 0) {
        html = `<div class="dice-total">${total}</div>`;
    } else {
        html += `<div class="dice-formula">${diceLabel(parsed)}</div>`;
        html += '<div class="dice-rolls">';
        kept.forEach(item => {
            const cls = item.keep === false ? 'discarded' : (parsed.keep ? 'kept' : '');
            html += `<span class="dice-chip ${cls}">${item.value}</span>`;
        });
        html += '</div>';
        if (parsed.modifier) {
            html += `<div class="dice-modifier">${parsed.modifier > 0 ? '+' : ''}${parsed.modifier}</div>`;
        }
        html += `<div class="dice-total">${total}</div>`;
    }
    if (!isNaN(target)) {
        const success = total >= target;
        html += `<div class="dice-target ${success ? 'success' : 'fail'}">${success ? '成功' : '失败'}（目标 ${target}）</div>`;
    }
    diceResult.innerHTML = html;
}

function addDiceHistory(result) {
    if (!result) return;
    diceHistoryList.unshift(`${diceLabel(result.parsed)} = ${result.total}`);
    if (diceHistoryList.length > 10) diceHistoryList.pop();
    diceHistory.innerHTML = diceHistoryList.map(e => `<div class="dice-history-item">${e}</div>`).join('');
}

function rollDice() {
    const parsed = parseExpression(diceExpression.value);
    if (!parsed) { diceResult.innerHTML = '<div class="dice-error">表达式无效，试试 2d6+3、1d20、2d20kh1</div>'; return; }
    const result = rollExpression(parsed);
    renderDiceResult(result);
    addDiceHistory(result);
}

function rollDiceTimes() {
    const times = Math.max(1, Math.min(20, parseInt(diceTimes.value, 10) || 1));
    const parsed = parseExpression(diceExpression.value);
    if (!parsed) { diceResult.innerHTML = '<div class="dice-error">表达式无效，试试 2d6+3、1d20、2d20kh1</div>'; return; }
    const target = parseInt(diceTarget.value, 10);
    let html = '';
    for (let i = 0; i < times; i++) {
        const result = rollExpression(parsed);
        addDiceHistory(result);
        let extra = '';
        if (!isNaN(target)) {
            const success = result.total >= target;
            extra = ` <span class="dice-target ${success ? 'success' : 'fail'}" style="display:inline;font-size:0.85em;margin-left:6px;">${success ? '成功' : '失败'}</span>`;
        }
        html += `<div class="dice-multi-row">第 ${i + 1} 次：<span class="dice-total-inline">${result.total}</span>${extra}</div>`;
    }
    diceResult.innerHTML = html;
}

document.querySelectorAll('.dice-quick').forEach(btn => {
    btn.addEventListener('click', () => {
        diceExpression.value = '1d' + btn.dataset.sides;
        rollDice();
    });
});
document.getElementById('dice-adv').addEventListener('click', () => { diceExpression.value = '2d20kh1'; rollDice(); });
document.getElementById('dice-dis').addEventListener('click', () => { diceExpression.value = '2d20kl1'; rollDice(); });
document.getElementById('dice-roll').addEventListener('click', rollDice);
document.getElementById('dice-roll-times').addEventListener('click', rollDiceTimes);
diceExpression.addEventListener('keydown', (e) => { if (e.key === 'Enter') rollDice(); });
diceTarget.addEventListener('keydown', (e) => { if (e.key === 'Enter') rollDice(); });

/* 猜数字 */
const guessModal = document.getElementById('guess-modal');
const guessInput = document.getElementById('guess-input');
const guessFeedback = document.getElementById('guess-feedback');
const guessHintText = document.getElementById('guess-hint-text');

let guessTarget = 0;
let guessCount = 0;
let guessDone = false;

function newGuessGame() {
    guessTarget = Math.floor(Math.random() * 100) + 1;
    guessCount = 0;
    guessDone = false;
    guessInput.disabled = false;
    guessFeedback.textContent = '';
    guessHintText.textContent = '我想了一个 1 到 100 之间的数字。';
    guessHintText.style.display = '';
    guessInput.value = '';
}

function submitGuess() {
    if (guessDone) return;
    const val = parseInt(guessInput.value, 10);
    if (isNaN(val) || val < 1 || val > 100) {
        guessFeedback.textContent = '请输入 1 到 100 之间的数字。';
        return;
    }
    guessCount++;
    if (val === guessTarget) {
        guessDone = true;
        guessInput.disabled = true;
        guessFeedback.textContent = `猜对了！你用了 ${guessCount} 次。`;
        guessHintText.style.display = 'none';
    } else if (val < guessTarget) {
        guessFeedback.textContent = '太小了。';
    } else {
        guessFeedback.textContent = '太大了。';
    }
    guessInput.value = '';
    if (!guessDone) guessInput.focus();
}

document.querySelectorAll('.tool-card[data-tool]').forEach(card => {
    card.setAttribute('role', 'button');
    card.setAttribute('tabindex', '0');
    card.addEventListener('click', () => {
        const tool = card.dataset.tool;
        if (tool === 'oracle') openOracle();
        if (tool === 'random') {
            diceResult.innerHTML = '';
            diceExpression.value = '1d20';
            diceTarget.value = '';
            diceTimes.value = '1';
            randomModal.classList.add('active');
            lockScroll(true);
        }
        if (tool === 'guess') {
            newGuessGame();
            guessModal.classList.add('active');
            lockScroll(true);
            setTimeout(() => guessInput.focus(), 100);
        }
    });
    card.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); card.click(); }
    });
});

function closeToolModal(m) {
    m.classList.remove('active');
    lockScroll(false);
}

document.getElementById('oracle-close').addEventListener('click', () => closeToolModal(oracleModal));
document.getElementById('random-close').addEventListener('click', () => closeToolModal(randomModal));
document.getElementById('guess-close').addEventListener('click', () => closeToolModal(guessModal));
document.getElementById('guess-restart').addEventListener('click', newGuessGame);
document.getElementById('guess-submit').addEventListener('click', submitGuess);
guessInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') submitGuess();
});

document.querySelectorAll('.tool-modal').forEach(m => {
    m.addEventListener('click', (e) => {
        if (e.target === m) closeToolModal(m);
    });
});

document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        document.querySelectorAll('.tool-modal.active').forEach(m => closeToolModal(m));
    }
});
</script>