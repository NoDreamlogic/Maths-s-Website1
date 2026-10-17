---
title: "迷你游戏"
---

<style>
    * { box-sizing: border-box; }

    #spire-page {
        max-width: 1100px;
        margin: 0 auto;
        padding: 20px;
        font-family: inherit;
    }
    #spire-page h1 {
        margin: 0 0 12px;
        font-size: 1.1em;
        color: #999;
        font-weight: 500;
    }

    #top-bar {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 24px;
        padding: 8px 0;
        border-bottom: 1px solid #eee;
        margin-bottom: 16px;
        font-size: 0.9em;
        color: #666;
    }
    #top-bar .turn { font-weight: 600; color: #333; letter-spacing: 0.05em; }
    #top-bar .menu-btn {
        padding: 4px 12px;
        border: 1px solid #ddd;
        border-radius: 6px;
        background: #fff;
        color: #666;
        cursor: pointer;
        font-family: inherit;
        font-size: 0.9em;
    }
    #top-bar .menu-btn:hover { background: #f5f5f5; }

        #arena {
        display: flex;
        gap: 0;
        margin-bottom: 16px;
        min-height: 320px;
    }
    .mid-strip {
        flex: 0 0 220px;
        align-self: stretch;
        background: #fafafa;
        border-left: 1px solid #eee;
        border-right: 1px solid #eee;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        user-select: none;
        overflow: hidden;
    }
    .mid-strip:hover { background: #f0f0f0; }
    .mid-strip.open {
        cursor: default;
        background: #fff;
        align-items: stretch;
    }
    .mid-strip-label {
        writing-mode: vertical-rl;
        font-size: 0.8em;
        color: #999;
        letter-spacing: 0.2em;
        text-align: center;
    }
    .mid-strip.open .mid-strip-label { display: none; }
    .mid-strip-content {
        display: none;
        flex-direction: column;
        width: 100%;
        height: 100%;
    }
    .mid-strip.open .mid-strip-content { display: flex; }
    .mid-strip-header {
        padding: 8px 12px;
        border-bottom: 1px solid #eee;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 0.85em;
        color: #666;
    }
    .mid-strip-close {
        cursor: pointer;
        color: #999;
        border: none;
        background: none;
        font-family: inherit;
        font-size: 1em;
        padding: 0 4px;
    }
    .mid-strip-log {
        flex: 1;
        padding: 10px 12px;
        overflow-y: auto;
        font-size: 0.8em;
        color: #666;
        line-height: 1.6;
    }

    .side-col { display: flex; flex-direction: column; gap: 8px; min-height: 0; }
    .side-col.player { flex: 4; }
    .side-col.enemy  { flex: 6; }

    .hp-row { display: flex; align-items: center; gap: 8px; }
    .hp-bar {
        flex: 1; height: 26px;
        background: #eee;
        border: 1px solid #ddd;
        border-radius: 5px;
        position: relative;
        overflow: hidden;
    }
    .hp-bar .fill {
        position: absolute; top: 0; left: 0; bottom: 0;
        background: #7ec8e3;
        transition: width 0.3s;
    }
    .side-col.enemy .hp-bar .fill { background: #6cc56c; }
    .hp-bar .text {
        position: absolute; inset: 0;
        display: flex; align-items: center; justify-content: center;
        font-size: 0.85em; font-weight: 600; color: #333;
    }

    .fx-row { display: flex; gap: 4px; min-height: 22px; cursor: pointer; flex-wrap: wrap; }
    .fx-slot {
        width: 22px; height: 22px;
        border: 1px solid #ddd;
        border-radius: 4px;
        background: #fff;
        display: flex; align-items: center; justify-content: center;
        font-size: 0.7em; color: #666;
    }
    .fx-slot.empty { background: #fafafa; }
    .fx-slot.frost { border-color: #6b8fbf; background: #eaf2fb; color: #3a5f8f; }
    .fx-slot.stat  { border-color: #a06b8f; background: #fbeaf2; color: #8f3a5f; }
    .fx-slot.atk   { border-color: #a04040; background: #fff0f0; color: #a04040; }

    .portrait {
        flex: 1; min-height: 180px;
        border: 1px solid #ddd; border-radius: 8px;
        background: #fafafa;
        display: flex; align-items: center; justify-content: center;
        color: #bbb; font-size: 0.9em;
    }

    .enemy-mid { display: flex; gap: 8px; flex: 1; min-height: 0; }
    .enemy-portrait {
        flex: 1;
        border: 1px solid #ddd; border-radius: 8px;
        background: #fafafa;
        display: flex; align-items: center; justify-content: center;
        color: #bbb; font-size: 0.9em;
    }
    .enemy-side { flex: 0 0 160px; display: flex; flex-direction: column; gap: 6px; }
    .trait-list { display: flex; flex-direction: column; gap: 3px; font-size: 0.75em; }
    .trait-chip {
        padding: 2px 6px;
        border-radius: 4px;
        border: 1px solid #ddd;
        background: #fafafa;
        color: #999;
    }
    .trait-chip.active { border-color: #7030a0; background: #7030a0; color: #fff; }
    .intent-box {
        flex: 1;
        min-height: 60px;
        border: 1px solid #ddd; border-radius: 8px;
        padding: 6px;
        display: flex; flex-wrap: wrap; gap: 4px;
        align-content: flex-start; font-size: 0.8em;
    }
    .intent-box .intent-label { color: #bbb; font-size: 0.85em; }
    .intent-chip {
        padding: 2px 6px; border-radius: 4px;
        border: 1px solid #e0a0a0; background: #fff8f8; color: #a04040;
    }
    .intent-chip.buff { border-color: #a0c0e0; background: #f5faff; color: #2060a0; }

    #bottom {
        display: flex; gap: 8px;
        min-height: 200px;
        border: 2px solid #ccc; border-radius: 10px;
        padding: 8px;
    }
    .bottom-side { flex: 0 0 64px; display: flex; flex-direction: column; gap: 6px; }
    .bottom-side .label-box {
        border: 1px solid #ddd; border-radius: 6px;
        background: #fafafa; color: #999;
        font-size: 0.7em; text-align: center;
        padding: 6px 4px; line-height: 1.4;
    }
    .bottom-side .queue-label {
        flex: 1; display: flex; align-items: center; justify-content: center;
        writing-mode: vertical-rl;
    }
    .bottom-side .draw-label { cursor: pointer; user-select: none; }
    .bottom-side .draw-label:hover { background: #f0f0f0; }
    .bottom-side .draw-label .count { font-weight: 600; color: #666; }

    .bottom-main {
        flex: 1;
        position: relative;
        display: flex;
        flex-direction: column;
        gap: 6px;
        min-width: 0;
    }
    #resolve-btn {
        position: absolute;
        top: 4px; right: 4px;
        padding: 6px 14px;
        border-radius: 6px;
        border: 1px solid #333; background: #333; color: #fff;
        cursor: pointer; font-family: inherit; font-size: 0.85em;
        z-index: 5;
    }
    #resolve-btn:disabled { opacity: 0.4; cursor: not-allowed; }

    #stage-queue {
        min-height: 56px;
        padding: 8px 100px 8px 8px;
        border: 1px dashed #ccc;
        border-radius: 8px;
        background: #fafafa;
        display: flex; flex-wrap: wrap;
        align-items: center; align-content: flex-start;
        gap: 6px;
    }
    #stage-queue:empty::before {
        content: '（空）';
        color: #ccc; font-size: 0.85em;
    }
    .queue-slot {
        padding: 6px 12px;
        border: 1px solid #ddd; border-radius: 6px;
        background: #fff; color: #333;
        font-size: 0.85em;
        cursor: pointer;
        transition: all 0.25s ease;
    }
    .queue-slot.special { border-color: #c99; background: #fff5f5; color: #a33; }
    .queue-slot.resolving {
        background: #fff8e1; border-color: #f0b400;
        transform: scale(1.15);
        box-shadow: 0 0 14px rgba(240,180,0,0.55);
        color: #a06800;
    }
    .queue-slot.special.resolving {
        background: #ffe0e0; border-color: #e05050;
        box-shadow: 0 0 14px rgba(224,80,80,0.55);
        color: #a02020;
    }

    #spire-hand {
        flex: 1; min-height: 120px;
        display: flex; flex-wrap: nowrap;
        justify-content: center;
        align-items: flex-end;
        gap: 0;
        padding: 8px;
    }
    .spire-card {
        position: relative;
        flex: 0 0 auto;
        width: 90px; height: 110px;
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
        display: flex; flex-direction: column;
        justify-content: center; align-items: center;
    }
    .spire-card:hover {
        border-color: #999;
        transform: translateY(-8px);
        z-index: 10;
        box-shadow: 0 6px 16px rgba(0,0,0,0.18);
    }
    .spire-card.disabled { opacity: 0.4; cursor: not-allowed; }
    .spire-card.disabled:hover { transform: none; border-color: #ddd; box-shadow: none; z-index: auto; }
    .spire-card .name { font-weight: 600; color: #222; line-height: 1.25; word-break: break-all; }
    .spire-card .desc { display: none; }

    .card-badge {
        position: absolute; top: -6px; left: -6px;
        min-width: 20px; height: 20px; padding: 0 4px;
        border-radius: 10px;
        font-size: 0.7em; font-weight: 600;
        color: #fff;
        display: flex; align-items: center; justify-content: center;
    }
    .card-badge.newborn { background: #6b8fbf; }
    .card-badge.mature { background: #d4a017; }
    .card-badge.tag { background: #3a8f6b; }

    #card-tooltip {
        position: fixed;
        background: #333; color: #fff;
        padding: 10px 14px; border-radius: 8px;
        font-size: 0.85em; max-width: 220px; line-height: 1.5;
        pointer-events: none; opacity: 0;
        transition: opacity 0.15s;
        z-index: 10000;
        box-shadow: 0 4px 16px rgba(0,0,0,0.2);
    }
    #card-tooltip.active { opacity: 1; }
    #card-tooltip .tip-name { font-weight: 600; margin-bottom: 4px; }
    #card-tooltip .tip-desc { color: #ddd; }

    #choice-modal, #pile-modal, #search-modal, #discard-modal {
        display: none;
        position: fixed; inset: 0;
        background: rgba(0,0,0,0.35);
        z-index: 200;
        align-items: center; justify-content: center;
    }
    #choice-modal.active, #pile-modal.active, #search-modal.active, #discard-modal.active { display: flex; }

    .choice-box, .pile-box-modal, .search-box-modal {
        background: #fff; border-radius: 12px;
        padding: 20px 24px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.2);
        max-width: 90vw; max-height: 80vh;
        overflow-y: auto;
    }
    .choice-box { text-align: center; }
    .choice-box h3 { margin: 0 0 16px; font-size: 1em; color: #333; }
    .choice-box button {
        display: block; width: 100%;
        padding: 10px 24px; margin: 6px 0;
        border-radius: 8px;
        border: 1px solid #333; background: #333; color: #fff;
        cursor: pointer; font-family: inherit; font-size: 0.95em;
    }
    .choice-box button.defend { background: #1976d2; border-color: #1976d2; }
    .choice-box button.skip { background: #fff; color: #666; border-color: #ddd; }

    .pile-box-modal h3, .search-box-modal h3 {
        margin: 0 0 12px; font-size: 0.95em; color: #666;
    }
    .pile-grid, .search-grid {
        display: flex; flex-wrap: wrap; gap: 6px;
        margin-bottom: 16px;
    }
    .pile-item, .search-item {
        padding: 4px 10px;
        border: 1px solid #ddd; border-radius: 6px;
        background: #fafafa;
        font-size: 0.85em; color: #555;
    }
    .pile-item.special { border-color: #c99; background: #fff5f5; color: #a33; }
    .search-item { cursor: pointer; user-select: none; }
    .search-item:hover { background: #f0f0f0; border-color: #999; }
    .search-item.selected { background: #333; color: #fff; border-color: #333; }

    #log-panel {
        display: none;
        position: fixed; top: 50px; right: 20px;
        width: 320px; max-height: 60vh;
        background: #fff;
        border: 1px solid #ddd; border-radius: 8px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.15);
        z-index: 300;
        overflow: hidden;
        flex-direction: column;
    }
    #log-panel.active { display: flex; }
    #log-panel .log-header {
        padding: 8px 12px;
        border-bottom: 1px solid #eee;
        font-size: 0.85em; color: #666;
        display: flex; justify-content: space-between; align-items: center;
    }
    #log-panel .log-close {
        cursor: pointer; color: #999; border: none; background: none;
        font-family: inherit; font-size: 1em;
    }
    #spire-log {
        padding: 10px 12px;
        overflow-y: auto;
        font-size: 0.8em; color: #666; line-height: 1.6;
        max-height: 50vh;
    }

        /* ============ 主菜单 ============ */
    #main-menu {
        display: flex;
        position: fixed; inset: 0;
        background: #fafafa;
        z-index: 95;
        align-items: center;
        justify-content: center;
    }
    #main-menu.hidden { display: none; }
    .menu-panel {
        text-align: center;
        padding: 40px;
    }
    .menu-panel h1 {
        margin: 0 0 40px;
        font-size: 2em;
        color: #333;
        letter-spacing: 0.1em;
        font-weight: 500;
    }
    .menu-main-btn {
        display: block;
        width: 280px;
        padding: 16px 24px;
        margin: 12px auto;
        border-radius: 10px;
        border: 1px solid #333;
        background: #333;
        color: #fff;
        cursor: pointer;
        font-family: inherit;
        font-size: 1em;
        letter-spacing: 0.05em;
        transition: opacity 0.15s;
        position: relative;
    }
    .menu-main-btn:hover:not(:disabled) { opacity: 0.85; }
    .menu-main-btn:disabled {
        background: #ddd;
        border-color: #ddd;
        color: #999;
        cursor: not-allowed;
    }
    .menu-main-btn .menu-sub {
        display: block;
        font-size: 0.7em;
        font-weight: 400;
        opacity: 0.7;
        margin-top: 4px;
        letter-spacing: 0;
    }
    .back-btn {
        margin-top: 12px;
        padding: 8px 20px;
        border-radius: 6px;
        border: 1px solid #ddd;
        background: none;
        color: #999;
        cursor: pointer;
        font-family: inherit;
        font-size: 0.85em;
        width: 100%;
    }
    .back-btn:hover { background: #f5f5f5; }

    /* ============ 词条释义 ============ */
    #glossary-modal {
        display: none;
        position: fixed; inset: 0;
        background: rgba(0,0,0,0.35);
        z-index: 400;
        align-items: center;
        justify-content: center;
    }
    #glossary-modal.active { display: flex; }
    .glossary-box {
        background: #fff;
        border-radius: 12px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.2);
        width: 90%;
        max-width: 560px;
        max-height: 80vh;
        display: flex;
        flex-direction: column;
    }
    .glossary-header {
        padding: 16px 20px;
        border-bottom: 1px solid #eee;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .glossary-header h3 {
        margin: 0;
        font-size: 1em;
        color: #333;
    }
        .glossary-search {
        padding: 12px 20px;
        border-bottom: 1px solid #eee;
    }
    .glossary-search input {
        width: 100%;
        padding: 8px 12px;
        border: 1px solid #ddd;
        border-radius: 6px;
        font-family: inherit;
        font-size: 0.9em;
        color: #333;
        outline: none;
    }
    .glossary-search input:focus {
        border-color: #999;
    }
    .glossary-empty {
        padding: 20px;
        text-align: center;
        color: #bbb;
        font-size: 0.85em;
    }
    .glossary-body {
        padding: 16px 20px;
        overflow-y: auto;
        font-size: 0.9em;
        color: #555;
        line-height: 1.7;
    }
    .glossary-body .glossary-entry {
        padding: 10px 0;
        border-bottom: 1px solid #f0f0f0;
    }
    .glossary-body .glossary-entry:last-child { border-bottom: none; }
    .glossary-body .glossary-term {
        font-weight: 600;
        color: #222;
        margin-bottom: 4px;
    }
    .glossary-body .glossary-def { color: #666; }

    #spire-select {
        display: none;
        position: fixed; inset: 0;
        background: #fafafa;
        z-index: 100;
        padding: 30px 20px;
        align-items: center; justify-content: center;
    }
    #spire-select.active { display: flex; }
    .spire-select-panel {
        display: flex;
        width: 100%; max-width: 1100px;
        height: 80vh; max-height: 600px;
        gap: 12px;
    }
    .spire-col {
        background: #fff;
        border: 1px solid #e0e0e0; border-radius: 10px;
        padding: 16px;
        display: flex; flex-direction: column;
        min-height: 0;
    }
    .spire-col-info { flex: 1.4; }
    .spire-col-wheel { flex: 1; padding: 8px; }
    .spire-col-action { flex: 0.8; align-items: center; justify-content: center; padding: 12px; }
    .spire-col-title {
        margin: 0 0 12px;
        font-size: 0.85em; color: #999;
        letter-spacing: 0.1em; font-weight: 500;
    }
    .spire-name { font-size: 1.3em; font-weight: 600; color: #222; margin-bottom: 12px; }
    .spire-desc { font-size: 0.9em; color: #555; line-height: 1.6; flex: 1; }
    .spire-stat {
        font-size: 0.85em; color: #999;
        margin-top: 12px; padding-top: 12px;
        border-top: 1px solid #eee;
    }
    .spire-wheel { flex: 1; overflow-y: auto; min-height: 0; scrollbar-width: thin; }
    .spire-wheel-item {
        padding: 10px 14px; margin: 4px 0;
        border-radius: 6px;
        cursor: pointer;
        color: #333; user-select: none;
        font-size: 0.95em;
    }
    .spire-wheel-item:hover { background: #f0f0f0; }
    .spire-wheel-item.selected { background: #333; color: #fff; font-weight: 600; }
    #start-battle-btn {
        padding: 14px 20px;
        border-radius: 8px;
        border: 1px solid #333; background: #333; color: #fff;
        cursor: pointer; font-family: inherit; font-size: 1em;
        width: 100%;
    }
    #start-battle-btn:disabled { opacity: 0.3; cursor: not-allowed; }
    @media (max-width: 820px) {
        .spire-select-panel { flex-direction: column; height: auto; max-height: 90vh; overflow-y: auto; }
        .spire-col { flex: none; }
        .spire-col-wheel { height: 180px; }
    }
</style>

<div id="spire-page">

<div id="main-menu">
    <div class="menu-panel">
        <h1>迷你游戏</h1>
        <button class="menu-main-btn" id="menu-fight">格斗模式</button>
        <button class="menu-main-btn" id="menu-roguelike" disabled>肉鸽模式<span class="menu-sub">未完成</span></button>
        <button class="menu-main-btn" id="menu-glossary">词条释义</button>
    </div>
</div>

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
            <button id="back-to-menu-btn" class="back-btn">返回主页</button>
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

<div id="top-bar">
    <span class="turn">Turn <span id="turn-num">1</span></span>
    <button class="menu-btn" id="log-btn">日志</button>
    <button class="menu-btn" id="restart-btn">重开</button>
</div>

<div id="arena">
    <div class="side-col player">
        <div class="hp-row">
            <div class="hp-bar">
                <div class="fill" id="player-hp-fill"></div>
                <div class="text"><span id="player-hp">80</span> / <span id="player-maxhp">80</span></div>
            </div>
        </div>
        <div class="fx-row" id="player-fx" title="点击查看所有效果"></div>
        <div class="portrait">
            <span id="player-portrait-name">我方</span>
        </div>
    </div>
    <div id="mid-strip" class="mid-strip" title="点击展开日志">
        <div class="mid-strip-label">日<br>志</div>
        <div class="mid-strip-content">
            <div class="mid-strip-header">
                <span>日志</span>
                <button class="mid-strip-close" id="mid-strip-close">✕</button>
            </div>
            <div class="mid-strip-log" id="mid-strip-log"></div>
        </div>
    </div>
    <div class="side-col enemy">
        <div class="hp-row">
            <div class="hp-bar">
                <div class="fill" id="enemy-hp-fill"></div>
                <div class="text"><span id="enemy-hp">50</span> / <span id="enemy-maxhp">50</span></div>
            </div>
        </div>
        <div class="fx-row" id="enemy-fx" title="点击查看所有效果"></div>
        <div class="enemy-mid">
            <div class="enemy-portrait">
                <span id="enemy-portrait-name">敌方</span>
            </div>
            <div class="enemy-side">
                <div class="trait-list" id="enemy-traits"></div>
                <div class="intent-box" id="enemy-intent">
                    <span class="intent-label">行动意图</span>
                </div>
            </div>
        </div>
    </div>
</div>

<div id="bottom">
    <div class="bottom-side">
        <div class="label-box queue-label">行动序列</div>
        <div class="label-box draw-label" id="draw-pile-btn">
            抽牌堆<br>
            <span class="count" id="draw-count">0</span>
        </div>
    </div>
    <div class="bottom-main">
        <button id="resolve-btn">结算</button>
        <div id="stage-queue"></div>
        <div id="spire-hand"></div>
    </div>
</div>

</div>

<div id="card-tooltip"></div>

<div id="choice-modal">
    <div class="choice-box">
        <h3 id="choice-title">抉择</h3>
        <div id="choice-options"></div>
    </div>
</div>

<div id="log-panel">
    <div class="log-header">
        <span>日志</span>
        <button class="log-close" id="log-close">✕</button>
    </div>
    <div id="spire-log"></div>
</div>

<div id="pile-modal">
    <div class="pile-box-modal">
        <h3>抽牌堆</h3>
        <div class="pile-grid" id="pile-modal-draw"></div>
        <h3>弃牌堆</h3>
        <div class="pile-grid" id="pile-modal-discard"></div>
    </div>
</div>

<div id="glossary-modal">
    <div class="glossary-box">
        <div class="glossary-header">
            <h3>词条释义</h3>
            <button class="log-close" id="glossary-close">✕</button>
        </div>
        <div class="glossary-search">
            <input type="text" id="glossary-search-input" placeholder="搜索词条（支持拼音 / 首字母）" autocomplete="off">
        </div>
        <div class="glossary-body" id="glossary-body"></div>
    </div>
</div>

<div id="search-modal">
    <div class="search-box-modal">
        <h3>从抽牌堆中选择</h3>
        <div class="search-grid" id="search-grid"></div>
        <div style="text-align:right;">
            <button id="search-confirm" style="padding:6px 16px;border-radius:6px;border:1px solid #333;background:#333;color:#fff;cursor:pointer;font-family:inherit;font-size:0.85em;">确认</button>
        </div>
    </div>
</div>

<div id="discard-modal">
    <div class="search-box-modal">
        <h3>选择 <span id="discard-required">2</span> 张牌弃置</h3>
        <div class="search-grid" id="discard-grid"></div>
        <div style="text-align:right;">
            <button id="discard-confirm" style="padding:6px 16px;border-radius:6px;border:1px solid #333;background:#333;color:#fff;cursor:pointer;font-family:inherit;font-size:0.85em;">确认</button>
        </div>
    </div>
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
function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

function shuffle(arr) {
    for (let i = arr.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
}

function log(msg) { state.log.push(msg); }

const isTouchOnly = window.matchMedia('(hover: none)').matches;

function isSpecialCard(card) {
    return card?.tags?.includes('special') || card?.isChoice;
}

/* 取卡牌的第一个“行为标签”（跳过 special） */
function firstBehaviorTag(card) {
    if (!card?.tags) return null;
    return card.tags.find(t => t !== 'special') || null;
}

/* debuff 名称 */
const DEBUFF_NAMES = {
    frost: '霜冻',
    stat_down: '属性降低'
};

/* ============================================
   卡牌 tooltip
   ============================================ */
function showCardTooltip(card, el) {
    const tip = document.getElementById('card-tooltip');
    let extra = '';
    if (card.states?.newborn) extra += '<br><span style="color:#9fc0e8;">[新生] 数值 -50%</span>';
    if (card.states?.mature) extra += '<br><span style="color:#e8c060;">[成熟] 数值 +100%</span>';
    if (card.states?.frostExtend) extra += '<br><span style="color:#7fb8d8;">[侵袭] 施加霜冻改为延长霜冻</span>';
    tip.innerHTML = `<div class="tip-name">${card.name}</div><div class="tip-desc">${card.description}${extra}</div>`;
    tip.classList.add('active');
    const rect = el.getBoundingClientRect();
    const tipRect = tip.getBoundingClientRect();
    let left = rect.left + rect.width / 2 - tipRect.width / 2;
    let top = rect.top - tipRect.height - 8;
    if (left < 8) left = 8;
    if (left + tipRect.width > window.innerWidth - 8) left = window.innerWidth - tipRect.width - 8;
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
        : { id, name: '?', description: '', effects: [], tags: [] };
    card.effects = (card.effects || []).map(e => Object.assign({}, e));
    card.tags = [...(card.tags || [])];
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
        tags: ['special', 'attack'], states: {},
        effects: [{ type: 'specialDamage' }],
        uid: nextCardUid++
    }),
    fill: () => ({
        id: 'fill', name: '虚构',
        description: '造成 1 点伤害，获得 1 点格挡。',
        tags: ['special', 'attack', 'buff'], states: {},
        effects: [
            { type: 'damage', value: 1 },
            { type: 'block', value: 1 }
        ],
        uid: nextCardUid++
    }),
    choice: () => ({
        id: 'choice', name: '祈愿',
        description: '抉择「造成 6 点伤害/获得 5 点格挡」。',
        tags: ['special'], isChoice: true, states: {},
        effects: [],
        uid: nextCardUid++
    }),
    chant_attack: () => ({
        id: 'chant_attack', name: '吟诵攻击',
        description: '造成 6 点伤害。',
        tags: ['special', 'attack'], states: {},
        effects: [{ type: 'damage', value: 6 }],
        uid: nextCardUid++
    })
};

function generateCard(key) {
    const gen = CARD_GENERATORS[key];
    return gen ? gen() : null;
}

/* ============================================
   玩家持续状态
   ============================================ */
function getAttackBonus() {
    if (!state?.player?.effects) return 0;
    return state.player.effects
        .filter(e => e.type === 'attackBonus')
        .reduce((s, e) => s + e.value, 0);
}

function addTimedEffect(type, value, turns) {
    state.player.effects.push({ type, value, turnsLeft: turns });
}

function tickPlayerEffects() {
    const before = state.player.effects.length;
    state.player.effects = state.player.effects.filter(e => {
        e.turnsLeft -= 1;
        return e.turnsLeft > 0;
    });
    const removed = before - state.player.effects.length;
    if (removed > 0) log(`[持续状态] ${removed} 条增益到期。`);
}

/* ============================================
   敌人 debuff
   ============================================ */
function getFrostTurns() {
    const f = state.enemy.debuffs.find(d => d.type === 'frost');
    return f ? f.turnsLeft : 0;
}

function applyFrost(amount) {
    const frost = state.enemy.debuffs.find(d => d.type === 'frost');
    if (!frost) {
        state.enemy.debuffs.push({ type: 'frost', turnsLeft: amount });
        log(`施加 ${amount} 回合霜冻。`);
    } else if (amount > frost.turnsLeft) {
        frost.turnsLeft = amount;
        log(`霜冻刷新为 ${amount} 回合（原 ${frost.turnsLeft} 回合）。`);
    } else {
        log(`霜冻已有 ${frost.turnsLeft} 回合，本次施加不生效。`);
    }
}

function extendFrost(amount) {
    const frost = state.enemy.debuffs.find(d => d.type === 'frost');
    if (!frost) {
        log('目标没有霜冻，无法延长。');
        return;
    }
    frost.turnsLeft += amount;
    log(`霜冻延长 ${amount} 回合（现在 ${frost.turnsLeft} 回合）。`);
}

function tickEnemyDebuffs() {
    for (const d of state.enemy.debuffs) d.turnsLeft -= 1;
    const before = state.enemy.debuffs.length;
    state.enemy.debuffs = state.enemy.debuffs.filter(d => {
        if (d.turnsLeft <= 0) {
            log(`敌人的「${DEBUFF_NAMES[d.type] || d.type}」已到期。`);
            return false;
        }
        return true;
    });
}

function getEnemyStatDown() {
    let atkDown = 0, blockDown = 0;
    for (const d of state.enemy.debuffs) {
        if (d.type === 'stat_down') {
            atkDown += d.value;
            blockDown += d.value;
        }
    }
    return { atkDown, blockDown };
}

/* ============================================
   通用追加卡牌被动
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
   追刃（L）
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
   牌赋予的延迟效果
   ============================================ */
function runDelayedCardEffects() {
    if (state.pendingChant) {
        const card = generateCard('chant_attack');
        if (card) {
            state.queue.push(card);
            log('「吟诵攻击」被插入队列末尾。');
        }
        state.pendingChant = null;
    }
}

/* ============================================
   位次快照
   ============================================ */
function snapshotQueuePositions() {
    state.queue.forEach((card, i) => { card.queuePosition = i + 1; });
}

/* ============================================
   熟成
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
   追击默认配置
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
    // Snowy：造成真实伤害时施加霜冻
    if (charPassive?.type === 'applyFrostOnHpDamage') {
        applyFrost(charPassive.value || 1);
    }
}

/* ============================================
   效果处理器
   ============================================ */
const EFFECT_HANDLERS = {
    damage(state, effect) {
        const mult = getCardStateMultiplier(state.resolvingCard);
        const tempBonus = getAttackBonus();
        const baseDmg = Math.floor((effect.value || 0) * mult) + tempBonus;
        const baseTimes = effect.times || 1;
        const repeatPassive = state.character?.passive?.type === 'extraDamageRepeat'
            ? state.character.passive : null;
        const isCombo = state.resolvingCard?.tags?.includes('combo');
        const bonus = (repeatPassive && isCombo) ? (repeatPassive.value || 0) : 0;
        const times = baseTimes + bonus;

        let totalReal = 0, totalAbsorbed = 0;
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
        if (times > 1) log(`造成 ${baseDmg} × ${times} 段（真实 ${totalReal}，吸收 ${totalAbsorbed}）。`);
        else log(`造成 ${totalReal} 点伤害（格挡吸收 ${totalAbsorbed}）。`);
        onPlayerDealtHpDamage(state, totalReal);
    },

    /* 刺骨：部分伤害穿透 */
    damageWithPierce(state, effect) {
        const mult = getCardStateMultiplier(state.resolvingCard);
        const tempBonus = getAttackBonus();
        const total = Math.floor((effect.value || 0) * mult) + tempBonus;
        const pierce = Math.min(effect.pierce || 0, total);
        const blockable = total - pierce;

        const absorbed = Math.min(state.enemy.block, blockable);
        state.enemy.block -= absorbed;
        let real = pierce + (blockable - absorbed);
        real = Math.min(real, getDamageCapRemaining());
        state.enemy.hp = Math.max(0, state.enemy.hp - real);
        state.enemy.damageTakenThisTurn += real;
        state.currentCardRealDamage += real;

        log(`造成 ${total} 点伤害（其中 ${pierce} 点穿盾，吸收 ${absorbed}，真实 ${real}）。`);
        onPlayerDealtHpDamage(state, real);
    },

    lostHpDamage(state, effect) {
        const mult = getCardStateMultiplier(state.resolvingCard);
        const tempBonus = getAttackBonus();
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

        let totalReal = 0, totalAbsorbed = 0;
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
        const tempBonus = getAttackBonus();
        const dmg = effectiveAttacks * cfg.perAttack + cfg.flatBonus + tempBonus;
        const absorbed = Math.min(state.enemy.block, dmg);
        state.enemy.block -= absorbed;
        let real = dmg - absorbed;
        let guaranteed = 0;
        if (real < cfg.minDamage) { guaranteed = cfg.minDamage - real; real += guaranteed; }
        real = Math.min(real, getDamageCapRemaining());
        state.enemy.hp = Math.max(0, state.enemy.hp - real);
        state.enemy.damageTakenThisTurn += real;
        state.currentCardRealDamage += real;
        let formula = `${state.attacksThisTurn} 次攻击`;
        if (cfg.bonusAttacks) formula += ` + 额外 ${cfg.bonusAttacks}`;
        formula += ` × ${cfg.perAttack}`;
        if (cfg.flatBonus) formula += ` + ${cfg.flatBonus}`;
        if (guaranteed > 0) log(`追击造成 ${dmg - absorbed} 点伤害（${formula}，吸收 ${absorbed}），保底追加 ${guaranteed} 点真实伤害。`);
        else log(`追击造成 ${real} 点伤害（${formula}，吸收 ${absorbed}）。`);
        onPlayerDealtHpDamage(state, real);
        for (const extra of cfg.extraEffects) {
            const handler = EFFECT_HANDLERS[extra.type];
            if (handler) handler(state, extra);
            else log(`追击的未知附加效果：${extra.type}`);
        }
    },

    /* 冬夜漫长：伤害 + 每层霜冻加成 */
    damagePerFrost(state, effect) {
        const mult = getCardStateMultiplier(state.resolvingCard);
        const tempBonus = getAttackBonus();
        const frost = getFrostTurns();
        const base = Math.floor((effect.base || 0) * mult) + tempBonus + frost * (effect.perFrost || 0);

        const absorbed = Math.min(state.enemy.block, base);
        state.enemy.block -= absorbed;
        let real = base - absorbed;
        real = Math.min(real, getDamageCapRemaining());
        state.enemy.hp = Math.max(0, state.enemy.hp - real);
        state.enemy.damageTakenThisTurn += real;
        state.currentCardRealDamage += real;

        log(`冬夜漫长：造成 ${base} 点伤害（${frost} 回合霜冻 × ${effect.perFrost}，吸收 ${absorbed}，真实 ${real}）。`);
        onPlayerDealtHpDamage(state, real);
    },

    /* 冰川破裂：连击数 = 霜冻回合数，伤害后移除霜冻 */
    damageComboPerFrost(state, effect) {
        const mult = getCardStateMultiplier(state.resolvingCard);
        const tempBonus = getAttackBonus();
        const frost = getFrostTurns();
        const perHit = Math.floor((effect.baseValue || 0) * mult) + tempBonus;
        const times = frost * (effect.perFrost || 1) + (effect.baseTimes || 0);

        if (times <= 0) {
            log('冰川破裂：没有霜冻，未造成伤害。');
            return;
        }

        let totalReal = 0, totalAbsorbed = 0;
        for (let r = 0; r < times; r++) {
            if (state.enemy.hp <= 0) break;
            const absorbed = Math.min(state.enemy.block, perHit);
            state.enemy.block -= absorbed;
            let real = perHit - absorbed;
            real = Math.min(real, getDamageCapRemaining());
            state.enemy.hp = Math.max(0, state.enemy.hp - real);
            state.enemy.damageTakenThisTurn += real;
            totalReal += real;
            totalAbsorbed += absorbed;
        }
        state.currentCardRealDamage += totalReal;
        log(`冰川破裂：造成 ${perHit} × ${times} 段（真实 ${totalReal}，吸收 ${totalAbsorbed}）。`);
        onPlayerDealtHpDamage(state, totalReal);
    },

    block(state, effect) {
        const mult = getCardStateMultiplier(state.resolvingCard);
        const v = Math.floor((effect.value || 0) * mult);
        state.player.block = Math.min(state.player.maxHp, state.player.block + v);
        log(`获得 ${v} 点格挡。`);
    },

    snowball(state, effect) {
        let count = 0;
        for (const c of state.queue) {
            c.effects = c.effects.map(e => {
                const copy = Object.assign({}, e);
                if (copy.type === 'damage' && typeof copy.value === 'number') copy.value += 1;
                if (copy.type === 'lostHpDamage' && typeof copy.flat === 'number') copy.flat += 1;
                if (copy.type === 'block' && typeof copy.value === 'number') copy.value += 1;
                return copy;
            });
            count++;
        }
        log(`渐强：给队列中剩余 ${count} 张牌数值 +1。`);
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
    },

    insertCopyAtEnd(state, effect) {
        const card = state.resolvingCard;
        if (card.queuePosition !== effect.requirePosition) {
            log(`「${card.name}」不在第 ${effect.requirePosition} 位（实际第 ${card.queuePosition} 位），未触发回响。`);
            return;
        }
        const copy = makeCard(card.id);
        copy.name = card.name + '·残响';
        if (!copy.tags.includes('special')) copy.tags.push('special');
        state.queue.push(copy);
        copy.queuePosition = state.queue.length;
        log(`「${card.name}」在队列末尾留下了残响。`);
    },

    chantClear(state, effect) {
        const removed = state.queue.slice();
        state.queue = [];
        let attackBonus = 0, blockGain = 0;
        for (const card of removed) {
            const tags = card.tags || [];
            if (tags.includes('attack')) attackBonus += 2;
            if (tags.includes('buff')) blockGain += 3;
        }
        if (attackBonus > 0) addTimedEffect('attackBonus', attackBonus, 2);
        if (blockGain > 0) state.player.block = Math.min(state.player.maxHp, state.player.block + blockGain);
        state.pendingChant = true;
        log(`吟诵移除了 ${removed.length} 张牌：攻击 +${attackBonus}（2 回合），格挡 +${blockGain}。`);
        if (removed.length > 0) log('下回合开始行动时，将插入「吟诵攻击」。');
    },

    discardHandAndDraw(state, effect) {
        const discarded = state.hand.length;
        for (const c of state.hand) {
            c.states = {};
            state.playedPile.push(c);
        }
        state.hand = [];
        drawToLimit(discarded);
        log(`弃置 ${discarded} 张手牌，抽 ${discarded} 张。`);
    },

    activateTrait(state, effect) {
        const card = state.resolvingCard;
        const traitId = card._activateTraitId;
        if (!traitId) return;
        const trait = state.enemy.traits.find(t => t.id === traitId);
        if (!trait || trait.active) return;
        trait.active = true;
        log(`[引燃] 激活了敌方词条「${trait.name}」。`);
    },

    /* ===== Snowy 专属效果 ===== */

    /* 冷风：造成伤害 + 施加霜冻（带侵袭标签则改为延长） */
    applyFrost(state, effect) {
        const card = state.resolvingCard;
        const amount = effect.value || 1;
        if (card?.states?.frostExtend && getFrostTurns() > 0) {
            extendFrost(amount);
        } else {
            applyFrost(amount);
        }
    },

    /* 寒潮：延长霜冻（不依赖侵袭标签） */
    extendFrost(state, effect) {
        extendFrost(effect.value || 1);
    },

    /* 侵袭：给队列中的攻击牌贴标签 */
    tagQueueAttacks(state, effect) {
        let count = 0;
        for (const c of state.queue) {
            if (c.tags?.includes('attack')) {
                c.states = c.states || {};
                c.states.frostExtend = true;
                count++;
            }
        }
        log(`侵袭：为队列中 ${count} 张攻击牌贴上标签。`);
    },

    /* 思维冷冻：施加属性降低 */
    applyStatDown(state, effect) {
        const frost = getFrostTurns();
        const value = (effect.value || 0) + frost * (effect.perFrost || 0);
        const turns = effect.turns || 2;
        const existing = state.enemy.debuffs.find(d => d.type === 'stat_down');
        if (existing) {
            if (value > existing.value) {
                existing.value = value;
                existing.turnsLeft = turns;
            } else if (value === existing.value) {
                existing.turnsLeft = Math.max(existing.turnsLeft, turns);
            }
        } else {
            state.enemy.debuffs.push({ type: 'stat_down', value, turnsLeft: turns });
        }
        log(`施加属性降低：攻击/格挡 -${value}，持续 ${turns} 回合。`);
    },

    /* 雪融之时：条件交换 / 检索 */
        async conditionalExchange(state, effect) {
        const frost = getFrostTurns();
        const n = effect.count || 2;

        if (frost > (effect.threshold || 3)) {
            // 弃 N 并检索 N
            const actual = Math.min(n, state.hand.length);
            if (actual > 0) {
                const selected = await showDiscardModal(actual);
                const sorted = [...selected].sort((a, b) => b - a);
                for (const idx of sorted) {
                    const c = state.hand.splice(idx, 1)[0];
                    c.states = {};
                    state.playedPile.push(c);
                }
            }
            log(`雪融之时：霜冻达 ${frost} 回合，弃置 ${actual} 张手牌。`);
            const picked = await showSearchModal(n);
            for (const c of picked) {
                state.hand.push(c);
            }
            log(`检索了 ${picked.length} 张牌。`);
        } else {
            // 交换 N：先手动弃 N 张，再抽 N 张
            const actual = Math.min(n, state.hand.length);
            if (actual > 0) {
                const selected = await showDiscardModal(actual);
                const sorted = [...selected].sort((a, b) => b - a);
                for (const idx of sorted) {
                    const c = state.hand.splice(idx, 1)[0];
                    c.states = {};
                    state.playedPile.push(c);
                }
            }
            drawToLimit(n);
            log(`交换 ${n}：弃 ${actual} 张，抽 ${n} 张。`);
        }
    },

    /* 冰川破裂：移除霜冻 */
    removeFrost(state, effect) {
        const before = state.enemy.debuffs.length;
        state.enemy.debuffs = state.enemy.debuffs.filter(d => d.type !== 'frost');
        if (state.enemy.debuffs.length < before) {
            log('霜冻被解除。');
        }
    }
};

/* ============================================
   检索引擎
   ============================================ */
let searchResolve = null;
let searchCount = 0;
let searchSelected = [];

function showSearchModal(count) {
    return new Promise(resolve => {
        searchCount = count;
        searchSelected = [];
        searchResolve = resolve;
        const grid = document.getElementById('search-grid');
        grid.innerHTML = '';
        state.drawPile.forEach((card, i) => {
            const el = document.createElement('div');
            el.className = 'search-item';
            el.textContent = card.name;
            el.dataset.idx = i;
            el.addEventListener('click', () => {
                const idx = searchSelected.indexOf(i);
                if (idx >= 0) {
                    searchSelected.splice(idx, 1);
                    el.classList.remove('selected');
                } else if (searchSelected.length < searchCount) {
                    searchSelected.push(i);
                    el.classList.add('selected');
                }
            });
            grid.appendChild(el);
        });
        document.getElementById('search-modal').classList.add('active');
    });
}

/* ============================================
   弃牌选择弹窗
   ============================================ */
let discardResolve = null;
let discardRequired = 0;
let discardSelected = [];

function showDiscardModal(count) {
    return new Promise(resolve => {
        discardRequired = count;
        discardSelected = [];
        discardResolve = resolve;
        document.getElementById('discard-required').textContent = count;
        const grid = document.getElementById('discard-grid');
        grid.innerHTML = '';
        state.hand.forEach((card, i) => {
            const el = document.createElement('div');
            el.className = 'search-item';
            el.textContent = card.name;
            el.dataset.idx = i;
            el.addEventListener('click', () => {
                const idx = discardSelected.indexOf(i);
                if (idx >= 0) {
                    discardSelected.splice(idx, 1);
                    el.classList.remove('selected');
                } else if (discardSelected.length < discardRequired) {
                    discardSelected.push(i);
                    el.classList.add('selected');
                }
                updateDiscardConfirm();
            });
            grid.appendChild(el);
        });
        updateDiscardConfirm();
        document.getElementById('discard-modal').classList.add('active');
    });
}

function updateDiscardConfirm() {
    const btn = document.getElementById('discard-confirm');
    btn.disabled = discardSelected.length !== Math.min(discardRequired, state.hand.length);
    btn.style.opacity = btn.disabled ? 0.4 : 1;
}

document.getElementById('discard-confirm').addEventListener('click', () => {
    if (!discardResolve) return;
    document.getElementById('discard-modal').classList.remove('active');
    const selected = [...discardSelected];
    const resolve = discardResolve;
    discardResolve = null;
    resolve(selected);
});

document.getElementById('search-confirm').addEventListener('click', () => {
    if (!searchResolve) return;
    document.getElementById('search-modal').classList.remove('active');
    const picked = [];
    // 按索引倒序 splice，避免索引错位
    const sorted = [...searchSelected].sort((a, b) => b - a);
    for (const idx of sorted) {
        picked.push(state.drawPile.splice(idx, 1)[0]);
    }
    picked.reverse();
    const resolve = searchResolve;
    searchResolve = null;
    resolve(picked);
});

/* ============================================
   敌人被动
   ============================================ */
const ENEMY_PASSIVE_HANDLERS = {
    fire_growth: {
        modifyAttackIntent(state, passive, intent) { intent.value += state.enemy.attackGrowthStacks * (passive.value || 0); },
        onEnemyTurnEnd(state) { state.enemy.attackGrowthStacks += 1; }
    },
    counter_strike: {
        modifyAttackIntent(state, passive, intent) {
            const bonus = Math.floor(state.enemy.lastPlayerDamageTaken * (passive.ratio || 0));
            intent.value += bonus;
        },
        onEnemyTurnEnd(state) { state.enemy.lastPlayerDamageTaken = state.enemy.damageTakenThisTurn; }
    },
    barrage: { modifyAttackIntent(state, passive, intent) { intent.times = (intent.times || 1) + 1; } },
    pierce_block: { getPierceAmount(state, passive, attackValue) { return Math.min(passive.value, attackValue); } },
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
    },
    flat_attack: { modifyAttackIntent(state, passive, intent) { intent.value += passive.value || 0; } },
    extra_action: { onEnemyTurnStart() {} },
    draw_penalty: {
        onEnemyTurnStart(state, passive) {
            state.enemy.nextDrawPenalty = (state.enemy.nextDrawPenalty || 0) + (passive.value || 1);
        }
    },
    hide_intent: {}
};

function getActiveEnemyPassives() {
    const list = [];
    if (state.enemy.passive) list.push(state.enemy.passive);
    for (const t of state.enemy.traits) {
        if (t.active && t.passive) list.push(t.passive);
    }
    return list;
}

function runEnemyPassive(hook, ...args) {
    if (!state?.enemy) return undefined;
    const passives = getActiveEnemyPassives();
    let lastResult;
    for (const passive of passives) {
        const handler = ENEMY_PASSIVE_HANDLERS[passive.type];
        if (handler && typeof handler[hook] === 'function') {
            const r = handler[hook](state, passive, ...args);
            if (r !== undefined) lastResult = r;
        }
    }
    return lastResult;
}

/* ============================================
   手牌布局
   ============================================ */
const HAND_GAP = 8;
const HAND_MIN_STEP = 26;
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
        if (state.drawPile.length === 0) {
            if (state.playedPile.length === 0) break;
            state.drawPile = shuffle(state.playedPile);
            state.playedPile = [];
        }
        state.hand.push(state.drawPile.pop());
        drawn++;
    }
}

/* ============================================
   主菜单
   ============================================ */
function showMainMenu() {
    state = null;
    document.getElementById('main-menu').classList.remove('hidden');
    document.getElementById('spire-select').classList.remove('active');
}

document.getElementById('menu-fight').addEventListener('click', () => {
    document.getElementById('main-menu').classList.add('hidden');
    showCharacterSelect();
});

document.getElementById('back-to-menu-btn').addEventListener('click', showMainMenu);

/* ============================================
   词条释义
   ============================================ */
/* ============================================
   词条释义
   ============================================ */
function matchesGlossary(entry, q) {
    if (!q) return true;
    const term = (entry.term || '').toLowerCase();
    const pinyin = (entry.pinyin || '').toLowerCase();
    const abbr = (entry.abbr || '').toLowerCase();
    return term.includes(q) || pinyin.includes(q) || abbr.includes(q);
}

function renderGlossary(query) {
    const body = document.getElementById('glossary-body');
    const q = (query || '').trim().toLowerCase();
    const filtered = GLOSSARY_DATA.filter(e => matchesGlossary(e, q));
    if (filtered.length === 0) {
        body.innerHTML = '<div class="glossary-empty">没有匹配的词条</div>';
        return;
    }
    body.innerHTML = filtered.map(e =>
        `<div class="glossary-entry">
            <div class="glossary-term">${e.term}</div>
            <div class="glossary-def">${e.def}</div>
        </div>`
    ).join('');
}

function showGlossary() {
    const input = document.getElementById('glossary-search-input');
    input.value = '';
    renderGlossary('');
    document.getElementById('glossary-modal').classList.add('active');
    setTimeout(() => input.focus(), 50);
}

document.getElementById('glossary-search-input').addEventListener('input', (e) => {
    renderGlossary(e.target.value);
});

document.getElementById('menu-glossary').addEventListener('click', showGlossary);
document.getElementById('glossary-close').addEventListener('click', () => {
    document.getElementById('glossary-modal').classList.remove('active');
});
document.getElementById('glossary-modal').addEventListener('click', (e) => {
    if (e.target.id === 'glossary-modal') e.target.classList.remove('active');
});

/* ============================================
   中间栏（日志）
   ============================================ */
document.getElementById('mid-strip').addEventListener('click', (e) => {
    const strip = document.getElementById('mid-strip');
    if (e.target.closest('.mid-strip-close')) return;   // 关闭按钮另处理
    if (e.target.closest('.mid-strip-log')) return;     // 点日志内容不收起
    strip.classList.toggle('open');
});

document.getElementById('mid-strip-close').addEventListener('click', (e) => {
    e.stopPropagation();
    document.getElementById('mid-strip').classList.remove('open');
});
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
    document.getElementById('start-battle-btn').disabled = !(selectedCharKey && selectedEnemyKey);
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
        character: characterDef, characterKey,
        enemyDef, enemyKey,
        player: {
            hp: characterDef.maxHp, maxHp: characterDef.maxHp, block: 0,
            queueLimitPenalty: 0, effects: []
        },
        enemy: {
            hp: enemyDef.maxHp, maxHp: enemyDef.maxHp, block: 0,
            baseQueueLimit: enemyDef.queueLimit,
            queueLimit: enemyDef.queueLimit,
            nextQueueLimitPenalty: 0, nextDrawPenalty: 0,
            intentPool: enemyDef.intentPool,
            passive: enemyDef.passive,
            attackGrowthStacks: 0, lastPlayerDamageTaken: 0, damageTakenThisTurn: 0,
            queue: [],
            debuffs: [],
            traits: (enemyDef.traits || []).map(t => Object.assign({}, t, { active: false }))
        },
        drawPile: [], hand: [], playedPile: [], queue: [],
        baseQueueLimit: BASE_QUEUE_LIMIT + (passive.queueLimitBonus || 0),
        queueLimit: BASE_QUEUE_LIMIT + (passive.queueLimitBonus || 0),
        handLimit: BASE_HAND_LIMIT + (passive.handLimitBonus || 0),
        turn: 1, phase: 'building',
        currentCardRealDamage: 0, attacksThisTurn: 0,
        passiveUsedThisTurn: false, snowballActive: false,
        specialAttackConfig: makeDefaultSpecialAttackConfig(characterDef),
        resolvingCard: null, resolvingCardUid: null,
        pendingChant: false, log: []
    };

    fillEnemyQueue(state.enemy.baseQueueLimit);

    const deck = characterDef.deck.map(id => makeCard(id));
    state.drawPile = shuffle(deck);

    let drawCount = BASE_DRAW_PER_TURN + (passive.drawBonus || 0) - (passive.drawPenalty || 0);
    drawToLimit(drawCount);

    if (passive.type === 'matureHand') {
        for (const card of state.hand) {
            card.states = card.states || {};
            card.states.newborn = true;
        }
    }

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
        showChoiceModal(index, [
            { label: '攻击 6', value: 'attack' },
            { label: '防御 5', value: 'defend', className: 'defend' }
        ], '祈愿');
        return;
    }
    if (card.id === 'ignite') {
        const available = state.enemy.traits.filter(t => !t.active);
        if (available.length === 0) {
            log('敌人没有可激活的词条，引燃不产生额外效果。');
            doPlayCard(index);
            return;
        }
        const options = available.map(t => ({ label: `激活「${t.name}」`, value: t.id }));
        options.push({ label: '跳过', value: 'skip', className: 'skip' });
        showChoiceModal(index, options, '激活敌方词条');
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
    const targetEl = document.querySelector(`#stage-queue .queue-slot[data-uid="${uid}"]`) ||
                     document.querySelector(`#spire-hand .spire-card[data-uid="${uid}"]`);
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
        margin: 0; pointer-events: none; z-index: 9999;
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
let choiceOptions = [];

function showChoiceModal(index, options, title) {
    choiceTargetIndex = index;
    choiceOptions = options;
    document.getElementById('choice-title').textContent = title || '抉择';
    const container = document.getElementById('choice-options');
    container.innerHTML = '';
    options.forEach((opt, i) => {
        const btn = document.createElement('button');
        btn.textContent = opt.label;
        if (opt.className) btn.className = opt.className;
        btn.addEventListener('click', () => handleChoice(i));
        container.appendChild(btn);
    });
    document.getElementById('choice-modal').classList.add('active');
}

function handleChoice(optIndex) {
    const opt = choiceOptions[optIndex];
    document.getElementById('choice-modal').classList.remove('active');
    if (choiceTargetIndex < 0 || !opt) return;
    const card = state.hand[choiceTargetIndex];
    if (!card) { choiceTargetIndex = -1; return; }

    if (card.isChoice) {
        card._wasChoice = true;
        if (opt.value === 'attack') {
            card.name = '攻击';
            card.description = '造成 6 点伤害。';
            card.effects = [{ type: 'damage', value: 6 }];
            if (!card.tags.includes('attack')) card.tags.push('attack');
        } else {
            card.name = '防御';
            card.description = '获得 5 点格挡。';
            card.effects = [{ type: 'block', value: 5 }];
            if (!card.tags.includes('buff')) card.tags.push('buff');
        }
        card.isChoice = false;
    } else if (card.id === 'ignite') {
        if (opt.value !== 'skip') {
            card._activateTraitId = opt.value;
            card.effects.push({ type: 'damage', value: 4 });
            card.effects.push({ type: 'activateTrait' });
        }
    }

    const idx = choiceTargetIndex;
    choiceTargetIndex = -1;
    choiceOptions = [];
    doPlayCard(idx);
}

/* ============================================
   撤回
   ============================================ */
function undoLastCard() {
    if (state.phase !== 'building') return;
    if (state.queue.length === 0) return;
    const card = state.queue.pop();
    if (card._wasChoice) {
        card.name = '祈愿';
        card.description = '打出时选择：攻击 6，或防御 5。';
        card.effects = [];
        card.isChoice = true;
        card.tags = card.tags.filter(t => t !== 'attack' && t !== 'buff');
        delete card._wasChoice;
    }
    if (card._activateTraitId) {
        card.effects = card.effects.filter(e => e.type !== 'activateTrait');
        const lastDmg = card.effects.map(e => e.type).lastIndexOf('damage');
        if (lastDmg >= 0) card.effects.splice(lastDmg, 1);
        delete card._activateTraitId;
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
   队列结算
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
        const isAttackCard = card.tags?.includes('attack');

        for (const effect of card.effects) {
            const handler = EFFECT_HANDLERS[effect.type];
            if (handler) await handler(state, effect);
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
        if (!isSpecialCard(card)) {
            card.states = {};
            const baseTags = CARD_LIBRARY[card.id]?.tags;
            if (baseTags) card.tags = [...baseTags];
            state.playedPile.push(card);
        }
        state.resolvingCard = null;
        state.resolvingCardUid = null;
        render();
        await sleep(220);

        if (state.player.hp <= 0) { state.phase = 'gameover'; log('你倒下了。'); return; }
        if (state.enemy.hp <= 0) { state.phase = 'gameover'; log('敌人倒下了。'); return; }
    }
    state.resolvingCard = null;
    state.resolvingCardUid = null;
}

/* ============================================
   冒险
   ============================================ */
function runAdventure() {
    const passive = state.character?.passive;
    if (passive?.type !== 'adventure') return;
    let attackCount = 0, buffCount = 0;
    for (const card of state.hand) {
        if (card.tags?.includes('attack')) attackCount++;
        else if (card.tags?.includes('buff')) buffCount++;
    }
    const total = state.hand.length;
    for (const c of state.hand) {
        c.states = {};
        state.playedPile.push(c);
    }
    state.hand = [];
    const atkBonus = attackCount * (passive.attackBonusPerCard || 0);
    const blkBonus = buffCount * (passive.blockPerCard || 0);
    if (atkBonus > 0) addTimedEffect('attackBonus', atkBonus, 1);
    if (blkBonus > 0) state.player.block = Math.min(state.player.maxHp, state.player.block + blkBonus);
    log(`[冒险] 弃置了 ${total} 张手牌：攻击 +${atkBonus}（1 回合），格挡 +${blkBonus}。`);
}

/* ============================================
   敌人回合
   ============================================ */
async function enemyActAllAsync() {
    state.enemy.block = 0;
    runEnemyPassive('onEnemyTurnStart');
    render();
    await sleep(300);

    const { atkDown, blockDown } = getEnemyStatDown();
    const actions = state.enemy.queue.slice();

    for (const intent of actions) {
        if (state.player.hp <= 0) return;
        if (intent.type === 'attack') {
            const baseValue = Math.max(0, intent.value - atkDown);
            const times = intent.times || 1;
            for (let t = 0; t < times; t++) {
                if (state.player.hp <= 0) break;
                const pierce = runEnemyPassive('getPierceAmount', baseValue) ?? 0;
                const blockable = baseValue - pierce;
                const absorbed = Math.min(state.player.block, blockable);
                state.player.block -= absorbed;
                const real = pierce + (blockable - absorbed);
                state.player.hp = Math.max(0, state.player.hp - real);
                if (pierce > 0 && absorbed > 0) log(`敌人攻击，造成 ${real} 点伤害（${pierce} 点穿盾 + 格挡吸收 ${absorbed}）。`);
                else if (pierce > 0) log(`敌人攻击，造成 ${real} 点伤害（其中 ${pierce} 点穿盾）。`);
                else log(`敌人攻击，造成 ${real} 点伤害（格挡吸收 ${absorbed}）。`);
                if (real > 0) runEnemyPassive('onPlayerTakeRealDamage', real);
                render();
                await sleep(500);
            }
        } else if (intent.type === 'buff') {
            const baseValue = Math.max(0, intent.value - blockDown);
            state.enemy.block = Math.min(state.enemy.maxHp, state.enemy.block + baseValue);
            log(`敌人获得 ${baseValue} 点格挡。`);
            render();
            await sleep(500);
        }
    }

    if (state.enemy.hp <= 0) return;
    runEnemyPassive('onEnemyTurnEnd');

    const penalty = state.enemy.nextQueueLimitPenalty;
    state.enemy.nextQueueLimitPenalty = 0;
    let limit = Math.max(0, state.enemy.baseQueueLimit - penalty);
    // 霜冻：行动上限 -1
    if (state.enemy.debuffs.some(d => d.type === 'frost')) {
        limit = Math.max(0, limit - 1);
    }
    state.enemy.queueLimit = limit;
    fillEnemyQueue(state.enemy.queueLimit);
    if (penalty > 0) log(`敌人的行动序列最大长度降为 ${state.enemy.queueLimit}。`);
}

/* ============================================
   新回合
   ============================================ */
function startNewTurn() {
    state.turn++;
    const passive = state.character?.passive;
    if (passive?.type !== 'blockPersist') state.player.block = 0;

    tickPlayerEffects();
    tickEnemyDebuffs();

    state.queueLimit = Math.max(0, state.baseQueueLimit - (state.player.queueLimitPenalty || 0));
    state.player.queueLimitPenalty = 0;
    state.attacksThisTurn = 0;
    state.passiveUsedThisTurn = false;
    state.enemy.damageTakenThisTurn = 0;
    state.snowballActive = false;
    state.specialAttackConfig = makeDefaultSpecialAttackConfig(state.character);

    if (passive?.type === 'matureHand') {
        for (const card of state.hand) {
            if (card.states?.newborn) {
                delete card.states.newborn;
                card.states.mature = true;
            }
        }
    }

    let drawCount = BASE_DRAW_PER_TURN + (passive?.drawBonus || 0) - (passive?.drawPenalty || 0);
    const enemyDrawPenalty = state.enemy.nextDrawPenalty || 0;
    drawCount = Math.max(0, drawCount - enemyDrawPenalty);
    if (enemyDrawPenalty > 0) {
        log(`[${state.enemyDef.name}] 你本回合抽牌 -${enemyDrawPenalty}。`);
        state.enemy.nextDrawPenalty = 0;
    }
    drawToLimit(drawCount);

    if (passive?.type === 'matureHand') {
        for (const card of state.hand) {
            card.states = card.states || {};
            if (!card.states.mature && !card.states.newborn) card.states.newborn = true;
        }
    }

    runInsertCardPassive('turnStart');
}

/* ============================================
   主流程
   ============================================ */
async function resolveAndEndTurn() {
    if (state.phase !== 'building') return;
    while (state.hand.length > state.handLimit) {
        const specialIdx = state.hand.findIndex(c => isSpecialCard(c));
        if (specialIdx >= 0) state.hand.splice(specialIdx, 1);
        else state.hand.pop();
    }

    state.phase = 'resolving';
    render();
    hideCardTooltip();
    await sleep(250);

    if (state.character?.passive?.type === 'adventure') {
        runAdventure();
        render();
        await sleep(350);
    }

    runDelayedCardEffects();
    runInsertCardPassive('beforeResolve');
    runAppendSpecialAttack();
    snapshotQueuePositions();
    render();
    await sleep(300);

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

    document.getElementById('turn-num').textContent = state.turn;

    // 我方 HP
    const pFill = document.getElementById('player-hp-fill');
    pFill.style.width = (state.player.hp / state.player.maxHp * 100) + '%';
    document.getElementById('player-hp').textContent = state.player.hp;
    document.getElementById('player-maxhp').textContent = state.player.maxHp;

    // 敌方 HP
    const eFill = document.getElementById('enemy-hp-fill');
    eFill.style.width = (state.enemy.hp / state.enemy.maxHp * 100) + '%';
    document.getElementById('enemy-hp').textContent = state.enemy.hp;
    document.getElementById('enemy-maxhp').textContent = state.enemy.maxHp;

    document.getElementById('player-portrait-name').textContent = state.character.name;
    document.getElementById('enemy-portrait-name').textContent = state.enemyDef.name;

    // 效果图标（4 格）
    const renderFx = (elId, effects) => {
        const el = document.getElementById(elId);
        el.innerHTML = '';
        for (let i = 0; i < 4; i++) {
            const slot = document.createElement('div');
            const fx = effects[i];
            if (fx) {
                slot.className = 'fx-slot' + (fx.cls ? ' ' + fx.cls : '');
                slot.title = fx.title || '';
                slot.textContent = (fx.label || '?').slice(0, 2);
            } else {
                slot.className = 'fx-slot empty';
            }
            el.appendChild(slot);
        }
    };

    const playerFx = state.player.effects
        .filter(e => e.type === 'attackBonus')
        .map(e => ({ label: `攻+${e.value}`, title: `攻击 +${e.value}（剩余 ${e.turnsLeft} 回合）`, cls: 'atk' }));
    renderFx('player-fx', playerFx);

    const enemyFx = state.enemy.debuffs.map(d => {
        if (d.type === 'frost') {
            return { label: `霜${d.turnsLeft}`, title: `霜冻：行动上限 -1（剩余 ${d.turnsLeft} 回合）`, cls: 'frost' };
        } else if (d.type === 'stat_down') {
            return { label: `弱${d.value}`, title: `属性降低：攻击/格挡 -${d.value}（剩余 ${d.turnsLeft} 回合）`, cls: 'stat' };
        }
        return { label: '?', title: d.type };
    });
    renderFx('enemy-fx', enemyFx);

    // 敌人词条
    const traitsEl = document.getElementById('enemy-traits');
    if (state.enemy.traits.length === 0) {
        traitsEl.innerHTML = '';
    } else {
        traitsEl.innerHTML = state.enemy.traits.map(t =>
            `<div class="trait-chip ${t.active ? 'active' : ''}" title="${t.description || ''}">${t.name}</div>`
        ).join('');
    }

    // 敌人意图
    const hideIntent = getActiveEnemyPassives().some(p => p.type === 'hide_intent');
    const { atkDown, blockDown } = getEnemyStatDown();
    const intentEl = document.getElementById('enemy-intent');
    if (state.enemy.queue.length === 0) {
        intentEl.innerHTML = '<span class="intent-label">行动意图</span>';
    } else {
        intentEl.innerHTML = state.enemy.queue.map(i => {
            if (i.type === 'attack') {
                const times = i.times || 1;
                const rawVal = i.value;
                const effective = Math.max(0, rawVal - atkDown);
                const display = hideIntent ? '?' : effective;
                const label = times > 1 ? `攻 ${display}×${times}` : `攻 ${display}`;
                return `<span class="intent-chip">${label}</span>`;
            } else if (i.type === 'buff') {
                const effective = Math.max(0, i.value - blockDown);
                const display = hideIntent ? '?' : effective;
                return `<span class="intent-chip buff">盾 +${display}</span>`;
            }
            return `<span class="intent-chip">未知</span>`;
        }).join('');
    }

    // 行动序列（始终渲染）
    const stageQueue = document.getElementById('stage-queue');
    stageQueue.innerHTML = state.queue.map(c => {
        const cls = ['queue-slot'];
        if (isSpecialCard(c)) cls.push('special');
        if (c.uid === state.resolvingCardUid) cls.push('resolving');
        return `<span class="${cls.join(' ')}" data-uid="${c.uid}">${c.name}</span>`;
    }).join('');

    // 手牌
    const handEl = document.getElementById('spire-hand');
    handEl.innerHTML = '';
    state.hand.forEach((card, i) => {
        const el = document.createElement('div');
        el.className = 'spire-card';
        el.dataset.uid = card.uid;
        if (state.queue.length >= state.queueLimit || state.phase !== 'building') {
            el.classList.add('disabled');
        }
        if (isSpecialCard(card)) el.style.borderColor = '#e0a0a0';
        el.innerHTML = `<div class="name">${card.name}</div>`;

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
        } else if (card.states?.frostExtend) {
            const b = document.createElement('div');
            b.className = 'card-badge tag';
            b.textContent = '侵';
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
        el.addEventListener('touchmove', () => clearTimeout(longPressTimer), { passive: true });

        el.addEventListener('click', () => {
            if (el._longPressed) { el._longPressed = false; return; }
            playCardFromHand(i);
        });
        handEl.appendChild(el);
    });
    layoutHand();

    document.getElementById('draw-count').textContent = state.drawPile.length;
    document.getElementById('resolve-btn').disabled = state.phase !== 'building';

    const logHtml = state.log.slice(-60).map(l => `<div>${l}</div>`).join('');
    const logEl = document.getElementById('spire-log');
    if (logEl) {
        logEl.innerHTML = logHtml;
        logEl.scrollTop = logEl.scrollHeight;
    }
    const midLog = document.getElementById('mid-strip-log');
    if (midLog) {
        midLog.innerHTML = logHtml;
        midLog.scrollTop = midLog.scrollHeight;
    }
}

/* ============================================
   按钮绑定
   ============================================ */
document.getElementById('resolve-btn').addEventListener('click', () => resolveAndEndTurn());

document.getElementById('restart-btn').addEventListener('click', () => {
    if (state && state.phase === 'resolving') return;
    document.getElementById('spire-log').innerHTML = '';
    showCharacterSelect();
});

document.getElementById('log-btn').addEventListener('click', () => {
    document.getElementById('log-panel').classList.toggle('active');
});
document.getElementById('log-close').addEventListener('click', () => {
    document.getElementById('log-panel').classList.remove('active');
});

document.getElementById('draw-pile-btn').addEventListener('click', () => {
    if (!state) return;
    const renderPile = (elId, cards) => {
        const el = document.getElementById(elId);
        el.innerHTML = cards.length === 0
            ? '<div style="color:#bbb;font-size:0.85em;">（空）</div>'
            : cards.map(c => {
                const cls = isSpecialCard(c) ? 'pile-item special' : 'pile-item';
                return `<span class="${cls}">${c.name}</span>`;
            }).join('');
    };
    renderPile('pile-modal-draw', state.drawPile);
    renderPile('pile-modal-discard', state.playedPile);
    document.getElementById('pile-modal').classList.add('active');
});
document.getElementById('pile-modal').addEventListener('click', (e) => {
    if (e.target.id === 'pile-modal') e.target.classList.remove('active');
});

document.getElementById('stage-queue').addEventListener('click', (e) => {
    if (!state || state.phase !== 'building') return;
    const slot = e.target.closest('.queue-slot');
    if (!slot) return;
    const uid = parseInt(slot.dataset.uid);
    const idx = state.queue.findIndex(c => c.uid === uid);
    if (idx < 0) return;

    const card = state.queue.splice(idx, 1)[0];
    if (card._wasChoice) {
        card.name = '祈愿';
        card.description = '打出时选择：攻击 6，或防御 5。';
        card.effects = [];
        card.isChoice = true;
        card.tags = card.tags.filter(t => t !== 'attack' && t !== 'buff');
        delete card._wasChoice;
    }
    if (card._activateTraitId) {
        card.effects = card.effects.filter(e => e.type !== 'activateTrait');
        const lastDmg = card.effects.map(e => e.type).lastIndexOf('damage');
        if (lastDmg >= 0) card.effects.splice(lastDmg, 1);
        delete card._activateTraitId;
    }
    delete card.handIndex;
    state.hand.push(card);
    render();
});

document.getElementById('start-battle-btn').addEventListener('click', () => {
    if (selectedCharKey && selectedEnemyKey) startBattle(selectedCharKey, selectedEnemyKey);
});

window.addEventListener('resize', () => { if (state) layoutHand(); });

/* ============================================
   启动
   ============================================ */
Promise.all([
    fetch('/data/ruogelike-card.json').then(r => r.json()),
    fetch('/data/ruogelike-character.json').then(r => r.json()),
    fetch('/data/ruogelike-enemy.json').then(r => r.json()),
    fetch('/data/ruogelike-glossary.json').then(r => r.json()).catch(() => [])
]).then(([cards, chars, enemies, glossary]) => {
    CARD_LIBRARY = cards;
    CHARACTER_LIBRARY = chars;
    ENEMY_LIBRARY = enemies;
    GLOSSARY_DATA = glossary || [];
    showMainMenu();
}).catch(err => {
    console.error('未能成功加载数据', err);
    document.getElementById('spire-log').innerHTML = '<div>加载数据失败，你要试试刷新吗？</div>';
});
</script>