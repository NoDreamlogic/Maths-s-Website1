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
    .spire-side .slot {
        display: inline-block;
        padding: 3px 8px;
        margin: 3px 3px 3px 0;
        background: #fff;
        border: 1px solid #ddd;
        border-radius: 5px;
        font-size: 0.85em;
        color: #555;
    }
    .spire-side .slot.attack {
        border-color: #e0a0a0;
        color: #a04040;
        background: #fff8f8;
    }
    .spire-side .slot.buff {
        border-color: #a0c0e0;
        color: #2060a0;
        background: #f5faff;
    }
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

    /* 5 栏选择界面 */
    #spire-select {
        display: none;
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background: #fafafa;
        z-index: 100;
        padding: 30px 20px;
        box-sizing: border-box;
        align-items: center;
        justify-content: center;
    }
    #spire-select.active { display: flex; }

    .spire-select-panel {
        display: flex;
        width: 100%;
        max-width: 1100px;
        height: 80vh;
        max-height: 600px;
        gap: 12px;
    }

    .spire-col {
        background: #fff;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 16px;
        display: flex;
        flex-direction: column;
        min-height: 0;
    }

    .spire-col-info { flex: 1.4; }
    .spire-col-wheel { flex: 1; padding: 8px; }
    .spire-col-action {
        flex: 0.8;
        align-items: center;
        justify-content: center;
        padding: 12px;
    }

    .spire-col-title {
        margin: 0 0 12px;
        font-size: 0.85em;
        color: #999;
        letter-spacing: 0.1em;
        font-weight: 500;
    }

    .spire-name {
        font-size: 1.3em;
        font-weight: 600;
        color: #222;
        margin-bottom: 12px;
    }

    .spire-desc {
        font-size: 0.9em;
        color: #555;
        line-height: 1.6;
        flex: 1;
    }

    .spire-stat {
        font-size: 0.85em;
        color: #999;
        margin-top: 12px;
        padding-top: 12px;
        border-top: 1px solid #eee;
    }

    .spire-wheel {
        flex: 1;
        overflow-y: auto;
        min-height: 0;
        scrollbar-width: thin;
    }

    .spire-wheel-item {
        padding: 10px 14px;
        margin: 4px 0;
        border-radius: 6px;
        cursor: pointer;
        transition: background 0.15s, color 0.15s;
        color: #333;
        user-select: none;
        font-size: 0.95em;
    }
    .spire-wheel-item:hover {
        background: #f0f0f0;
    }
    .spire-wheel-item.selected {
        background: #333;
        color: #fff;
        font-weight: 600;
    }

    #start-battle-btn {
        padding: 14px 20px;
        border-radius: 8px;
        border: 1px solid #333;
        background: #333;
        color: #fff;
        cursor: pointer;
        font-family: inherit;
        font-size: 1em;
        width: 100%;
        transition: opacity 0.15s;
    }
    #start-battle-btn:disabled {
        opacity: 0.3;
        cursor: not-allowed;
    }

    @media (max-width: 820px) {
        .spire-select-panel {
            flex-direction: column;
            height: auto;
            max-height: 90vh;
            overflow-y: auto;
        }
        .spire-col { flex: none; }
        .spire-col-wheel { height: 180px; }
        .spire-col-action { padding: 16px; }
    }
</style>

<div id="spire-page">
<h1>迷你游戏</h1>

<div id="spire-select">
    <div class="spire-select-panel">
        <div class="spire-col spire-col-info">
            <h3 class="spire-col-title">我方</h3>
            <div class="spire-name" id="char-name-display">—</div>
            <div class="spire-desc" id="char-desc-display">请从右侧列表选择角色</div>
            <div class="spire-stat" id="char-stat-display"></div>
        </div>
        <div class="spire-col spire-col-wheel">
            <div class="spire-wheel" id="char-wheel"></div>
        </div>
        <div class="spire-col spire-col-action">
            <button id="start-battle-btn" disabled>开始战斗</button>
        </div>
        <div class="spire-col spire-col-wheel">
            <div class="spire-wheel" id="enemy-wheel"></div>
        </div>
        <div class="spire-col spire-col-info">
            <h3 class="spire-col-title">敌方</h3>
            <div class="spire-name" id="enemy-name-display">—</div>
            <div class="spire-desc" id="enemy-desc-display">请从左侧列表选择敌人</div>
            <div class="spire-stat" id="enemy-stat-display"></div>
        </div>
    </div>
</div>

<div id="spire-status">
<div class="spire-side">
<h3>你 · <span id="player-char">?</span></h3>
<div class="hp">HP：<span id="player-hp">80</span> / <span id="player-maxhp">80</span></div>
<div class="block">格挡：<span id="player-block">0</span></div>
<div>出牌上限：<span id="queue-limit">4</span></div>
</div>
<div class="spire-side">
<h3>敌人 · <span id="enemy-name">?</span></h3>
<div class="hp">HP：<span id="enemy-hp">50</span> / <span id="enemy-maxhp">50</span></div>
<div class="block">格挡：<span id="enemy-block">0</span></div>
<div>行动（上限 <span id="enemy-queue-limit">2</span>）：<span id="enemy-queue-display">（无）</span></div>
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
let ENEMY_LIBRARY = {};
let state = null;
let nextCardUid = 1;

let selectedCharKey = null;
let selectedEnemyKey = null;

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

function makeChaseCard() {
    return {
        id: 'chase',
        name: '追击',
        description: '造成 本回合攻击次数 × 倍率 的伤害。',
        isSpecial: true,
        effects: [{ type: 'specialDamage' }],
        uid: nextCardUid++
    };
}

/* ============================================
   敌人意图池 / 队列填充
   ============================================ */
function rollEnemyIntentFromPool(pool) {
    const total = pool.reduce((s, e) => s + (e.weight || 1), 0);
    let r = Math.random() * total;
    for (const entry of pool) {
        r -= (entry.weight || 1);
        if (r <= 0) {
            const intent = { type: entry.type, value: entry.value };
            if (entry.times) intent.times = entry.times;
            return intent;
        }
    }
    return { type: 'attack', value: 5 };
}

function fillEnemyQueue(limit) {
    state.enemy.queue = [];
    const pool = state.enemy.intentPool;
    for (let i = 0; i < limit; i++) {
        let intent = rollEnemyIntentFromPool(pool);
        intent = applyEnemyPassiveToIntent(intent);
        state.enemy.queue.push(intent);
    }
}

function applyEnemyPassiveToIntent(intent) {
    const passive = state.enemy.passive;
    if (!passive) return intent;

    if (passive.type === 'fire_growth' && intent.type === 'attack') {
        intent.value += state.enemy.attackGrowthStacks * (passive.value || 0);
    }

    if (passive.type === 'counter_strike' && intent.type === 'attack') {
        const bonus = Math.floor(state.enemy.lastPlayerDamageTaken * (passive.ratio || 0));
        intent.value += bonus;
    }

    if (passive.type === 'barrage' && intent.type === 'attack') {
        intent.times = (intent.times || 1) + 1;
    }

    return intent;
}

function getDamageCapRemaining() {
    const passive = state.enemy?.passive;
    if (passive?.type !== 'damage_cap') return Infinity;
    const cap = Math.floor(state.enemy.maxHp * passive.percent);
    return Math.max(0, cap - state.enemy.damageTakenThisTurn);
}

/* ============================================
   HP 伤害钩子
   ============================================ */
function onPlayerDealtHpDamage(state, amount) {
    if (amount <= 0) return;
    const charPassive = state.character?.passive;
    if (charPassive?.type === 'reduceEnemyQueueLimit') {
        if (state.enemy.nextQueueLimitPenalty < charPassive.value) {
            state.enemy.nextQueueLimitPenalty = charPassive.value;
            log(`[${state.character.name}] 敌人下回合行动上限 -${charPassive.value}。`);
        }
    }
}

/* ============================================
   效果处理器
   ============================================ */
const EFFECT_HANDLERS = {

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
            let real = baseDmg - absorbed;
            real = Math.min(real, getDamageCapRemaining());
            state.enemy.hp = Math.max(0, state.enemy.hp - real);
            state.enemy.damageTakenThisTurn += real;
            totalReal += real;
            totalAbsorbed += absorbed;
        }
        state.currentCardRealDamage += totalReal;

        if (times > 1) {
            log(`造成 ${baseDmg} × ${times} 段（真实 ${totalReal}，吸收 ${totalAbsorbed}）。`);
        } else {
            log(`造成 ${totalReal} 点伤害（格挡吸收 ${totalAbsorbed}）。`);
        }

        onPlayerDealtHpDamage(state, totalReal);
    },

    lostHpDamage(state, effect) {
        const flat = effect.flat || 0;
        const pct = effect.lostHpPercent || 0;
        const lostHp = state.player.maxHp - state.player.hp;
        const variable = Math.floor(lostHp * pct);
        const baseDmg = flat + variable;
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
            let real = baseDmg - absorbed;
            real = Math.min(real, getDamageCapRemaining());
            state.enemy.hp = Math.max(0, state.enemy.hp - real);
            state.enemy.damageTakenThisTurn += real;
            totalReal += real;
            totalAbsorbed += absorbed;
        }
        state.currentCardRealDamage += totalReal;

        log(`造成 ${baseDmg} 点伤害` +
            `（固定 ${flat} + 已损失 ${lostHp} × ${Math.round(pct * 100)}% = ${variable}，` +
            `真实 ${totalReal}，吸收 ${totalAbsorbed}）。`);

        onPlayerDealtHpDamage(state, totalReal);
    },

    specialDamage(state, effect) {
        const cfg = state.specialAttackConfig;
        const effectiveAttacks = state.attacksThisTurn + cfg.bonusAttacks;
        const dmg = effectiveAttacks * cfg.perAttack + cfg.flatBonus;

        const absorbed = Math.min(state.enemy.block, dmg);
        state.enemy.block -= absorbed;
        let real = dmg - absorbed;

        let guaranteed = 0;
        if (real < cfg.minDamage) {
            guaranteed = cfg.minDamage - real;
            real += guaranteed;
        }

        real = Math.min(real, getDamageCapRemaining());
        state.enemy.hp = Math.max(0, state.enemy.hp - real);
        state.enemy.damageTakenThisTurn += real;
        state.currentCardRealDamage += real;

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

        onPlayerDealtHpDamage(state, real);

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
   敌人被动处理表
   ============================================ */
const ENEMY_PASSIVE_HANDLERS = {
    regen: {
        onTurnStart(state, passive) {
            const before = state.enemy.hp;
            state.enemy.hp = Math.min(state.enemy.maxHp, state.enemy.hp + passive.value);
            const gain = state.enemy.hp - before;
            if (gain > 0) log(`[${state.enemyDef.name}] 再生，回复 ${gain} HP。`);
        }
    },
    thorns: {
        onPlayerAttackResolved(state, passive, realDamage) {
            if (realDamage <= 0) return;
            state.player.hp = Math.max(0, state.player.hp - passive.value);
            log(`[${state.enemyDef.name}] 荆棘，反弹 ${passive.value} 点伤害。`);
        }
    },
    shield_up: {
        onTurnStart(state, passive) {
            state.enemy.block += passive.value;
            log(`[${state.enemyDef.name}] 获得 ${passive.value} 点格挡。`);
        }
    }
};

function runEnemyPassive(hook, ...args) {
    const passive = state.enemy?.passive;
    if (!passive) return;
    const handler = ENEMY_PASSIVE_HANDLERS[passive.type];
    if (handler && handler[hook]) {
        handler[hook](state, passive, ...args);
    }
}

/* ============================================
   抽牌
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

/* ============================================
   5 栏选择界面
   ============================================ */
function showCharacterSelect() {
    state = null;
    document.getElementById('spire-select').classList.add('active');

    buildCharWheel();
    buildEnemyWheel();

    const charKeys = Object.keys(CHARACTER_LIBRARY);
    if (!selectedCharKey && charKeys.length > 0) selectedCharKey = charKeys[0];
    if (selectedCharKey) selectCharacter(selectedCharKey);

    const enemyKeys = Object.keys(ENEMY_LIBRARY);
    if (!selectedEnemyKey && enemyKeys.length > 0) selectedEnemyKey = enemyKeys[0];
    if (selectedEnemyKey) selectEnemy(selectedEnemyKey);
}

function buildCharWheel() {
    const container = document.getElementById('char-wheel');
    container.innerHTML = '';
    Object.keys(CHARACTER_LIBRARY).forEach(key => {
        const c = CHARACTER_LIBRARY[key];
        const el = document.createElement('div');
        el.className = 'spire-wheel-item';
        el.dataset.key = key;
        el.textContent = c.name;
        el.addEventListener('click', () => selectCharacter(key));
        container.appendChild(el);
    });
}

function buildEnemyWheel() {
    const container = document.getElementById('enemy-wheel');
    container.innerHTML = '';
    Object.keys(ENEMY_LIBRARY).forEach(key => {
        const e = ENEMY_LIBRARY[key];
        const el = document.createElement('div');
        el.className = 'spire-wheel-item';
        el.dataset.key = key;
        el.textContent = e.name;
        el.addEventListener('click', () => selectEnemy(key));
        container.appendChild(el);
    });
}

function selectCharacter(key) {
    selectedCharKey = key;
    document.querySelectorAll('#char-wheel .spire-wheel-item').forEach(el => {
        el.classList.toggle('selected', el.dataset.key === key);
    });
    const c = CHARACTER_LIBRARY[key];
    document.getElementById('char-name-display').textContent = c.name;
    document.getElementById('char-desc-display').textContent = c.description;
    document.getElementById('char-stat-display').textContent = `HP ${c.maxHp}`;
    updateStartButton();
}

function selectEnemy(key) {
    selectedEnemyKey = key;
    document.querySelectorAll('#enemy-wheel .spire-wheel-item').forEach(el => {
        el.classList.toggle('selected', el.dataset.key === key);
    });
    const e = ENEMY_LIBRARY[key];
    document.getElementById('enemy-name-display').textContent = e.name;
    document.getElementById('enemy-desc-display').textContent = e.description;
    document.getElementById('enemy-stat-display').textContent =
        `HP ${e.maxHp} · 行动上限 ${e.queueLimit}`;
    updateStartButton();
}

function updateStartButton() {
    const btn = document.getElementById('start-battle-btn');
    btn.disabled = !(selectedCharKey && selectedEnemyKey);
}

/* ============================================
   开始战斗
   ============================================ */
function startBattle(characterKey, enemyKey) {
    const characterDef = CHARACTER_LIBRARY[characterKey];
    const enemyDef = ENEMY_LIBRARY[enemyKey];
    if (!characterDef || !enemyDef) return;

    state = {
        character: characterDef,
        characterKey: characterKey,
        enemyDef: enemyDef,
        enemyKey: enemyKey,
        player: {
            hp: characterDef.maxHp,
            maxHp: characterDef.maxHp,
            block: 0,
            queueLimitPenalty: 0
        },
        enemy: {
            hp: enemyDef.maxHp, maxHp: enemyDef.maxHp, block: 0,
            baseQueueLimit: enemyDef.queueLimit,
            queueLimit: enemyDef.queueLimit,
            nextQueueLimitPenalty: 0,
            intentPool: enemyDef.intentPool,
            passive: enemyDef.passive,
            attackGrowthStacks: 0,
            lastPlayerDamageTaken: 0,
            damageTakenThisTurn: 0,
            queue: []
        },
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

    fillEnemyQueue(state.enemy.baseQueueLimit);

    const deck = characterDef.deck.map(id => makeCard(id));
    state.drawPile = shuffle(deck);
    drawHand(5);

    document.getElementById('spire-select').classList.remove('active');
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
   玩家队列结算（异步）
   ============================================ */
async function resolveQueueAsync() {
    while (state.queue.length > 0) {
        const card = state.queue[0];
        state.resolvingCard = card;
        state.resolvingCardUid = card.uid;
        render();
        await sleep(450);

        log(`你使用了「${card.name}」。`);
        state.currentCardRealDamage = 0;
        const isAttackCard = card.effects.some(e =>
            e.type === 'damage' || e.type === 'specialDamage' || e.type === 'lostHpDamage');

        for (const effect of card.effects) {
            const handler = EFFECT_HANDLERS[effect.type];
            if (handler) handler(state, effect);
            else log(`未知效果：${effect.type}`);
        }

        if (isAttackCard) {
            state.attacksThisTurn++;

            if (state.character?.passive?.type === 'lifesteal') {
                const cost = Math.floor(state.player.hp * state.character.passive.costPercent);
                const heal = state.currentCardRealDamage;
                state.player.hp = Math.max(0, state.player.hp - cost + heal);
                log(`[W] 消耗 ${cost} HP，回复 ${heal} HP。`);
            }
            if (state.currentCardRealDamage > 0) {
                runEnemyPassive('onPlayerAttackResolved', state.currentCardRealDamage);
            }
        }

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
   敌人回合（异步）
   ============================================ */
async function enemyActAllAsync() {
    state.enemy.block = 0;
    runEnemyPassive('onTurnStart');
    render();
    await sleep(300);

    const actions = state.enemy.queue.slice();
    for (const intent of actions) {
        if (state.player.hp <= 0) return;

        if (intent.type === 'attack') {
            const times = intent.times || 1;
            for (let t = 0; t < times; t++) {
                if (state.player.hp <= 0) break;
                const dmg = intent.value;
                const absorbed = Math.min(state.player.block, dmg);
                state.player.block -= absorbed;
                const real = dmg - absorbed;
                state.player.hp = Math.max(0, state.player.hp - real);
                log(`敌人攻击，造成 ${real} 点伤害（格挡吸收 ${absorbed}）。`);

                if (real > 0 && state.enemy.passive?.type === 'chill_player') {
                    const v = state.enemy.passive.value || 1;
                    if (state.player.queueLimitPenalty < v) {
                        state.player.queueLimitPenalty = v;
                        log(`[${state.enemyDef.name}] 你下回合出牌上限 -${v}。`);
                    }
                }

                const ep = state.enemy.passive;
                if (ep?.type === 'pierce_block' && ep.value > 0) {
                    state.player.hp = Math.max(0, state.player.hp - ep.value);
                    log(`[${state.enemyDef.name}] 穿盾，额外造成 ${ep.value} 点真实伤害。`);
                }

                render();
                await sleep(500);
            }
        } else if (intent.type === 'buff') {
            state.enemy.block += intent.value;
            log(`敌人获得 ${intent.value} 点格挡。`);
            render();
            await sleep(500);
        }
    }

    if (state.enemy.hp <= 0) return;

    if (state.enemy.passive?.type === 'counter_strike') {
        state.enemy.lastPlayerDamageTaken = state.enemy.damageTakenThisTurn;
    }

    if (state.enemy.passive?.type === 'fire_growth') {
        state.enemy.attackGrowthStacks += 1;
    }

    const penalty = state.enemy.nextQueueLimitPenalty;
    state.enemy.nextQueueLimitPenalty = 0;
    state.enemy.queueLimit = Math.max(0, state.enemy.baseQueueLimit - penalty);
    fillEnemyQueue(state.enemy.queueLimit);

    if (penalty > 0) {
        log(`敌人的行动序列最大长度降为 ${state.enemy.queueLimit}。`);
    }
}

/* ============================================
   新回合
   ============================================ */
function startNewTurn() {
    state.turn++;
    state.player.block = 0;
    state.queueLimit = Math.max(0, 4 - (state.player.queueLimitPenalty || 0));
    state.player.queueLimitPenalty = 0;
    state.attacksThisTurn = 0;
    state.specialAttackInsertedThisTurn = false;
    state.enemy.damageTakenThisTurn = 0;
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
}

/* ============================================
   主流程
   ============================================ */
async function resolveAndEndTurn() {
    if (state.phase !== 'building') return;

    state.phase = 'resolving';
    render();

    if (state.character?.passive?.type === 'appendSpecialAttack'
        && !state.specialAttackInsertedThisTurn) {
        state.queue.push(makeChaseCard());
        state.specialAttackInsertedThisTurn = true;
        log(`[L] 在队列末尾插入「追击」。`);
        render();
        await sleep(350);
    }

    await resolveQueueAsync();

    if (state.phase === 'gameover') {
        render();
        return;
    }

    await sleep(250);
    await enemyActAllAsync();

    if (state.player.hp <= 0 || state.enemy.hp <= 0) {
        state.phase = 'gameover';
        render();
        return;
    }

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

    document.getElementById('enemy-name').textContent = state.enemyDef.name;
    document.getElementById('enemy-hp').textContent = state.enemy.hp;
    document.getElementById('enemy-maxhp').textContent = state.enemy.maxHp;
    document.getElementById('enemy-block').textContent = state.enemy.block;
    document.getElementById('enemy-queue-limit').textContent = state.enemy.queueLimit;

    const enemyQueueEl = document.getElementById('enemy-queue-display');
    if (state.enemy.queue.length === 0) {
        enemyQueueEl.innerHTML = '<span style="color:#999;">（无）</span>';
    } else {
        enemyQueueEl.innerHTML = state.enemy.queue.map(i => {
            if (i.type === 'attack') {
                const times = i.times || 1;
                const label = times > 1
                    ? `攻击 ${i.value} × ${times}`
                    : `攻击 ${i.value}`;
                return `<span class="slot attack">${label}</span>`;
            } else if (i.type === 'buff') {
                return `<span class="slot buff">格挡 +${i.value}</span>`;
            }
            return `<span class="slot">未知</span>`;
        }).join('');
    }

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

    const logEl = document.getElementById('spire-log');
    logEl.innerHTML = state.log.slice(-40).map(l => `<div>${l}</div>`).join('');
    logEl.scrollTop = logEl.scrollHeight;

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
    document.getElementById('spire-log').innerHTML = '';
    showCharacterSelect();
});

document.getElementById('start-battle-btn').addEventListener('click', () => {
    if (selectedCharKey && selectedEnemyKey) {
        startBattle(selectedCharKey, selectedEnemyKey);
    }
});

/* ============================================
   启动
   ============================================ */
Promise.all([
    fetch('/data/ruogelike-card.json').then(r => r.json()),
    fetch('/data/ruogelike-character.json').then(r => r.json()),
    fetch('/data/ruogelike-enemy.json').then(r => r.json())
]).then(([cards, chars, enemies]) => {
    CARD_LIBRARY = cards;
    CHARACTER_LIBRARY = chars;
    ENEMY_LIBRARY = enemies;
    showCharacterSelect();
}).catch(err => {
    console.error('未能成功加载数据', err);
    document.getElementById('spire-log').innerHTML =
        '<div>加载数据失败，你要试试刷新吗？</div>';
});
</script>