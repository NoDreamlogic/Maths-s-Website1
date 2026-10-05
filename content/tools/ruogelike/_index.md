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
        width: 90px;
        padding: 12px 8px;
        background: #fff;
        border: 1px solid #ddd;
        border-radius: 8px;
        cursor: pointer;
        text-align: center;
        font-size: 0.85em;
        transition: all 0.2s;
        user-select: none;
        -webkit-user-select: none;
        -webkit-touch-callout: none;
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
    }
    .spire-card .desc {
        display: none;
    }

    /* 卡牌提示 */
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

    /* 抉择弹窗 */
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

const HAND_LIMIT = 8;
const DRAW_PER_TURN = 5;

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
    tip.innerHTML = `
        <div class="tip-name">${card.name}</div>
        <div class="tip-desc">${card.description}</div>
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
    if (top < 8) {
        top = rect.bottom + 8;
    }

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
    card.uid = nextCardUid++;
    return card;
}

/* ============================================
   特殊卡生成器注册表
   ============================================ */
const CARD_GENERATORS = {
    chase: () => ({
        id: 'chase',
        name: '追击',
        description: '造成 本回合攻击次数 × 倍率 的伤害。',
        isSpecial: true,
        effects: [{ type: 'specialDamage' }],
        uid: nextCardUid++
    }),
    fill: () => ({
        id: 'fill',
        name: '打1防1',
        description: '造成 1 点伤害，获得 1 点格挡。',
        isSpecial: true,
        isFill: true,
        effects: [
            { type: 'damage', value: 1 },
            { type: 'block', value: 1 }
        ],
        uid: nextCardUid++
    }),
    choice: () => ({
        id: 'choice',
        name: '抉择',
        description: '打出时选择：攻击 6，或防御 5。',
        isSpecial: true,
        isChoice: true,
        effects: [],
        uid: nextCardUid++
    })
};

function generateCard(key) {
    const gen = CARD_GENERATORS[key];
    return gen ? gen() : null;
}

/* ============================================
   通用追加卡牌被动
   ============================================ */
function runInsertCardPassive(trigger) {
    const passive = state.character?.passive;
    if (passive?.type !== 'insertCard') return false;
    if (passive.trigger !== trigger) return false;
    if (passive.oncePerTurn && state.passiveUsedThisTurn) return false;

    const container = passive.target === 'hand' ? state.hand : state.queue;
    let inserted = 0;

    if (passive.count === 'fillToLimit') {
        while (state.queue.length < state.queueLimit) {
            const card = generateCard(passive.card);
            if (!card) break;
            state.queue.push(card);
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

        log(`造成 ${baseDmg} 点伤害（固定 ${flat} + 已损失 ${lostHp} × ${Math.round(pct*100)}% = ${variable}，真实 ${totalReal}，吸收 ${totalAbsorbed}）。`);
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
        const v = effect.value || 0;
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
            state.enemy.block = Math.min(state.enemy.maxHp, state.enemy.block + passive.value);
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
function drawToLimit(count) {
    let drawn = 0;
    while (drawn < count && state.hand.length < HAND_LIMIT) {
        if (state.drawPile.length === 0) break;
        state.hand.push(state.drawPile.pop());
        drawn++;
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
        playedPile: [],
        queue: [],
        queueLimit: 4,
        turn: 1,
        phase: 'building',
        currentCardRealDamage: 0,
        attacksThisTurn: 0,
        passiveUsedThisTurn: false,
        snowballActive: false,
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

    // 起手
    drawToLimit(DRAW_PER_TURN);

    // 开局也执行一次 turnStart 触发（B 的抉择）
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

    if (sourceRect) {
        animateCardFly(sourceRect, card.uid);
    }
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
        position: fixed;
        left: 0;
        top: 0;
        width: ${sourceRect.width}px;
        height: ${sourceRect.height}px;
        margin: 0;
        box-sizing: border-box;
        pointer-events: none;
        z-index: 9999;
        transform-origin: top left;
        transform: translate(${sourceRect.left}px, ${sourceRect.top}px) scale(1);
        transition: transform 0.32s cubic-bezier(0.4, 0, 0.2, 1);
    `;
    document.body.appendChild(clone);
    targetEl.style.visibility = 'hidden';

    const scaleX = targetRect.width / sourceRect.width;
    const scaleY = targetRect.height / sourceRect.height;
    const scale = Math.min(scaleX, scaleY);
    const scaledW = sourceRect.width * scale;
    const scaledH = sourceRect.height * scale;
    const targetCx = targetRect.left + targetRect.width / 2;
    const targetCy = targetRect.top + targetRect.height / 2;
    const finalX = targetCx - scaledW / 2;
    const finalY = targetCy - scaledH / 2;

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

    // 如果是抉择变成的，恢复成抉择
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

        if (state.snowballActive && wasSnowball) {
            applySnowballToQueue();
        }

        state.queue.shift();
        if (!card.isSpecial) {
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
        }
    }
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

                const ep = state.enemy.passive;
                const pierce = (ep?.type === 'pierce_block')
                    ? Math.min(ep.value, intent.value) : 0;
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

                if (real > 0 && ep?.type === 'chill_player') {
                    const v = ep.value || 1;
                    if (state.player.queueLimitPenalty < v) {
                        state.player.queueLimitPenalty = v;
                        log(`[${state.enemyDef.name}] 你下回合出牌上限 -${v}。`);
                    }
                }

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

    if (state.character?.passive?.type !== 'blockPersist') {
        state.player.block = 0;
    }

    state.queueLimit = Math.max(0, 4 - (state.player.queueLimitPenalty || 0));
    state.player.queueLimitPenalty = 0;
    state.attacksThisTurn = 0;
    state.passiveUsedThisTurn = false;
    state.enemy.damageTakenThisTurn = 0;
    state.snowballActive = false;
    state.specialAttackConfig = {
        perAttack: 3,
        flatBonus: 0,
        minDamage: 0,
        bonusAttacks: 0,
        extraEffects: []
    };

    // 洗回：抽牌堆 + 已打出区
    state.drawPile = shuffle(state.drawPile.concat(state.playedPile));
    state.playedPile = [];

    // 抽牌
    let drawCount = DRAW_PER_TURN;
    const passive = state.character?.passive;
    if (passive?.type === 'insertCard' && passive.drawPenalty) {
        drawCount -= passive.drawPenalty;
    }
    drawToLimit(drawCount);

    // 通用追加：回合开始
    runInsertCardPassive('turnStart');
}

/* ============================================
   主流程
   ============================================ */
async function resolveAndEndTurn() {
    if (state.phase !== 'building') return;

    // 出牌结束：手牌超上限销毁（优先特殊牌）
    while (state.hand.length > HAND_LIMIT) {
        const specialIdx = state.hand.findIndex(c => c.isSpecial);
        if (specialIdx >= 0) {
            state.hand.splice(specialIdx, 1);
        } else {
            state.hand.pop();
        }
    }

    state.phase = 'resolving';
    render();
    hideCardTooltip();

    // 通用追加：结算前
    if (runInsertCardPassive('beforeResolve')) {
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
document.getElementById('resolve-btn').addEventListener('click', () => {
    resolveAndEndTurn();
});
document.getElementById('undo-btn').addEventListener('click', () => {
    undoLastCard();
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