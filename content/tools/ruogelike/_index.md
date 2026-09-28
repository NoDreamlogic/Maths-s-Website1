---
title: "迷你游戏"
---

<style>
    #spire-page {
        max-width: 800px;
        margin: 0 auto;
        padding: 40px 20px;
        font-family: inherit;
    }
    #spire-status {
        display: flex;
        justify-content: space-between;
        gap: 16px;
        margin-bottom: 20px;
        padding: 16px;
        background: #fafafa;
        border: 1px solid #eee;
        border-radius: 10px;
        font-size: 0.95em;
    }
    .spire-side { flex: 1; }
    .spire-side h3 {
        margin: 0 0 8px;
        font-size: 0.95em;
        color: #333;
        letter-spacing: 0.05em;
    }
    .spire-side .hp { color: #333; }
    .spire-side .block { color: #1976d2; }
    #spire-queue {
        margin: 16px 0;
        padding: 12px;
        min-height: 60px;
        background: #f5f5f5;
        border: 1px dashed #ccc;
        border-radius: 8px;
        font-size: 0.9em;
        color: #666;
    }
    #spire-queue .slot {
        display: inline-block;
        padding: 4px 10px;
        margin: 4px;
        background: #fff;
        border: 1px solid #ddd;
        border-radius: 6px;
        color: #333;
        transition: all 0.25s ease;
    }
    #spire-queue .slot.resolving {
        background: #fff8e1;
        border-color: #f0b400;
        transform: scale(1.15);
        box-shadow: 0 0 14px rgba(240,180,0,0.55);
        color: #a06800;
    }
    #spire-queue .slot.special {
        border-color: #c99;
        background: #fff5f5;
        color: #a33;
    }
    #spire-queue .slot.special.resolving {
        background: #ffe0e0;
        border-color: #e05050;
        box-shadow: 0 0 14px rgba(224,80,80,0.55);
        color: #a02020;
    }
    #spire-hand {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin: 16px 0;
        min-height: 90px;
    }
    .spire-card {
        width: 110px;
        padding: 10px;
        background: #fff;
        border: 1px solid #ddd;
        border-radius: 8px;
        cursor: pointer;
        text-align: center;
        font-size: 0.85em;
        transition: all 0.2s;
    }
    .spire-card:hover {
        border-color: #999;
        transform: translateY(-2px);
    }
    .spire-card.disabled {
        opacity: 0.4;
        cursor: not-allowed;
    }
    .spire-card.disabled:hover {
        transform: none;
        border-color: #ddd;
    }
    .spire-card .name {
        font-weight: 600;
        color: #222;
        margin-bottom: 6px;
    }
    .spire-card .desc {
        color: #666;
        line-height: 1.4;
    }
    #spire-actions {
        margin-top: 20px;
        display: flex;
        gap: 10px;
    }
    #spire-actions button {
        padding: 10px 20px;
        border-radius: 6px;
        border: 1px solid #333;
        background: #333;
        color: #fff;
        cursor: pointer;
        font-family: inherit;
        font-size: 0.95em;
        transition: opacity 0.15s;
    }
    #spire-actions button:disabled {
        opacity: 0.4;
        cursor: not-allowed;
    }
    #spire-actions button.secondary {
        background: none;
        color: #666;
        border-color: #ddd;
    }
    #spire-log {
        margin-top: 20px;
        padding: 12px;
        background: #fafafa;
        border: 1px solid #eee;
        border-radius: 8px;
        font-size: 0.85em;
        color: #666;
        max-height: 200px;
        overflow-y: auto;
        line-height: 1.6;
    }

    #spire-charselect {
        display: none;
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background: rgba(255,255,255,0.96);
        z-index: 100;
        padding: 60px 20px;
        text-align: center;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    #spire-charselect.active { display: flex; }
    #spire-charselect h2 {
        margin: 0 0 24px;
        font-weight: 600;
        color: #222;
    }
    #spire-charoptions {
        display: flex;
        gap: 16px;
        justify-content: center;
        flex-wrap: wrap;
        max-width: 800px;
    }
    .char-option {
        width: 220px;
        padding: 20px;
        background: #fff;
        border: 2px solid #ddd;
        border-radius: 10px;
        cursor: pointer;
        transition: all 0.2s;
        text-align: left;
    }
    .char-option:hover {
        border-color: #333;
        transform: translateY(-2px);
        box-shadow: 0 4px 16px rgba(0,0,0,0.08);
    }
    .char-option .char-name {
        font-size: 1.2em;
        font-weight: 600;
        margin-bottom: 8px;
        color: #222;
    }
    .char-option .char-desc {
        font-size: 0.85em;
        color: #666;
        line-height: 1.5;
        min-height: 5em;
    }
    .char-option .char-hp {
        margin-top: 10px;
        font-size: 0.8em;
        color: #999;
    }
</style>

<div id="spire-page">
<h1>迷你游戏</h1>

<div id="spire-charselect">
    <h2>选择角色</h2>
    <div id="spire-charoptions"></div>
</div>

<div id="spire-status">
<div class="spire-side">
<h3>你 · <span id="player-char">?</span></h3>
<div class="hp">HP：<span id="player-hp">80</span> / <span id="player-maxhp">80</span></div>
<div class="block">格挡：<span id="player-block">0</span></div>
<div>出牌上限：<span id="queue-limit">4</span></div>
</div>
<div class="spire-side">
<h3>敌人</h3>
<div class="hp">HP：<span id="enemy-hp">50</span> / <span id="enemy-maxhp">50</span></div>
<div class="block">格挡：<span id="enemy-block">0</span></div>
<div>意图：<span id="enemy-intent">未知</span></div>
</div>
</div>

<div id="spire-queue">出牌队列：（空）</div>

<div id="spire-hand"></div>

<div id="spire-actions">
<button id="resolve-btn">结算并结束回合</button>
<button id="restart-btn" class="secondary">重新开始</button>
</div>

<div id="spire-log"></div>
</div>

<script>
/* ============================================
   全局
   ============================================ */
let CARD_LIBRARY = {};
let CHARACTER_LIBRARY = {};
let state = null;
let nextCardUid = 1;

/* ============================================
   工具
   ============================================ */
function sleep(ms) {
    return new Promise(r => setTimeout(r, ms));
}

function shuffle(arr) {
    for (let i = arr.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
}

function log(msg) {
    state.log.push(msg);
}

/* ============================================
   卡牌工厂
   ============================================ */
function makeCard(id) {
    const base = CARD_LIBRARY[id];
    const card = base
        ? Object.assign({}, base)
        : { id, name: '?', description: '', effects: [] };
    card.uid = nextCardUid++;
    return card;
}

/* 追击牌：一次性消耗品，不进弃牌堆。
   伤害公式在结算时算（见 specialDamage 处理器）。 */
function makeChaseCard() {
    return {
        id: 'chase',
        name: '追击',
        description: '造成 本回合攻击次数 × 倍率 的伤害（结算时确定）。',
        isSpecial: true,
        effects: [{ type: 'specialDamage' }],
        uid: nextCardUid++
    };
}

/* ============================================
   效果处理器
   ============================================ */
const EFFECT_HANDLERS = {

    /* 普通伤害。times 是基础段数，K 的连击加成会 +1 段。 */
    damage(state, effect) {
        const baseDmg = effect.value || 0;
        const baseTimes = effect.times || 1;

        const isK = state.character?.passive?.type === 'extraDamageRepeat';
        const isCombo = state.resolvingCard?.tags?.includes('combo');
        const bonus = (isK && isCombo) ? (state.character.passive.value || 0) : 0;
        const times = baseTimes + bonus;

        let totalReal = 0;
        let totalAbsorbed = 0;
        for (let r = 0; r < times; r++) {
            if (state.enemy.hp <= 0) break;
            const absorbed = Math.min(state.enemy.block, baseDmg);
            state.enemy.block -= absorbed;
            const real = baseDmg - absorbed;
            state.enemy.hp = Math.max(0, state.enemy.hp - real);
            totalReal += real;
            totalAbsorbed += absorbed;
        }
        state.currentCardRealDamage += totalReal;

        if (times > 1) {
            log(`造成 ${baseDmg} × ${times} 段（真实 ${totalReal}，吸收 ${totalAbsorbed}）。`);
        } else {
            log(`造成 ${totalReal} 点伤害（格挡吸收 ${totalAbsorbed}）。`);
        }
    },

    /* 追击伤害：结算时才算。读 specialAttackConfig。 */
    specialDamage(state, effect) {
        const cfg = state.specialAttackConfig;
        const effectiveAttacks = state.attacksThisTurn + cfg.bonusAttacks;
        const dmg = effectiveAttacks * cfg.perAttack + cfg.flatBonus;

        // 常规伤害（可被格挡）
        const absorbed = Math.min(state.enemy.block, dmg);
        state.enemy.block -= absorbed;
        let real = dmg - absorbed;

        // 保底真伤
        let guaranteed = 0;
        if (real < cfg.minDamage) {
            guaranteed = cfg.minDamage - real;
            real += guaranteed;
        }

        state.enemy.hp = Math.max(0, state.enemy.hp - real);
        state.currentCardRealDamage += real;

        // 日志
        let formula = `${state.attacksThisTurn} 次攻击`;
        if (cfg.bonusAttacks) formula += ` + 额外 ${cfg.bonusAttacks}`;
        formula += ` × ${cfg.perAttack}`;
        if (cfg.flatBonus) formula += ` + ${cfg.flatBonus}`;

        if (guaranteed > 0) {
            log(`追击造成 ${dmg - absorbed} 点伤害（${formula}，吸收 ${absorbed}），` +
                `保底追加 ${guaranteed} 点真实伤害。`);
        } else {
            log(`追击造成 ${real} 点伤害（${formula}，吸收 ${absorbed}）。`);
        }

        // 附加效果
        for (const extra of cfg.extraEffects) {
            const handler = EFFECT_HANDLERS[extra.type];
            if (handler) handler(state, extra);
            else log(`追击的未知附加效果：${extra.type}`);
        }
    },

    block(state, effect) {
        const v = effect.value || 0;
        state.player.block += v;
        log(`获得 ${v} 点格挡。`);
    },

    draw(state, effect) {
        const n = effect.value || 0;
        for (let i = 0; i < n; i++) {
            if (state.drawPile.length === 0) {
                state.drawPile = shuffle(state.discardPile.slice());
                state.discardPile = [];
            }
            if (state.drawPile.length === 0) break;
            state.hand.push(state.drawPile.pop());
        }
        log(`抽了 ${n} 张牌。`);
    },

    /* 修改本回合追击的配置 */
    buffSpecialAttack(state, effect) {
        const cfg = state.specialAttackConfig;
        if (effect.perAttackDelta) cfg.perAttack += effect.perAttackDelta;
        if (effect.flatBonusDelta) cfg.flatBonus += effect.flatBonusDelta;
        if (effect.minDamageSet !== undefined) cfg.minDamage = effect.minDamageSet;
        if (effect.bonusAttacksDelta) cfg.bonusAttacks += effect.bonusAttacksDelta;
        if (effect.extraEffects) cfg.extraEffects.push(...effect.extraEffects);

        let desc = `本回合追击：每次攻击 × ${cfg.perAttack}`;
        if (cfg.bonusAttacks) desc += `，额外计入 ${cfg.bonusAttacks} 次攻击`;
        if (cfg.flatBonus) desc += ` + ${cfg.flatBonus}`;
        log(desc + '。');
    }
};

/* ============================================
   抽牌 / 意图
   ============================================ */
function drawHand(n) {
    for (let i = 0; i < n; i++) {
        if (state.drawPile.length === 0) {
            state.drawPile = shuffle(state.discardPile.slice());
            state.discardPile = [];
        }
        if (state.drawPile.length === 0) break;
        state.hand.push(state.drawPile.pop());
    }
}

function rollEnemyIntent() {
    const r = Math.random();
    if (r < 0.6) {
        state.enemy.intent = { type: 'attack', value: 8 };
    } else if (r < 0.85) {
        state.enemy.intent = { type: 'attack', value: 5 };
    } else {
        state.enemy.intent = { type: 'buff', value: 5 };
    }
}

/* ============================================
   角色选择
   ============================================ */
function showCharacterSelect() {
    const container = document.getElementById('spire-charoptions');
    container.innerHTML = '';
    Object.keys(CHARACTER_LIBRARY).forEach(key => {
        const c = CHARACTER_LIBRARY[key];
        const el = document.createElement('div');
        el.className = 'char-option';
        el.innerHTML = `
            <div class="char-name">${c.name}</div>
            <div class="char-desc">${c.description}</div>
            <div class="char-hp">HP ${c.maxHp}</div>
        `;
        el.addEventListener('click', () => newGame(key));
        container.appendChild(el);
    });
    document.getElementById('spire-charselect').classList.add('active');
}

/* ============================================
   新游戏
   ============================================ */
function newGame(characterKey) {
    const characterDef = CHARACTER_LIBRARY[characterKey];
    if (!characterDef) return;

    state = {
        character: characterDef,
        player: { hp: characterDef.maxHp, maxHp: characterDef.maxHp, block: 0 },
        enemy: { hp: 50, maxHp: 50, block: 0, intent: null },
        drawPile: [],
        hand: [],
        discardPile: [],
        queue: [],
        queueLimit: 4,
        turn: 1,
        phase: 'building',
        currentCardRealDamage: 0,
        attacksThisTurn: 0,
        specialAttackInsertedThisTurn: false,
        specialAttackConfig: {
            perAttack: 3,
            flatBonus: 0,
            minDamage: 0,
            bonusAttacks: 0,
            extraEffects: []
        },
        resolvingCard: null,
        resolvingCardUid: null,
        log: []
    };

    const deck = characterDef.deck.map(id => makeCard(id));
    state.drawPile = shuffle(deck);
    drawHand(5);
    rollEnemyIntent();

    document.getElementById('spire-charselect').classList.remove('active');
    render();
}

/* ============================================
   玩家操作
   ============================================ */
function playCardFromHand(index) {
    if (state.phase !== 'building') return;
    if (state.queue.length >= state.queueLimit) {
        log('出牌队列已满。');
        render();
        return;
    }
    const card = state.hand.splice(index, 1)[0];
    state.queue.push(card);
    render();
}

/* ============================================
   结算核心（异步）
   ============================================ */
async function resolveQueueAsync() {
    while (state.queue.length > 0) {
        const card = state.queue[0];
        state.resolvingCard = card;
        state.resolvingCardUid = card.uid;
        render();
        await sleep(450);

        log(`打出「${card.name}」。`);
        state.currentCardRealDamage = 0;
        const isAttackCard = card.effects.some(e =>
            e.type === 'damage' || e.type === 'specialDamage');

        for (const effect of card.effects) {
            const handler = EFFECT_HANDLERS[effect.type];
            if (handler) handler(state, effect);
            else log(`未知效果：${effect.type}`);
        }

        if (isAttackCard) {
            state.attacksThisTurn++;

            // W 的吸血被动
            if (state.character?.passive?.type === 'lifesteal') {
                const cost = Math.floor(state.player.hp * state.character.passive.costPercent);
                const heal = state.currentCardRealDamage;
                state.player.hp = Math.max(0, state.player.hp - cost + heal);
                log(`[W] 消耗 ${cost} HP，回复 ${heal} HP。`);
            }
        }

        // 移出队列。追击牌是消耗品，不进弃牌堆。
        state.queue.shift();
        if (!card.isSpecial) {
            state.discardPile.push(card);
        }
        state.resolvingCard = null;
        state.resolvingCardUid = null;
        render();
        await sleep(220);

        if (state.player.hp <= 0) {
            state.phase = 'gameover';
            log('你倒下了。');
            return;
        }
        if (state.enemy.hp <= 0) {
            state.phase = 'gameover';
            log('敌人倒下了。');
            return;
        }
    }

    state.resolvingCard = null;
    state.resolvingCardUid = null;
}

/* ============================================
   敌人行动（异步）
   ============================================ */
async function enemyActAsync() {
    state.enemy.block = 0;
    const intent = state.enemy.intent;
    if (!intent) return;

    if (intent.type === 'attack') {
        const dmg = intent.value;
        const absorbed = Math.min(state.player.block, dmg);
        state.player.block -= absorbed;
        const real = dmg - absorbed;
        state.player.hp = Math.max(0, state.player.hp - real);
        log(`敌人攻击，造成 ${real} 点伤害（格挡吸收 ${absorbed}）。`);
        render();
        await sleep(500);
    } else if (intent.type === 'buff') {
        state.enemy.block += intent.value;
        log(`敌人获得 ${intent.value} 点格挡。`);
        render();
        await sleep(500);
    }
}

/* ============================================
   新回合
   ============================================ */
function startNewTurn() {
    state.turn++;
    state.player.block = 0;
    state.queueLimit = 4;
    state.attacksThisTurn = 0;
    state.specialAttackInsertedThisTurn = false;
    state.specialAttackConfig = {
        perAttack: 3,
        flatBonus: 0,
        minDamage: 0,
        bonusAttacks: 0,
        extraEffects: []
    };
    state.discardPile.push(...state.hand);
    state.hand = [];
    drawHand(5);
    rollEnemyIntent();
}

/* ============================================
   主流程
   ============================================ */
async function resolveAndEndTurn() {
    if (state.phase !== 'building') return;

    state.phase = 'resolving';
    render();

    // 1. L 的追击：立刻插入队尾
    if (state.character?.passive?.type === 'appendSpecialAttack'
        && !state.specialAttackInsertedThisTurn) {
        state.queue.push(makeChaseCard());
        state.specialAttackInsertedThisTurn = true;
        log(`[L] 在队列末尾插入「追击」。`);
        render();
        await sleep(350);
    }

    // 2. 逐张结算
    await resolveQueueAsync();

    if (state.phase === 'gameover') {
        render();
        return;
    }

    // 3. 敌人行动
    await sleep(250);
    await enemyActAsync();

    if (state.player.hp <= 0 || state.enemy.hp <= 0) {
        state.phase = 'gameover';
        render();
        return;
    }

    // 4. 新回合
    await sleep(250);
    startNewTurn();
    state.phase = 'building';
    render();
}

/* ============================================
   渲染
   ============================================ */
function render() {
    if (!state) return;

    document.getElementById('player-char').textContent = state.character.name;
    document.getElementById('player-hp').textContent = state.player.hp;
    document.getElementById('player-maxhp').textContent = state.player.maxHp;
    document.getElementById('player-block').textContent = state.player.block;
    document.getElementById('queue-limit').textContent = state.queueLimit;

    document.getElementById('enemy-hp').textContent = state.enemy.hp;
    document.getElementById('enemy-maxhp').textContent = state.enemy.maxHp;
    document.getElementById('enemy-block').textContent = state.enemy.block;

    const intentEl = document.getElementById('enemy-intent');
    if (state.enemy.intent) {
        const i = state.enemy.intent;
        if (i.type === 'attack') intentEl.textContent = `攻击 ${i.value}`;
        else if (i.type === 'buff') intentEl.textContent = `格挡 +${i.value}`;
        else intentEl.textContent = '未知';
    }

    // 队列
    const queueEl = document.getElementById('spire-queue');
    if (state.queue.length === 0) {
        queueEl.textContent = '出牌队列：（空）';
    } else {
        queueEl.innerHTML = '出牌队列：' +
            state.queue.map(c => {
                const cls = ['slot'];
                if (c.isSpecial) cls.push('special');
                if (c.uid === state.resolvingCardUid) cls.push('resolving');
                return `<span class="${cls.join(' ')}">${c.name}</span>`;
            }).join('');
    }

    // 手牌
    const handEl = document.getElementById('spire-hand');
    handEl.innerHTML = '';
    state.hand.forEach((card, i) => {
        const el = document.createElement('div');
        el.className = 'spire-card';
        if (state.queue.length >= state.queueLimit || state.phase !== 'building') {
            el.classList.add('disabled');
        }
        el.innerHTML = `<div class="name">${card.name}</div><div class="desc">${card.description}</div>`;
        el.addEventListener('click', () => playCardFromHand(i));
        handEl.appendChild(el);
    });

    // 日志
    const logEl = document.getElementById('spire-log');
    logEl.innerHTML = state.log.slice(-40).map(l => `<div>${l}</div>`).join('');
    logEl.scrollTop = logEl.scrollHeight;

    // 按钮
    document.getElementById('resolve-btn').disabled = state.phase !== 'building';
    document.getElementById('restart-btn').disabled = state.phase === 'resolving';
}

/* ============================================
   按钮绑定
   ============================================ */
document.getElementById('resolve-btn').addEventListener('click', () => {
    resolveAndEndTurn();
});

document.getElementById('restart-btn').addEventListener('click', () => {
    if (state && state.phase === 'resolving') return;
    state = null;
    document.getElementById('spire-log').innerHTML = '';
    showCharacterSelect();
});

/* ============================================
   启动
   ============================================ */
Promise.all([
    fetch('/data/ruogelike-card.json').then(r => r.json()),
    fetch('/data/ruogelike-character.json').then(r => r.json())
]).then(([cards, chars]) => {
    CARD_LIBRARY = cards;
    CHARACTER_LIBRARY = chars;
    showCharacterSelect();
}).catch(err => {
    console.error('未能成功加载数据', err);
    document.getElementById('spire-log').innerHTML =
        '<div>加载数据失败，你要试试刷新吗？</div>';
});
</script>