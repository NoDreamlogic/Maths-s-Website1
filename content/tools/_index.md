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
        color: rgb(0,0,0);
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
        background: rgba(255, 255, 255, 0.5);
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
    .tool-card:hover {
        border-color: #ccc;
        transform: translateY(-2px);
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
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
    .oracle-card-front { background: #fff; border: 1px solid #ddd; transform: rotateY(180deg); font-size: 0.75em; padding: 6px; text-align: center; color: #333; line-height: 1.3; }
    #oracle-result { opacity: 0; transition: opacity 0.5s; margin-bottom: 20px; }
    #oracle-result.show { opacity: 1; }
    #oracle-result-level { font-size: 0.8em; letter-spacing: 0.3em; color: #999; margin-bottom: 12px; min-height: 1.2em; }
    #oracle-result-text { font-size: 1.05em; line-height: 1.8; color: #333; margin: 0; }

    /* 随机数 */
    .random-inputs { display: flex; gap: 12px; margin-bottom: 20px; justify-content: center; }
    .random-inputs label { display: flex; flex-direction: column; font-size: 0.85em; color: #888; gap: 4px; flex: 1; }
    .random-inputs input { width: 100%; box-sizing: border-box; padding: 8px 10px; border: 1px solid #ddd; border-radius: 6px; font-size: 1em; text-align: center; font-family: inherit; }
    #random-result { font-size: 3em; font-weight: 600; color: #222; margin: 20px 0; min-height: 1.2em; line-height: 1.1; }

    /* 猜数字 */
    #guess-input-row { display: flex; gap: 10px; justify-content: center; margin: 16px 0; }
    #guess-input { width: 120px; box-sizing: border-box; padding: 8px 10px; border: 1px solid #ddd; border-radius: 6px; font-size: 1em; text-align: center; font-family: inherit; }
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
<p>点击卡片使用，标有“→”的会跳转到独立页面。</p>

<div class="tool-grid">
<div class="tool-card" data-tool="oracle">未知的命运</div>
<div class="tool-card" data-tool="random">遵从骰子之意</div>
<div class="tool-card" data-tool="guess">猜数字</div>
<a href="/tools/minesweeper/" class="tool-card" data-bg="minesweeper">M.Sweeper</a>
</div>
</div>

<div id="oracle-modal" class="tool-modal">
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

<div id="random-modal" class="tool-modal">
<div class="tool-panel">
<h3>骰子的意愿</h3>
<div class="random-inputs">
<label>
取最低值
<input type="number" id="random-min" value="1">
</label>
<label>
取最高值
<input type="number" id="random-max" value="100">
</label>
</div>
<div id="random-result">--</div>
<div class="tool-actions">
<button class="tool-btn primary" id="random-generate">求取</button>
<button class="tool-btn" id="random-close">关闭</button>
</div>
</div>
</div>

<div id="guess-modal" class="tool-modal">
<div class="tool-panel">
<h3>猜数字</h3>
<p id="guess-hint">我想了一个 1 到 100 之间的数字。</p>
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
    .then(data => { oracleItems = data; })
    .catch(err => console.error('占卜数据加载失败', err));

const oracleModal = document.getElementById('oracle-modal');
const oracleCardsEl = document.getElementById('oracle-cards');
const oracleResult = document.getElementById('oracle-result');
const oracleResultLevel = document.getElementById('oracle-result-level');
const oracleResultText = document.getElementById('oracle-result-text');
const oracleHint = document.getElementById('oracle-hint');

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
        card.innerHTML = '<div class="oracle-card-inner"><div class="oracle-card-back"></div><div class="oracle-card-front"></div></div>';
        card.addEventListener('click', () => pickCard(card));
        oracleCardsEl.appendChild(card);
    }
    oracleModal.classList.add('active');
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

    setTimeout(() => { card.classList.add('flipped'); }, 400);
    setTimeout(() => {
        oracleHint.style.display = 'none';
        oracleResultLevel.textContent = item.name || '';
        oracleResultText.textContent = item.text;
        oracleResult.classList.add('show');
    }, 1000);
}

const randomModal = document.getElementById('random-modal');
const randomResult = document.getElementById('random-result');
const randomMinInput = document.getElementById('random-min');
const randomMaxInput = document.getElementById('random-max');

function generateRandom() {
    let min = parseInt(randomMinInput.value, 10);
    let max = parseInt(randomMaxInput.value, 10);
    if (isNaN(min) || isNaN(max)) {
        randomResult.textContent = '请输入数字';
        return;
    }
    if (min > max) {
        [min, max] = [max, min];
        randomMinInput.value = min;
        randomMaxInput.value = max;
    }
    const n = Math.floor(Math.random() * (max - min + 1)) + min;
    randomResult.textContent = n;
}

/* 猜数字 */
const guessModal = document.getElementById('guess-modal');
const guessInput = document.getElementById('guess-input');
const guessFeedback = document.getElementById('guess-feedback');
const guessHint = document.getElementById('guess-hint');

let guessTarget = 0;
let guessCount = 0;

function newGuessGame() {
    guessTarget = Math.floor(Math.random() * 100) + 1;
    guessCount = 0;
    guessFeedback.textContent = '';
    guessHint.textContent = '我想了一个 1 到 100 之间的数字。';
    guessHint.style.display = '';
    guessInput.value = '';
}

function submitGuess() {
    const val = parseInt(guessInput.value, 10);
    if (isNaN(val) || val < 1 || val > 100) {
        guessFeedback.textContent = '请输入 1 到 100 之间的数字。';
        return;
    }
    guessCount++;
    if (val === guessTarget) {
        guessFeedback.textContent = `猜对了！你用了 ${guessCount} 次。`;
        guessHint.style.display = 'none';
    } else if (val < guessTarget) {
        guessFeedback.textContent = '太小了。';
    } else {
        guessFeedback.textContent = '太大了。';
    }
    guessInput.value = '';
    guessInput.focus();
}

document.querySelectorAll('.tool-card[data-tool]').forEach(card => {
    card.addEventListener('click', () => {
        const tool = card.dataset.tool;
        if (tool === 'oracle') openOracle();
        if (tool === 'random') {
            randomResult.textContent = '--';
            randomModal.classList.add('active');
        }
        if (tool === 'guess') {
            newGuessGame();
            guessModal.classList.add('active');
            setTimeout(() => guessInput.focus(), 100);
        }
    });
});

document.getElementById('oracle-close').addEventListener('click', () => oracleModal.classList.remove('active'));
document.getElementById('random-close').addEventListener('click', () => randomModal.classList.remove('active'));
document.getElementById('random-generate').addEventListener('click', generateRandom);
document.getElementById('guess-close').addEventListener('click', () => guessModal.classList.remove('active'));
document.getElementById('guess-restart').addEventListener('click', newGuessGame);
document.getElementById('guess-submit').addEventListener('click', submitGuess);
guessInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') submitGuess();
});

document.querySelectorAll('.tool-modal').forEach(m => {
    m.addEventListener('click', (e) => {
        if (e.target === m) m.classList.remove('active');
    });
});

document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        document.querySelectorAll('.tool-modal.active').forEach(m => m.classList.remove('active'));
    }
});
</script>