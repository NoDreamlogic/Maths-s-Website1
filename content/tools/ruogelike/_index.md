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
        flex-wrap: nowrap;
        justify-content: center;
        align-items: flex-end;
        gap: 0;
        margin: 16px 0;
        min-height: 130px;
        padding: 12px 0 6px;
    }
    .spire-card {
        position: relative;
        flex: 0 0 auto;
        width: 90px;
        height: 110px;
        box-sizing: border-box;
        padding: 12px 8px;
        background: #fff;
        border: 1px solid #ddd;
        border-radius: 8px;
        cursor: pointer;
        text-align: center;
        font-size: 0.85em;
        transition: transform 0.18s ease, border-color 0.18s ease, box-shadow 0.18s ease;
        user-select: none;
        -webkit-user-select: none;
        -webkit-touch-callout: none;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .spire-card:hover {
        border-color: #999;
        transform: translateY(-8px);
        z-index: 10;
        box-shadow: 0 6px 16px rgba(0,0,0,0.18);
    }
    .spire-card.disabled {
        opacity: 0.4;
        cursor: not-allowed;
    }
    .spire-card.disabled:hover {
        transform: none;
        border-color: #ddd;
        box-shadow: none;
        z-index: auto;
    }
    .spire-card .name {
        font-weight: 600;
        color: #222;
    }
    .spire-card .desc {
        display: none;
    }
    .card-badge {
        position: absolute;
        top: -6px;
        left: -6px;
        min-width: 20px;
        height: 20px;
        padding: 0 4px;
        border-radius: 10px;
        font-size: 0.7em;
        font-weight: 600;
        color: #fff;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .card-badge.newborn { background: #6b8fbf; }
    .card-badge.mature { background: #d4a017; }

    #card-tooltip {
        position: fixed;
        background: #333;
        color: #fff;
        padding: 10px 14px;
        border-radius: 8px;
        font-size: 0.85em;
        max-width: 200px;
        line-height: 1.5;
        pointer-events: none;
        opacity: 0;
        transition: opacity 0.15s;
        z-index: 10000;
        box-shadow: 0 4px 16px rgba(0,0,0,0.2);
    }
    #card-tooltip.active { opacity: 1; }
    #card-tooltip .tip-name {
        font-weight: 600;
        margin-bottom: 4px;
    }
    #card-tooltip .tip-desc {
        color: #ddd;
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
    .spire-wheel-item:hover { background: #f0f0f0; }
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

    #choice-modal {
        display: none;
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background: rgba(0,0,0,0.35);
        z-index: 200;
        align-items: center;
        justify-content: center;
    }
    #choice-modal.active { display: flex; }
    .choice-box {
        background: #fff;
        border-radius: 12px;
        padding: 24px 28px;
        text-align: center;
        box-shadow: 0 8px 32px rgba(0,0,0,0.2);
    }
    .choice-box h3 {
        margin: 0 0 16px;
        font-size: 1em;
        color: #333;
    }
    .choice-box button {
        padding: 10px 24px;
        margin: 0 6px;
        border-radius: 8px;
        border: 1px solid #333;
        background: #333;
        color: #fff;
        cursor: pointer;
        font-family: inherit;
        font-size: 0.95em;
    }
    .choice-box button.defend {
        background: #1976d2;
        border-color: #1976d2;
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

<div id="card-tooltip"></div>

<div id="choice-modal">
    <div class="choice-box">
        <h3>抉择</h3>
        <button data-choice="attack">攻击 6</button>
        <button data-choice="defend" class="defend">防御 5</button>
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
<button id="undo-btn" class="secondary" disabled>撤回</button>
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

const BASE_HAND_LIMIT = 8;
const BASE_DRAW_PER_TURN = 5;
const BASE_QUEUE_LIMIT = 4;

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

const isTouchOnly = window.matchMedia('(hover: none)').matches;

/* ============================================
   卡牌 tooltip
   ============================================ */
function showCardTooltip(card, el) {
    const tip = document.getElementById('card-tooltip');
    let extra = '';
    if (card.states?.newborn) extra += '<br><span style="color:#9fc0e8;">[新生] 数值 -50%</span>';
    if (card.states?.mature) extra += '<br><span style="color:#e8c060;">[成熟] 数值 +100%</span>';
    tip.innerHTML = `
        <div class="tip-name">${card.name}</div>
        <div class="tip-desc">${card.description}${extra}</div>
    `;
    tip.classList.add('active');

    const rect = el.getBoundingClientRect();
    const tipRect = tip.getBoundingClientRect();

    let left = rect.left + rect.width / 2 - tipRect.width / 2;
    let top = rect.top - tipRect.height - 8;
    if (left < 8) left = 8;
    if (left + tipRect.width > window.innerWidth - 8) {
        left = window.innerWidth - tipRect.width - 8;
    }
    if (top < 8) top = rect.bottom + 8;

    tip.style.left = left + 'px';
    tip.style.top = top + 'px';
}

function hideCardTooltip() {
    document.getElementById('card-tooltip').classList.remove('active');
}

/* ============================================
   卡牌工厂
   ============================================ */
function makeCard(id) {
    const base = CARD_LIBRARY[id];
    const card = base
        ? Object.assign({}, base)
        : { id, name: '?', description: '', effects: [] };
    card.effects = card.effects.map(e => Object.assign({}, e));
    card.states = {};
    card.uid = nextCardUid++;
    return card;
}

/* ============================================
   特殊卡生成器
   ============================================ */
const CARD_GENERATORS = {
    chase: () => ({
        id: 'chase', name: '追击',
        description: '造成 本回合攻击次数 × 倍率 的伤害。',
        isSpecial: true, states: {},
        effects: [{ type: 'specialDamage' }],
        uid: nextCardUid++
    }),
    fill: () => ({
        id: 'fill', name: '虚构',
        description: '造成 1 点伤害，获得 1 点格挡。',
        isSpecial: true, isFill: true, states: {},
        effects: [
            { type: 'damage', value: 1 },
            { type: 'block', value: 1 }
        ],
        uid: nextCardUid++
    }),
    choice: () => ({
        id: 'choice', name: '祈愿',
        description: '抉择「造成 6 点伤害/获得 5 点格挡」。',
        isSpecial: true, isChoice: true, states: {},
        effects: [],
        uid: nextCardUid++
    })
};

function generateCard(key) {
    const gen = CARD_GENERATORS[key];
    return gen ? gen() : null;
}

/* ============================================
   通用追加卡牌被动（insertCard）
   ============================================ */
function runInsertCardPassive(trigger) {
    const passive = state.character?.passive;
    if (passive?.type !== 'insertCard') return false;
    if (passive.trigger !== trigger) return false;
    if (passive.oncePerTurn && state.passiveUsedThisTurn) return false;

    const isHand = passive.target === 'hand';
    const container = isHand ? state.hand : state.queue;
    const limit = isHand ? state.handLimit : state.queueLimit;
    let inserted = 0;

    if (passive.count === 'fillToLimit') {
        while (container.length < limit) {
            const card = generateCard(passive.card);
            if (!card) break;
            container.push(card);
            inserted++;
        }
    } else {
        const n = passive.count || 1;
        for (let i = 0; i < n; i++) {
            const card = generateCard(passive.card);
            if (!card) break;
            container.push(card);
            inserted++;
        }
    }

    if (inserted > 0) {
        state.passiveUsedThisTurn = true;
        log(`[${state.character.name}] 追加 ${inserted} 张特殊牌。`);
    }
    return inserted > 0;
}

/* ============================================
   追刃（L）：结算前在队列末尾追加「追击」
   ============================================ */
function runAppendSpecialAttack() {
    const passive = state.character?.passive;
    if (passive?.type !== 'appendSpecialAttack') return false;
    const card = generateCard('chase');
    if (!card) return false;
    state.queue.push(card);
    log(`[${state.character.name}] 追加「追击」。`);
    return true;
}

/* ============================================
   熟成：卡牌状态乘数
   ============================================ */
function getCardStateMultiplier(card) {
    if (!card?.states) return 1;
    const passive = state.character?.passive;
    if (passive?.type !== 'matureHand') return 1;
    if (card.states.mature) return passive.matureMultiplier ?? 2;
    if (card.states.newborn) return passive.newbornMultiplier ?? 0.5;
    return 1;
}

/* ============================================
   追击（specialDamage）默认配置
   ============================================ */
function makeDefaultSpecialAttackConfig(characterDef) {
    const passive = characterDef?.passive;
    const cfg = { perAttack: 3, flatBonus: 0, minDamage: 0, bonusAttacks: 0, extraEffects: [] };
    if (passive?.type === 'appendSpecialAttack') {
        cfg.perAttack = passive.damagePerAttack ?? cfg.perAttack;
    }
    return cfg;
}

/* ============================================
   敌人意图池
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
        const intent = rollEnemyIntentFromPool(pool);
        if (intent.type === 'attack') {
            runEnemyPassive('modifyAttackIntent', intent);
        }
        state.enemy.queue.push(intent);
    }
}

function getDamageCapRemaining() {
    const v = runEnemyPassive('getRemainingDamageCap');
    return v === undefined ? Infinity : v;
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
        const mult = getCardStateMultiplier(state.resolvingCard);
        const tempBonus = state.player.tempAttackBonus || 0;
        const baseDmg = Math.floor((effect.value || 0) * mult) + tempBonus;
        const baseTimes = effect.times || 1;

        const repeatPassive = state.character?.passive?.type === 'extraDamageRepeat'
            ? state.character.passive : null;
        const isCombo = state.resolvingCard?.tags?.includes('combo');
        const bonus = (repeatPassive && isCombo) ? (repeatPassive.value || 0) : 0;
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
        const mult = getCardStateMultiplier(state.resolvingCard);
        const tempBonus = state.player.tempAttackBonus || 0;
        const flat = Math.floor((effect.flat || 0) * mult);
        const pct = effect.lostHpPercent || 0;
        const lostHp = state.player.maxHp - state.player.hp;
        const variable = Math.floor(lostHp * pct);
        const baseDmg = flat + variable + tempBonus;
        const baseTimes = effect.times || 1;

        const repeatPassive = state.character?.passive?.type === 'extraDamageRepeat'
            ? state.character.passive : null;
        const isCombo = state.resolvingCard?.tags?.includes('combo');
        const bonus = (repeatPassive && isCombo) ? (repeatPassive.value || 0) : 0;
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

        log(`造成 ${baseDmg} 点伤害（真实 ${totalReal}，吸收 ${totalAbsorbed}）。`);
        onPlayerDealtHpDamage(state, totalReal);
    },

    specialDamage(state, effect) {
        const cfg = state.specialAttackConfig;
        const effectiveAttacks = state.attacksThisTurn + cfg.bonusAttacks;
        const tempBonus = state.player.tempAttackBonus || 0;
        const dmg = effectiveAttacks * cfg.perAttack + cfg.flatBonus + tempBonus;

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
            log(`追击造成 ${dmg - absorbed} 点伤害（${formula}，吸收 ${absorbed}），保底追加 ${guaranteed} 点真实伤害。`);
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
        const mult = getCardStateMultiplier(state.resolvingCard);
        const v = Math.floor((effect.value || 0) * mult);
        state.player.block = Math.min(state.player.maxHp, state.player.block + v);
        log(`获得 ${v} 点格挡。`);
    },

    snowball(state, effect) {
        state.snowballActive = true;
        log('渐强激活：后续每张牌结算时，其后面的牌数值 +1。');
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
   每个被动按 hook 声明；runEnemyPassive 返回 handler 结果
   hook 一览：
     modifyAttackIntent(state, passive, intent)       — 生成攻击意图时修改
     onEnemyTurnStart(state, passive)                 — 敌人回合开始
     onEnemyTurnEnd(state, passive)                   — 敌人行动结算完后
     getPierceAmount(state, passive, attackValue)     — 返回穿盾值
     onPlayerTakeRealDamage(state, passive, real)     — 玩家受到真实伤害时
     getRemainingDamageCap(state, passive)            — 返回本回合剩余伤害上限
     onPlayerAttackResolved(state, passive, real)     — 玩家单张攻击牌结算后
   ============================================ */
const ENEMY_PASSIVE_HANDLERS = {
    fire_growth: {
        modifyAttackIntent(state, passive, intent) {
            intent.value += state.enemy.attackGrowthStacks * (passive.value || 0);
        },
        onEnemyTurnEnd(state, passive) {
            state.enemy.attackGrowthStacks += 1;
        }
    },
    counter_strike: {
        modifyAttackIntent(state, passive, intent) {
            const bonus = Math.floor(state.enemy.lastPlayerDamageTaken * (passive.ratio || 0));
            intent.value += bonus;
        },
        onEnemyTurnEnd(state, passive) {
            state.enemy.lastPlayerDamageTaken = state.enemy.damageTakenThisTurn;
        }
    },
    barrage: {
        modifyAttackIntent(state, passive, intent) {
            intent.times = (intent.times || 1) + 1;
        }
    },
    pierce_block: {
        getPierceAmount(state, passive, attackValue) {
            return Math.min(passive.value, attackValue);
        }
    },
    chill_player: {
        onPlayerTakeRealDamage(state, passive, real) {
            if (real <= 0) return;
            const v = passive.value || 1;
            if (state.player.queueLimitPenalty < v) {
                state.player.queueLimitPenalty = v;
                log(`[${state.enemyDef.name}] 你下回合出牌上限 -${v}。`);
            }
        }
    },
    damage_cap: {
        getRemainingDamageCap(state, passive) {
            const cap = Math.floor(state.enemy.maxHp * passive.percent);
            return Math.max(0, cap - state.enemy.damageTakenThisTurn);
        }
    },
    regen: {
        onEnemyTurnStart(state, passive) {
            const before = state.enemy.hp;
            state.enemy.hp = Math.min(state.enemy.maxHp, state.enemy.hp + passive.value);
            const gain = state.enemy.hp - before;
            if (gain > 0) log(`[${state.enemyDef.name}] 再生，回复 ${gain} HP。`);
        }
    },
    shield_up: {
        onEnemyTurnStart(state, passive) {
            state.enemy.block = Math.min(state.enemy.maxHp, state.enemy.block + passive.value);
            log(`[${state.enemyDef.name}] 获得 ${passive.value} 点格挡。`);
        }
    },
    thorns: {
        onPlayerAttackResolved(state, passive, real) {
            if (real <= 0) return;
            state.player.hp = Math.max(0, state.player.hp - passive.value);
            log(`[${state.enemyDef.name}] 荆棘，反弹 ${passive.value} 点伤害。`);
        }
    }
};

function runEnemyPassive(hook, ...args) {
    const passive = state.enemy?.passive;
    if (!passive) return undefined;
    const handler = ENEMY_PASSIVE_HANDLERS[passive.type];
    if (!handler || typeof handler[hook] !== 'function') return undefined;
    return handler[hook](state, passive, ...args);
}

/* ============================================
   手牌布局：不换行、居中、可重叠
   ============================================ */
const HAND_GAP = 8;          // 不重叠时的卡间距
const HAND_MIN_STEP = 26;    // 重叠时每张卡最少露出的宽度
function layoutHand() {
    const handEl = document.getElementById('spire-hand');
    if (!handEl) return;
    const cards = handEl.querySelectorAll('.spire-card');
    const n = cards.length;
    if (n === 0) return;

    const containerW = handEl.clientWidth;
    const cardW = cards[0].getBoundingClientRect().width || 90;
    const totalNeeded = n * cardW + (n - 1) * HAND_GAP;

    if (totalNeeded <= containerW) {
        cards.forEach(c => { c.style.marginLeft = ''; });
        return;
    }

    const step = Math.max(HAND_MIN_STEP, (containerW - cardW) / (n - 1));
    cards.forEach((c, i) => {
        c.style.marginLeft = i === 0 ? '' : `${step - cardW}px`;
    });
}
/* ============================================
   抽牌
   ============================================ */
function drawToLimit(count) {
    let drawn = 0;
    while (drawn < count && state.hand.length < state.handLimit) {
        if (state.drawPile.length === 0) break;
        state.hand.push(state.drawPile.pop());
        drawn++;
    }
}

/* ============================================
   选择界面
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
    document.getElementById('enemy-stat-display').textContent = `HP ${e.maxHp} · 行动上限 ${e.queueLimit}`;
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

    const passive = characterDef.passive || {};

    state = {
        character: characterDef,
        characterKey: characterKey,
        enemyDef: enemyDef,
        enemyKey: enemyKey,
        player: {
            hp: characterDef.maxHp,
            maxHp: characterDef.maxHp,
            block: 0,
            queueLimitPenalty: 0,
            tempAttackBonus: 0
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
        playedPile: [],
        queue: [],
        baseQueueLimit: BASE_QUEUE_LIMIT + (passive.queueLimitBonus || 0),
        queueLimit: BASE_QUEUE_LIMIT + (passive.queueLimitBonus || 0),
        handLimit: BASE_HAND_LIMIT + (passive.handLimitBonus || 0),
        turn: 1,
        phase: 'building',
        currentCardRealDamage: 0,
        attacksThisTurn: 0,
        passiveUsedThisTurn: false,
        snowballActive: false,
        specialAttackConfig: makeDefaultSpecialAttackConfig(characterDef),
        resolvingCard: null,
        resolvingCardUid: null,
        log: []
    };

    fillEnemyQueue(state.enemy.baseQueueLimit);

    const deck = characterDef.deck.map(id => makeCard(id));
    state.drawPile = shuffle(deck);

    let drawCount = BASE_DRAW_PER_TURN + (passive.drawBonus || 0) - (passive.drawPenalty || 0);
    drawToLimit(drawCount);

    // 熟成：初始手牌全部标记为新生
    if (passive.type === 'matureHand') {
        for (const card of state.hand) {
            card.states = card.states || {};
            card.states.newborn = true;
        }
    }

    // 开局也执行 turnStart 触发（B 的抉择）
    runInsertCardPassive('turnStart');

    document.getElementById('spire-select').classList.remove('active');
    render();
}

/* ============================================
   玩家操作
   ============================================ */
function playCardFromHand(index) {
    hideCardTooltip();
    if (state.phase !== 'building') return;
    if (state.queue.length >= state.queueLimit) {
        log('出牌队列已满。');
        render();
        return;
    }
    const card = state.hand[index];
    if (!card) return;
    if (card.isChoice) {
        showChoiceModal(index);
        return;
    }
    doPlayCard(index);
}

function doPlayCard(index) {
    const sourceEl = document.querySelectorAll('#spire-hand .spire-card')[index];
    const sourceRect = sourceEl ? sourceEl.getBoundingClientRect() : null;

    const card = state.hand.splice(index, 1)[0];
    card.handIndex = index;
    state.queue.push(card);
    render();

    if (sourceRect) animateCardFly(sourceRect, card.uid);
}

function animateCardFly(sourceRect, uid) {
    const targetEl = document.querySelector(`#spire-queue .slot[data-uid="${uid}"]`);
    if (!targetEl) return;
    const targetRect = targetEl.getBoundingClientRect();
    const card = state.queue.find(c => c.uid === uid);
    if (!card) return;

    const clone = document.createElement('div');
    clone.className = 'spire-card';
    clone.innerHTML = `<div class="name">${card.name}</div>`;
    clone.style.cssText = `
        position: fixed; left: 0; top: 0;
        width: ${sourceRect.width}px; height: ${sourceRect.height}px;
        margin: 0; box-sizing: border-box; pointer-events: none; z-index: 9999;
        transform-origin: top left;
        transform: translate(${sourceRect.left}px, ${sourceRect.top}px) scale(1);
        transition: transform 0.32s cubic-bezier(0.4, 0, 0.2, 1);
    `;
    document.body.appendChild(clone);
    targetEl.style.visibility = 'hidden';

    const scale = Math.min(targetRect.width / sourceRect.width, targetRect.height / sourceRect.height);
    const scaledW = sourceRect.width * scale;
    const scaledH = sourceRect.height * scale;
    const finalX = (targetRect.left + targetRect.width / 2) - scaledW / 2;
    const finalY = (targetRect.top + targetRect.height / 2) - scaledH / 2;

    requestAnimationFrame(() => {
        clone.style.transform = `translate(${finalX}px, ${finalY}px) scale(${scale})`;
    });

    setTimeout(() => {
        clone.remove();
        if (targetEl.parentNode) targetEl.style.visibility = 'visible';
    }, 330);
}

/* ============================================
   抉择弹窗
   ============================================ */
let choiceTargetIndex = -1;

function showChoiceModal(index) {
    choiceTargetIndex = index;
    document.getElementById('choice-modal').classList.add('active');
}

document.querySelectorAll('#choice-modal button').forEach(btn => {
    btn.addEventListener('click', () => {
        const choice = btn.dataset.choice;
        document.getElementById('choice-modal').classList.remove('active');
        if (choiceTargetIndex < 0) return;
        const card = state.hand[choiceTargetIndex];
        if (!card || !card.isChoice) return;
        card._wasChoice = true;
        if (choice === 'attack') {
            card.name = '攻击';
            card.description = '造成 6 点伤害。';
            card.effects = [{ type: 'damage', value: 6 }];
        } else {
            card.name = '防御';
            card.description = '获得 5 点格挡。';
            card.effects = [{ type: 'block', value: 5 }];
        }
        card.isChoice = false;
        const idx = choiceTargetIndex;
        choiceTargetIndex = -1;
        doPlayCard(idx);
    });
});

/* ============================================
   撤回
   ============================================ */
function undoLastCard() {
    if (state.phase !== 'building') return;
    if (state.queue.length === 0) return;
    const card = state.queue.pop();
    if (card._wasChoice) {
        card.name = '抉择';
        card.description = '打出时选择：攻击 6，或防御 5。';
        card.effects = [];
        card.isChoice = true;
        delete card._wasChoice;
    }
    const idx = card.handIndex;
    if (idx !== undefined && idx <= state.hand.length) {
        state.hand.splice(idx, 0, card);
    } else {
        state.hand.push(card);
    }
    delete card.handIndex;
    render();
}

/* ============================================
   玩家队列结算
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
        const isAttackCard = !card.isFill && card.effects.some(e =>
            e.type === 'damage' || e.type === 'specialDamage' || e.type === 'lostHpDamage');

        const wasSnowball = state.snowballActive;

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

        if (state.snowballActive && wasSnowball) applySnowballToQueue();

        state.queue.shift();
        if (!card.isSpecial) {
            card.states = {};   // 打出后重置熟成状态，洗回牌堆后重新从「新生」开始
            state.playedPile.push(card);
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

function applySnowballToQueue() {
    for (const c of state.queue) {
        for (const eff of c.effects) {
            if (eff.type === 'damage' || eff.type === 'lostHpDamage') {
                if (typeof eff.value === 'number') eff.value += 1;
                if (typeof eff.flat === 'number') eff.flat += 1;
            }
            if (eff.type === 'block' && typeof eff.value === 'number') {
                eff.value += 1;
            }
            // specialDamage 的数值存于 specialAttackConfig，无法按“某一张牌”独立加成，
            // 故不在此处处理。
        }
    }
}

/* ============================================
   冒险：销毁所有手牌
   ============================================ */
function runAdventure() {
    const passive = state.character?.passive;
    if (passive?.type !== 'adventure') return;

    let attackCount = 0;
    let stateCount = 0;
    for (const card of state.hand) {
        if (card.tags?.includes('attack')) attackCount++;
        else if (card.tags?.includes('buff')) stateCount++;
    }
    const total = state.hand.length;
    state.hand = [];

    const atkBonus = attackCount * (passive.attackBonusPerCard || 0);
    const blkBonus = stateCount * (passive.blockPerCard || 0);

    state.player.tempAttackBonus += atkBonus;
    state.player.block = Math.min(state.player.maxHp, state.player.block + blkBonus);

    log(`[冒险] 销毁了 ${total} 张手牌：攻击 +${atkBonus}，格挡 +${blkBonus}。`);
}

/* ============================================
   敌人回合
   ============================================ */
async function enemyActAllAsync() {
    state.enemy.block = 0;
    runEnemyPassive('onEnemyTurnStart');
    render();
    await sleep(300);

    const actions = state.enemy.queue.slice();
    for (const intent of actions) {
        if (state.player.hp <= 0) return;

        if (intent.type === 'attack') {
            const times = intent.times || 1;
            for (let t = 0; t < times; t++) {
                if (state.player.hp <= 0) break;
                const pierce = runEnemyPassive('getPierceAmount', intent.value) ?? 0;
                const blockable = intent.value - pierce;

                const absorbed = Math.min(state.player.block, blockable);
                state.player.block -= absorbed;
                const real = pierce + (blockable - absorbed);
                state.player.hp = Math.max(0, state.player.hp - real);

                if (pierce > 0 && absorbed > 0) {
                    log(`敌人攻击，造成 ${real} 点伤害（${pierce} 点穿盾 + 格挡吸收 ${absorbed}）。`);
                } else if (pierce > 0) {
                    log(`敌人攻击，造成 ${real} 点伤害（其中 ${pierce} 点穿盾）。`);
                } else {
                    log(`敌人攻击，造成 ${real} 点伤害（格挡吸收 ${absorbed}）。`);
                }

                if (real > 0) runEnemyPassive('onPlayerTakeRealDamage', real);
                render();
                await sleep(500);
            }
        } else if (intent.type === 'buff') {
            state.enemy.block = Math.min(state.enemy.maxHp, state.enemy.block + intent.value);
            log(`敌人获得 ${intent.value} 点格挡。`);
            render();
            await sleep(500);
        }
    }

    if (state.enemy.hp <= 0) return;

    runEnemyPassive('onEnemyTurnEnd');

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

    const passive = state.character?.passive;

    if (passive?.type !== 'blockPersist') {
        state.player.block = 0;
    }

    state.queueLimit = Math.max(0, state.baseQueueLimit - (state.player.queueLimitPenalty || 0));
    state.player.queueLimitPenalty = 0;
    state.player.tempAttackBonus = 0;
    state.attacksThisTurn = 0;
    state.passiveUsedThisTurn = false;
    state.enemy.damageTakenThisTurn = 0;
    state.snowballActive = false;
    state.specialAttackConfig = makeDefaultSpecialAttackConfig(state.character);

    // 熟成：新生 → 成熟
    if (passive?.type === 'matureHand') {
        for (const card of state.hand) {
            if (card.states?.newborn) {
                delete card.states.newborn;
                card.states.mature = true;
            }
        }
    }

    // 洗回
    state.drawPile = shuffle(state.drawPile.concat(state.playedPile));
    state.playedPile = [];

    // 抽牌
    let drawCount = BASE_DRAW_PER_TURN + (passive?.drawBonus || 0) - (passive?.drawPenalty || 0);
    drawToLimit(drawCount);

    // 熟成：新抽的牌标记为新生
    if (passive?.type === 'matureHand') {
        for (const card of state.hand) {
            card.states = card.states || {};
            if (!card.states.mature && !card.states.newborn) {
                card.states.newborn = true;
            }
        }
    }

    // 通用追加：回合开始（B 的抉择）
    runInsertCardPassive('turnStart');
}

/* ============================================
   主流程
   ============================================ */
async function resolveAndEndTurn() {
    if (state.phase !== 'building') return;

    // 出牌结束：手牌超上限销毁
    while (state.hand.length > state.handLimit) {
        const specialIdx = state.hand.findIndex(c => c.isSpecial);
        if (specialIdx >= 0) state.hand.splice(specialIdx, 1);
        else state.hand.pop();
    }

    state.phase = 'resolving';
    render();
    hideCardTooltip();

    // 冒险：销毁所有手牌
    if (state.character?.passive?.type === 'adventure') {
        runAdventure();
        render();
        await sleep(350);
    }

    // 通用追加：结算前（A）
    if (runInsertCardPassive('beforeResolve')) {
        render();
        await sleep(350);
    }

    // 追刃：结算前追加追击（L）
    if (runAppendSpecialAttack()) {
        render();
        await sleep(350);
    }

    await resolveQueueAsync();
    if (state.phase === 'gameover') { render(); return; }

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
                const label = times > 1 ? `攻击 ${i.value} × ${times}` : `攻击 ${i.value}`;
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
                return `<span class="${cls.join(' ')}" data-uid="${c.uid}">${c.name}</span>`;
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
        if (card.isSpecial) el.style.borderColor = '#e0a0a0';
        el.innerHTML = `<div class="name">${card.name}</div><div class="desc">${card.description}</div>`;

        // 熟成标签
        if (card.states?.newborn) {
            const b = document.createElement('div');
            b.className = 'card-badge newborn';
            b.textContent = '新';
            el.appendChild(b);
        } else if (card.states?.mature) {
            const b = document.createElement('div');
            b.className = 'card-badge mature';
            b.textContent = '熟';
            el.appendChild(b);
        }

        if (!isTouchOnly) {
            el.addEventListener('mouseenter', () => showCardTooltip(card, el));
            el.addEventListener('mouseleave', hideCardTooltip);
        }

        let longPressTimer = null;
        el.addEventListener('touchstart', () => {
            el._longPressed = false;
            longPressTimer = setTimeout(() => {
                el._longPressed = true;
                showCardTooltip(card, el);
                if (navigator.vibrate) navigator.vibrate(10);
            }, 400);
        }, { passive: true });
        el.addEventListener('touchend', () => {
            clearTimeout(longPressTimer);
            setTimeout(hideCardTooltip, 150);
        });
        el.addEventListener('touchcancel', () => {
            clearTimeout(longPressTimer);
            hideCardTooltip();
        });
        el.addEventListener('touchmove', () => {
            clearTimeout(longPressTimer);
        }, { passive: true });

        el.addEventListener('click', () => {
            if (el._longPressed) {
                el._longPressed = false;
                return;
            }
            playCardFromHand(i);
        });
        handEl.appendChild(el);
    });

     // 手牌布局（不换行 + 重叠）
    layoutHand();

    const logEl = document.getElementById('spire-log');
    logEl.innerHTML = state.log.slice(-40).map(l => `<div>${l}</div>`).join('');
    logEl.scrollTop = logEl.scrollHeight;

    document.getElementById('resolve-btn').disabled = state.phase !== 'building';
    document.getElementById('undo-btn').disabled =
        state.phase !== 'building' || state.queue.length === 0;
    document.getElementById('restart-btn').disabled = state.phase === 'resolving';
}

/* ============================================
   按钮绑定
   ============================================ */
document.getElementById('resolve-btn').addEventListener('click', () => resolveAndEndTurn());
document.getElementById('undo-btn').addEventListener('click', () => undoLastCard());
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

/* 窗口尺寸变化时重新布局手牌 */
window.addEventListener('resize', () => {
    if (state) layoutHand();
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