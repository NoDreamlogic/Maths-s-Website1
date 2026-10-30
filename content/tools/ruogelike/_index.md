---
title: "迷你游戏"
---

<style>
    * { box-sizing: border-box; }
    #spire-page { max-width: 1100px; margin: 0 auto; padding: 20px; font-family: inherit; }
    #spire-page h1 { margin: 0 0 12px; font-size: 1.1em; color: #999; font-weight: 500; }
    #top-bar { display: flex; align-items: center; justify-content: center; gap: 24px; padding: 8px 0; border-bottom: 1px solid #eee; margin-bottom: 16px; font-size: 0.9em; color: #666; }
    #top-bar .turn { font-weight: 600; color: #333; letter-spacing: 0.05em; }
    #top-bar .menu-btn { padding: 4px 12px; border: 1px solid #ddd; border-radius: 6px; background: #fff; color: #666; cursor: pointer; font-family: inherit; font-size: 0.9em; }
    #top-bar .menu-btn:hover { background: #f5f5f5; }
    #arena { display: flex; gap: 0; margin-bottom: 16px; min-height: 320px; }
    .mid-strip { flex: 0 0 16px; align-self: stretch; background: #fafafa; border-left: 1px solid #eee; border-right: 1px solid #eee; cursor: pointer; display: flex; align-items: center; justify-content: center; user-select: none; transition: flex-basis 0.25s ease, background 0.15s; overflow: hidden; }
    .mid-strip:hover { background: #f0f0f0; }
    .mid-strip.open { flex: 0 0 280px; cursor: default; background: #fff; align-items: stretch; }
    .mid-strip-label { writing-mode: vertical-rl; font-size: 0.8em; color: #999; letter-spacing: 0.2em; text-align: center; }
    .mid-strip.open .mid-strip-label { display: none; }
    .mid-strip-content { display: none; flex-direction: column; width: 100%; height: 100%; }
    .mid-strip.open .mid-strip-content { display: flex; }
    .mid-strip-header { padding: 8px 12px; border-bottom: 1px solid #eee; display: flex; justify-content: space-between; align-items: center; font-size: 0.85em; color: #666; }
    .mid-strip-close { cursor: pointer; color: #999; border: none; background: none; font-family: inherit; font-size: 1em; padding: 0 4px; }
    .mid-strip-log { flex: 1; padding: 10px 12px; overflow-y: auto; font-size: 0.8em; color: #666; line-height: 1.6; }
    .side-col { display: flex; flex-direction: column; gap: 8px; min-height: 0; }
    .side-col.player { flex: 4; }
    .side-col.enemy  { flex: 6; }
    .hp-row { display: flex; align-items: center; gap: 8px; }
    .hp-bar { flex: 1; height: 26px; background: #eee; border: 1px solid #ddd; border-radius: 5px; position: relative; overflow: hidden; }
    .hp-bar .fill { position: absolute; top: 0; left: 0; bottom: 0; background: #7ec8e3; transition: width 0.3s; }
    .side-col.enemy .hp-bar .fill { background: #6cc56c; }
    .hp-bar .text { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; font-size: 0.85em; font-weight: 600; color: #333; }
    .block-indicator { flex: 0 0 46px; height: 26px; border-radius: 5px; border: 1px solid #1976d2; background: #e3f2fd; color: #1976d2; font-size: 0.9em; font-weight: 600; display: flex; align-items: center; justify-content: center; }
    .block-indicator::before { content: '🛡'; font-size: 0.8em; margin-right: 2px; }
    .block-indicator.zero { opacity: 0.3; }
    .fx-row { display: flex; gap: 4px; min-height: 22px; cursor: pointer; flex-wrap: wrap; }
    .fx-slot { width: 22px; height: 22px; border: 1px solid #ddd; border-radius: 4px; background: #fff; display: flex; align-items: center; justify-content: center; font-size: 0.7em; color: #666; }
    .fx-slot.empty { background: #fafafa; }
    .fx-slot.frost { border-color: #6b8fbf; background: #eaf2fb; color: #3a5f8f; }
    .fx-slot.stat  { border-color: #a06b8f; background: #fbeaf2; color: #8f3a5f; }
    .fx-slot.atk   { border-color: #a04040; background: #fff0f0; color: #a04040; }
    .fx-slot.debug { border-color: #7030a0; background: #f5f0fa; color: #7030a0; }
    .portrait { flex: 1; min-height: 180px; border: 1px solid #ddd; border-radius: 8px; background: #fafafa; display: flex; align-items: center; justify-content: center; color: #bbb; font-size: 0.9em; }
    .enemy-mid { display: flex; gap: 8px; flex: 1; min-height: 0; }
    .enemy-portrait { flex: 1; border: 1px solid #ddd; border-radius: 8px; background: #fafafa; display: flex; align-items: center; justify-content: center; color: #bbb; font-size: 0.9em; }
    .enemy-side { flex: 0 0 160px; display: flex; flex-direction: column; gap: 6px; }
    .trait-list { display: flex; flex-direction: column; gap: 3px; font-size: 0.75em; }
    .trait-chip { padding: 2px 6px; border-radius: 4px; border: 1px solid #ddd; background: #fafafa; color: #999; }
    .trait-chip.active { border-color: #7030a0; background: #7030a0; color: #fff; }
    .intent-box { flex: 1; min-height: 60px; border: 1px solid #ddd; border-radius: 8px; padding: 6px; display: flex; flex-wrap: wrap; gap: 4px; align-content: flex-start; font-size: 0.8em; }
    .intent-box .intent-label { color: #bbb; font-size: 0.85em; }
    .intent-chip { padding: 2px 6px; border-radius: 4px; border: 1px solid #e0a0a0; background: #fff8f8; color: #a04040; }
    .intent-chip.buff { border-color: #a0c0e0; background: #f5faff; color: #2060a0; }
    #bottom { display: flex; gap: 8px; min-height: 200px; border: 2px solid #ccc; border-radius: 10px; padding: 8px; }
    .bottom-side { flex: 0 0 64px; display: flex; flex-direction: column; gap: 6px; }
    .bottom-side .label-box { border: 1px solid #ddd; border-radius: 6px; background: #fafafa; color: #999; font-size: 0.7em; text-align: center; padding: 6px 4px; line-height: 1.4; }
    .bottom-side .queue-label { flex: 1; display: flex; align-items: center; justify-content: center; writing-mode: vertical-rl; }
    .bottom-side .draw-label { cursor: pointer; user-select: none; }
    .bottom-side .draw-label:hover { background: #f0f0f0; }
    .bottom-side .draw-label .count { font-weight: 600; color: #666; }
    .bottom-main { flex: 1; position: relative; display: flex; flex-direction: column; gap: 6px; min-width: 0; }
    #resolve-btn { position: absolute; top: 4px; right: 4px; padding: 6px 14px; border-radius: 6px; border: 1px solid #333; background: #333; color: #fff; cursor: pointer; font-family: inherit; font-size: 0.85em; z-index: 5; }
    #resolve-btn:disabled { opacity: 0.4; cursor: not-allowed; }
    #stage-queue { min-height: 56px; padding: 8px 100px 8px 8px; border: 1px dashed #ccc; border-radius: 8px; background: #fafafa; display: flex; flex-wrap: wrap; align-items: center; align-content: flex-start; gap: 6px; }
    #stage-queue:empty::before { content: '（空）'; color: #ccc; font-size: 0.85em; }
    .queue-slot { padding: 6px 12px; border: 1px solid #ddd; border-radius: 6px; background: #fff; color: #333; font-size: 0.85em; cursor: pointer; transition: all 0.25s ease; }
    .queue-slot.special { border-color: #c99; background: #fff5f5; color: #a33; }
    .queue-slot.resolving { background: #fff8e1; border-color: #f0b400; transform: scale(1.15); box-shadow: 0 0 14px rgba(240,180,0,0.55); color: #a06800; }
    .queue-slot.special.resolving { background: #ffe0e0; border-color: #e05050; box-shadow: 0 0 14px rgba(224,80,80,0.55); color: #a02020; }
    #spire-hand { flex: 1; min-height: 120px; display: flex; flex-wrap: nowrap; justify-content: center; align-items: flex-end; gap: 0; padding: 8px; }
    .spire-card { position: relative; flex: 0 0 auto; width: 90px; height: 110px; padding: 12px 8px; background: #fff; border: 1px solid #ddd; border-radius: 8px; cursor: pointer; text-align: center; font-size: 0.85em; transition: transform 0.18s ease, border-color 0.18s ease, box-shadow 0.18s ease; user-select: none; display: flex; flex-direction: column; justify-content: center; align-items: center; }
    .spire-card:hover { border-color: #999; transform: translateY(-8px); z-index: 10; box-shadow: 0 6px 16px rgba(0,0,0,0.18); }
    .spire-card.disabled { opacity: 0.4; cursor: not-allowed; }
    .spire-card.disabled:hover { transform: none; border-color: #ddd; box-shadow: none; z-index: auto; }
    .spire-card .name { font-weight: 600; color: #222; line-height: 1.25; word-break: break-all; }
    .card-badge { position: absolute; top: -6px; left: -6px; min-width: 20px; height: 20px; padding: 0 4px; border-radius: 10px; font-size: 0.7em; font-weight: 600; color: #fff; display: flex; align-items: center; justify-content: center; }
    .card-badge.newborn { background: #6b8fbf; }
    .card-badge.mature { background: #d4a017; }
    .card-badge.tag { background: #3a8f6b; }
    .card-badge.debug { background: #7030a0; }
    #card-tooltip { position: fixed; background: #333; color: #fff; padding: 10px 14px; border-radius: 8px; font-size: 0.85em; max-width: 220px; line-height: 1.5; pointer-events: none; opacity: 0; transition: opacity 0.15s; z-index: 10000; box-shadow: 0 4px 16px rgba(0,0,0,0.2); }
    #card-tooltip.active { opacity: 1; }
    #card-tooltip .tip-name { font-weight: 600; margin-bottom: 4px; }
    #card-tooltip .tip-desc { color: #ddd; }
    #choice-modal, #pile-modal, #search-modal, #discard-modal { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.35); z-index: 200; align-items: center; justify-content: center; }
    #choice-modal.active, #pile-modal.active, #search-modal.active, #discard-modal.active { display: flex; }
    .choice-box, .pile-box-modal, .search-box-modal { background: #fff; border-radius: 12px; padding: 20px 24px; box-shadow: 0 8px 32px rgba(0,0,0,0.2); max-width: 90vw; max-height: 80vh; overflow-y: auto; }
    .choice-box { text-align: center; }
    .choice-box h3 { margin: 0 0 16px; font-size: 1em; color: #333; }
    .choice-box button { display: block; width: 100%; padding: 10px 24px; margin: 6px 0; border-radius: 8px; border: 1px solid #333; background: #333; color: #fff; cursor: pointer; font-family: inherit; font-size: 0.95em; }
    .choice-box button.defend { background: #1976d2; border-color: #1976d2; }
    .choice-box button.skip { background: #fff; color: #666; border-color: #ddd; }
    .pile-box-modal h3, .search-box-modal h3 { margin: 0 0 12px; font-size: 0.95em; color: #666; }
    .pile-grid, .search-grid { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 16px; }
    .pile-item, .search-item { padding: 4px 10px; border: 1px solid #ddd; border-radius: 6px; background: #fafafa; font-size: 0.85em; color: #555; }
    .pile-item.special { border-color: #c99; background: #fff5f5; color: #a33; }
    .search-item { cursor: pointer; user-select: none; }
    .search-item:hover { background: #f0f0f0; border-color: #999; }
    .search-item.selected { background: #333; color: #fff; border-color: #333; }
    .modal-btn { padding: 6px 16px; border-radius: 6px; border: 1px solid #333; background: #333; color: #fff; cursor: pointer; font-family: inherit; font-size: 0.85em; display: inline-block; }
    #main-menu { display: flex; position: fixed; inset: 0; background: #fafafa; z-index: 95; align-items: center; justify-content: center; }
    #main-menu.hidden { display: none; }
    .menu-panel { text-align: center; padding: 40px; }
    .menu-panel h1 { margin: 0 0 40px; font-size: 2em; color: #333; letter-spacing: 0.1em; font-weight: 500; }
    .menu-main-btn { display: block; width: 280px; padding: 16px 24px; margin: 12px auto; border-radius: 10px; border: 1px solid #333; background: #333; color: #fff; cursor: pointer; font-family: inherit; font-size: 1em; letter-spacing: 0.05em; transition: opacity 0.15s; position: relative; }
    .menu-main-btn:hover:not(:disabled) { opacity: 0.85; }
    .menu-main-btn:disabled { background: #ddd; border-color: #ddd; color: #999; cursor: not-allowed; }
    .menu-main-btn .menu-sub { display: block; font-size: 0.7em; font-weight: 400; opacity: 0.7; margin-top: 4px; letter-spacing: 0; }
    .back-btn { margin-top: 12px; padding: 8px 20px; border-radius: 6px; border: 1px solid #ddd; background: none; color: #999; cursor: pointer; font-family: inherit; font-size: 0.85em; width: 100%; }
    .back-btn:hover { background: #f5f5f5; }
    #glossary-modal { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.35); z-index: 400; align-items: center; justify-content: center; }
    #glossary-modal.active { display: flex; }
    .glossary-box { background: #fff; border-radius: 12px; box-shadow: 0 8px 32px rgba(0,0,0,0.2); width: 90%; max-width: 560px; max-height: 80vh; display: flex; flex-direction: column; }
    .glossary-header { padding: 16px 20px; border-bottom: 1px solid #eee; display: flex; justify-content: space-between; align-items: center; }
    .glossary-header h3 { margin: 0; font-size: 1em; color: #333; }
    .glossary-search { padding: 12px 20px; border-bottom: 1px solid #eee; }
    .glossary-search input { width: 100%; padding: 8px 12px; border: 1px solid #ddd; border-radius: 6px; font-family: inherit; font-size: 0.9em; color: #333; outline: none; }
    .glossary-search input:focus { border-color: #999; }
    .glossary-empty { padding: 20px; text-align: center; color: #bbb; font-size: 0.85em; }
    .glossary-body { padding: 16px 20px; overflow-y: auto; font-size: 0.9em; color: #555; line-height: 1.7; }
    .glossary-body .glossary-entry { padding: 10px 0; border-bottom: 1px solid #f0f0f0; }
    .glossary-body .glossary-entry:last-child { border-bottom: none; }
    .glossary-body .glossary-term { font-weight: 600; color: #222; margin-bottom: 4px; }
    .glossary-body .glossary-def { color: #666; }
    #spire-select { display: none; position: fixed; inset: 0; background: #fafafa; z-index: 100; padding: 30px 20px; align-items: center; justify-content: center; }
    #spire-select.active { display: flex; }
    .spire-select-panel { display: flex; width: 100%; max-width: 1100px; height: 80vh; max-height: 600px; gap: 12px; }
    .spire-col { background: #fff; border: 1px solid #e0e0e0; border-radius: 10px; padding: 16px; display: flex; flex-direction: column; min-height: 0; }
    .spire-col-info { flex: 1.4; }
    .spire-col-wheel { flex: 1; padding: 8px; }
    .spire-col-action { flex: 0.8; align-items: center; justify-content: center; padding: 12px; }
    .spire-col-title { margin: 0 0 12px; font-size: 0.85em; color: #999; letter-spacing: 0.1em; font-weight: 500; }
    .spire-name { font-size: 1.3em; font-weight: 600; color: #222; margin-bottom: 8px; }
    .spire-passive-name { font-size: 0.85em; font-weight: 600; color: #7030a0; background: #f5f0fa; border: 1px solid #d0b0e0; display: inline-block; padding: 4px 10px; border-radius: 6px; margin-bottom: 12px; }
    .spire-desc { font-size: 0.9em; color: #555; line-height: 1.6; flex: 1; }
    .spire-stat { font-size: 0.85em; color: #999; margin-top: 12px; padding-top: 12px; border-top: 1px solid #eee; }
    .spire-wheel { flex: 1; overflow-y: auto; min-height: 0; scrollbar-width: thin; }
    .spire-wheel-item { padding: 10px 14px; margin: 4px 0; border-radius: 6px; cursor: pointer; color: #333; user-select: none; font-size: 0.95em; }
    .spire-wheel-item:hover { background: #f0f0f0; }
    .spire-wheel-item.selected { background: #333; color: #fff; font-weight: 600; }
    #start-battle-btn { padding: 14px 20px; border-radius: 8px; border: 1px solid #333; background: #333; color: #fff; cursor: pointer; font-family: inherit; font-size: 1em; width: 100%; }
    #start-battle-btn:disabled { opacity: 0.3; cursor: not-allowed; }
    @media (max-width: 820px) { .spire-select-panel { flex-direction: column; height: auto; max-height: 90vh; overflow-y: auto; } .spire-col { flex: none; } .spire-col-wheel { height: 180px; } }
</style>

<div id="spire-page">
<div id="main-menu">
    <div class="menu-panel">
        <h1>迷你游戏</h1>
        <div class="menu-main-btn" id="menu-fight">格斗模式</div>
        <div class="menu-main-btn" id="menu-roguelike" style="opacity:0.5; cursor:not-allowed;">肉鸽模式<span class="menu-sub">未完成</span></div>
        <div class="menu-main-btn" id="menu-glossary">词条释义</div>
    </div>
</div>

<div id="spire-select">
    <div class="spire-select-panel">
        <div class="spire-col spire-col-info">
            <h3 class="spire-col-title">我方</h3>
            <div class="spire-name" id="char-name-display">—</div>
            <div class="spire-passive-name" id="char-passive-display" style="display:none;">被动：—</div>
            <div class="spire-desc" id="char-desc-display">请从右侧列表选择角色</div>
            <div class="spire-stat" id="char-stat-display"></div>
        </div>
        <div class="spire-col spire-col-wheel"><div class="spire-wheel" id="char-wheel"></div></div>
        <div class="spire-col spire-col-action">
            <div id="start-battle-btn" style="text-align:center; cursor:not-allowed; opacity:0.3; pointer-events:none;">开始战斗</div>
            <div id="back-to-menu-btn" class="back-btn" style="text-align:center;">返回主页</div>
        </div>
        <div class="spire-col spire-col-wheel"><div class="spire-wheel" id="enemy-wheel"></div></div>
        <div class="spire-col spire-col-info">
            <h3 class="spire-col-title">敌方</h3>
            <div class="spire-name" id="enemy-name-display">—</div>
            <div class="spire-desc" id="enemy-desc-display">请从左侧列表选择敌人</div>
            <div class="spire-stat" id="enemy-stat-display"></div>
        </div>
    </div>
</div>

<div id="top-bar">
    <span class="turn">Turn <span id="turn-num">1</span></span>
    <div class="menu-btn" id="log-btn">日志</div>
    <div class="menu-btn" id="restart-btn">重开</div>
</div>

<div id="arena">
    <div class="side-col player">
        <div class="hp-row">
            <div class="hp-bar"><div class="fill" id="player-hp-fill"></div><div class="text"><span id="player-hp">80</span> / <span id="player-maxhp">80</span></div></div>
            <div class="block-indicator" id="player-block">0</div>
        </div>
        <div class="fx-row" id="player-fx" title="点击查看所有效果"></div>
        <div class="portrait"><span id="player-portrait-name">我方</span></div>
    </div>
    <div id="mid-strip" class="mid-strip">
        <div class="mid-strip-label">日<br>志</div>
        <div class="mid-strip-content">
            <div class="mid-strip-header"><span>日志</span><div class="mid-strip-close" id="mid-strip-close">✕</div></div>
            <div class="mid-strip-log" id="mid-strip-log"></div>
        </div>
    </div>
    <div class="side-col enemy">
        <div class="hp-row">
            <div class="hp-bar"><div class="fill" id="enemy-hp-fill"></div><div class="text"><span id="enemy-hp">50</span> / <span id="enemy-maxhp">50</span></div></div>
            <div class="block-indicator" id="enemy-block">0</div>
        </div>
        <div class="fx-row" id="enemy-fx" title="点击查看所有效果"></div>
        <div class="enemy-mid">
            <div class="enemy-portrait"><span id="enemy-portrait-name">敌方</span></div>
            <div class="enemy-side">
                <div class="trait-list" id="enemy-traits"></div>
                <div class="intent-box" id="enemy-intent"><span class="intent-label">行动意图</span></div>
            </div>
        </div>
    </div>
</div>

<div id="bottom">
    <div class="bottom-side">
        <div class="label-box queue-label">行动序列</div>
        <div class="label-box draw-label" id="draw-pile-btn">抽牌堆<br><span class="count" id="draw-count">0</span></div>
    </div>
    <div class="bottom-main">
        <div id="resolve-btn">结算</div>
        <div id="stage-queue"></div>
        <div id="spire-hand"></div>
    </div>
</div>
</div>

<div id="card-tooltip"></div>
<div id="choice-modal"><div class="choice-box"><h3 id="choice-title">抉择</h3><div id="choice-options"></div></div></div>
<div id="pile-modal"><div class="pile-box-modal"><h3>抽牌堆</h3><div class="pile-grid" id="pile-modal-draw"></div><h3>弃牌堆</h3><div class="pile-grid" id="pile-modal-discard"></div></div></div>
<div id="glossary-modal">
    <div class="glossary-box">
        <div class="glossary-header"><h3>词条释义</h3><div class="mid-strip-close" id="glossary-close">✕</div></div>
        <div class="glossary-search"><input type="text" id="glossary-search-input" placeholder="搜索词条（支持拼音 / 首字母）" autocomplete="off"></div>
        <div class="glossary-body" id="glossary-body"></div>
    </div>
</div>
<div id="search-modal"><div class="search-box-modal"><h3>从抽牌堆中选择</h3><div class="search-grid" id="search-grid"></div><div style="text-align:right;"><div id="search-confirm" class="modal-btn">确认</div></div></div></div>
<div id="discard-modal"><div class="search-box-modal"><h3>选择 <span id="discard-required">2</span> 张牌弃置</h3><div class="search-grid" id="discard-grid"></div><div style="text-align:right;"><div id="discard-confirm" class="modal-btn">确认</div></div></div></div>

<script>
let CARD_LIBRARY = {}, CHARACTER_LIBRARY = {}, ENEMY_LIBRARY = {}, LOG = {}, state = null, nextCardUid = 1;
let selectedCharKey = null, selectedEnemyKey = null, GLOSSARY_DATA = [];
const BASE_HAND_LIMIT = 8, BASE_DRAW_PER_TURN = 5, BASE_QUEUE_LIMIT = 4;
const isTouchOnly = window.matchMedia('(hover: none)').matches;

function bindEvent(id, event, fn) { const el = document.getElementById(id); if (el) el.addEventListener(event, fn); }
function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }
function shuffle(arr) { for (let i = arr.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [arr[i], arr[j]] = [arr[j], arr[i]]; } return arr; }

function getDeepValue(obj, path) {
    return path.split('.').reduce((acc, part) => acc && acc[part], obj);
}

// 核心日志工具：自动填值，防崩溃
function logT(key, params = {}) {
    let text = getDeepValue(LOG, key) || `<缺少文本: ${key}>`;
    for (const [k, v] of Object.entries(params)) {
        text = text.replace(new RegExp(`\\$\\{${k}\\}`, 'g'), v);
    }
    if (state && state.log) state.log.push(text);
    else console.log(text);
}

function isSpecialCard(card) { return card?.tags?.includes('special') || card?.isChoice; }

function showCardTooltip(card, el) {
    const tip = document.getElementById('card-tooltip');
    let extra = '';
    if (card.states?.newborn) extra += '<br><span style="color:#9fc0e8;">[新生] 数值 -50%</span>';
    if (card.states?.mature) extra += '<br><span style="color:#e8c060;">[成熟] 数值 +100%</span>';
    if (card.states?.frostExtend) extra += '<br><span style="color:#7fb8d8;">[侵袭] 施加霜冻改为延长</span>';
    tip.innerHTML = `<div class="tip-name">${card.name}</div><div class="tip-desc">${card.description}${extra}</div>`;
    tip.classList.add('active');
    const rect = el.getBoundingClientRect(), tipRect = tip.getBoundingClientRect();
    let left = rect.left + rect.width / 2 - tipRect.width / 2, top = rect.top - tipRect.height - 8;
    if (left < 8) left = 8;
    if (left + tipRect.width > window.innerWidth - 8) left = window.innerWidth - tipRect.width - 8;
    if (top < 8) top = rect.bottom + 8;
    tip.style.left = left + 'px'; tip.style.top = top + 'px';
}
function hideCardTooltip() { document.getElementById('card-tooltip').classList.remove('active'); }

function makeCard(id) {
    const base = CARD_LIBRARY[id];
    const card = base ? Object.assign({}, base) : { id, name: '?', description: '', effects: [], tags: [] };
    card.effects = (card.effects || []).map(e => Object.assign({}, e));
    card.tags = [...(card.tags || [])];
    card.states = {}; card.uid = nextCardUid++;
    return card;
}

const CARD_GENERATORS = {
    chase: () => ({ id: 'chase', name: '追击', description: '造成 本回合攻击次数 × 2 + 调试次数 × 4 的伤害。', tags: ['special', 'attack'], states: {}, effects: [{ type: 'specialDamage' }], uid: nextCardUid++ }),
    fill: () => ({ id: 'fill', name: '虚构', description: '造成 1 点伤害，获得 1 点格挡。', tags: ['special', 'attack', 'buff'], states: {}, effects: [{ type: 'damage', value: 1 }, { type: 'block', value: 1 }], uid: nextCardUid++ }),
    choice: () => ({ id: 'choice', name: '祈愿', description: '抉择「造成 6 点伤害/获得 5 点格挡」。', tags: ['special'], isChoice: true, states: {}, effects: [], uid: nextCardUid++ }),
    chant_attack: () => ({ id: 'chant_attack', name: '吟诵攻击', description: '造成 6 点伤害。', tags: ['special', 'attack'], states: {}, effects: [{ type: 'damage', value: 6 }], uid: nextCardUid++ })
};
function generateCard(key) { return CARD_GENERATORS[key] ? CARD_GENERATORS[key]() : null; }

function getAttackBonus() { return state?.player?.effects?.filter(e => e.type === 'attackBonus').reduce((s, e) => s + e.value, 0) || 0; }
function getDebugPower() { return state?.player?.effects?.filter(e => e.type === 'debug_power').reduce((s, e) => s + e.value, 0) || 0; }
function getDebugTimes() { return state?.player?.effects?.filter(e => e.type === 'debug_times').reduce((s, e) => s + e.value, 0) || 0; }
function getDebugPierce() { return state?.player?.effects?.filter(e => e.type === 'debug_pierce').reduce((s, e) => s + e.value, 0) || 0; }
function getDebugVuln() { return state?.player?.effects?.filter(e => e.type === 'debug_vuln').reduce((s, e) => s + e.value, 0) || 0; }

function addTimedEffect(type, value, turns) { state.player.effects.push({ type, value, turnsLeft: turns }); }

function tickPlayerEffects() {
    const before = state.player.effects.length;
    state.player.effects = state.player.effects.filter(e => { e.turnsLeft -= 1; return e.turnsLeft > 0; });
    if (before - state.player.effects.length > 0) logT('status.buffExpired');
}

function getFrostTurns() { return state.enemy.debuffs.find(d => d.type === 'frost')?.turnsLeft || 0; }
function applyFrost(amount) {
    const frost = state.enemy.debuffs.find(d => d.type === 'frost');
    if (!frost) { state.enemy.debuffs.push({ type: 'frost', turnsLeft: amount }); logT('frost.apply', { amount }); }
    else if (amount > frost.turnsLeft) { frost.turnsLeft = amount; logT('frost.refresh', { amount }); }
    else { logT('frost.already', { turnsLeft: frost.turnsLeft }); }
}
function extendFrost(amount) {
    const frost = state.enemy.debuffs.find(d => d.type === 'frost');
    if (!frost) return logT('frost.cannotExtend');
    frost.turnsLeft += amount; logT('frost.extend', { amount, turnsLeft: frost.turnsLeft });
}
function tickEnemyDebuffs() {
    for (const d of state.enemy.debuffs) d.turnsLeft -= 1;
    state.enemy.debuffs = state.enemy.debuffs.filter(d => d.turnsLeft > 0);
}
function getEnemyStatDown() {
    let atkDown = 0, blockDown = 0;
    for (const d of state.enemy.debuffs) if (d.type === 'stat_down') { atkDown += d.value; blockDown += d.value; }
    return { atkDown, blockDown };
}

function runInsertCardPassive(trigger) {
    const passive = state.character?.passive;
    if (passive?.type !== 'insertCard' || passive.trigger !== trigger || (passive.oncePerTurn && state.passiveUsedThisTurn)) return false;
    const isHand = passive.target === 'hand', container = isHand ? state.hand : state.queue, limit = isHand ? state.handLimit : state.queueLimit;
    let inserted = 0;
    if (passive.count === 'fillToLimit') {
        while (container.length < limit) { const card = generateCard(passive.card); if (!card) break; container.push(card); inserted++; }
    } else {
        const n = passive.count || 1;
        for (let i = 0; i < n; i++) { const card = generateCard(passive.card); if (!card) break; container.push(card); inserted++; }
    }
    if (inserted > 0) { state.passiveUsedThisTurn = true; logT('passive.insertCard', { name: state.character.name, inserted }); }
    return inserted > 0;
}

function runAppendSpecialAttack() {
    const passive = state.character?.passive;
    if (passive?.type !== 'appendSpecialAttack') return false;
    const card = generateCard('chase');
    if (card) { state.queue.push(card); logT('passive.appendChase', { name: state.character.name }); }
    return true;
}

function runDelayedCardEffects() {
    if (state.pendingChant) {
        const card = generateCard('chant_attack');
        if (card) { state.queue.push(card); logT('passive.chantAttack'); }
        state.pendingChant = false;
    }
}

function snapshotQueuePositions() { state.queue.forEach((card, i) => { card.queuePosition = i + 1; }); }
function getCardStateMultiplier(card) {
    if (!card?.states) return 1;
    const passive = state.character?.passive;
    if (passive?.type !== 'matureHand') return 1;
    if (card.states.mature) return passive.matureMultiplier ?? 2;
    if (card.states.newborn) return passive.newbornMultiplier ?? 0.5;
    return 1;
}
function makeDefaultSpecialAttackConfig() { return { perAttack: 2, perDebug: 4, flatBonus: 0, minDamage: 0, bonusAttacks: 0, extraEffects: [] }; }

function rollEnemyIntentFromPool(pool) {
    const total = pool.reduce((s, e) => s + (e.weight || 1), 0); let r = Math.random() * total;
    for (const entry of pool) { r -= (entry.weight || 1); if (r <= 0) { const intent = { type: entry.type, value: entry.value }; if (entry.times) intent.times = entry.times; return intent; } }
    return { type: 'attack', value: 5 };
}
function fillEnemyQueue(limit) {
    state.enemy.queue = []; const pool = state.enemy.intentPool;
    for (let i = 0; i < limit; i++) {
        const intent = rollEnemyIntentFromPool(pool);
        if (intent.type === 'attack') runEnemyPassive('modifyAttackIntent', intent);
        state.enemy.queue.push(intent);
    }
}
function getDamageCapRemaining() { const v = runEnemyPassive('getRemainingDamageCap'); return v === undefined ? Infinity : v; }

function onPlayerDealtHpDamage(state, amount) {
    if (amount <= 0) return;
    const charPassive = state.character?.passive;
    if (charPassive?.type === 'reduceEnemyQueueLimit' && state.enemy.nextQueueLimitPenalty < charPassive.value) {
        state.enemy.nextQueueLimitPenalty = charPassive.value; logT('passive.queueLimitDown', { name: state.character.name, value: charPassive.value });
    }
    if (charPassive?.type === 'applyFrostOnHpDamage') applyFrost(charPassive.value || 1);
}

const EFFECT_HANDLERS = {
    damage(state, effect) {
        const mult = getCardStateMultiplier(state.resolvingCard), tempBonus = getAttackBonus();
        let baseDmg = Math.floor((effect.value || 0) * mult) + tempBonus;
        
        if (state.resolvingCard.id === 'spell_lianxie') {
            baseDmg += (state.specialPlayedThisTurn || 0) * 3;
            logT('special.damageBySpecialCount', { dmg: baseDmg, base: Math.floor(effect.value * mult) + tempBonus, bonus: (state.specialPlayedThisTurn || 0) * 3 });
        }

        const repeat = state.character?.passive?.type === 'extraDamageRepeat' ? state.character.passive : null;
        const isCombo = state.resolvingCard?.tags?.includes('combo');
        const admin = state.resolvingCard.adminPrivilege || {};
        const times = (effect.times || 1) + (repeat && isCombo ? repeat.value : 0) + (admin.times || 0);

        let totalReal = 0, pierceLeft = admin.pierce || 0;
        for (let r = 0; r < times; r++) {
            if (state.enemy.hp <= 0) break;
            let p = Math.min(pierceLeft, baseDmg); pierceLeft -= p;
            let b = baseDmg - p, absorbed = Math.min(state.enemy.block, b);
            state.enemy.block -= absorbed; let real = p + (b - absorbed);
            real = Math.min(real, getDamageCapRemaining());
            state.enemy.hp = Math.max(0, state.enemy.hp - real); state.enemy.damageTakenThisTurn += real;
            totalReal += real;
        }
        state.currentCardRealDamage += totalReal;
        
        if (state.resolvingCard.id !== 'spell_lianxie') {
            logT('cards.damage', { baseDmg, times, totalReal });
        }
        onPlayerDealtHpDamage(state, totalReal);
        if (admin.vuln) state.enemy.debuffs.push({ type: 'vuln', value: admin.vuln, turnsLeft: 2 });
    },
    
    damageByLostHp(state, effect) {
        const mult = getCardStateMultiplier(state.resolvingCard);
        const base = Math.floor((effect.base || 0) * mult) + getAttackBonus();
        const lostRatio = (state.enemy.maxHp - state.enemy.hp) / state.enemy.maxHp;
        const bonus = Math.floor(lostRatio * (effect.flat + state.enemy.maxHp * effect.scale));
        const dmg = base + bonus;
        const absorbed = Math.min(state.enemy.block, dmg);
        state.enemy.block -= absorbed;
        const real = Math.min(dmg - absorbed, getDamageCapRemaining());
        state.enemy.hp = Math.max(0, state.enemy.hp - real);
        state.enemy.damageTakenThisTurn += real;
        state.currentCardRealDamage += real;
        logT('cards.damageByLostHp', { dmg, base, bonus });
        onPlayerDealtHpDamage(state, real);
    },

    damageWithPierce(state, effect) {
        const mult = getCardStateMultiplier(state.resolvingCard), tempBonus = getAttackBonus();
        const total = Math.floor((effect.value || 0) * mult) + tempBonus;
        const p = Math.min(effect.pierce || 0, total);
        const absorbed = Math.min(state.enemy.block, total - p);
        state.enemy.block -= absorbed;
        const real = Math.min(p + (total - p - absorbed), getDamageCapRemaining());
        state.enemy.hp = Math.max(0, state.enemy.hp - real);
        state.enemy.damageTakenThisTurn += real;
        state.currentCardRealDamage += real;
        logT('cards.damageByPierce', { total, p });
        onPlayerDealtHpDamage(state, real);
    },

    damageByBalance(state, effect) {
        const tempBonus = getAttackBonus();
        let atk = 0, buff = 0;
        for (let i = 0; i < state.resolvingCard.queuePosition - 1; i++) {
            const c = state.queue[i]; if (c.tags.includes('attack')) atk++; else if (c.tags.includes('buff')) buff++;
        }
        const diff = Math.abs(atk - buff);
        const times = Math.max(1, Math.floor((state.queueLimit - diff) / 2 + 1));
        const baseDmg = 3 + tempBonus;
        let total = 0;
        for (let r = 0; r < times; r++) {
            const absorbed = Math.min(state.enemy.block, baseDmg);
            state.enemy.block -= absorbed;
            const real = Math.min(baseDmg - absorbed, getDamageCapRemaining());
            state.enemy.hp = Math.max(0, state.enemy.hp - real); total += real; state.enemy.damageTakenThisTurn += real;
        }
        state.currentCardRealDamage += total;
        logT('cards.damageByBalance', { diff, times, total });
        onPlayerDealtHpDamage(state, total);
    },

    damageWithPierceCondition(state, effect) {
        const base = Math.floor((effect.value || 0) * getCardStateMultiplier(state.resolvingCard)) + getAttackBonus();
        const isPierce = state.enemy.block > base * 1.5;
        const pierce = isPierce ? 2 : 0;
        const blockable = base - pierce;
        const absorbed = Math.min(state.enemy.block, blockable);
        state.enemy.block -= absorbed;
        const real = Math.min(pierce + (blockable - absorbed), getDamageCapRemaining());
        state.enemy.hp = Math.max(0, state.enemy.hp - real);
        state.enemy.damageTakenThisTurn += real;
        state.currentCardRealDamage += real;
        logT('special.insight', { isPierce: isPierce ? '触发穿透 2' : '未触发穿透', real });
        onPlayerDealtHpDamage(state, real);
    },

    damageByGainCards(state, effect) {
        const base = effect.value + getAttackBonus();
        let buffs = state.queue.filter(c => c.tags.includes('buff')).length;
        let mult = buffs >= 3 ? 1 : (buffs > 0 ? 1.5 : 2);
        const dmg = Math.floor(base * mult);
        const absorbed = Math.min(state.enemy.block, dmg);
        state.enemy.block -= absorbed;
        const real = Math.min(dmg - absorbed, getDamageCapRemaining());
        state.enemy.hp = Math.max(0, state.enemy.hp - real); state.enemy.damageTakenThisTurn += real;
        state.currentCardRealDamage += real;
        logT('cards.damageByGainCards', { buffs, real });
        onPlayerDealtHpDamage(state, real);
    },

    damageAndBlockByQueue(state, effect) {
        let atk = 0, buff = 0;
        for (let i = 0; i < state.resolvingCard.queuePosition - 1; i++) {
            const c = state.queue[i]; if (c.tags.includes('attack')) atk++; else if (c.tags.includes('buff')) buff++;
        }
        const dmg = effect.base + atk * 2 + getAttackBonus();
        const blk = effect.block + buff * 2;
        state.player.block += blk;
        const absorbed = Math.min(state.enemy.block, dmg);
        state.enemy.block -= absorbed;
        const real = Math.min(dmg - absorbed, getDamageCapRemaining());
        state.enemy.hp = Math.max(0, state.enemy.hp - real); state.enemy.damageTakenThisTurn += real;
        state.currentCardRealDamage += real;
        logT('special.resonance', { real, blk });
        onPlayerDealtHpDamage(state, real);
    },

    healOrBlock(state, effect) {
        let intentAtk = 0; state.enemy.queue.forEach(i => { if (i.type === 'attack') intentAtk += i.value * (i.times||1); });
        if (intentAtk >= effect.threshold) {
            const heal = Math.min(effect.value, state.player.maxHp - state.player.hp);
            state.player.hp += heal;
            const over = effect.value - heal;
            if (over > 0) state.player.block += over;
            logT('cards.healOrBlock_heal', { heal, over });
        } else {
            state.player.block += effect.value; logT('cards.healOrBlock_block', { value: effect.value });
        }
    },

    debugPower(state, effect) {
        state.specialAttackConfig.perAttack += effect.pAtk; state.specialAttackConfig.perDebug += effect.pDbg;
        logT('debug.power');
    },

    debugTimes(state, effect) { addTimedEffect('debug_times', effect.value, effect.turns); logT('debug.times', { value: effect.value }); },
    debugPierce(state, effect) { addTimedEffect('debug_pierce', effect.value, effect.turns); logT('debug.pierce', { value: effect.value }); },
    debugVuln(state, effect) { addTimedEffect('debug_vuln', effect.value, effect.turns); logT('debug.vuln'); },

    debugCall(state, effect) {
        const admin = {
            pierce: getDebugPierce(), times: getDebugTimes(), vuln: getDebugVuln(),
            pAtk: state.specialAttackConfig.perAttack, pDbg: state.specialAttackConfig.perDebug
        };
        let count = 0;
        for (const c of state.queue) {
            if (!c.tags.includes('special') && c.tags.includes('attack')) { c.adminPrivilege = admin; count++; }
        }
        logT('debug.call', { count });
    },

    specialDamage(state, effect) {
        const cfg = state.specialAttackConfig, debugCount = state.debugCountThisTurn || 0;
        let base = (state.attacksThisTurn * cfg.perAttack) + (debugCount * cfg.perDebug) + getAttackBonus();
        const times = 1 + getDebugTimes();
        let totalReal = 0, totalAbsorbed = 0, pierceLeft = getDebugPierce();
        for (let i = 0; i < times; i++) {
            let p = Math.min(pierceLeft, base); pierceLeft -= p;
            let b = base - p, absorbed = Math.min(state.enemy.block, b); state.enemy.block -= absorbed;
            let real = Math.min(p + (b - absorbed), getDamageCapRemaining());
            state.enemy.hp = Math.max(0, state.enemy.hp - real); state.enemy.damageTakenThisTurn += real;
            totalReal += real; totalAbsorbed += absorbed;
        }
        state.currentCardRealDamage += totalReal;
        logT('special.specialDamage_hit', { base, times, totalReal });
        onPlayerDealtHpDamage(state, totalReal);

        const statDownVal = state.player.effects.filter(e => e.type === 'debug_statdown').reduce((s, e) => s + e.value, 0);
        if (statDownVal > 0) {
            const ext = state.enemy.debuffs.find(d => d.type === 'stat_down');
            if (ext) { if (statDownVal > ext.value) { ext.value = statDownVal; ext.turnsLeft = 2; } }
            else state.enemy.debuffs.push({ type: 'stat_down', value: statDownVal, turnsLeft: 2 });
            logT('special.specialDamage_statDown', { val: statDownVal });
        }
        if (state.player.effects.some(e => e.type === 'debug_blockgain') && totalAbsorbed > 0) {
            state.player.block += totalAbsorbed;
            logT('special.specialDamage_blockGain', { absorbed: totalAbsorbed });
        }
        if (getDebugVuln() > 0) state.enemy.debuffs.push({ type: 'vuln', value: getDebugVuln(), turnsLeft: 2 });
    },

    block(state, effect) {
        if (state.resolvingCard.id === 'spell_xuji') {
            (async () => {
                if (state.hand.length > 0) {
                    await new Promise(resolve => {
                        openDiscardModal(1, (cards) => {
                            for (const c of cards) {
                                const idx = state.hand.indexOf(c);
                                if (idx >= 0) state.hand.splice(idx, 1);
                                c.states = {}; state.playedPile.push(c);
                            }
                            render(); resolve();
                        });
                    });
                }
                const wish = generateCard('choice');
                if (wish) state.hand.push(wish);
                addTimedEffect('attackBonus', 2, 2);
                render();
                logT('special.xuji');
            })();
            return;
        }
        if (state.resolvingCard.id === 'debug_block') {
            addTimedEffect('debug_blockgain', 1, 3);
            drawToLimit(1);
            logT('special.debugBlockGain');
            return;
        }
        const v = Math.floor((effect.value || 0) * getCardStateMultiplier(state.resolvingCard));
        state.player.block += v; logT('cards.block', { v });
    },

    applyStatDown(state, effect) {
        if (state.resolvingCard.id === 'debug_weak') {
            addTimedEffect('debug_statdown', 2, 2);
            drawToLimit(1);
            logT('debug.weak', { val: 2, turns: 2 });
            return;
        }
        const val = effect.value + getFrostTurns() * (effect.perFrost || 0);
        const ext = state.enemy.debuffs.find(d => d.type === 'stat_down');
        if (ext && val > ext.value) { ext.value = val; ext.turnsLeft = effect.turns; }
        else if (!ext) state.enemy.debuffs.push({ type: 'stat_down', value: val, turnsLeft: effect.turns });
        logT('cards.applyStatDown', { val });
    },

    snowball(state, effect) {
        for (const c of state.queue) { c.effects.forEach(e => { if (e.value) e.value++; if (e.flat) e.flat++; }); }
        logT('cards.snowball');
    },
    
    buffSpecialAttack(state, effect) {
        if (effect.perAttackDelta) state.specialAttackConfig.perAttack += effect.perAttackDelta;
        if (effect.flatBonusDelta) state.specialAttackConfig.flatBonus += effect.flatBonusDelta;
        logT('debug.buffUpdate');
    },

    insertCopyAtEnd(state, effect) {
        if (state.resolvingCard.queuePosition !== effect.requirePosition) return;
        const copy = makeCard(state.resolvingCard.id); copy.name += '·残响'; copy.tags.push('special');
        state.queue.push(copy); copy.queuePosition = state.queue.length;
        logT('cards.insertCopy');
    },

    applyFrost(state, effect) {
        if (state.resolvingCard.states?.frostExtend && getFrostTurns() > 0) extendFrost(effect.value);
        else applyFrost(effect.value);
    },
    extendFrost(state, effect) { extendFrost(effect.value); },
    tagQueueAttacks(state, effect) {
        for (const c of state.queue) if (c.tags.includes('attack')) c.states.frostExtend = true;
        logT('cards.tagQueue');
    },
    removeFrost(state, effect) { state.enemy.debuffs = state.enemy.debuffs.filter(d => d.type !== 'frost'); },

    lostHpDamage(state, effect) {
        const mult = getCardStateMultiplier(state.resolvingCard), base = Math.floor((effect.flat || 0) * mult) + getAttackBonus();
        const bonus = Math.floor((state.enemy.maxHp - state.enemy.hp) * (effect.lostHpPercent || 0)), dmg = base + bonus;
        const absorbed = Math.min(state.enemy.block, dmg); state.enemy.block -= absorbed;
        const real = Math.min(dmg - absorbed, getDamageCapRemaining()); state.enemy.hp = Math.max(0, state.enemy.hp - real);
        state.enemy.damageTakenThisTurn += real; state.currentCardRealDamage += real;
        logT('special.lostHpDamage', { dmg, base, bonus });
        onPlayerDealtHpDamage(state, real);
    },

    chantClear(state, effect) {
        const remaining = state.queue.slice(1); let atk = 0, buff = 0;
        for (const c of remaining) { if (c.tags.includes('attack')) atk++; else if (c.tags.includes('buff')) buff++; }
        state.queue = [state.queue[0]];
        if (atk > 0) addTimedEffect('attackBonus', atk * 2, 2); if (buff > 0) state.player.block += buff * 3;
        state.pendingChant = true;
        logT('special.chantClear', { atk, buff });
    },

    async conditionalExchange(state, effect) {
        const threshold = effect.threshold ?? 3, count = effect.count ?? 2, frost = getFrostTurns();
        if (frost > threshold) {
            for (let i = 0; i < count; i++) await new Promise(r => openDiscardModal(1, (cards) => { cards.forEach(c => { const idx = state.hand.indexOf(c); if (idx >= 0) state.hand.splice(idx, 1); c.states = {}; state.playedPile.push(c); }); render(); r(); }));
            for (let i = 0; i < count; i++) await new Promise(r => openSearchModal((card) => { if (card) { const idx = state.drawPile.indexOf(card); if (idx >= 0) { state.drawPile.splice(idx, 1); state.hand.push(card); } } render(); r(); }));
            logT('special.exchange_frost', { frost, threshold });
        } else {
            drawToLimit(count); render();
            await new Promise(r => openDiscardModal(count, (cards) => { cards.forEach(c => { const idx = state.hand.indexOf(c); if (idx >= 0) state.hand.splice(idx, 1); c.states = {}; state.playedPile.push(c); }); render(); r(); }));
            logT('special.exchange_normal', { count });
        }
    },

    damagePerFrost(state, effect) {
        const mult = getCardStateMultiplier(state.resolvingCard), base = Math.floor((effect.base || 0) * mult) + getAttackBonus(), frost = getFrostTurns(), frostAdd = frost * (effect.perFrost || 0), dmg = base + frostAdd;
        const absorbed = Math.min(state.enemy.block, dmg); state.enemy.block -= absorbed;
        const real = Math.min(dmg - absorbed, getDamageCapRemaining()); state.enemy.hp = Math.max(0, state.enemy.hp - real);
        state.enemy.damageTakenThisTurn += real; state.currentCardRealDamage += real;
        logT('special.damagePerFrost', { dmg, base, frostAdd });
        onPlayerDealtHpDamage(state, real);
    },

    damageComboPerFrost(state, effect) {
        const mult = getCardStateMultiplier(state.resolvingCard), base = Math.floor((effect.baseValue || 0) * mult) + getAttackBonus(), times = (effect.baseTimes || 0) + getFrostTurns() * (effect.perFrost || 0);
        let totalReal = 0;
        for (let r = 0; r < times; r++) { if (state.enemy.hp <= 0) break; const absorbed = Math.min(state.enemy.block, base); state.enemy.block -= absorbed; const real = Math.min(base - absorbed, getDamageCapRemaining()); state.enemy.hp = Math.max(0, state.enemy.hp - real); state.enemy.damageTakenThisTurn += real; totalReal += real; }
        state.currentCardRealDamage += totalReal;
        logT('special.damageComboPerFrost', { base, times, totalReal });
        onPlayerDealtHpDamage(state, totalReal);
    },

    discardHandAndDraw(state, effect) {
        if (state.resolvingCard.id !== 'debug_block' && state.resolvingCard.id !== 'debug_weak') {
            drawToLimit(1); logT('debug.draw');
        }
    },

    activateTrait(state, effect) {
        const id = state.resolvingCard._activateTraitId; if (!id) return;
        const trait = state.enemy.traits.find(t => t.id === id);
        if (trait && !trait.active) { trait.active = true; logT('special.activateTrait', { name: trait.name }); }
    }
};

const ENEMY_PASSIVE_HANDLERS = {
    fire_growth: { modifyAttackIntent(s, p, i) { i.value += s.enemy.attackGrowthStacks * (p.value || 0); }, onEnemyTurnEnd(s) { s.enemy.attackGrowthStacks += 1; } },
    counter_strike: { modifyAttackIntent(s, p, i) { i.value += Math.floor(s.enemy.lastPlayerDamageTaken * (p.ratio || 0)); }, onEnemyTurnEnd(s) { s.enemy.lastPlayerDamageTaken = s.enemy.damageTakenThisTurn; } },
    barrage: { modifyAttackIntent(s, p, i) { i.times = (i.times || 1) + 1; } },
    pierce_block: { getPierceAmount(s, p, a) { return Math.min(p.value, a); } },
    chill_player: { onPlayerTakeRealDamage(s, p, r) { if (r > 0) s.player.queueLimitPenalty = Math.max(s.player.queueLimitPenalty, p.value || 1); } },
    damage_cap: { getRemainingDamageCap(s, p) { return Math.max(0, Math.floor(s.enemy.maxHp * p.percent) - s.enemy.damageTakenThisTurn); } },
    regen: { onEnemyTurnStart(s, p) { s.enemy.hp = Math.min(s.enemy.maxHp, s.enemy.hp + p.value); } },
    shield_up: { onEnemyTurnStart(s, p) { s.enemy.block = Math.min(s.enemy.maxHp, s.enemy.block + p.value); } },
    thorns: { onPlayerAttackResolved(s, p, r) { if (r > 0) s.player.hp = Math.max(0, s.player.hp - p.value); } },
    flat_attack: { modifyAttackIntent(s, p, i) { i.value += p.value || 0; } },
    draw_penalty: { onEnemyTurnStart(s, p) { s.enemy.nextDrawPenalty = (s.enemy.nextDrawPenalty || 0) + (p.value || 1); } },
    hide_intent: {},
    extra_action: { getExtraActions(s, p) { return p.value || 1; } }
};
function getActiveEnemyPassives() { const list = []; if (state.enemy.passive) list.push(state.enemy.passive); for (const t of state.enemy.traits) if (t.active && t.passive) list.push(t.passive); return list; }
function runEnemyPassive(hook, ...args) { let res; for (const p of getActiveEnemyPassives()) { const h = ENEMY_PASSIVE_HANDLERS[p.type]; if (h && h[hook]) { const r = h[hook](state, p, ...args); if (r !== undefined) res = r; } } return res; }

const HAND_GAP = 8, HAND_MIN_STEP = 26;
function layoutHand() {
    const handEl = document.getElementById('spire-hand'); if (!handEl) return;
    const cards = handEl.querySelectorAll('.spire-card'); if (cards.length === 0) return;
    const containerW = handEl.clientWidth, cardW = cards[0].getBoundingClientRect().width || 90;
    if (cards.length * cardW + (cards.length - 1) * HAND_GAP <= containerW) { cards.forEach(c => c.style.marginLeft = ''); return; }
    const step = Math.max(HAND_MIN_STEP, (containerW - cardW) / (cards.length - 1));
    cards.forEach((c, i) => c.style.marginLeft = i === 0 ? '' : `${step - cardW}px`);
}
function drawToLimit(count) {
    let drawn = 0;
    while (drawn < count && state.hand.length < state.handLimit) {
        if (state.drawPile.length === 0) { if (state.playedPile.length === 0) break; state.drawPile = shuffle(state.playedPile); state.playedPile = []; }
        state.hand.push(state.drawPile.pop()); drawn++;
    }
}
function showMainMenu() { state = null; document.getElementById('main-menu').classList.remove('hidden'); document.getElementById('spire-select').classList.remove('active'); const midLog = document.getElementById('mid-strip-log'); if (midLog) midLog.innerHTML = ''; }
function matchesGlossary(e, q) { if (!q) return true; return (e.term||'').toLowerCase().includes(q) || (e.pinyin||'').toLowerCase().includes(q) || (e.abbr||'').toLowerCase().includes(q); }
function renderGlossary(query) { const body = document.getElementById('glossary-body'), q = (query || '').trim().toLowerCase(); const filtered = GLOSSARY_DATA.filter(e => matchesGlossary(e, q)); body.innerHTML = filtered.length === 0 ? '<div class="glossary-empty">没有匹配的词条</div>' : filtered.map(e => `<div class="glossary-entry"><div class="glossary-term">${e.term}</div><div class="glossary-def">${e.def}</div></div>`).join(''); }
function showGlossary() { const input = document.getElementById('glossary-search-input'); input.value = ''; renderGlossary(''); document.getElementById('glossary-modal').classList.add('active'); setTimeout(() => input.focus(), 50); }

function showCharacterSelect() {
    state = null;
    document.getElementById('spire-select').classList.add('active');
    buildCharWheel(); buildEnemyWheel();
    const charKeys = Object.keys(CHARACTER_LIBRARY); if (!selectedCharKey && charKeys.length > 0) selectedCharKey = charKeys[0];
    if (selectedCharKey) selectCharacter(selectedCharKey);
    const enemyKeys = Object.keys(ENEMY_LIBRARY); if (!selectedEnemyKey && enemyKeys.length > 0) selectedEnemyKey = enemyKeys[0];
    if (selectedEnemyKey) selectEnemy(selectedEnemyKey);
}
function buildCharWheel() { const container = document.getElementById('char-wheel'); container.innerHTML = ''; Object.keys(CHARACTER_LIBRARY).forEach(key => { const el = document.createElement('div'); el.className = 'spire-wheel-item'; el.dataset.key = key; el.textContent = CHARACTER_LIBRARY[key].name; el.addEventListener('click', () => selectCharacter(key)); container.appendChild(el); }); }
function buildEnemyWheel() { const container = document.getElementById('enemy-wheel'); container.innerHTML = ''; Object.keys(ENEMY_LIBRARY).forEach(key => { const el = document.createElement('div'); el.className = 'spire-wheel-item'; el.dataset.key = key; el.textContent = ENEMY_LIBRARY[key].name; el.addEventListener('click', () => selectEnemy(key)); container.appendChild(el); }); }
function selectCharacter(key) {
    selectedCharKey = key;
    document.querySelectorAll('#char-wheel .spire-wheel-item').forEach(el => el.classList.toggle('selected', el.dataset.key === key));
    const c = CHARACTER_LIBRARY[key]; document.getElementById('char-name-display').textContent = c.name;
    const pEl = document.getElementById('char-passive-display'); if (c.passiveName) { pEl.textContent = `被动：${c.passiveName}`; pEl.style.display = 'inline-block'; } else { pEl.style.display = 'none'; }
    document.getElementById('char-desc-display').textContent = c.description; document.getElementById('char-stat-display').textContent = `HP ${c.maxHp}`; updateStartButton();
}
function selectEnemy(key) {
    selectedEnemyKey = key;
    document.querySelectorAll('#enemy-wheel .spire-wheel-item').forEach(el => el.classList.toggle('selected', el.dataset.key === key));
    const e = ENEMY_LIBRARY[key]; document.getElementById('enemy-name-display').textContent = e.name; document.getElementById('enemy-desc-display').textContent = e.description; document.getElementById('enemy-stat-display').textContent = `HP ${e.maxHp} · 行动上限 ${e.queueLimit}`; updateStartButton();
}
function updateStartButton() { const btn = document.getElementById('start-battle-btn'); if (!btn) return; if (selectedCharKey && selectedEnemyKey) { btn.style.opacity = '1'; btn.style.cursor = 'pointer'; btn.style.pointerEvents = 'auto'; } else { btn.style.opacity = '0.3'; btn.style.cursor = 'not-allowed'; btn.style.pointerEvents = 'none'; } }

function startBattle(characterKey, enemyKey) {
    const c = CHARACTER_LIBRARY[characterKey], e = ENEMY_LIBRARY[enemyKey]; if (!c || !e) return;
    const p = c.passive || {};
    state = {
        character: c, characterKey: characterKey, enemyDef: e, enemyKey: enemyKey,
        player: { hp: c.maxHp, maxHp: c.maxHp, block: 0, queueLimitPenalty: 0, effects: [] },
        enemy: { hp: e.maxHp, maxHp: e.maxHp, block: 0, baseQueueLimit: e.queueLimit, queueLimit: e.queueLimit, nextQueueLimitPenalty: 0, nextDrawPenalty: 0, intentPool: e.intentPool, passive: e.passive, attackGrowthStacks: 0, lastPlayerDamageTaken: 0, damageTakenThisTurn: 0, queue: [], debuffs: [], traits: (e.traits || []).map(t => Object.assign({}, t, { active: false })) },
        drawPile: [], hand: [], playedPile: [], queue: [],
        baseQueueLimit: BASE_QUEUE_LIMIT + (p.queueLimitBonus || 0), queueLimit: BASE_QUEUE_LIMIT + (p.queueLimitBonus || 0), handLimit: BASE_HAND_LIMIT + (p.handLimitBonus || 0),
        turn: 1, phase: 'building', currentCardRealDamage: 0, attacksThisTurn: 0, debugCountThisTurn: 0, passiveUsedThisTurn: false, snowballActive: false, specialPlayedThisTurn: 0,
        specialAttackConfig: makeDefaultSpecialAttackConfig(), resolvingCard: null, resolvingCardUid: null, pendingChant: false, log: []
    };
    const extra = runEnemyPassive('getExtraActions') || 0; if (extra > 0) { state.enemy.baseQueueLimit += extra; state.enemy.queueLimit += extra; }
    fillEnemyQueue(state.enemy.baseQueueLimit);
    state.drawPile = shuffle(c.deck.map(id => makeCard(id)));
    drawToLimit(BASE_DRAW_PER_TURN + (p.drawBonus || 0) - (p.drawPenalty || 0));
    if (p.type === 'matureHand') state.hand.forEach(card => card.states.newborn = true);
    runInsertCardPassive('turnStart'); document.getElementById('spire-select').classList.remove('active'); render();
}

function playCardFromHand(index) {
    hideCardTooltip(); if (state.phase !== 'building' || state.queue.length >= state.queueLimit) return logT('battle.unknownEffect', {type: '无法打出'});
    const card = state.hand[index]; if (!card) return;
    if (card.isChoice) return showChoiceModal(index, [{ label: '攻击 6', value: 'attack' }, { label: '防御 5', value: 'defend', className: 'defend' }], '祈愿');
    if (card.id === 'ignite' && state.enemy.traits.filter(t => !t.active).length > 0) {
        const opts = state.enemy.traits.filter(t => !t.active).map(t => ({ label: `激活「${t.name}」`, value: t.id }));
        opts.push({ label: '跳过', value: 'skip', className: 'skip' }); return showChoiceModal(index, opts, '激活敌方词条');
    }
    doPlayCard(index);
}
function doPlayCard(index) {
    const sourceEl = document.querySelectorAll('#spire-hand .spire-card')[index]; const sourceRect = sourceEl ? sourceEl.getBoundingClientRect() : null;
    const card = state.hand.splice(index, 1)[0]; card.handIndex = index; state.queue.push(card); render();
    if (sourceRect) animateCardFly(sourceRect, card.uid);
}
function animateCardFly(sourceRect, uid) {
    const targetEl = document.querySelector(`#stage-queue .queue-slot[data-uid="${uid}"]`); if (!targetEl) return;
    const targetRect = targetEl.getBoundingClientRect(); const clone = document.createElement('div'); clone.className = 'spire-card';
    clone.innerHTML = `<div class="name">${state.queue.find(c => c.uid === uid).name}</div>`;
    clone.style.cssText = `position:fixed;left:0;top:0;width:${sourceRect.width}px;height:${sourceRect.height}px;margin:0;pointer-events:none;z-index:9999;transform-origin:top left;transform:translate(${sourceRect.left}px,${sourceRect.top}px) scale(1);transition:transform 0.32s cubic-bezier(0.4,0,0.2,1);`;
    document.body.appendChild(clone); targetEl.style.visibility = 'hidden';
    const scale = Math.min(targetRect.width / sourceRect.width, targetRect.height / sourceRect.height);
    requestAnimationFrame(() => { clone.style.transform = `translate(${targetRect.left + targetRect.width/2 - (sourceRect.width*scale)/2}px, ${targetRect.top + targetRect.height/2 - (sourceRect.height*scale)/2}px) scale(${scale})`; });
    setTimeout(() => { clone.remove(); if (targetEl.parentNode) targetEl.style.visibility = 'visible'; }, 330);
}

let choiceTargetIndex = -1, choiceOptions = [];
function showChoiceModal(index, options, title) {
    choiceTargetIndex = index; choiceOptions = options; document.getElementById('choice-title').textContent = title || '抉择';
    const c = document.getElementById('choice-options'); c.innerHTML = '';
    options.forEach((opt, i) => { const b = document.createElement('div'); b.className = 'modal-btn'; b.style.display='block'; b.style.margin='6px 0'; b.style.textAlign='center'; b.textContent = opt.label; if (opt.className) b.classList.add(opt.className); b.addEventListener('click', () => handleChoice(i)); c.appendChild(b); });
    document.getElementById('choice-modal').classList.add('active');
}
function handleChoice(optIndex) {
    const opt = choiceOptions[optIndex]; document.getElementById('choice-modal').classList.remove('active');
    if (choiceTargetIndex < 0 || !opt) return;
    const card = state.hand[choiceTargetIndex]; if (!card) { choiceTargetIndex = -1; return; }
    if (card.isChoice) {
        card._wasChoice = true;
        if (opt.value === 'attack') { card.name = '攻击'; card.description = '造成 6 点伤害。'; card.effects = [{ type: 'damage', value: 6 }]; if (!card.tags.includes('attack')) card.tags.push('attack'); }
        else { card.name = '防御'; card.description = '获得 5 点格挡。'; card.effects = [{ type: 'block', value: 5 }]; if (!card.tags.includes('buff')) card.tags.push('buff'); }
        card.isChoice = false;
    } else if (card.id === 'ignite' && opt.value !== 'skip') {
        card._activateTraitId = opt.value; card.effects.push({ type: 'damage', value: 4 }); card.effects.push({ type: 'activateTrait' });
    }
    const idx = choiceTargetIndex; choiceTargetIndex = -1; doPlayCard(idx);
}

async function resolveQueueAsync() {
    while (state.queue.length > 0) {
        const card = state.queue[0]; state.resolvingCard = card; state.resolvingCardUid = card.uid;
        render(); await sleep(450); logT('battle.playCard', { name: card.name }); state.currentCardRealDamage = 0;
        const isAtk = card.tags?.includes('attack'); if (card.tags?.includes('debug')) state.debugCountThisTurn++;
        for (const effect of card.effects) { const h = EFFECT_HANDLERS[effect.type]; if (h) await h(state, effect); else logT('battle.unknownEffect', { type: effect.type }); }
        if (isAtk) {
            state.attacksThisTurn++;
            if (state.character?.passive?.type === 'lifesteal') { const cost = Math.floor(state.player.hp * state.character.passive.costPercent), heal = state.currentCardRealDamage; state.player.hp = Math.max(0, state.player.hp - cost + heal); logT('battle.lifesteal', { cost, heal }); }
            if (state.currentCardRealDamage > 0) runEnemyPassive('onPlayerAttackResolved', state.currentCardRealDamage);
        }
        if (isSpecialCard(card)) state.specialPlayedThisTurn++;
        state.queue.shift(); if (!isSpecialCard(card)) { card.states = {}; const bt = CARD_LIBRARY[card.id]?.tags; if (bt) card.tags = [...bt]; state.playedPile.push(card); }
        state.resolvingCard = null; state.resolvingCardUid = null; render(); await sleep(220);
        if (state.player.hp <= 0) { state.phase = 'gameover'; logT('battle.playerDead'); return; }
        if (state.enemy.hp <= 0) { state.phase = 'gameover'; logT('battle.enemyDead'); return; }
    }
    state.resolvingCard = null; state.resolvingCardUid = null;
}

async function enemyActAllAsync() {
    state.enemy.block = 0; runEnemyPassive('onEnemyTurnStart'); render(); await sleep(300);
    const { atkDown, blockDown } = getEnemyStatDown();
    for (const intent of state.enemy.queue.slice()) {
        if (state.player.hp <= 0) return;
        if (intent.type === 'attack') {
            const val = Math.max(0, intent.value - atkDown), times = intent.times || 1;
            for (let t = 0; t < times; t++) {
                if (state.player.hp <= 0) break;
                const pierce = runEnemyPassive('getPierceAmount', val) ?? 0; const blockable = val - pierce, absorbed = Math.min(state.player.block, blockable);
                state.player.block -= absorbed; const real = pierce + (blockable - absorbed); state.player.hp = Math.max(0, state.player.hp - real);
                logT('battle.enemyAttack', { real, absorbed }); if (real > 0) runEnemyPassive('onPlayerTakeRealDamage', real); render(); await sleep(500);
            }
        } else if (intent.type === 'buff') {
            const val = Math.max(0, intent.value - blockDown); state.enemy.block = Math.min(state.enemy.maxHp, state.enemy.block + val);
            logT('battle.enemyBlock', { val }); render(); await sleep(500);
        }
    }
    if (state.enemy.hp <= 0) return;
    runEnemyPassive('onEnemyTurnEnd');
    const penalty = state.enemy.nextQueueLimitPenalty; state.enemy.nextQueueLimitPenalty = 0;
    let limit = Math.max(0, state.enemy.baseQueueLimit - penalty); if (state.enemy.debuffs.some(d => d.type === 'frost')) limit = Math.max(0, limit - 1);
    limit += runEnemyPassive('getExtraActions') || 0;
    state.enemy.queueLimit = limit; fillEnemyQueue(limit);
}

function startNewTurn() {
    state.turn++; const p = state.character?.passive;
    if (p?.type !== 'blockPersist') state.player.block = 0;
    tickPlayerEffects(); tickEnemyDebuffs();
    state.queueLimit = Math.max(0, state.baseQueueLimit - (state.player.queueLimitPenalty || 0));
    state.player.queueLimitPenalty = 0; state.attacksThisTurn = 0; state.debugCountThisTurn = 0;
    state.passiveUsedThisTurn = false; state.enemy.damageTakenThisTurn = 0; state.snowballActive = false; state.specialPlayedThisTurn = 0;
    state.specialAttackConfig = makeDefaultSpecialAttackConfig();
    if (p?.type === 'matureHand') for (const c of state.hand) if (c.states?.newborn) { delete c.states.newborn; c.states.mature = true; }
    let dc = BASE_DRAW_PER_TURN + (p?.drawBonus || 0) - (p?.drawPenalty || 0) - (state.enemy.nextDrawPenalty || 0); state.enemy.nextDrawPenalty = 0;
    drawToLimit(Math.max(0, dc));
    if (p?.type === 'matureHand') for (const c of state.hand) if (!c.states.mature && !c.states.newborn) c.states.newborn = true;
    runInsertCardPassive('turnStart');
}

async function resolveAndEndTurn() {
    if (state.phase !== 'building') return;
    while (state.hand.length > state.handLimit) { const si = state.hand.findIndex(c => isSpecialCard(c)); if (si >= 0) state.hand.splice(si, 1); else state.hand.pop(); }
    state.phase = 'resolving'; render(); hideCardTooltip(); await sleep(250);
    if (state.character?.passive?.type === 'adventure') {
        let a = 0, b = 0; for (const c of state.hand) { if (c.tags?.includes('attack')) a++; else if (c.tags?.includes('buff')) b++; }
        state.hand.forEach(c => { c.states = {}; state.playedPile.push(c); }); state.hand = [];
        if (a > 0) addTimedEffect('attackBonus', a * (state.character.passive.attackBonusPerCard || 2), 1); if (b > 0) state.player.block += b * (state.character.passive.blockPerCard || 3);
        render(); await sleep(350);
    }
    runDelayedCardEffects(); runInsertCardPassive('beforeResolve'); runAppendSpecialAttack(); snapshotQueuePositions(); render(); await sleep(300);
    await resolveQueueAsync(); if (state.phase === 'gameover') { render(); return; }
    await sleep(250); await enemyActAllAsync();
    if (state.player.hp <= 0 || state.enemy.hp <= 0) { state.phase = 'gameover'; render(); return; }
    await sleep(250); startNewTurn(); state.phase = 'building'; render();
}

function render() {
    if (!state) return;
    const el = document.getElementById('turn-num'); if (el) el.textContent = state.turn;
    const el1 = document.getElementById('player-hp-fill'); if (el1) el1.style.width = (state.player.hp / state.player.maxHp * 100) + '%';
    const el2 = document.getElementById('player-hp'); if (el2) el2.textContent = state.player.hp;
    const el3 = document.getElementById('player-maxhp'); if (el3) el3.textContent = state.player.maxHp;
    const pB = document.getElementById('player-block'); if (pB) { pB.childNodes[pB.childNodes.length - 1].textContent = state.player.block; pB.classList.toggle('zero', state.player.block === 0); }
    const el4 = document.getElementById('enemy-hp-fill'); if (el4) el4.style.width = (state.enemy.hp / state.enemy.maxHp * 100) + '%';
    const el5 = document.getElementById('enemy-hp'); if (el5) el5.textContent = state.enemy.hp;
    const el6 = document.getElementById('enemy-maxhp'); if (el6) el6.textContent = state.enemy.maxHp;
    const eB = document.getElementById('enemy-block'); if (eB) { eB.childNodes[eB.childNodes.length - 1].textContent = state.enemy.block; eB.classList.toggle('zero', state.enemy.block === 0); }
    const el7 = document.getElementById('player-portrait-name'); if (el7) el7.textContent = state.character.name;
    const el8 = document.getElementById('enemy-portrait-name'); if (el8) el8.textContent = state.enemyDef.name;
    const rFx = (id, arr) => {
        const el = document.getElementById(id); if (!el) return; el.innerHTML = '';
        for (let i = 0; i < 4; i++) { const s = document.createElement('div'), f = arr[i]; if (f) { s.className = 'fx-slot ' + (f.cls || ''); s.title = f.title || ''; s.textContent = f.label.slice(0,2); } else s.className = 'fx-slot empty'; el.appendChild(s); }
    };
    rFx('player-fx', state.player.effects.map(e => { if (e.type === 'attackBonus') return { label: `攻+${e.value}`, title: `攻击 +${e.value}`, cls: 'atk' }; if (e.type.startsWith('debug')) return { label: `调+${e.value}`, title: `调试增益：${e.type}`, cls: 'debug' }; return { label: '?', title: '' }; }));
    rFx('enemy-fx', state.enemy.debuffs.map(d => { if (d.type === 'frost') return { label: `霜${d.turnsLeft}`, title: `霜冻：上限 -1`, cls: 'frost' }; if (d.type === 'stat_down') return { label: `弱${d.value}`, title: `属性降低`, cls: 'stat' }; return { label: '?', title: d.type }; }));
    const traitsEl = document.getElementById('enemy-traits'); if (traitsEl) traitsEl.innerHTML = state.enemy.traits.map(t => `<div class="trait-chip ${t.active ? 'active' : ''}" title="${t.description || ''}">${t.name}</div>`).join('');
    const hi = getActiveEnemyPassives().some(p => p.type === 'hide_intent'), { atkDown, blockDown } = getEnemyStatDown();
    const iBox = document.getElementById('enemy-intent'); if (iBox) { iBox.innerHTML = state.enemy.queue.length === 0 ? '<span class="intent-label">行动意图</span>' : state.enemy.queue.map(i => { if (i.type === 'attack') return `<span class="intent-chip">攻 ${hi?'?':Math.max(0,i.value-atkDown)}${i.times>1?'×'+i.times:''}</span>`; if (i.type === 'buff') return `<span class="intent-chip buff">盾 +${hi?'?':Math.max(0,i.value-blockDown)}</span>`; return `<span class="intent-chip">未知</span>`; }).join(''); }
    const stageEl = document.getElementById('stage-queue'); if (stageEl) { stageEl.innerHTML = state.queue.map(c => { const cls = ['queue-slot']; if (isSpecialCard(c)) cls.push('special'); if (c.uid === state.resolvingCardUid) cls.push('resolving'); return `<span class="${cls.join(' ')}" data-uid="${c.uid}">${c.name}</span>`; }).join(''); }
    const hEl = document.getElementById('spire-hand');
    if (hEl) {
        hEl.innerHTML = '';
        state.hand.forEach((card, i) => {
            const cardEl = document.createElement('div'); cardEl.className = 'spire-card'; cardEl.dataset.uid = card.uid;
            if (state.queue.length >= state.queueLimit || state.phase !== 'building') cardEl.classList.add('disabled');
            if (isSpecialCard(card)) cardEl.style.borderColor = '#e0a0a0';
            cardEl.innerHTML = `<div class="name">${card.name}</div>`;
            if (card.states?.newborn) cardEl.innerHTML += `<div class="card-badge newborn">新</div>`; else if (card.states?.mature) cardEl.innerHTML += `<div class="card-badge mature">熟</div>`; else if (card.states?.frostExtend) cardEl.innerHTML += `<div class="card-badge tag">侵</div>`;
            if (card.tags?.includes('debug')) cardEl.innerHTML += `<div class="card-badge debug">调</div>`;
            if (!isTouchOnly) { cardEl.addEventListener('mouseenter', () => showCardTooltip(card, cardEl)); cardEl.addEventListener('mouseleave', hideCardTooltip); }
            cardEl.addEventListener('click', () => playCardFromHand(i)); hEl.appendChild(cardEl);
        }); layoutHand();
    }
    const dc = document.getElementById('draw-count'); if (dc) dc.textContent = state.drawPile.length;
    const rb = document.getElementById('resolve-btn'); if (rb) rb.disabled = state.phase !== 'building';
    const logEl = document.getElementById('mid-strip-log'); if (logEl) { logEl.innerHTML = state.log.slice(-60).map(l => `<div>${l}</div>`).join(''); logEl.scrollTop = logEl.scrollHeight; }
}

let searchCallback = null, searchSelected = null, discardCallback = null, discardSelected = [];
function openSearchModal(callback) {
    const grid = document.getElementById('search-grid'); if (!grid) { callback(null); return; } grid.innerHTML = ''; searchSelected = null;
    if (state.drawPile.length === 0) { callback(null); return; }
    state.drawPile.forEach(c => { const el = document.createElement('div'); el.className = 'search-item'; el.textContent = c.name; el.addEventListener('click', () => { grid.querySelectorAll('.search-item').forEach(x => x.classList.remove('selected')); el.classList.add('selected'); searchSelected = c; }); grid.appendChild(el); });
    searchCallback = callback; document.getElementById('search-modal').classList.add('active');
}
function openDiscardModal(count, callback) {
    const grid = document.getElementById('discard-grid'); if (!grid) { callback([]); return; } grid.innerHTML = ''; discardSelected = [];
    const req = document.getElementById('discard-required'); if (req) req.textContent = count;
    if (state.hand.length === 0) { callback([]); return; }
    state.hand.forEach(c => { const el = document.createElement('div'); el.className = 'search-item'; el.textContent = c.name; el.addEventListener('click', () => { const idx = discardSelected.indexOf(c); if (idx >= 0) { discardSelected.splice(idx, 1); el.classList.remove('selected'); } else if (discardSelected.length < count) { discardSelected.push(c); el.classList.add('selected'); } }); grid.appendChild(el); });
    discardCallback = callback; document.getElementById('discard-modal').classList.add('active');
}

bindEvent('search-confirm', 'click', () => { document.getElementById('search-modal').classList.remove('active'); const cb = searchCallback, card = searchSelected; searchCallback = null; searchSelected = null; if (cb) cb(card); });
bindEvent('discard-confirm', 'click', () => { document.getElementById('discard-modal').classList.remove('active'); const cb = discardCallback, cards = discardSelected.slice(); discardCallback = null; discardSelected = []; if (cb) cb(cards); });
bindEvent('resolve-btn', 'click', resolveAndEndTurn);
bindEvent('restart-btn', 'click', () => { if (state?.phase !== 'resolving') { document.getElementById('mid-strip-log').innerHTML = ''; showCharacterSelect(); } });
bindEvent('log-btn', 'click', () => document.getElementById('mid-strip').classList.toggle('open'));
bindEvent('mid-strip-close', 'click', (e) => { e.stopPropagation(); document.getElementById('mid-strip').classList.remove('open'); });
bindEvent('menu-fight', 'click', () => { document.getElementById('main-menu').classList.add('hidden'); showCharacterSelect(); });
bindEvent('back-to-menu-btn', 'click', showMainMenu);
bindEvent('menu-glossary', 'click', showGlossary);
bindEvent('glossary-search-input', 'input', (e) => renderGlossary(e.target.value));
bindEvent('glossary-close', 'click', () => document.getElementById('glossary-modal').classList.remove('active'));
bindEvent('draw-pile-btn', 'click', () => {
    if (!state) return;
    const rp = (id, arr) => { const el = document.getElementById(id); if (el) el.innerHTML = arr.length === 0 ? '<div style="color:#bbb;font-size:0.85em;">（空）</div>' : arr.map(c => `<span class="pile-item ${isSpecialCard(c)?'special':''}">${c.name}</span>`).join(''); };
    rp('pile-modal-draw', state.drawPile); rp('pile-modal-discard', state.playedPile); document.getElementById('pile-modal').classList.add('active');
});
bindEvent('pile-modal', 'click', (e) => { if (e.target.id === 'pile-modal') e.target.classList.remove('active'); });
bindEvent('stage-queue', 'click', (e) => {
    if (!state || state.phase !== 'building') return;
    const slot = e.target.closest('.queue-slot'); if (!slot) return;
    const idx = state.queue.findIndex(c => c.uid === parseInt(slot.dataset.uid)); if (idx < 0) return;
    const card = state.queue.splice(idx, 1)[0];
    if (card._wasChoice) { card.name = '祈愿'; card.description = '打出时选择：攻击 6，或防御 5。'; card.effects = []; card.isChoice = true; card.tags = card.tags.filter(t => t !== 'attack' && t !== 'buff'); delete card._wasChoice; }
    if (card._activateTraitId) { card.effects = card.effects.filter(e => e.type !== 'activateTrait'); const l = card.effects.map(e => e.type).lastIndexOf('damage'); if (l >= 0) card.effects.splice(l, 1); delete card._activateTraitId; }
    delete card.handIndex; state.hand.push(card); render();
});
bindEvent('start-battle-btn', 'click', () => { if (selectedCharKey && selectedEnemyKey) startBattle(selectedCharKey, selectedEnemyKey); });
window.addEventListener('resize', () => { if (state) layoutHand(); });

Promise.all([
    fetch('/data/ruogelike-card.json').then(r => r.json()),
    fetch('/data/ruogelike-character.json').then(r => r.json()),
    fetch('/data/ruogelike-enemy.json').then(r => r.json()),
    fetch('/data/ruogelike-glossary.json').then(r => r.json()).catch(() => []),
    fetch('/data/ruogelike-logs.json').then(r => r.json()).catch(() => ({}))
]).then(([c, ch, e, g, l]) => {
    CARD_LIBRARY = c; CHARACTER_LIBRARY = ch; ENEMY_LIBRARY = e; GLOSSARY_DATA = g || []; 
    LOG = new Proxy(l || {}, {
        get(target, prop) {
            if (prop in target) {
                const val = target[prop];
                if (typeof val === 'object' && val !== null) {
                    return new Proxy(val, {
                        get(t, p) { return p in t ? t[p] : `<缺少文本: ${String(prop)}.${String(p)}>`; }
                    });
                }
                return val;
            }
            return `<缺少文本: ${String(prop)}>`;
        }
    });
    showMainMenu();
}).catch(err => {
    console.error(err); document.body.innerHTML = '<div style="padding:20px;">加载失败，请检查 JSON。</div>';
});
</script>