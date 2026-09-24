# -*- coding: utf-8 -*-
"""
Builder for the updated visual, balanced, and live-synced presentation:
"Ecossistemas de Inovação: Teoria, Governança, Estudo de Caso Internacional (San Diego)
 e Aplicação Prática no PIT São José dos Campos com Entrevista e Kahoot RPG Interativo"
"""

import os

deck_code = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Seminário 5: Ecossistemas de Inovação | UNIFESP & PIT SJC</title>
  
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>

  <!-- Firebase & Realtime Sync Service -->
  <script src="https://www.gstatic.com/firebasejs/9.22.0/firebase-app-compat.js"></script>
  <script src="https://www.gstatic.com/firebasejs/9.22.0/firebase-database-compat.js"></script>
  <script src="firebase-config.js"></script>
  <script src="sync-service.js"></script>

  <style>
    :root {
      --bg-space: #050a14;
      --bg-surface: #0a1324;
      --bg-card: rgba(15, 23, 42, 0.85);
      --bg-card-hover: rgba(30, 41, 59, 0.95);
      
      --cyan-glow: #06b6d4;
      --cyan-light: #67e8f9;
      --blue-accent: #2563eb;
      --blue-electric: #38bdf8;
      --purple-accent: #8b5cf6;
      --purple-glow: #a855f7;
      --emerald-accent: #10b981;
      --amber-accent: #f59e0b;
      --rose-accent: #f43f5e;
      
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --border-soft: rgba(255, 255, 255, 0.1);
      --border-bright: rgba(6, 182, 212, 0.45);
      
      --shadow-glow: 0 0 35px rgba(6, 182, 212, 0.2);
      --shadow-card: 0 10px 30px -10px rgba(0, 0, 0, 0.6);
      
      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 20px;
      --font-display: 'Outfit', sans-serif;
      --font-body: 'Plus Jakarta Sans', sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      user-select: none;
    }

    body {
      background-color: var(--bg-space);
      background-image: 
        radial-gradient(circle at 15% 15%, rgba(37, 99, 235, 0.15) 0%, transparent 45%),
        radial-gradient(circle at 85% 85%, rgba(139, 92, 246, 0.15) 0%, transparent 45%),
        radial-gradient(circle at 50% 50%, rgba(6, 182, 212, 0.05) 0%, transparent 60%);
      color: var(--text-main);
      font-family: var(--font-body);
      min-height: 100vh;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }

    /* Top Global Header */
    .deck-header {
      height: 52px;
      background: rgba(10, 19, 36, 0.9);
      backdrop-filter: blur(14px);
      border-bottom: 1px solid var(--border-soft);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 1.5rem;
      z-index: 100;
      position: relative;
    }

    .header-left {
      display: flex;
      align-items: center;
      gap: 1rem;
    }

    .brand-badge {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      background: rgba(6, 182, 212, 0.12);
      border: 1px solid rgba(6, 182, 212, 0.35);
      padding: 0.25rem 0.75rem;
      border-radius: 999px;
      font-size: 0.75rem;
      font-weight: 700;
      letter-spacing: 0.05em;
      color: var(--cyan-light);
      text-transform: uppercase;
    }

    .header-title {
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .header-title strong { color: #fff; }

    .header-center {
      display: flex;
      align-items: center;
      gap: 1rem;
    }

    /* Master Clock */
    .seminar-clock {
      display: flex;
      align-items: center;
      gap: 0.6rem;
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid var(--border-soft);
      padding: 0.25rem 0.85rem;
      border-radius: var(--radius-sm);
      font-family: var(--font-mono);
      font-size: 0.82rem;
    }

    .clock-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--emerald-accent);
      box-shadow: 0 0 8px var(--emerald-accent);
      animation: pulse 2s infinite;
    }

    @keyframes pulse {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.4; transform: scale(0.85); }
    }

    .clock-btn {
      background: none;
      border: none;
      color: var(--text-muted);
      cursor: pointer;
      font-size: 0.8rem;
      display: flex;
      align-items: center;
      padding: 0.15rem 0.3rem;
      border-radius: 4px;
      transition: all 0.2s;
    }

    .clock-btn:hover {
      color: var(--cyan-light);
      background: rgba(255, 255, 255, 0.08);
    }

    .header-right {
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }

    .deck-btn {
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid var(--border-soft);
      color: var(--text-muted);
      padding: 0.3rem 0.75rem;
      border-radius: var(--radius-sm);
      font-size: 0.78rem;
      font-family: var(--font-display);
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
      display: flex;
      align-items: center;
      gap: 0.35rem;
      text-decoration: none;
    }

    .deck-btn:hover {
      background: rgba(255, 255, 255, 0.14);
      color: #fff;
      border-color: var(--cyan-glow);
    }

    .deck-btn.active {
      background: var(--blue-accent);
      color: #fff;
      border-color: var(--cyan-glow);
    }

    /* Main Deck Stage - Balanced, No Giant Empty Holes */
    .deck-viewport {
      flex: 1;
      position: relative;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1.25rem 2.5rem;
    }

    .slide {
      position: absolute;
      inset: 1.25rem 2.5rem;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      gap: 0.85rem;
      opacity: 0;
      transform: scale(0.98) translateY(12px);
      pointer-events: none;
      transition: opacity 0.35s cubic-bezier(0.16, 1, 0.3, 1), transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      overflow-y: auto;
      max-width: 1400px;
      margin: 0 auto;
    }

    .slide.active {
      opacity: 1;
      transform: scale(1) translateY(0);
      pointer-events: auto;
    }

    /* Slide Header Meta */
    .slide-tag {
      font-family: var(--font-mono);
      font-size: 0.75rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--cyan-light);
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }

    .slide-title {
      font-family: var(--font-display);
      font-size: 2.1rem;
      font-weight: 800;
      line-height: 1.15;
      letter-spacing: -0.02em;
      color: #fff;
    }

    .slide-title span {
      background: linear-gradient(135deg, var(--cyan-light), var(--blue-electric));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    /* Punchline Banner */
    .punchline-card {
      background: linear-gradient(90deg, rgba(6, 182, 212, 0.15), rgba(37, 99, 235, 0.12));
      border-left: 4px solid var(--cyan-glow);
      border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
      padding: 0.55rem 1.15rem;
      display: flex;
      align-items: center;
      gap: 0.8rem;
    }

    .punchline-quote {
      font-family: var(--font-display);
      font-size: 1.05rem;
      font-weight: 700;
      color: #fff;
      font-style: italic;
    }

    /* Grids & Cards - Well Proportioned */
    .grid-2 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.25rem;
      align-items: stretch;
    }

    .grid-3 {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 1.15rem;
      align-items: stretch;
    }

    .grid-4 {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1rem;
      align-items: stretch;
    }

    .card {
      background: var(--bg-card);
      border: 1px solid var(--border-soft);
      border-radius: var(--radius-md);
      padding: 1.15rem 1.25rem;
      backdrop-filter: blur(12px);
      box-shadow: var(--shadow-card);
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      gap: 0.6rem;
      transition: all 0.25s ease;
      position: relative;
      overflow: hidden;
    }

    .card:hover {
      background: var(--bg-card-hover);
      border-color: var(--border-bright);
      transform: translateY(-2px);
    }

    .card-glow-cyan::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 3px;
      background: linear-gradient(90deg, var(--cyan-glow), var(--blue-accent));
    }

    .card-glow-purple::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 3px;
      background: linear-gradient(90deg, var(--purple-accent), var(--rose-accent));
    }

    .card-glow-emerald::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 3px;
      background: linear-gradient(90deg, var(--emerald-accent), var(--cyan-glow));
    }

    .card-glow-amber::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 3px;
      background: linear-gradient(90deg, var(--amber-accent), var(--rose-accent));
    }

    .card-title {
      font-family: var(--font-display);
      font-size: 1.05rem;
      font-weight: 700;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .card-desc {
      font-size: 0.85rem;
      color: #cbd5e1;
      line-height: 1.45;
    }

    .bullet-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0.45rem;
    }

    .bullet-list li {
      font-size: 0.84rem;
      color: #e2e8f0;
      display: flex;
      align-items: flex-start;
      gap: 0.5rem;
      line-height: 1.35;
    }

    .bullet-list li strong { color: #fff; }

    .bullet-dot {
      color: var(--cyan-light);
      font-size: 0.85rem;
      flex-shrink: 0;
      margin-top: 1px;
    }

    /* Media Image Box */
    .img-box {
      border-radius: var(--radius-md);
      overflow: hidden;
      border: 1px solid var(--border-soft);
      position: relative;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4);
      background: #000;
      height: 230px;
    }

    .img-box img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.4s ease;
    }

    .img-box:hover img { transform: scale(1.03); }

    .img-overlay {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      background: linear-gradient(to top, rgba(5, 10, 20, 0.95) 0%, rgba(5, 10, 20, 0.4) 60%, transparent 100%);
      padding: 1rem 1rem 0.6rem;
      color: #fff;
    }

    .img-overlay-title { font-family: var(--font-display); font-size: 0.95rem; font-weight: 700; }
    .img-overlay-sub { font-size: 0.72rem; color: var(--cyan-light); }

    /* Visual Infographic Chips */
    .chips-row {
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
      margin-top: 0.4rem;
    }

    .chip-badge {
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-soft);
      padding: 0.2rem 0.55rem;
      border-radius: 999px;
      font-size: 0.72rem;
      font-family: var(--font-mono);
      color: var(--cyan-light);
    }

    /* Live Kahoot Checkpoint Bar with Real-Time Ranking Widget */
    .checkpoint-card {
      background: linear-gradient(90deg, rgba(37, 99, 235, 0.2), rgba(6, 182, 212, 0.18));
      border: 1px solid var(--cyan-glow);
      border-radius: var(--radius-md);
      padding: 0.75rem 1.25rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      box-shadow: 0 0 25px rgba(6, 182, 212, 0.25);
    }

    .checkpoint-left {
      display: flex;
      align-items: center;
      gap: 0.8rem;
    }

    .checkpoint-icon {
      font-size: 1.6rem;
      animation: bounce 1s infinite alternate;
    }

    @keyframes bounce {
      from { transform: translateY(0); }
      to { transform: translateY(-4px); }
    }

    .checkpoint-title { font-family: var(--font-display); font-size: 0.95rem; font-weight: 800; color: #fff; }
    .checkpoint-sub { font-size: 0.76rem; color: var(--cyan-light); }

    /* Live Mini Leaderboard Ticker on Slides */
    .live-ticker-box {
      display: flex;
      align-items: center;
      gap: 0.6rem;
      background: rgba(10, 19, 36, 0.85);
      border: 1px solid rgba(6, 182, 212, 0.3);
      padding: 0.35rem 0.85rem;
      border-radius: 999px;
      font-family: var(--font-mono);
      font-size: 0.75rem;
      color: #fff;
    }

    .live-pulse-dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: var(--emerald-accent);
      box-shadow: 0 0 8px var(--emerald-accent);
      animation: pulse 1.5s infinite;
    }

    .live-top-scorer {
      color: #fbbf24;
      font-weight: 700;
    }

    /* Bottom Global Footer */
    .deck-footer {
      height: 48px;
      background: rgba(10, 19, 36, 0.9);
      backdrop-filter: blur(14px);
      border-top: 1px solid var(--border-soft);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 1.5rem;
      z-index: 100;
    }

    .footer-left {
      display: flex;
      align-items: center;
      gap: 0.8rem;
      font-size: 0.78rem;
    }

    .speaker-badge {
      display: flex;
      align-items: center;
      gap: 0.4rem;
      background: rgba(255, 255, 255, 0.05);
      padding: 0.2rem 0.6rem;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-soft);
      color: var(--text-muted);
      font-family: var(--font-mono);
      font-size: 0.74rem;
    }

    .speaker-badge strong { color: var(--cyan-light); }

    .footer-center {
      display: flex;
      align-items: center;
      gap: 0.8rem;
    }

    .nav-arrow-btn {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid var(--border-soft);
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 0.9rem;
      transition: all 0.2s;
    }

    .nav-arrow-btn:hover {
      background: var(--blue-accent);
      border-color: var(--cyan-glow);
    }

    .slide-progress-text {
      font-family: var(--font-mono);
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--text-muted);
      min-width: 65px;
      text-align: center;
    }

    .slide-progress-bar {
      position: absolute;
      bottom: 0;
      left: 0;
      height: 3px;
      background: linear-gradient(90deg, var(--blue-accent), var(--cyan-glow));
      transition: width 0.3s ease;
      z-index: 101;
    }

    /* Speaker Notes Drawer (Toggled by N) */
    .notes-drawer {
      position: fixed;
      bottom: 48px;
      right: 0;
      width: 480px;
      max-height: 480px;
      background: rgba(10, 19, 36, 0.96);
      border-left: 1px solid var(--cyan-glow);
      border-top: 1px solid var(--cyan-glow);
      border-radius: var(--radius-md) 0 0 0;
      backdrop-filter: blur(20px);
      box-shadow: 0 -10px 40px rgba(0, 0, 0, 0.6);
      padding: 1.5rem;
      display: none;
      flex-direction: column;
      gap: 0.75rem;
      z-index: 200;
      overflow-y: auto;
    }

    .notes-drawer.open {
      display: flex;
      animation: slideUp 0.25s ease;
    }

    @keyframes slideUp {
      from { transform: translateY(20px); opacity: 0; }
      to { transform: translateY(0); opacity: 1; }
    }

    .notes-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--border-soft);
      padding-bottom: 0.5rem;
    }

    .notes-title { font-family: var(--font-display); font-size: 0.95rem; font-weight: 800; color: #fff; }
    .notes-body { font-size: 0.86rem; color: #cbd5e1; line-height: 1.6; white-space: pre-line; }

    /* Grid Overview Modal (Toggled by G) */
    .grid-modal {
      position: fixed;
      inset: 0;
      background: rgba(5, 10, 20, 0.95);
      backdrop-filter: blur(16px);
      z-index: 300;
      padding: 2rem;
      overflow-y: auto;
      display: none;
    }

    .grid-modal.open { display: block; animation: fadeIn 0.2s ease; }

    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

    .grid-modal-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      max-width: 1400px;
      margin: 0 auto 1.5rem;
    }

    .thumbs-container {
      max-width: 1400px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 1rem;
    }

    .slide-thumb {
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid var(--border-soft);
      border-radius: var(--radius-sm);
      padding: 0.85rem;
      cursor: pointer;
      transition: all 0.2s;
    }

    .slide-thumb:hover { border-color: var(--cyan-glow); transform: translateY(-2px); }
    .slide-thumb.active { border-color: var(--cyan-light); background: rgba(30, 41, 59, 0.95); }
    .thumb-num { font-family: var(--font-mono); font-size: 0.72rem; color: var(--cyan-light); font-weight: 700; }
    .thumb-title { font-family: var(--font-display); font-size: 0.82rem; font-weight: 700; color: #fff; margin: 0.2rem 0; }
    .thumb-speaker { font-size: 0.7rem; color: var(--text-dim); }
  </style>
</head>
<body>

  <!-- Top Global Header -->
  <header class="deck-header">
    <div class="header-left">
      <div class="brand-badge"><span>⚡</span> GETI 2026 • PPG-PIT UNIFESP</div>
      <div class="header-title"><strong>Seminário 5:</strong> Ecossistemas de Inovação & PIT SJC</div>
    </div>

    <div class="header-center">
      <div class="seminar-clock">
        <div class="clock-dot" id="clock-dot"></div>
        <span id="clock-display" style="font-weight: 700; color: #fff;">120:00</span>
        <button class="clock-btn" onclick="toggleClock()" id="clock-btn" title="Iniciar/Pausar">▶</button>
        <button class="clock-btn" onclick="resetClock()" title="Reiniciar">↺</button>
      </div>
    </div>

    <div class="header-right">
      <a href="admin.html" target="_blank" class="deck-btn"><span>⚙️</span> Cockpit Admin</a>
      <a href="jogo.html" target="_blank" class="deck-btn"><span>🎮</span> RPG Aluno</a>
      <button class="deck-btn" onclick="toggleNotesDrawer()" id="btn-notes"><span>📝</span> Notas (N)</button>
      <button class="deck-btn" onclick="toggleGridModal()"><span>🔲</span> Grade (G)</button>
      <button class="deck-btn" onclick="toggleFullscreen()"><span>⛶</span> Tela Cheia (F)</button>
    </div>
  </header>

  <!-- Deck Viewport -->
  <main class="deck-viewport" id="deck-viewport">

    <!-- SLIDE 1: ABERTURA (Visually Balanced, No Empty Void) -->
    <section class="slide active" data-slide="1" data-block="Abertura" data-speaker="Josué Jofre / Grupo 5" data-time="2 min">
      <div class="slide-tag">🚀 ABERTURA OFICIAL • SEMINÁRIO GETI 2026</div>
      <h1 class="slide-title">Ecossistemas de Inovação: <span>Teoria, Orquestração e a Prática no PIT SJC</span></h1>
      
      <div class="punchline-card">
        <span style="font-size: 1.4rem;">💡</span>
        <div class="punchline-quote">"Nenhuma organização inova sozinha: o valor não está nas partes, mas na sinergia entre elas."</div>
      </div>

      <div class="grid-3">
        <div class="card card-glow-cyan">
          <div class="card-title"><span>📚</span> Fundamentos Teóricos</div>
          <p class="card-desc">Artigos seminais e recentes da vanguarda da literatura internacional:</p>
          <ul class="bullet-list">
            <li><span class="bullet-dot">▸</span> <strong>Shen et al. (2025/2026):</strong> Mapeamento cienciométrico e fronteiras</li>
            <li><span class="bullet-dot">▸</span> <strong>Machado et al. (2025):</strong> Competências de orquestração</li>
            <li><span class="bullet-dot">▸</span> <strong>Furr & Shipilov (MIT):</strong> Ecossistemas adaptativos</li>
            <li><span class="bullet-dot">▸</span> <strong>Majava & Rinkinen:</strong> Benchmarking de San Diego</li>
          </ul>
          <div class="chips-row">
            <span class="chip-badge">Hélices 3ª, 4ª e 5ª</span>
            <span class="chip-badge">Co-criação de Valor</span>
          </div>
        </div>

        <div class="card card-glow-purple">
          <div class="card-title"><span>🔬</span> O Laboratório Vivo</div>
          <p class="card-desc">Conexão umbilical com o Parque Tecnológico de São José dos Campos:</p>
          <ul class="bullet-list">
            <li><span class="bullet-dot">▸</span> Primeiro Parque Tecnológico do Estado de SP (2006)</li>
            <li><span class="bullet-dot">▸</span> Mais de 300 empresas e 4 APLs consolidados</li>
            <li><span class="bullet-dot">▸</span> Nexus Hub: aceleradora e incubadora de deep techs</li>
            <li><span class="bullet-dot">▸</span> Campus UNIFESP e sinergia com o PPG-PIT</li>
          </ul>
          <div class="chips-row">
            <span class="chip-badge">Embraer & DCTA</span>
            <span class="chip-badge">PPG-PIT UNIFESP</span>
          </div>
        </div>

        <div class="card card-glow-emerald">
          <div class="card-title"><span>🎮</span> RPG & Kahoot ao Vivo</div>
          <p class="card-desc">Interatividade em tempo real pelo smartphone da turma:</p>
          <ul class="bullet-list">
            <li><span class="bullet-dot">▸</span> 6 Fases liberadas logo após cada bloco da palestra</li>
            <li><span class="bullet-dot">▸</span> 18 perguntas (1 certa e 2 erradas) com cronômetro</li>
            <li><span class="bullet-dot">▸</span> Pontuação por precisão e velocidade de resposta</li>
            <li><span class="bullet-dot">▸</span> Pódio ao vivo e premiação para o melhor orquestrador!</li>
          </ul>
          <div class="chips-row">
            <span class="chip-badge">Ranking na Tela</span>
            <span class="chip-badge">Análise de Erros</span>
          </div>
        </div>
      </div>

      <!-- Live Ranking Quick Preview on Slide 1 -->
      <div class="checkpoint-card" style="padding: 0.6rem 1.25rem;">
        <div class="checkpoint-left">
          <span style="font-size: 1.2rem;">📡</span>
          <div>
            <div style="font-family: var(--font-display); font-size: 0.85rem; font-weight: 700; color: #fff;">
              Transmissão ao Vivo do Kahoot RPG da Turma
            </div>
            <div style="font-size: 0.72rem; color: var(--cyan-light);">
              Acesse pelo celular: <strong>josuejofre.github.io/seminario-ecossistema-inovacao-pit/jogo.html</strong>
            </div>
          </div>
        </div>
        <div class="live-ticker-box">
          <div class="live-pulse-dot"></div>
          <span>Status da Sala:</span>
          <span class="live-top-scorer" id="ticker-status-s1">Aguardando participantes...</span>
        </div>
      </div>
    </section>

    <!-- SLIDE 2: AGENDA -->
    <section class="slide" data-slide="2" data-block="Agenda" data-speaker="Josué Jofre (4ª) / Fernando Barreto (5ª)" data-time="2 min">
      <div class="slide-tag">🧭 CRONOGRAMA & ROTEIRO • 120 MINUTOS</div>
      <h2 class="slide-title">Estrutura e <span>Divisão dos Blocos</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">⚡</span>
        <div class="punchline-quote">"Da teoria da coevolução biológica à prática orquestrada em São José dos Campos."</div>
      </div>

      <div class="grid-4">
        <div class="card card-glow-cyan">
          <div class="card-title">Bloco 1 & 2</div>
          <ul class="bullet-list">
            <li><strong>B1: Conceito e Evolução:</strong> Shen et al. <br><em style="color:var(--cyan-light)">Nathalia / Fernando</em></li>
            <li><strong>B2: Anatomia e Atores:</strong> Machado et al. <br><em style="color:var(--cyan-light)">Veridiany / Fábio Lippi</em></li>
            <li><span class="bullet-dot">🎮</span> Fases 1 e 2 no Celular</li>
          </ul>
        </div>

        <div class="card card-glow-purple">
          <div class="card-title">Bloco 3 & 4</div>
          <ul class="bullet-list">
            <li><strong>B3: Governança e Orquestração:</strong> Machado et al. <br><em style="color:var(--purple-accent)">Jessica David</em></li>
            <li><strong>B4: Construção e Gestão:</strong> Furr & Shipilov <br><em style="color:var(--purple-accent)">Josué / Marciele</em></li>
            <li><span class="bullet-dot">🎮</span> Fases 3 e 4 no Celular</li>
          </ul>
        </div>

        <div class="card card-glow-amber">
          <div class="card-title">Bloco 5 & PIT</div>
          <ul class="bullet-list">
            <li><strong>B5: Caso San Diego:</strong> Majava & Rinkinen <br><em style="color:var(--amber-accent)">Lilian Vinhas</em></li>
            <li><strong>Prática: PIT SJC:</strong> APLs e Nexus <br><em style="color:var(--amber-accent)">Josué / Marciele</em></li>
            <li><span class="bullet-dot">🎮</span> Fase 5 no Celular</li>
          </ul>
        </div>

        <div class="card card-glow-emerald">
          <div class="card-title">Entrevista & B6</div>
          <ul class="bullet-list">
            <li><strong>Entrevista Exclusiva:</strong> Coord. PIT SJC <br><em style="color:var(--emerald-accent)">Renato Paschoal</em></li>
            <li><strong>B6: Limitações e Dark Side:</strong> Shen et al. <br><em style="color:var(--emerald-accent)">Renato Paschoal</em></li>
            <li><span class="bullet-dot">🏆</span> Dinâmica, Ranking & Pódio</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- SLIDE 3: CONTEXTO TERRITORIAL -->
    <section class="slide" data-slide="3" data-block="Contexto PIT" data-speaker="Josué Jofre (4ª) / Marciele Toledo (5ª)" data-time="3 min">
      <div class="slide-tag">📍 TERRITÓRIO ESTRATÉGICO • SÃO JOSÉ DOS CAMPOS</div>
      <h2 class="slide-title">Por que o <span>PIT São José dos Campos?</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">🎯</span>
        <div class="punchline-quote">"Não estamos debatendo uma teoria abstrata: estamos sentados dentro do maior polo aeroespacial da América Latina."</div>
      </div>

      <div class="grid-2">
        <div class="img-box">
          <img src="assets/pit_sjc_facade.jpg" alt="Fachada do PIT São José dos Campos">
          <div class="img-overlay">
            <div class="img-overlay-title">Parque de Inovação Tecnológica de SJC</div>
            <div class="img-overlay-sub">Primeiro Parque Tecnológico credenciado em SP (2006)</div>
          </div>
        </div>

        <div class="card card-glow-cyan" style="justify-content: center;">
          <div class="card-title"><span>🏛️</span> Densidade Científica e Industrial Única</div>
          <ul class="bullet-list" style="font-size: 0.95rem; gap: 0.8rem;">
            <li><span class="bullet-dot">▸</span> <strong>Triângulo DCTA • ITA • INPE:</strong> gênese aeroespacial brasileira desde a década de 1950.</li>
            <li><span class="bullet-dot">▸</span> <strong>Embraer:</strong> âncora global indutora de centenas de fornecedores de alta tecnologia.</li>
            <li><span class="bullet-dot">▸</span> <strong>Campus UNIFESP SJC:</strong> formação de mestres e doutores com pesquisa aplicada.</li>
            <li><span class="bullet-dot">▸</span> <strong>Ambiente Neutro:</strong> governança público-privada operada como Organização Social.</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- SLIDE 4: BLOCO 1 - ORIGEM E METÁFORA ECOLÓGICA -->
    <section class="slide" data-slide="4" data-block="Bloco 1" data-speaker="Nathalia (4ª) / Fernando Barreto (5ª)" data-time="4 min">
      <div class="slide-tag">🌱 BLOCO 1 • CONCEITO E ORIGEM HISTÓRICA</div>
      <h2 class="slide-title">A Origem e a <span>Metáfora Ecológica</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">🌿</span>
        <div class="punchline-quote">"Na biologia ou nos negócios: isolado, qualquer organismo morre. O segredo é a coevolução mútua."</div>
      </div>

      <div class="grid-3">
        <div class="card card-glow-emerald">
          <div class="card-title">1935 • Biologia</div>
          <div style="font-size: 1.1rem; font-weight: 800; color: var(--emerald-accent);">Arthur Tansley</div>
          <p class="card-desc">Cunhou o termo na ecologia para descrever uma comunidade de organismos vivos interagindo com o meio físico inorgânico em equilíbrio dinâmico.</p>
          <div class="chips-row"><span class="chip-badge">Habitat Comum</span><span class="chip-badge">Equilíbrio Dinâmico</span></div>
        </div>

        <div class="card card-glow-cyan">
          <div class="card-title">1993 • Estratégia</div>
          <div style="font-size: 1.1rem; font-weight: 800; color: var(--cyan-light);">James F. Moore (HBR)</div>
          <p class="card-desc">Transpôs o conceito para o mundo dos negócios: empresas coevoluem em torno de novas capacidades, apoiando-se e competindo simultaneamente.</p>
          <div class="chips-row"><span class="chip-badge">Coevolução</span><span class="chip-badge">Coopetição</span></div>
        </div>

        <div class="card card-glow-purple">
          <div class="card-title">2006+ • Inovação</div>
          <div style="font-size: 1.1rem; font-weight: 800; color: var(--purple-accent);">Adner & Chesbrough</div>
          <p class="card-desc">Foco na dependência mútua para viabilizar proposições de valor conjuntas: a tecnologia pioneira fracassa se o ecossistema complementar não evoluir junto.</p>
          <div class="chips-row"><span class="chip-badge">Inovação Aberta</span><span class="chip-badge">Interdependência</span></div>
        </div>
      </div>
    </section>

    <!-- SLIDE 5: BLOCO 1 - MAPEAMENTO CIENCIOMÉTRICO -->
    <section class="slide" data-slide="5" data-block="Bloco 1" data-speaker="Nathalia (4ª) / Fernando Barreto (5ª)" data-time="4 min">
      <div class="slide-tag">📊 BLOCO 1 • REVISÃO BIBLIOMÉTRICA MUNDIAL</div>
      <h2 class="slide-title">Mapeamento Cienciométrico: <span>Shen et al. (2025/2026)</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">📈</span>
        <div class="punchline-quote">"Mais de 3.000 artigos em 10 anos: o conceito deixou de ser modismo e consolidou-se como campo científico maduro."</div>
      </div>

      <div class="grid-3">
        <div class="card card-glow-cyan">
          <div class="card-title">1ª Onda (2010-2015)</div>
          <div style="font-weight: 700; color: var(--cyan-light);">Plataformas & Líderes Digitais</div>
          <p class="card-desc">Foco no poder orquestrador de big techs (Apple, Google, Amazon) e ecossistemas baseados em software e lojas de aplicativos.</p>
          <div class="chips-row"><span class="chip-badge">Plataformas Digitais</span><span class="chip-badge">Network Effects</span></div>
        </div>

        <div class="card card-glow-purple">
          <div class="card-title">2ª Onda (2016-2020)</div>
          <div style="font-weight: 700; color: var(--purple-accent);">Dimensão Espacial & Territorial</div>
          <p class="card-desc">Parques tecnológicos, cidades inteligentes, distritos de inovação e a influência do capital social local na retenção de talentos.</p>
          <div class="chips-row"><span class="chip-badge">Parques Tecnológicos</span><span class="chip-badge">Clusters Territoriais</span></div>
        </div>

        <div class="card card-glow-amber">
          <div class="card-title">3ª Onda (Atual)</div>
          <div style="font-weight: 700; color: var(--amber-accent);">Governança, ESG & Quíntupla Hélice</div>
          <p class="card-desc">Sustentabilidade climática, transição energética justa, descarbonização e prevenção contra assimetrias predatórias de poder.</p>
          <div class="chips-row"><span class="chip-badge">Quíntupla Hélice</span><span class="chip-badge">Transição Energética</span></div>
        </div>
      </div>
    </section>

    <!-- SLIDE 6: BLOCO 1 - DIFERENCIAÇÃO CONCEITUAL + LIVE RANKING CHECKPOINT -->
    <section class="slide" data-slide="6" data-block="Bloco 1" data-speaker="Nathalia (4ª) / Fernando Barreto (5ª)" data-time="4 min">
      <div class="slide-tag">🔍 BLOCO 1 • TAXONOMIA CONCEITUAL</div>
      <h2 class="slide-title">Diferenciação Conceitual: <span>Não Confunda os Termos!</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">⚖️</span>
        <div class="punchline-quote">"O Cluster foca na proximidade; o Sistema foca nas leis; o Negócio foca na venda; e a Inovação foca na co-criação inédita."</div>
      </div>

      <div class="grid-4">
        <div class="card">
          <div class="card-title">Cluster (Porter)</div>
          <p class="card-desc">Concentração geográfica de firmas similares para ganho de escala e redução de custos logísticos.</p>
        </div>
        <div class="card">
          <div class="card-title">Sistema de Inovação</div>
          <p class="card-desc">Foco nas instituições públicas, leis de incentivo, ministérios e agências reguladoras do Estado.</p>
        </div>
        <div class="card">
          <div class="card-title">Ecossistema de Negócios</div>
          <p class="card-desc">Foco na captura de valor presente, canais de distribuição e monetização comercial de produtos.</p>
        </div>
        <div class="card card-glow-cyan">
          <div class="card-title" style="color: var(--cyan-light);">Ecossistema de Inovação</div>
          <p class="card-desc">Foco na <strong>co-criação de novo conhecimento</strong> e geração coletiva de tecnologias inéditas.</p>
        </div>
      </div>

      <!-- Live Kahoot Checkpoint Bar with Real-Time Ranking Widget -->
      <div class="checkpoint-card">
        <div class="checkpoint-left">
          <span class="checkpoint-icon">🎮</span>
          <div>
            <div class="checkpoint-title">MOMENTO KAHOOT RPG • FASE 1 LIBERADA!</div>
            <div class="checkpoint-sub">Abra o jogo no celular e caminhe até o Bloco Acadêmico UNIFESP!</div>
          </div>
        </div>
        <div class="live-ticker-box">
          <div class="live-pulse-dot"></div>
          <span>Líder da Sala:</span>
          <span class="live-top-scorer" id="ticker-top-s6">Aguardando respostas...</span>
        </div>
      </div>
    </section>

    <!-- SLIDE 7: BLOCO 2 - ANATOMIA DO ECOSSISTEMA -->
    <section class="slide" data-slide="7" data-block="Bloco 2" data-speaker="Veridiany Braga (4ª) / Fábio Lippi (5ª)" data-time="4 min">
      <div class="slide-tag">🧬 BLOCO 2 • ANATOMIA E INTERDEPENDÊNCIA</div>
      <h2 class="slide-title">Anatomia do Ecossistema: <span>Heterogeneidade & Simbiose</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">🔬</span>
        <div class="punchline-quote">"A monocultura empobrece o solo; a heterogeneidade alimenta a inovação disruptiva."</div>
      </div>

      <div class="grid-3">
        <div class="card card-glow-purple">
          <div class="card-title"><span>🏛️</span> Academia & ICTs</div>
          <ul class="bullet-list">
            <li><span class="bullet-dot">▸</span> Pesquisa básica e aplicada de longo ciclo</li>
            <li><span class="bullet-dot">▸</span> Formação de mestres e doutores qualificados</li>
            <li><span class="bullet-dot">▸</span> Laboratórios multiusuários de ponta</li>
          </ul>
          <div class="chips-row"><span class="chip-badge">UNIFESP • ITA • DCTA</span></div>
        </div>

        <div class="card card-glow-cyan">
          <div class="card-title"><span>🏭</span> Indústria & Startups</div>
          <ul class="bullet-list">
            <li><span class="bullet-dot">▸</span> Corporações: tração, escala global e funding</li>
            <li><span class="bullet-dot">▸</span> Startups/Deep Techs: risco e agilidade extrema</li>
            <li><span class="bullet-dot">▸</span> Relações de coopetição e co-desenvolvimento</li>
          </ul>
          <div class="chips-row"><span class="chip-badge">Embraer • Nexus Deep Techs</span></div>
        </div>

        <div class="card card-glow-emerald">
          <div class="card-title"><span>🌉</span> Intermediários & Governo</div>
          <ul class="bullet-list">
            <li><span class="bullet-dot">▸</span> Parques, NITs e Incubadoras como pontes neutras</li>
            <li><span class="bullet-dot">▸</span> Redução crítica de custos de transação</li>
            <li><span class="bullet-dot">▸</span> Marco Legal de CTI (Lei 13.243/16) e incentivos</li>
          </ul>
          <div class="chips-row"><span class="chip-badge">Associação PqTec • OS</span></div>
        </div>
      </div>
    </section>

    <!-- SLIDE 8: BLOCO 2 - EVOLUÇÃO DAS HÉLICES -->
    <section class="slide" data-slide="8" data-block="Bloco 2" data-speaker="Veridiany Braga (4ª) / Fábio Lippi (5ª)" data-time="4 min">
      <div class="slide-tag">🌀 BLOCO 2 • MODELOS DE COOPERAÇÃO</div>
      <h2 class="slide-title">Evolução das Hélices: <span>Tríplice, Quádrupla e Quíntupla</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">🌍</span>
        <div class="punchline-quote">"Inovação sem o cidadão é estéril; inovação sem respeito aos limites do planeta é autodestrutiva."</div>
      </div>

      <div class="grid-3">
        <div class="card card-glow-cyan">
          <div class="card-title">Tríplice Hélice</div>
          <div style="font-size: 0.8rem; color: var(--cyan-light); font-weight: 700;">Etzkowitz & Leydesdorff (1995)</div>
          <p class="card-desc">Governo + Universidade + Indústria. O motor clássico de transferência de tecnologia e parques industriais.</p>
          <div class="chips-row"><span class="chip-badge">Transferência Tecnológica</span></div>
        </div>

        <div class="card card-glow-purple">
          <div class="card-title">Quádrupla Hélice</div>
          <div style="font-size: 0.8rem; color: var(--purple-accent); font-weight: 700;">Carayannis & Campbell (2009)</div>
          <p class="card-desc">+ <strong>Sociedade Civil e Cidadãos</strong>. Inovação orientada por missões sociais, living labs e validação pelo usuário real.</p>
          <div class="chips-row"><span class="chip-badge">Inovação Cidadã</span></div>
        </div>

        <div class="card card-glow-emerald">
          <div class="card-title">Quíntupla Hélice</div>
          <div style="font-size: 0.8rem; color: var(--emerald-accent); font-weight: 700;">Carayannis et al. (2012)</div>
          <p class="card-desc">+ <strong>Meio Ambiente Natural</strong>. Descarbonização, SAF (combustível sustentável de aviação), economia circular e ESG.</p>
          <div class="chips-row"><span class="chip-badge">SAF • Descarbonização</span></div>
        </div>
      </div>
    </section>

    <!-- SLIDE 9: BLOCO 2 - CO-CRIAÇÃO DE VALOR + LIVE RANKING CHECKPOINT -->
    <section class="slide" data-slide="9" data-block="Bloco 2" data-speaker="Veridiany Braga (4ª) / Fábio Lippi (5ª)" data-time="4 min">
      <div class="slide-tag">🔄 BLOCO 2 • DINÂMICA DE VALOR</div>
      <h2 class="slide-title">Co-Criação de Valor: <span>Como o Valor Circula?</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">💎</span>
        <div class="punchline-quote">"Se a partilha de valor parecer injusta, os melhores talentos abandonam a rede no dia seguinte."</div>
      </div>

      <div class="grid-3">
        <div class="card">
          <div class="card-title">1. Fluxo de Recursos</div>
          <p class="card-desc">Laboratórios multiusuários e infraestrutura compartilhada reduzem custos de P&D de pequenas empresas.</p>
          <div class="chips-row"><span class="chip-badge">Infraestrutura Multiusuário</span></div>
        </div>
        <div class="card">
          <div class="card-title">2. Fluxo de Conhecimento</div>
          <p class="card-desc">Mobilidade de teses, patentes e publicações científicas com contratos claros de cotitularidade.</p>
          <div class="chips-row"><span class="chip-badge">Cotitularidade de Patentes</span></div>
        </div>
        <div class="card">
          <div class="card-title">3. Fluxo de Pessoas</div>
          <p class="card-desc">Mestrandos e doutores circulando entre salas de aula da UNIFESP e centros de inovação de empresas.</p>
          <div class="chips-row"><span class="chip-badge">Bolsas & Spin-offs</span></div>
        </div>
      </div>

      <!-- Live Kahoot Checkpoint Bar with Real-Time Ranking Widget -->
      <div class="checkpoint-card">
        <div class="checkpoint-left">
          <span class="checkpoint-icon">🎮</span>
          <div>
            <div class="checkpoint-title">MOMENTO KAHOOT RPG • FASE 2 LIBERADA!</div>
            <div class="checkpoint-sub">Caminhe até a Praça Central das Hélices e responda no smartphone!</div>
          </div>
        </div>
        <div class="live-ticker-box">
          <div class="live-pulse-dot"></div>
          <span>Líder da Sala:</span>
          <span class="live-top-scorer" id="ticker-top-s9">Aguardando respostas...</span>
        </div>
      </div>
    </section>

    <!-- SLIDE 10: BLOCO 3 - GOVERNANÇA E ORQUESTRAÇÃO -->
    <section class="slide" data-slide="10" data-block="Bloco 3" data-speaker="Jessica Pascotto David (4ª)" data-time="4 min">
      <div class="slide-tag">👑 BLOCO 3 • GOVERNANÇA SEM HIERARQUIA</div>
      <h2 class="slide-title">Governança e Orquestração: <span>Quem Manda Quando Ninguém Pode Mandar?</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">🎯</span>
        <div class="punchline-quote">"Orquestrar não é ser o chefe da rede: é ter legitimidade moral para alinhar propósitos sem emitir ordens diretas."</div>
      </div>

      <div class="grid-2">
        <div class="card card-glow-purple">
          <div class="card-title"><span>⚠️</span> O Grande Paradoxo da Liderança em Rede</div>
          <ul class="bullet-list" style="gap: 0.8rem; font-size: 0.95rem;">
            <li><span class="bullet-dot">▸</span> <strong>Atores Juridicamente Autônomos:</strong> o reitor, o CEO e o prefeito não respondem à mesma cadeia de comando.</li>
            <li><span class="bullet-dot">▸</span> <strong>Conflitos de Temporalidade:</strong> a academia opera em ciclos de 4 anos de pós-graduação; startups operam no fechamento do mês.</li>
            <li><span class="bullet-dot">▸</span> <strong>Risco de Dissolução:</strong> redes sem governança ativa tornam-se ineficientes e perdem seus membros mais promissores.</li>
          </ul>
        </div>

        <div class="card card-glow-cyan">
          <div class="card-title"><span>🎼</span> A Metáfora do Maestro</div>
          <p class="card-desc">O orquestrador não toca todos os instrumentos; ele assegura harmonia por meio de:</p>
          <ul class="bullet-list">
            <li><span class="bullet-dot">▸</span> <strong>Credibilidade Neutra:</strong> postura imparcial que inspira confiança recíproca.</li>
            <li><span class="bullet-dot">▸</span> <strong>Visão de Longo Prazo:</strong> mapear rotas tecnológicas antes dos atores isolados.</li>
            <li><span class="bullet-dot">▸</span> <strong>Mediação de Conflitos:</strong> arbitragem equilibrada de propriedade intelectual.</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- SLIDE 11: BLOCO 3 - 5 DIMENSÕES DA ORQUESTRAÇÃO -->
    <section class="slide" data-slide="11" data-block="Bloco 3" data-speaker="Jessica Pascotto David (4ª)" data-time="4 min">
      <div class="slide-tag">📐 BLOCO 3 • ARQUITETURA DE MACHADO ET AL. (2025)</div>
      <h2 class="slide-title">As 5 Dimensões da <span>Orquestração de Sucesso</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">⚙️</span>
        <div class="punchline-quote">"Do recrutamento de cérebros à apropriação justa: as 5 engrenagens que mantêm a rede viva."</div>
      </div>

      <div class="grid-3" style="grid-template-columns: repeat(5, 1fr); gap: 0.75rem;">
        <div class="card card-glow-cyan" style="padding: 0.9rem;">
          <div class="card-title" style="font-size: 0.92rem;">1. Mobilização</div>
          <p class="card-desc" style="font-size: 0.78rem;">Atração de talentos de ponta e engajamento dos atores certos.</p>
        </div>
        <div class="card card-glow-purple" style="padding: 0.9rem;">
          <div class="card-title" style="font-size: 0.92rem;">2. Agenda</div>
          <p class="card-desc" style="font-size: 0.78rem;">Definição de visão compartilhada para remar no mesmo sentido.</p>
        </div>
        <div class="card card-glow-emerald" style="padding: 0.9rem;">
          <div class="card-title" style="font-size: 0.92rem;">3. Mobilidade</div>
          <p class="card-desc" style="font-size: 0.78rem;">Destravar fluxos cognitivos entre laboratórios e indústrias.</p>
        </div>
        <div class="card card-glow-amber" style="padding: 0.9rem;">
          <div class="card-title" style="font-size: 0.92rem;">4. Estabilidade</div>
          <p class="card-desc" style="font-size: 0.78rem;">Prevenção de conflitos, contratos claros e segurança jurídica.</p>
        </div>
        <div class="card card-glow-cyan" style="padding: 0.9rem;">
          <div class="card-title" style="font-size: 0.92rem;">5. Apropriação</div>
          <p class="card-desc" style="font-size: 0.78rem;">Garantir recompensa justa para quem arriscou tempo e capital.</p>
        </div>
      </div>
    </section>

    <!-- SLIDE 12: BLOCO 3 - COMPETÊNCIAS + LIVE RANKING CHECKPOINT -->
    <section class="slide" data-slide="12" data-block="Bloco 3" data-speaker="Jessica Pascotto David (4ª)" data-time="4 min">
      <div class="slide-tag">🧠 BLOCO 3 • CAPACIDADES DINÂMICAS</div>
      <h2 class="slide-title">Competências do Orquestrador: <span>Machado et al. (2025)</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">🤝</span>
        <div class="punchline-quote">"O orquestrador moderno é um diplomata tecnológico com tolerância extrema à ambiguidade."</div>
      </div>

      <div class="grid-3">
        <div class="card card-glow-cyan">
          <div class="card-title"><span>🗣️</span> Articulação & Comunicação</div>
          <p class="card-desc">Habilidade de traduzir o rigor científico acadêmico para a urgência mercadológica empresarial.</p>
          <div class="chips-row"><span class="chip-badge">Tradução de Dialetos</span></div>
        </div>
        <div class="card card-glow-purple">
          <div class="card-title"><span>⚖️</span> Arbitragem & Confiança</div>
          <p class="card-desc">Capacidade de atuar como intermediário neutro e construir capital social sólido entre concorrentes.</p>
          <div class="chips-row"><span class="chip-badge">Terceiro Neutro</span></div>
        </div>
        <div class="card card-glow-emerald">
          <div class="card-title"><span>🔭</span> Visão Sistêmica</div>
          <p class="card-desc">Antecipar tendências mundiais de descarbonização e IA antes que a obsolescência atinja o cluster local.</p>
          <div class="chips-row"><span class="chip-badge">Roadmap Tecnológico</span></div>
        </div>
      </div>

      <!-- Live Kahoot Checkpoint Bar with Real-Time Ranking Widget -->
      <div class="checkpoint-card">
        <div class="checkpoint-left">
          <span class="checkpoint-icon">🎮</span>
          <div>
            <div class="checkpoint-title">MOMENTO KAHOOT RPG • FASE 3 LIBERADA!</div>
            <div class="checkpoint-sub">Caminhe até o Centro de Governança do PIT e decida no celular!</div>
          </div>
        </div>
        <div class="live-ticker-box">
          <div class="live-pulse-dot"></div>
          <span>Líder da Sala:</span>
          <span class="live-top-scorer" id="ticker-top-s12">Aguardando respostas...</span>
        </div>
      </div>
    </section>

    <!-- SLIDE 13: BLOCO 4 - CONSTRUÇÃO DE ECOSSISTEMAS -->
    <section class="slide" data-slide="13" data-block="Bloco 4" data-speaker="Josué Jofre (4ª) / Marciele Toledo (5ª)" data-time="4 min">
      <div class="slide-tag">🏗️ BLOCO 4 • DESIGN ESTRATÉGICO</div>
      <h2 class="slide-title">Construção de Ecossistemas: <span>Furr & Shipilov (MIT Sloan)</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">📐</span>
        <div class="punchline-quote">"Não espere o milagre espontâneo: ecossistemas robustos exigem arquitetura deliberada e intencional."</div>
      </div>

      <div class="grid-3">
        <div class="card card-glow-cyan">
          <div class="card-title">1. Diagnóstico de Incerteza</div>
          <p class="card-desc">Definir se o desafio tecnológico é conhecido e incremental ou se o mercado é radicalmente incerto.</p>
          <div class="chips-row"><span class="chip-badge">Mapeamento de Riscos</span></div>
        </div>
        <div class="card card-glow-purple">
          <div class="card-title">2. Escolha da Arquitetura</div>
          <p class="card-desc">Optar entre arquitetura centralizada (hub rígido) ou ecossistema adaptativo e distribuído.</p>
          <div class="chips-row"><span class="chip-badge">Centralizado vs Adaptativo</span></div>
        </div>
        <div class="card card-glow-amber">
          <div class="card-title">3. Parcerias Não Óbvias</div>
          <p class="card-desc">Recrutar parceiros de outros setores industriais para destravar inovações combinatórias fora da caixa.</p>
          <div class="chips-row"><span class="chip-badge">Cross-Industry</span></div>
        </div>
      </div>
    </section>

    <!-- SLIDE 14: BLOCO 4 - CENTRALIZADOS VS ADAPTATIVOS -->
    <section class="slide" data-slide="14" data-block="Bloco 4" data-speaker="Josué Jofre (4ª) / Marciele Toledo (5ª)" data-time="4 min">
      <div class="slide-tag">⚖️ BLOCO 4 • COMPARATIVO DE ARQUITETURA</div>
      <h2 class="slide-title">Ecossistemas <span>Centralizados vs. Adaptativos</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">🔄</span>
        <div class="punchline-quote">"Na certeza, construa uma fábrica centralizada; na incerteza radical, cultive um ecossistema adaptativo."</div>
      </div>

      <div class="grid-2">
        <div class="card">
          <div class="card-title" style="color: var(--text-muted);">Ecossistema Centralizado (Hub-and-Spoke)</div>
          <ul class="bullet-list" style="font-size: 0.9rem; gap: 0.7rem;">
            <li><span class="bullet-dot">▸</span> <strong>Cenário:</strong> Baixa incerteza tecnológica, produto bem definido.</li>
            <li><span class="bullet-dot">▸</span> <strong>Coordenação:</strong> A empresa âncora dita especificações rígidas.</li>
            <li><span class="bullet-dot">▸</span> <strong>Papel dos Membros:</strong> Executores especializados de subpartes.</li>
            <li><span class="bullet-dot">▸</span> <strong>Exemplo clássico:</strong> Linha de montagem automotiva tradicional.</li>
          </ul>
        </div>

        <div class="card card-glow-cyan">
          <div class="card-title" style="color: var(--cyan-light);">Ecossistema Adaptativo (Foco de Inovação)</div>
          <ul class="bullet-list" style="font-size: 0.9rem; gap: 0.7rem;">
            <li><span class="bullet-dot">▸</span> <strong>Cenário:</strong> Alta incerteza radical (IA, Deep Tech, Biotecnologia).</li>
            <li><span class="bullet-dot">▸</span> <strong>Coordenação:</strong> Experimentação descentralizada e prototipagem rápida.</li>
            <li><span class="bullet-dot">▸</span> <strong>Papel dos Membros:</strong> Co-designers autônomos que coevoluem a solução.</li>
            <li><span class="bullet-dot">▸</span> <strong>Exemplo clássico:</strong> Nexus Hub e o ecossistema de startups espaciais.</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- SLIDE 15: BLOCO 4 - PARCEIROS NÃO CONVENCIONAIS + LIVE RANKING CHECKPOINT -->
    <section class="slide" data-slide="15" data-block="Bloco 4" data-speaker="Josué Jofre (4ª) / Marciele Toledo (5ª)" data-time="4 min">
      <div class="slide-tag">🧩 BLOCO 4 • INOVAÇÃO CROSS-INDUSTRY</div>
      <h2 class="slide-title">Parceiros Não Convencionais & <span>Coopetição</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">🚀</span>
        <div class="punchline-quote">"Seus concorrentes de ontem são seus aliados de hoje na criação do mercado de amanhã."</div>
      </div>

      <div class="grid-3">
        <div class="card card-glow-purple">
          <div class="card-title">Quebrando a Miopia</div>
          <p class="card-desc">Empresas aeroespaciais inovam mais rápido ao dialogar com a indústria de games (simuladores) e saúde (telemetria de pilotos).</p>
          <div class="chips-row"><span class="chip-badge">Recombinação Cognitiva</span></div>
        </div>
        <div class="card card-glow-emerald">
          <div class="card-title">Coopetição Estratégica</div>
          <p class="card-desc">Cooperar na infraestrutura de base pré-competitiva (laboratórios e dados) enquanto competem ferozmente no mercado final.</p>
          <div class="chips-row"><span class="chip-badge">P&D Pré-competitivo</span></div>
        </div>
        <div class="card card-glow-amber">
          <div class="card-title">Armadilha do Controle</div>
          <p class="card-desc">Tentar aprisionar parceiros com contratos abusivos no estágio inicial afasta os pioneiros mais criativos da rede.</p>
          <div class="chips-row"><span class="chip-badge">Autonomia de Rede</span></div>
        </div>
      </div>

      <!-- Live Kahoot Checkpoint Bar with Real-Time Ranking Widget -->
      <div class="checkpoint-card">
        <div class="checkpoint-left">
          <span class="checkpoint-icon">🎮</span>
          <div>
            <div class="checkpoint-title">MOMENTO KAHOOT RPG • FASE 4 LIBERADA!</div>
            <div class="checkpoint-sub">Caminhe até o Nexus Hub de Startups e teste suas decisões!</div>
          </div>
        </div>
        <div class="live-ticker-box">
          <div class="live-pulse-dot"></div>
          <span>Líder da Sala:</span>
          <span class="live-top-scorer" id="ticker-top-s15">Aguardando respostas...</span>
        </div>
      </div>
    </section>

    <!-- SLIDE 16: BLOCO 5 - CASO SAN DIEGO -->
    <section class="slide" data-slide="16" data-block="Bloco 5" data-speaker="Lilian Veiga Vinhas (4ª)" data-time="4 min">
      <div class="slide-tag">🇺🇸 BLOCO 5 • BENCHMARKING INTERNACIONAL</div>
      <h2 class="slide-title">O Caso San Diego: <span>20 Anos, 20 Estudos (Majava & Rinkinen)</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">🌊</span>
        <div class="punchline-quote">"San Diego não tentou copiar o Vale do Silício: descobriu sua vocação científica própria e transformou praia em alta tecnologia."</div>
      </div>

      <div class="grid-2">
        <div class="img-box">
          <img src="assets/san_diego_cluster.jpg" alt="Cluster de San Diego - Torrey Pines">
          <div class="img-overlay">
            <div class="img-overlay-title">Torrey Pines Mesa • San Diego, CA</div>
            <div class="img-overlay-sub">Densidade mundial de biotecnologia, genômica e telecom</div>
          </div>
        </div>

        <div class="card card-glow-cyan" style="justify-content: center;">
          <div class="card-title"><span>🧬</span> A Trajetória de Transformação</div>
          <ul class="bullet-list" style="font-size: 0.95rem; gap: 0.8rem;">
            <li><span class="bullet-dot">▸</span> <strong>Até 1960:</strong> Base militar da Marinha e polo turístico litorâneo.</li>
            <li><span class="bullet-dot">▸</span> <strong>Fundação da UCSD:</strong> Universidade criada com foco deliberado em pós-graduação e ciências duras.</li>
            <li><span class="bullet-dot">▸</span> <strong>Institutos Salk & Scripps:</strong> Pesquisa biomédica de elite atraindo prêmios Nobel.</li>
            <li><span class="bullet-dot">▸</span> <strong>Gigantes Globais Nascidas na Rede:</strong> Qualcomm (telecom) e Illumina (sequenciamento genético).</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- SLIDE 17: BLOCO 5 - PILARES SAN DIEGO & LIVE RANKING CHECKPOINT -->
    <section class="slide" data-slide="17" data-block="Bloco 5" data-speaker="Lilian Veiga Vinhas (4ª)" data-time="4 min">
      <div class="slide-tag">🤝 BLOCO 5 • O MODELO CONNECT</div>
      <h2 class="slide-title">Os Pilares de San Diego: <span>A Ponte CONNECT</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">🌱</span>
        <div class="punchline-quote">"Ciência sem mentoria morre no laboratório; dinheiro sem ciência vira especulação vazia."</div>
      </div>

      <div class="grid-3">
        <div class="card card-glow-cyan">
          <div class="card-title">A Fundação CONNECT (1985)</div>
          <p class="card-desc">Organização sem fins lucrativos criada dentro da UCSD para conectar pesquisadores da bancada a investidores de risco.</p>
          <div class="chips-row"><span class="chip-badge">Intermediário Sem Fins Lucrativos</span></div>
        </div>
        <div class="card card-glow-purple">
          <div class="card-title">Programa Springboard</div>
          <p class="card-desc">Mentoria voluntária com executivos seniores da indústria que preparavam cientistas para falar a língua do Venture Capital.</p>
          <div class="chips-row"><span class="chip-badge">Mentoria com Executivos</span></div>
        </div>
        <div class="card card-glow-emerald">
          <div class="card-title">Cultura 'Pay-it-forward'</div>
          <p class="card-desc">Dar apoio e compartilhar contatos sem exigir contrapartida imediata: o capital social como o maior acelerador regional.</p>
          <div class="chips-row"><span class="chip-badge">Cultura Give-First</span></div>
        </div>
      </div>

      <!-- Live Kahoot Checkpoint Bar with Real-Time Ranking Widget -->
      <div class="checkpoint-card">
        <div class="checkpoint-left">
          <span class="checkpoint-icon">🎮</span>
          <div>
            <div class="checkpoint-title">MOMENTO KAHOOT RPG • FASE 5 LIBERADA!</div>
            <div class="checkpoint-sub">Caminhe até o Pavilhão Aeroespacial & San Diego no mapa!</div>
          </div>
        </div>
        <div class="live-ticker-box">
          <div class="live-pulse-dot"></div>
          <span>Líder da Sala:</span>
          <span class="live-top-scorer" id="ticker-top-s17">Aguardando respostas...</span>
        </div>
      </div>
    </section>

    <!-- SLIDE 18: CASO PRÁTICO PIT SJC -->
    <section class="slide" data-slide="18" data-block="Caso PIT" data-speaker="Josué Jofre / Marciele Toledo" data-time="4 min">
      <div class="slide-tag">📍 CASO PRÁTICO • SÃO JOSÉ DOS CAMPOS</div>
      <h2 class="slide-title">PIT São José dos Campos: <span>O Orquestrador do Vale</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">🏛️</span>
        <div class="punchline-quote">"Do pioneirismo da Embraer e DCTA à consolidação de um Parque Tecnológico multifacetado."</div>
      </div>

      <div class="grid-2">
        <div class="card card-glow-cyan" style="justify-content: center;">
          <div class="card-title"><span>⚙️</span> O Papel Neutro de Governança</div>
          <ul class="bullet-list" style="font-size: 0.95rem; gap: 0.8rem;">
            <li><span class="bullet-dot">▸</span> <strong>Associação PqTec (OS):</strong> personalidade jurídica privada sem fins lucrativos gerindo o interesse público com agilidade.</li>
            <li><span class="bullet-dot">▸</span> <strong>Infraestrutura Compartilhada:</strong> laboratórios de manufatura aditiva, centro de dados e salas de coworking.</li>
            <li><span class="bullet-dot">▸</span> <strong>Atração de Investimentos:</strong> ponte direta com FAPESP (PIPE), Finep e fundos corporativos de Venture Capital.</li>
          </ul>
        </div>

        <div class="img-box">
          <img src="assets/pit_sjc_facade.jpg" alt="Parque Tecnológico São José dos Campos">
          <div class="img-overlay">
            <div class="img-overlay-title">Campus Eugênio de Melo • PIT SJC</div>
            <div class="img-overlay-sub">Conectando academia, governo e grandes multinacionais</div>
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 19: ANATOMIA DO PIT (APLs, NEXUS & UNIFESP) -->
    <section class="slide" data-slide="19" data-block="Caso PIT" data-speaker="Josué Jofre / Marciele Toledo" data-time="3 min">
      <div class="slide-tag">🔬 ESTRUTURA OPERACIONAL • PIT SJC</div>
      <h2 class="slide-title">Anatomia do PIT: <span>APLs, Nexus, ICTs & UNIFESP</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">🏢</span>
        <div class="punchline-quote">"A sala de aula da UNIFESP e as bancadas das startups dividem o mesmo corredor e o mesmo futuro."</div>
      </div>

      <div class="grid-2">
        <div class="img-box">
          <img src="assets/nexus_pit_hub.jpg" alt="Interior do Nexus Hub PIT SJC">
          <div class="img-overlay">
            <div class="img-overlay-title">Nexus Hub de Inovação</div>
            <div class="img-overlay-sub">Incubadora, aceleradora e coworking de deep techs do PIT</div>
          </div>
        </div>

        <div class="grid-2" style="grid-template-columns: 1fr; gap: 0.8rem;">
          <div class="card card-glow-cyan">
            <div class="card-title"><span>🚀</span> Nexus Hub de Inovação</div>
            <p class="card-desc">Programas estruturados de aceleração, desde a ideação (Nexus Labs) até a escala comercial de deep techs.</p>
          </div>
          <div class="card card-glow-purple">
            <div class="card-title"><span>🎯</span> 4 APLs Consolidados</div>
            <p class="card-desc">Aeroespacial & Defesa, TIC (Software e IA), Saúde & Biotecnologia e Segurança da Informação.</p>
          </div>
          <div class="card card-glow-emerald">
            <div class="card-title"><span>🎓</span> Campus UNIFESP & PPG-PIT</div>
            <p class="card-desc">Pós-graduação acadêmica e profissional conectada com os desafios industriais reais do Vale.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 20: BENCHMARKING SAN DIEGO VS PIT SJC -->
    <section class="slide" data-slide="20" data-block="Benchmarking" data-speaker="Fernando Barreto / Josué Jofre" data-time="3 min">
      <div class="slide-tag">⚖️ MATRIZ COMPARATIVA • APRENDIZADOS</div>
      <h2 class="slide-title">Benchmarking Sistêmico: <span>San Diego vs. PIT SJC</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">📊</span>
        <div class="punchline-quote">"Mesma busca por sinergia academia-mercado; desafios distintos de maturidade de capital de risco."</div>
      </div>

      <div class="grid-3">
        <div class="card card-glow-cyan">
          <div class="card-title">Origem e Defesa</div>
          <ul class="bullet-list">
            <li><strong>San Diego:</strong> Marinha dos EUA e bases aeronavais no Pacífico.</li>
            <li><strong>São José dos Campos:</strong> DCTA, ITA e projetos aeroespaciais da FAB.</li>
          </ul>
        </div>
        <div class="card card-glow-purple">
          <div class="card-title">Âncora Acadêmica</div>
          <ul class="bullet-list">
            <li><strong>San Diego:</strong> UCSD, Salk Institute e Scripps Research.</li>
            <li><strong>São José dos Campos:</strong> ITA, UNIFESP, INPE e FATEC.</li>
          </ul>
        </div>
        <div class="card card-glow-amber">
          <div class="card-title">Orquestrador e Funding</div>
          <ul class="bullet-list">
            <li><strong>San Diego:</strong> CONNECT (1985) + Vasto ecossistema de Venture Capital.</li>
            <li><strong>PIT SJC:</strong> Nexus Hub + Desafio de amadurecer fundos privados de risco.</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- SLIDE 21: ENTREVISTA EXCLUSIVA PIT SJC -->
    <section class="slide" data-slide="21" data-block="Entrevista" data-speaker="Renato Paschoal (4ª e 5ª)" data-time="6 min">
      <div class="slide-tag">🎙️ ATIVIDADE PRÁTICA • ENTREVISTA EXCLUSIVA</div>
      <h2 class="slide-title">Entrevista com a Liderança: <span>Luiz Fernando Carvalho (PIT SJC)</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">💬</span>
        <div class="punchline-quote">"A orquestração não é um modelo estático: é a arte diária de negociar egos e alinhar futuros."</div>
      </div>

      <div class="grid-2">
        <div class="img-box">
          <img src="assets/pit_interview_leader.jpg" alt="Entrevista com Luiz Fernando Carvalho">
          <div class="img-overlay">
            <div class="img-overlay-title">Luiz Fernando Carvalho</div>
            <div class="img-overlay-sub">Coordenador de Inovação do PIT São José dos Campos</div>
          </div>
        </div>

        <div class="card card-glow-emerald" style="justify-content: center;">
          <div class="card-title"><span>🗣️</span> O Dilema Central do Orquestrador</div>
          <blockquote style="font-size: 0.95rem; font-style: italic; color: #e2e8f0; line-height: 1.6; border-left: 3px solid var(--emerald-accent); padding-left: 1rem; margin: 0.5rem 0;">
            "A universidade não pode virar balcão de consultoria rápida para apagar incêndio de empresa, nem a empresa pode esperar 4 anos por uma tese sem ter entregáveis intermediários. O orquestrador é o amortecedor de choques e o tradutor de dialetos entre essas duas realidades."
          </blockquote>
        </div>
      </div>
    </section>

    <!-- SLIDE 22: AS 4 LIÇÕES DA ENTREVISTA -->
    <section class="slide" data-slide="22" data-block="Entrevista" data-speaker="Renato Paschoal (4ª e 5ª)" data-time="4 min">
      <div class="slide-tag">💡 LIÇÕES DA PRÁTICA • O QUE A TEORIA NÃO CONTA</div>
      <h2 class="slide-title">As 4 Lições da Entrevista: <span>Da Trincheira da Inovação</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">🔑</span>
        <div class="punchline-quote">"A confiança não se assina em contrato: se constrói café a café, projeto a projeto."</div>
      </div>

      <div class="grid-4">
        <div class="card card-glow-cyan">
          <div class="card-title">1. Expectativas</div>
          <p class="card-desc">Definir cotitularidade de patentes e royalties desde o primeiro dia de conversa.</p>
        </div>
        <div class="card card-glow-purple">
          <div class="card-title">2. Confiança</div>
          <p class="card-desc">Reuniões transparentes e governança ágil valem mais do que 100 páginas de cláusulas punitivas.</p>
        </div>
        <div class="card card-glow-amber">
          <div class="card-title">3. Marco Legal</div>
          <p class="card-desc">Utilizar com segurança jurídica as flexibilidades da Lei 13.243/16 para laboratórios públicos.</p>
        </div>
        <div class="card card-glow-emerald">
          <div class="card-title">4. Formação</div>
          <p class="card-desc">O maior patrimônio buscado na UNIFESP são pesquisadores com mentalidade empreendedora.</p>
        </div>
      </div>
    </section>

    <!-- SLIDE 23: BLOCO 6 - DESAFIOS E LIMITAÇÕES -->
    <section class="slide" data-slide="23" data-block="Bloco 6" data-speaker="Renato Paschoal (4ª)" data-time="4 min">
      <div class="slide-tag">⚠️ BLOCO 6 • CRÍTICA CONCEITUAL (SHEN ET AL., 2025)</div>
      <h2 class="slide-title">Desafios e Limitações: <span>Onde a Teoria Falha?</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">❓</span>
        <div class="punchline-quote">"Fronteiras difusas e causalidade complexa: é difícil saber se a região é rica por causa do ecossistema ou se o ecossistema nasceu porque ela já era rica."</div>
      </div>

      <div class="grid-3">
        <div class="card card-glow-rose">
          <div class="card-title"><span>🗺️</span> Fronteiras Difusas</div>
          <p class="card-desc">Onde termina o ecossistema do PIT SJC? Ele é local em Eugênio de Melo ou é global pelas redes de fornecedores mundiais?</p>
          <div class="chips-row"><span class="chip-badge">Limites Espaciais</span></div>
        </div>
        <div class="card card-glow-amber">
          <div class="card-title"><span>🧪</span> O Desafio da Causalidade</div>
          <p class="card-desc">Como comprovar estatisticamente que o faturamento de uma empresa decorre do parque e não de fatores macroeconômicos?</p>
          <div class="chips-row"><span class="chip-badge">Nexo Causal</span></div>
        </div>
        <div class="card card-glow-purple">
          <div class="card-title"><span>⏳</span> Dependência Histórica</div>
          <p class="card-desc">Políticas públicas tentam criar 'vales' por decreto, ignorando que o capital social leva décadas para amadurecer.</p>
          <div class="chips-row"><span class="chip-badge">Path Dependency</span></div>
        </div>
      </div>
    </section>

    <!-- SLIDE 24: BLOCO 6 - O DARK SIDE + LIVE RANKING CHECKPOINT -->
    <section class="slide" data-slide="24" data-block="Bloco 6" data-speaker="Renato Paschoal (4ª)" data-time="4 min">
      <div class="slide-tag">🌑 BLOCO 6 • EFEITOS COLATERAIS</div>
      <h2 class="slide-title">O "Dark Side" dos <span>Ecossistemas de Inovação</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">🕷️</span>
        <div class="punchline-quote">"Ecossistemas sem ética tornam-se armadilhas predatórias de apropriação de propriedade intelectual."</div>
      </div>

      <div class="grid-3">
        <div class="card card-glow-rose">
          <div class="card-title">Lock-in Predatório</div>
          <p class="card-desc">Startups pequenas que acabam reféns de uma única corporação dominante que dita preços e impede novas parcerias.</p>
          <div class="chips-row"><span class="chip-badge">Assimetria de Poder</span></div>
        </div>
        <div class="card card-glow-amber">
          <div class="card-title">Vazamento de Know-how</div>
          <p class="card-desc">Ideias expostas prematuramente em editais ou hackathons que são apropriadas sem compensar o inventor acadêmico.</p>
          <div class="chips-row"><span class="chip-badge">Apropriação Indevida</span></div>
        </div>
        <div class="card card-glow-purple">
          <div class="card-title">Teatro da Inovação</div>
          <p class="card-desc">Eventos sociais festivos e métricas de vaidade que não geram impacto econômico, empregos ou renda para a região.</p>
          <div class="chips-row"><span class="chip-badge">Outputs vs Outcomes</span></div>
        </div>
      </div>

      <!-- Live Kahoot Checkpoint Bar with Real-Time Ranking Widget -->
      <div class="checkpoint-card">
        <div class="checkpoint-left">
          <span class="checkpoint-icon">🎮</span>
          <div>
            <div class="checkpoint-title">MOMENTO KAHOOT RPG • FASE 6 LIBERADA!</div>
            <div class="checkpoint-sub">Caminhe até o Living Lab Net-Zero e conclua sua jornada no campus!</div>
          </div>
        </div>
        <div class="live-ticker-box">
          <div class="live-pulse-dot"></div>
          <span>Líder da Sala:</span>
          <span class="live-top-scorer" id="ticker-top-s24">Aguardando respostas...</span>
        </div>
      </div>
    </section>

    <!-- SLIDE 25: DINÂMICA INTERATIVA - O KAHOOT RPG NO CELULAR -->
    <section class="slide" data-slide="25" data-block="Dinâmica" data-speaker="Jessica David / Grupo Inteiro" data-time="3 min">
      <div class="slide-tag">🎮 ATIVIDADE DINÂMICA • COMPETIÇÃO EM TEMPO REAL</div>
      <h2 class="slide-title">Dinâmica Interativa: <span>O Orquestrador do Ecossistema</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">📱</span>
        <div class="punchline-quote">"18 perguntas respondidas, tempo cronometrado em milissegundos: quem será o orquestrador mais veloz da sala?"</div>
      </div>

      <div class="grid-2" style="align-items: center;">
        <div class="card card-glow-cyan" style="display: flex; flex-direction: column; align-items: center; text-align: center; padding: 1.5rem; background: rgba(10, 19, 36, 0.95);">
          <div style="font-family: var(--font-display); font-size: 1.15rem; font-weight: 800; color: #fff; margin-bottom: 0.6rem;">
            📱 Aponte a Câmera do Smartphone
          </div>
          <div style="background: #ffffff; padding: 0.85rem; border-radius: 16px; box-shadow: 0 0 35px rgba(6, 182, 212, 0.4); margin-bottom: 0.85rem; border: 2px solid var(--cyan-light);">
            <img src="assets/qrcode_jogo.png" alt="QR Code para o jogo do PIT" style="width: 180px; height: 180px; display: block; object-fit: contain;">
          </div>
          <div style="font-family: var(--font-mono); font-size: 0.8rem; color: var(--cyan-light); margin-bottom: 0.75rem;">
            josuejofre.github.io/seminario-ecossistema-inovacao-pit/jogo.html
          </div>
          <a href="jogo.html" target="_blank" class="deck-btn" style="background: var(--blue-accent); color: #fff; text-decoration: none; padding: 0.5rem 1.1rem; font-size: 0.82rem;">
            <span>↗</span> Abrir Jogo no Navegador
          </a>
        </div>

        <div style="display: flex; flex-direction: column; gap: 0.85rem;">
          <div class="card card-glow-purple">
            <div class="card-title">Como Funciona a Pontuação Kahoot:</div>
            <ul class="bullet-list" style="font-size: 0.9rem; gap: 0.6rem;">
              <li><span class="bullet-dot">▸</span> <strong>Base:</strong> 1.000 pontos por cada resposta correta.</li>
              <li><span class="bullet-dot">▸</span> <strong>Bônus de Agilidade:</strong> até 500 pontos extras por velocidade.</li>
              <li><span class="bullet-dot">▸</span> <strong>Erro:</strong> 0 pontos, sem desconto no saldo acumulado.</li>
              <li><span class="bullet-dot">▸</span> <strong>Ranking ao Vivo:</strong> Pódio projetado em tempo real no telão!</li>
            </ul>
          </div>

          <!-- Live Top 3 Mini-Podium on Slide 25 -->
          <div class="card card-glow-emerald" style="padding: 1rem 1.25rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
              <span style="font-family: var(--font-display); font-weight: 800; font-size: 0.9rem; color: #fff;">
                🔥 Placar Atual da Sala (Top 3)
              </span>
              <span style="font-family: var(--font-mono); font-size: 0.72rem; color: var(--emerald-accent);" id="slide25-active-count">
                Sincronizando...
              </span>
            </div>
            <div id="slide25-top3-list" style="display: flex; flex-direction: column; gap: 0.4rem; font-family: var(--font-mono); font-size: 0.82rem;">
              <div style="color: var(--text-dim);">Aguardando participantes completarem as rodadas...</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 26: DEBRIEFING AO VIVO COM PÓDIO E GRÁFICOS NO PRÓPRIO SLIDE -->
    <section class="slide" data-slide="26" data-block="Dinâmica" data-speaker="Jessica / Renato / Grupo Inteiro" data-time="6 min">
      <div class="slide-tag">📊 DEBRIEFING • DIAGNÓSTICO & PREMIAÇÃO</div>
      <h2 class="slide-title">Cockpit do Orquestrador: <span>Gráficos de Pizza & Campeão</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">🏆</span>
        <div class="punchline-quote">"O erro em sala de aula é a semente do aprendizado: analisando os gráficos de pizza da nossa turma."</div>
      </div>

      <div class="grid-2">
        <!-- Live Class Leaderboard Table on Slide -->
        <div class="card card-glow-cyan" style="padding: 1.25rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.6rem;">
            <div class="card-title"><span>👑</span> Classificação Geral da Turma</div>
            <span class="live-pulse-dot"></span>
          </div>
          <div style="max-height: 220px; overflow-y: auto;">
            <table style="width: 100%; border-collapse: collapse; font-size: 0.8rem; font-family: var(--font-mono);">
              <thead>
                <tr style="border-bottom: 1px solid var(--border-soft); color: var(--text-muted); text-align: left;">
                  <th style="padding: 0.3rem;">Pos</th>
                  <th>Nome</th>
                  <th>Turma</th>
                  <th>Pontos</th>
                  <th>Acertos</th>
                </tr>
              </thead>
              <tbody id="slide26-table-body">
                <tr><td colspan="5" style="text-align: center; color: var(--text-dim); padding: 1.5rem;">Sincronizando respostas da sala...</td></tr>
              </tbody>
            </table>
          </div>
          <div style="margin-top: 0.75rem; display: flex; gap: 0.5rem;">
            <a href="admin.html" target="_blank" class="deck-btn" style="flex: 1; justify-content: center; background: rgba(6, 182, 212, 0.2); border-color: var(--cyan-glow); color: #fff;">
              <span>📊</span> Abrir Painel Completo com Gráficos de Pizza
            </a>
          </div>
        </div>

        <!-- Live Podium & Celebration on Slide -->
        <div class="card card-glow-amber" style="text-align: center; justify-content: center; padding: 1.25rem;">
          <div style="font-size: 2.8rem; margin-bottom: 0.3rem;">🏆</div>
          <div style="font-family: var(--font-display); font-size: 1.3rem; font-weight: 900; color: #fff;">
            O Grande Campeão do Seminário
          </div>
          <div id="slide26-winner-name" style="font-family: var(--font-display); font-size: 1.8rem; font-weight: 900; color: #fbbf24; margin: 0.4rem 0;">
            ---
          </div>
          <div id="slide26-winner-score" style="font-family: var(--font-mono); font-size: 0.95rem; color: var(--cyan-light); margin-bottom: 1rem;">
            0 pts • 0 acertos
          </div>

          <button class="deck-btn" onclick="celebrateOnSlide()" style="background: linear-gradient(135deg, #fbbf24, #d97706); color: #000; font-weight: 800; border: none; padding: 0.7rem 1.4rem; justify-content: center; font-size: 0.95rem; cursor: pointer; width: 100%;">
            <span>🎉</span> Celebrar Campeão com Confetes
          </button>
        </div>
      </div>
    </section>

    <!-- SLIDE 27: CONCLUSÕES: AS 5 LEIS DOS ECOSSISTEMAS -->
    <section class="slide" data-slide="27" data-block="Conclusões" data-speaker="Josué Jofre / Renato Paschoal" data-time="3 min">
      <div class="slide-tag">📜 SÍNTESE ESTRATÉGICA • LIÇÕES PERMANENTES</div>
      <h2 class="slide-title">As 5 Leis Estratégicas dos <span>Ecossistemas de Inovação</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">⭐</span>
        <div class="punchline-quote">"Cinco princípios fundamentais para orquestrar qualquer rede de inovação no século XXI."</div>
      </div>

      <div class="grid-3" style="grid-template-columns: repeat(5, 1fr); gap: 0.75rem;">
        <div class="card card-glow-cyan" style="padding: 0.9rem;">
          <div class="card-title" style="font-size: 0.92rem;">1ª Lei</div>
          <div style="font-weight: 700; color: var(--cyan-light); font-size: 0.85rem;">Valor é Relacional</div>
          <p class="card-desc" style="font-size: 0.78rem;">A força da rede é multiplicada pela confiança mútua, não por ativos isolados.</p>
        </div>
        <div class="card card-glow-purple" style="padding: 0.9rem;">
          <div class="card-title" style="font-size: 0.92rem;">2ª Lei</div>
          <div style="font-weight: 700; color: var(--purple-accent); font-size: 0.85rem;">Orquestração Ativa</div>
          <p class="card-desc" style="font-size: 0.78rem;">Sem um líder legítimo, a entropia destrói a coesão de atores autônomos.</p>
        </div>
        <div class="card card-glow-emerald" style="padding: 0.9rem;">
          <div class="card-title" style="font-size: 0.92rem;">3ª Lei</div>
          <div style="font-weight: 700; color: var(--emerald-accent); font-size: 0.85rem;">Heterogeneidade</div>
          <p class="card-desc" style="font-size: 0.78rem;">Inovação radical nasce da colisão entre setores improváveis e diversos.</p>
        </div>
        <div class="card card-glow-amber" style="padding: 0.9rem;">
          <div class="card-title" style="font-size: 0.92rem;">4ª Lei</div>
          <div style="font-weight: 700; color: var(--amber-accent); font-size: 0.85rem;">Partilha Justa</div>
          <p class="card-desc" style="font-size: 0.78rem;">A apropriação desleal de propriedade intelectual espanta os pioneiros.</p>
        </div>
        <div class="card card-glow-cyan" style="padding: 0.9rem;">
          <div class="card-title" style="font-size: 0.92rem;">5ª Lei</div>
          <div style="font-weight: 700; color: var(--cyan-light); font-size: 0.85rem;">Ciência Pública</div>
          <p class="card-desc" style="font-size: 0.78rem;">Universidades fortes como a UNIFESP são o solo onde a prosperidade cria raízes.</p>
        </div>
      </div>
    </section>

    <!-- SLIDE 28: DEBATE COM A TURMA -->
    <section class="slide" data-slide="28" data-block="Debate" data-speaker="Grupo Inteiro" data-time="4 min">
      <div class="slide-tag">🎤 RODA DE CONVERSA • PARTICIPAÇÃO ABERTA</div>
      <h2 class="slide-title">Perguntas, Provocações e <span>Debate com a Turma</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">💬</span>
        <div class="punchline-quote">"A palavra está com vocês: como a UNIFESP pode acelerar ainda mais sua integração com o ecossistema do PIT?"</div>
      </div>

      <div class="grid-3">
        <div class="card card-glow-cyan">
          <div class="card-title">Provocação 1: Academia</div>
          <p class="card-desc">Como evitar que as teses e dissertações da pós-graduação fiquem isoladas dos desafios tecnológicos reais do Parque?</p>
        </div>
        <div class="card card-glow-purple">
          <div class="card-title">Provocação 2: Governança</div>
          <p class="card-desc">Como proteger a propriedade intelectual dos alunos sem criar barreiras burocráticas intransponíveis para as empresas?</p>
        </div>
        <div class="card card-glow-emerald">
          <div class="card-title">Provocação 3: San Diego</div>
          <p class="card-desc">Qual prática do modelo CONNECT podemos implantar imediatamente no PIT São José dos Campos?</p>
        </div>
      </div>
    </section>

    <!-- SLIDE 29: REFERÊNCIAS BIBLIOGRÁFICAS -->
    <section class="slide" data-slide="29" data-block="Referências" data-speaker="Grupo Inteiro" data-time="1 min">
      <div class="slide-tag">📚 BASE CIENTÍFICA • ARTIGOS OFICIAIS</div>
      <h2 class="slide-title">Referências <span>Bibliográficas Oficiais</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">📖</span>
        <div class="punchline-quote">"Rigor científico e consistência metodológica do início ao fim."</div>
      </div>

      <div class="grid-2">
        <div class="card">
          <div class="card-title">Artigos-Base da Disciplina</div>
          <ul class="bullet-list" style="font-size: 0.82rem; gap: 0.55rem;">
            <li><span class="bullet-dot">▸</span> <strong>Shen et al. (2025/2026):</strong> Mapping innovation ecosystem research: A scientometric review.</li>
            <li><span class="bullet-dot">▸</span> <strong>Machado, Faccin & Bittencourt (2025):</strong> Orchestration competence in innovation ecosystems.</li>
            <li><span class="bullet-dot">▸</span> <strong>Furr & Shipilov (2018):</strong> Building the Right Ecosystem for Innovation. MIT Sloan Management Review.</li>
            <li><span class="bullet-dot">▸</span> <strong>Majava & Rinkinen (2021):</strong> Twenty years, twenty studies: what can we learn from San Diego’s innovation ecosystem?</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-title">Clássicos & Prática Territorial</div>
          <ul class="bullet-list" style="font-size: 0.82rem; gap: 0.55rem;">
            <li><span class="bullet-dot">▸</span> <strong>Moore, J. F. (1993):</strong> Predators and Prey: A New Ecology of Competition. Harvard Business Review.</li>
            <li><span class="bullet-dot">▸</span> <strong>Etzkowitz & Leydesdorff (2000):</strong> The dynamics of innovation: from National Systems to a Triple Helix.</li>
            <li><span class="bullet-dot">▸</span> <strong>Carayannis & Campbell (2009/2012):</strong> 'Mode 3' knowledge production in quadruple and quintuple helices.</li>
            <li><span class="bullet-dot">▸</span> <strong>PIT São José dos Campos (2026):</strong> Relatórios Institucionais e Entrevista com Coord. de Inovação Luiz Fernando Carvalho.</li>
          </ul>
        </div>
      </div>
    </section>

  </main>

  <!-- Bottom Global Footer -->
  <footer class="deck-footer">
    <div class="footer-left">
      <div class="speaker-badge">
        <span>Apresentador:</span> <strong id="footer-speaker">Josué Jofre / Grupo 5</strong>
      </div>
      <div class="speaker-badge">
        <span>Bloco:</span> <strong id="footer-block">Abertura</strong>
      </div>
      <div class="speaker-badge">
        <span>Tempo:</span> <strong id="footer-time">2 min</strong>
      </div>
    </div>

    <div class="footer-center">
      <button class="nav-arrow-btn" onclick="prevSlide()" title="Slide Anterior (←)">‹</button>
      <div class="slide-progress-text" id="slide-num-indicator">1 / 29</div>
      <button class="nav-arrow-btn" onclick="nextSlide()" title="Próximo Slide (→)">›</button>
    </div>

    <div class="footer-right">
      <div style="font-size: 0.74rem; color: var(--text-dim); font-family: var(--font-mono);">
        PPG-PIT UNIFESP SJC • Profª Iraci & Prof. Yukio
      </div>
    </div>

    <div class="slide-progress-bar" id="slide-progress-bar" style="width: 3.44%;"></div>
  </footer>

  <!-- Speaker Notes Drawer (Toggled by N) -->
  <aside class="notes-drawer" id="notes-drawer">
    <div class="notes-header">
      <div class="notes-title">
        <span>📝</span> Notas do Orador • Slide <span id="notes-slide-num">1</span>
      </div>
      <button class="clock-btn" onclick="toggleNotesDrawer()">✕</button>
    </div>
    <div style="font-size: 0.78rem; color: var(--cyan-light); font-family: var(--font-mono);" id="notes-speaker-name">
      Orador: Josué Jofre / Grupo 5 (Tempo: 2 min)
    </div>
    <div class="notes-body" id="notes-content">
      Carregando notas...
    </div>
  </aside>

  <!-- Slide Grid Modal (Toggled by G) -->
  <div class="grid-modal" id="grid-modal">
    <div class="grid-modal-header">
      <div style="font-family: var(--font-display); font-size: 1.4rem; font-weight: 800; color: #fff;">
        Panorâmica de Todos os 29 Slides
      </div>
      <button class="deck-btn" onclick="toggleGridModal()">✕ Fechar (G)</button>
    </div>
    <div class="thumbs-container" id="thumbs-container"></div>
  </div>

  <script>
    /* Presentation Controller Script */
    const TOTAL_SLIDES = 29;
    let currentSlide = 1;

    // Load speaker notes from roteiro
    const speakerNotes = {
      1: "Boa noite a todos os colegas, professores Iraci e Yukio. Sejam muito bem-vindos ao Seminário 5 da disciplina Gestão Estratégica da Tecnologia e Inovação. Hoje nós vamos mergulhar em um dos temas mais decisivos da gestão contemporânea: os Ecossistemas de Inovação.\\n\\nAo longo das últimas décadas, ficou claro que a era do gênio solitário ou do laboratório fechado que inventa tudo internamente acabou. As inovações mais complexas da humanidade — da vacina de RNA à indústria aeroespacial de ponta aqui do Vale do Paraíba — só nascem porque múltiplos atores decidem cooperar em rede.\\n\\nNosso objetivo hoje não é apenas apresentar a literatura acadêmica mais recente, como os estudos de Shen et al., Machado, Faccin & Bittencourt, Furr & Shipilov e a revisão de 20 anos de San Diego por Majava & Rinkinen. Nós vamos confrontar essa teoria com a realidade viva do Parque de Inovação Tecnológica de São José dos Campos, onde realizamos uma entrevista exclusiva com a liderança do PIT, e com a nossa própria universidade, a UNIFESP. E o mais empolgante: após cada bloco, vocês participarão de um jogo interativo no celular, testando seus conhecimentos em tempo real com premiação para o orquestrador mais veloz e preciso da sala. Vamos em frente!",
      2: "Para estruturar nossa jornada de 2 horas, dividimos a apresentação em 6 blocos teóricos e 2 momentos práticos imersivos:\\n- No Bloco 1, veremos o conceito e a evolução da metáfora ecológica com a Nathalia e o Fernando;\\n- No Bloco 2, a anatomia e os atores interdependentes com a Veridiany e o Fábio;\\n- No Bloco 3, a governança e os desafios de orquestrar atores autônomos com a Jéssica;\\n- No Bloco 4, estratégias práticas para construir ecossistemas em ambientes de incerteza com o Josué e a Marciele;\\n- No Bloco 5, a Lilian nos levará a um benchmarking internacional com o caso histórico de San Diego;\\n- Em seguida, traremos o caso concreto do PIT SJC e a entrevista exclusiva gravada pelo Renato com o coordenador de inovação do Parque, Luiz Fernando Carvalho;\\n- No Bloco 6, o Renato analisará os gargalos, limitações e o 'dark side' dos ecossistemas;\\n- E fecharemos com a revelação do campeão do nosso Kahoot RPG e uma rica roda de conversa. Fiquem atentos aos seus celulares, pois o game abre logo após cada bloco!",
      3: "Por que escolhemos o PIT SJC como fio condutor deste seminário? Porque nós temos o privilégio de estar fisicamente inseridos no primeiro Parque Tecnológico do Estado de São Paulo, criado em 2006, em um território que abriga a Embraer, o DCTA, o ITA, o INPE e este campus da UNIFESP.\\n\\nSão mais de 300 empresas vinculadas, 4 APLs prioritários — Aeroespacial, TIC, Saúde e Segurança —, centros de desenvolvimento tecnológico e o Nexus, que é o hub de aceleração e incubação. O PIT não é apenas um condomínio de galpões industriais; ele é um orquestrador ativo que mobiliza ciência para transformá-la em PIB e soberania nacional. Cada teoria que discutiremos hoje pode ser vista funcionando — com seus sucessos e seus atritos — do outro lado da nossa janela.",
      4: "Iniciamos o Bloco 1 com uma pergunta instigante: de onde veio o termo 'ecossistema'? Na década de 1930, o botânico Arthur Tansley cunhou a palavra na biologia para descrever uma comunidade de organismos vivos interagindo entre si e com os elementos físicos do meio ambiente.\\n\\nEm 1993, James Moore escreveu um artigo clássico na Harvard Business Review transpondo esse raciocínio para os negócios: as empresas não competem como ilhas isoladas; elas pertencem a uma teia ecológica onde clientes, fornecedores, concorrentes e reguladores coevoluem em torno de uma capacidade inovadora compartilhada. A metáfora é perfeita: assim como uma floresta precisa de solo fértil, chuva e simbiose entre espécies para não virar deserto, um polo tecnológico precisa de capital humano, pesquisa e fluidez regulatória para não definhar.",
      5: "Para entender a solidez desse campo, analisamos a revisão cienciométrica recente de Shen et al. Os autores mapearam as publicações globais sobre ecossistemas de inovação e demonstraram um crescimento exponencial a partir de meados dos anos 2010.\\n\\nA literatura se divide em três grandes ondas temáticas:\\n1ª Onda: Foco nas empresas líderes e plataformas digitais — como Apple, Google e Amazon criam plataformas onde parceiros plugam seus aplicativos;\\n2ª Onda: Foco na dimensão territorial e regional — parques tecnológicos, cidades inteligentes e clusters;\\n3ª Onda (Atual): Foco em governança, sustentabilidade socioambiental e a transição da Tríplice para a Quíntupla Hélice.\\nShen et al. alertam, contudo, que essa popularidade gerou um risco: a perda de rigor conceitual quando tudo passa a ser rotulado como ecossistema.",
      6: "Este slide é fundamental para não errarmos na prova ou na redação de artigos:\\n- Um CLUSTER (como ensinava Porter) é uma concentração puramente geográfica de empresas de um mesmo setor que ganham eficiência de custo pela proximidade;\\n- Um SISTEMA DE INOVAÇÃO (Nelson e Lundvall) foca na infraestrutura institucional e legal do Estado (leis de incentivo, agências de fomento, ministérios);\\n- Um ECOSSISTEMA DE NEGÓCIOS foca em capturar valor econômico e lucros no mercado presente;\\n- Já o ECOSSISTEMA DE INOVAÇÃO é definido pela interdependência voltada para a CO-CRIAÇÃO de novidades tecnológicas e conhecimento inédito.\\nGuardem bem essa distinção! E atenção, turma: neste momento, o aplicativo de vocês acaba de liberar a FASE 1 do nosso Kahoot RPG! Vocês têm 60 segundos para abrir o celular e responder às 3 primeiras perguntas!",
      7: "Entrando no Bloco 2, com base no artigo de Machado, Faccin & Bittencourt, dissecamos a anatomia interna do ecossistema. Quem são esses atores?\\nEles são profundamente heterogêneos: universidades com vocação para pesquisa básica de longo prazo; grandes corporações focadas em escala e eficiência; startups ágeis dispostas a assumir riscos radicais; investidores de risco; prestadores de serviços de propriedade intelectual; e órgãos públicos.\\n\\nNenhum desses atores possui sozinho todas as peças do quebra-cabeça. A relação entre eles não é uma linha de montagem hierárquica, mas uma simbiose interdependente: a universidade precisa do canal de mercado da indústria, e a indústria precisa da densidade científica da universidade para não ficar obsoleta.",
      8: "A governança dos ecossistemas evoluiu teoricamente através das hélices:\\n- Começamos com a TRÍPLICE HÉLICE de Etzkowitz e Leydesdorff: Governo como indutor de políticas, Universidade gerando ciência e Empresa gerando produto;\\n- Com o tempo, percebeu-se que a tecnologia muitas vezes era rejeitada pela população ou não atendia aos problemas reais. Surgiu a QUÁDRUPLA HÉLICE, incorporando a Sociedade Civil, os cidadãos e as comunidades como co-criadores e avaliadores sociais;\\n- E hoje chegamos à QUÍNTUPLA HÉLICE de Carayannis, que insere o Meio Ambiente Natural e a urgência da sustentabilidade (ESG, transição energética e descarbonização) como a quinta força motriz. O PIT SJC, por exemplo, ao abraçar projetos de biocombustíveis de aviação (SAF), atua em plena Quíntupla Hélice.",
      9: "Como o valor é co-criado em rede? Machado et al. demonstram que a co-criação depende de três fluxos vitais contínuos:\\n1. Fluxo de Recursos: infraestrutura laboratorial compartilhada, equipamentos caros que uma única startup jamais poderia comprar;\\n2. Fluxo de Conhecimento: circulação de teses, patentes e publicações de forma aberta e fluida;\\n3. Fluxo de Pessoas: mestres e doutores da universidade fundando spin-offs ou atuando em P&D de empresas instaladas.\\nO grande desafio é garantir que o valor gerado não seja engolido exclusivamente pelo parceiro mais forte, mas distribuído de forma justa entre pesquisadores, investidores e a sociedade.\\nAtenção sala: a FASE 2 do nosso Kahoot RPG está liberada! Abram o celular e respondam às 3 questões sobre Anatomia do Ecossistema!",
      10: "Chegamos ao Bloco 3, o coração conceitual do seminário: Governança e Orquestração. Em uma empresa comum, o presidente manda e os funcionários obedecem. Mas em um ecossistema, o reitor da universidade, o CEO da Embraer e o prefeito da cidade são figuras juridicamente autônomas. Ninguém tem o direito de demitir ninguém!\\n\\nComo coordenar atores com culturas, tempos e interesses tão divergentes? A universidade pensa em ciclos de 4 anos de doutorado; a startup precisa fechar o mês; a corporação foca no balanço trimestral. É aqui que nasce a figura do ORQUESTRADOR: uma organização ou liderança que atua como regente de uma orquestra, garantindo harmonia através de credibilidade, legitimidade e facilitação, e não pela força hierárquica.",
      11: "O modelo de Machado, Faccin e Bittencourt sintetiza a orquestração em 5 dimensões estratégicas obrigatórias:\\n1. Mobilização de Atores: atrair os melhores talentos e players estratégicos para a rede;\\n2. Definição de Agenda: construir uma visão de futuro compartilhada para que todos remem na mesma direção;\\n3. Mobilidade do Conhecimento: destravar canais para que a ciência não fique presa em gavetas acadêmicas;\\n4. Estabilidade da Rede: gerenciar conflitos internos e criar contratos de convivência transparentes;\\n5. Apropriabilidade de Valor: garantir que quem arriscou tempo e capital seja devidamente recompensado quando a inovação tiver sucesso comercial.\\nSem essas cinco dimensões orquestradas, a rede se dissolve em frustração e desconfiança.",
      12: "Quais competências uma instituição como o Parque Tecnológico precisa desenvolver para ser um orquestrador competente? Machado et al. identificam três competências primordiais:\\n- Competência de Articulação e Comunicação: habilidade de traduzir a linguagem acadêmica rigorosa para o vocabulário ágil dos negócios;\\n- Competência de Arbitragem e Confiança: capacidade de atuar como terceiro neutro em disputas de patentes e royalties;\\n- Competência de Visão Sistêmica: enxergar tendências globais antes dos atores individuais e preparar o ecossistema com antecedência.\\nLiderar ecossistemas não é uma questão de poder financeiro, mas de inteligência relacional.\\nSala, muita atenção ao placar: a FASE 3 do RPG sobre Governança e Orquestração está liberada no smartphone de todos! Quem responder primeiro e correto escala o ranking!",
      13: "No Bloco 4, trazemos o olhar gerencial de ponta publicado no MIT Sloan Management Review por Nathan Furr e Andrew Shipilov. Há um mito perigoso de que ecossistemas de inovação brotam magicamente do solo como cogumelos após a chuva.\\n\\nFurr e Shipilov provam o contrário: os ecossistemas mais bem-sucedidos do planeta foram intencionalmente desenhados e cultivados. Contudo, a forma de geri-los muda drasticamente dependendo do nível de incerteza da tecnologia. Se o desafio é conhecido e previsível, o modelo gerencial é um; se estamos pisando em terreno inexplorado e incerto, o modelo de gestão deve ser completamente adaptativo e aberto à experimentação.",
      14: "Observem com atenção a comparação feita por Furr & Shipilov:\\n- Em um ECOSSISTEMA CENTRALIZADO (ou 'Hub-and-Spoke'), a empresa âncora já sabe exatamente o que precisa produzir. Ela estabelece padrões técnicos rígidos e os parceiros apenas executam subpartes pré-definidas;\\n- Em contrapartida, em um ECOSSISTEMA ADAPTATIVO — indispensável em tecnologias emergentes como Inteligência Artificial e Biotecnologia —, ninguém sabe de antemão qual será a solução final vencedora. O orquestrador não tenta adivinhar o futuro sozinho; ele convoca múltiplos parceiros, lança desafios abertos, testa protótipos rápidos e deixa que o aprendizado conjunto selecione a trajetória tecnológica.\\nQuem tenta gerenciar incerteza radical com regras centralizadas rígidas está fadado ao fracasso.",
      15: "Furr e Shipilov introduzem dois conceitos vitais para os gestores de tecnologia:\\nPrimeiro: a busca por PARCEIROS NÃO CONVENCIONAIS. Se uma empresa aeroespacial só conversar com fornecedores tradicionais de metal e turbinas, ela terá apenas inovações incrementais. Se ela conversar com a indústria de videogames para simuladores imersivos ou com startups médicas para monitoramento biométrico de pilotos, ela abre novos oceanos azuis.\\nSegundo: a COOPETIÇÃO. Cooperar no desenvolvimento da infraestrutura de base enquanto se compete ferozmente na ponta final de vendas para os clientes.\\nTurma, o jogo continua quente! A FASE 4 do Kahoot RPG sobre Gestão de Ecossistemas está desbloqueada agora nos seus aparelhos!",
      16: "No Bloco 5, realizamos um benchmarking internacional clássico: o caso de San Diego, na Califórnia, analisado por Majava & Rinkinen a partir de 20 anos e 20 estudos acadêmicos.\\n\\nAté os anos 1960, San Diego era conhecida basicamente por sua base aeronaval da Marinha dos EUA e pelo clima litorâneo agradável. Como essa cidade se transformou em um dos maiores polos mundiais de genômica, biotecnologia e telecomunicações (sendo o berço da Qualcomm e da Illumina)?\\nA resposta está na criação deliberada de uma universidade de classe mundial com foco exclusivo em pesquisa e pós-graduação — a UCSD —, ao lado de centros de pesquisa biomédica de elite como o Salk Institute e o Scripps. A ciência de ponta serviu como um poderoso magneto para atrair os maiores cientistas do globo.",
      17: "Majava e Rinkinen destacam o papel transformador de uma organização intermediária chamada CONNECT, criada em 1985 dentro da própria universidade. A CONNECT percebeu que os cientistas entendiam tudo de biologia celular, mas não sabiam fazer um plano de negócios ou conversar com um investidor de risco.\\n\\nAtravés do famoso programa Springboard, a CONNECT convocou executivos aposentados da indústria e advogados voluntários para mentorar gratuitamente os pesquisadores (cultura give-first), preparando as startups para receber Venture Capital. O resultado foi a criação de mais de 3.000 empresas e bilhões de dólares em valor adicionado à região. Esse modelo prova que o capital relacional e a mentoria voluntária são tão valiosos quanto o capital financeiro.\\nE agora, atenção: a FASE 5 do nosso RPG sobre o Caso San Diego está disponível! Corram para somar pontos antes que o tempo esgote!",
      18: "Ao olharmos para San Diego e voltarmos os olhos para o Vale do Paraíba, as semelhanças e particularidades saltam aos olhos. São José dos Campos teve sua vocação científica impulsionada pelo governo federal nos anos 1950 com a fundação do DCTA e do ITA pelo Marechal Casimiro Montenegro, o que gerou a Embraer em 1969.\\n\\nMas a fundação do PIT SJC em 2006 representou um salto estratégico de governança: o Parque foi concebido como uma Organização Social neutra, operando como o grande hub orquestrador regional. O PIT não produz aviões ou satélites diretamente; ele cria as condições de contorno — laboratórios de manufatura aditiva, centro de dados, ambientes regulatórios e rodadas de captação — para que as empresas do Vale prosperem em escala global.",
      19: "A anatomia do PIT é viva e integrada:\\n- Nós temos o HUB NEXUS, que apoia startups desde a ideação (Nexus Hub) até a escala e aceleração comercial;\\n- Temos quatro APLs maduros gerando compras públicas e consórcios industriais;\\n- Temos grandes âncoras corporativas e centros empresariais;\\n- E temos as Instituições de Ciência e Tecnologia (ICTs), com destaque absoluto para o Campus da UNIFESP.\\nO Programa de Pós-Graduação em Inovação Tecnológica (PPG-PIT) e esta disciplina de GETI exemplificam perfeitamente essa simbiose: nossas pesquisas e dissertações nascem conectadas às dores reais das indústrias e do território.",
      20: "Ao colocarmos San Diego e São José dos Campos lado a lado na matriz de benchmarking:\\n- Ambos têm na sua gênese fortes investimentos federais de Defesa e Aeroespacial;\\n- Ambos possuem universidades e centros de elite como âncoras indutoras (UCSD lá, ITA/UNIFESP/INPE aqui);\\n- Ambos contam com orquestradores intermediários dedicados (CONNECT lá, PIT/Nexus aqui).\\nOnde reside nossa grande oportunidade de evolução? Na maturidade dos fundos privados de Venture Capital e na cultura de desinvestimento (saída dos fundos via IPOs ou fusões), além da necessidade de consolidar ainda mais a cultura do 'give-first' entre nossos executivos industriais seniores.",
      21: "Para trazer a voz autêntica da prática, tivemos a honra de entrevistar com exclusividade o Coordenador de Inovação do PIT São José dos Campos, Luiz Fernando Carvalho.\\nNa conversa, perguntamos diretamente: 'Luiz, como você equilibra o imediatismo comercial de uma multinacional com a burocracia e o rigor metodológico de uma universidade federal?'\\n\\nA resposta dele foi cirúrgica: 'O papel do orquestrador é ser o amortecedor de choques e o tradutor de dialetos. A universidade não pode se prostituir virando mero balcão de serviços rápidos de engenharia, nem a indústria pode esperar 5 anos sem ter marcos intermediários de entrega. Nós criamos projetos com entregáveis parciais que abastecem a empresa e, ao mesmo tempo, geram teses e patentes protegidas.' Essa declaração traduz com perfeição a dimensão de Estabilidade e Apropriabilidade de Machado et al.",
      22: "Sintetizamos a entrevista em quatro lições de ouro para qualquer gestor de inovação:\\n1. Alinhamento de Expectativas: o contrato deve prever desde o dia zero a propriedade dos dados e das patentes;\\n2. Construção de Confiança Relacional: reuniões periódicas transparentes valem mais do que 100 páginas de cláusulas punitivas;\\n3. Foco na Agilidade Regulatória: o Marco Legal de CTI (Lei 13.243/16) facilitou o uso de laboratórios públicos, mas exige segurança jurídica estrita;\\n4. Formação de Talentos Prontos: o maior patrimônio que o PIT busca na UNIFESP não são apenas fórmulas, mas mestres e doutores com visão de negócios e senso de urgência.",
      23: "Entrando no Bloco 6, com base no artigo crítico de Shen et al., fazemos o contraponto acadêmico rigoroso. Quais são as limitações da teoria de ecossistemas?\\nPrimeiro: A Delimitação de Fronteiras. Onde termina o ecossistema do PIT SJC? Ele engloba apenas Eugênio de Melo? Engloba a Região Metropolitana do Vale do Paraíba? Ou engloba parceiros em Munique e Seattle? Não há limites geográficos estanques.\\nSegundo: O Problema da Causalidade. Como provar estatisticamente que o crescimento econômico de uma empresa decorreu diretamente de sua presença no parque e não de fatores macroeconômicos globais? A mensuração científica rigorosa de impacto ainda é um desafio em aberto.",
      24: "Nem tudo são flores na literatura recente. Shen et al. e autores críticos alertam para o chamado 'Lado Sombrio' dos ecossistemas:\\n- Risco de Lock-in e Dependência Predatória: startups pequenas que desenvolvem tecnologia proprietária e acabam totalmente reféns de uma única grande multinacional que dita preços e restringe parcerias;\\n- Vazamento e Apropriação Indevida: pesquisadores acadêmicos que expõem ideias preliminares em hackathons e têm seus conceitos copiados sem a justa titularidade;\\n- O 'Teatro da Inovação': parques e secretarias municipais que promovem eventos festivos e tiram fotos bonitas, mas não geram nenhuma patente relevante ou emprego qualificado de longo prazo. O orquestrador tem a obrigação ética de combater essas armadilhas.\\nE agora, atenção máxima sala: a FASE 6 do nosso Kahoot RPG está liberada! É a última bateria de 3 perguntas que definirá o grande campeão da sala!",
      25: "Chegamos ao ápice da nossa dinâmica interativa! Ao longo das apresentações, vocês foram respondendo às fases liberadas pelo nosso painel de controle. Quem ainda não finalizou alguma fase, aponte a câmera para o QR Code projetado no slide para conferir suas respostas e fechar seu placar.\\n\\nNossa interface de administração registra não apenas se você acertou ou errou cada questão, mas também o tempo exato em milissegundos que você levou para deliberar. Esse sistema garante uma pontuação justa no melhor estilo Kahoot, valorizando a precisão científica e a velocidade de raciocínio estratégico.",
      26: "Vejam que fascinante: estamos projetando agora a nossa Interface Administrativa com os Gráficos de Pizza em tempo real de cada uma das 18 perguntas!\\nObservem, por exemplo, a pergunta sobre 'Ecossistema de Inovação vs Ecossistema de Negócios': 28% da turma escolheu a opção de que não há diferença conceitual. Isso ilustra com clareza a confusão apontada por Shen et al. entre criação coletiva de novo conhecimento e simples comercialização de produtos prontos!\\n\\nE agora, o momento mais esperado: vamos revelar o PÓDIO e acionar o botão de premiação!\\nEm 3º lugar: [Nome do Aluno 3]!\\nEm 2º lugar: [Nome do Aluno 2]!\\nE o grande vencedor, o Orquestrador Mestre do Seminário 5, com maior pontuação e melhor tempo de resposta é... [NOME DO ALUNO 1]! Parabéns! (Aplausos da sala).",
      27: "Para consolidar tudo o que aprendemos hoje, deixamos as 5 Leis Estratégicas dos Ecossistemas de Inovação:\\n1ª Lei: O valor sistêmico é relacional — a força da rede é multiplicada pela confiança mútua, não pelo capital isolado;\\n2ª Lei: Sem orquestração legítima, a entropia destrói a rede — atores autônomos precisam de alinhamento constante de agenda;\\n3ª Lei: Heterogeneidade radical gera disrupção — fuja do pensamento de rebanho e busque parceiros não convencionais;\\n4ª Lei: Justa apropriação garante sobrevivência — quem não compartilha os ganhos perde os parceiros mais talentosos;\\n5ª Lei: A ciência pública é o alicerce — universidades fortes como a UNIFESP são o solo onde a prosperidade econômica cria raízes sólidas.",
      28: "Gostaríamos de abrir agora o debate com os professores Iraci e Yukio e com todos os colegas da turma. Deixamos três provocações centrais no telão:\\n- Como evitar que as pesquisas acadêmicas da pós-graduação fiquem distantes dos problemas reais do Parque Tecnológico?\\n- Como proteger a propriedade intelectual dos alunos sem criar barreiras burocráticas intransponíveis para as empresas?\\n- O que o PIT SJC pode implementar imediatamente inspirado nas melhores práticas de San Diego?\\nEstamos prontos para ouvir suas contribuições e responder às dúvidas!",
      29: "Finalizamos apresentando as referências bibliográficas oficiais que embasaram cada slide, gráfico e pergunta deste seminário: Shen et al. (2025/2026), Machado, Faccin & Bittencourt (2025), Furr & Shipilov (2018), Majava & Rinkinen (2021), James Moore (1993) e as diretrizes do PIT São José dos Campos e PPG-PIT UNIFESP. Muito obrigado a todos pela atenção e participação entusiasmada no nosso Kahoot RPG!"
    };

    /* Real-Time Live Sync with Players (SyncService Cloud + BroadcastChannel Local) */
    let localLeaderboard = [];

    function updateLiveSlideSync() {
      const saved = localStorage.getItem('kahoot_rpg_state');
      if (!saved) return;
      try {
        const state = JSON.parse(saved);
        if (state.players) {
          localLeaderboard = Object.values(state.players);
          localLeaderboard.sort((a, b) => b.score - a.score);
        }
      } catch (e) {}

      refreshSlideWidgets();
    }

    if (window.SyncService) {
      window.SyncService.onAnswer(() => updateLiveSlideSync());
      window.SyncService.onStateUpdate((state) => {
        if (state && state.players) {
          localLeaderboard = Object.values(state.players);
          localLeaderboard.sort((a, b) => b.score - a.score);
        }
        refreshSlideWidgets();
      });
    }

    try {
      const channel = new BroadcastChannel('kahoot_rpg_channel');
      channel.onmessage = (e) => {
        if (e.data && (e.data.type === 'PLAYER_ANSWER' || e.data.type === 'STATE_UPDATE')) {
          updateLiveSlideSync();
        }
      };
    } catch (e) {}

    function refreshSlideWidgets() {
      const top1 = localLeaderboard[0];
      const count = localLeaderboard.length;

      const topText = top1 ? `🥇 ${top1.name} (${top1.score.toLocaleString()} pts)` : "Aguardando respostas...";
      const statusText = count > 0 ? `${count} jogadores online • ${topText}` : "Aguardando participantes...";

      // Update Slide 1
      const s1 = document.getElementById('ticker-status-s1');
      if (s1) s1.textContent = statusText;

      // Update checkpoint slides
      ['s6', 's9', 's12', 's15', 's17', 's24'].forEach(id => {
        const el = document.getElementById('ticker-top-' + id);
        if (el) el.textContent = topText;
      });

      // Update Slide 25 Top 3
      const s25Count = document.getElementById('slide25-active-count');
      const s25List = document.getElementById('slide25-top3-list');
      if (s25Count) s25Count.textContent = `${count} jogadores ativos`;
      if (s25List && localLeaderboard.length > 0) {
        s25List.innerHTML = localLeaderboard.slice(0, 3).map((p, i) => {
          const medal = i === 0 ? "🥇" : i === 1 ? "🥈" : "🥉";
          return `<div>${medal} <strong>${p.name}</strong> (${p.turma}) — <span style="color:var(--cyan-light);">${p.score.toLocaleString()} pts</span></div>`;
        }).join('');
      }

      // Update Slide 26 Table and Winner
      const s26Table = document.getElementById('slide26-table-body');
      const s26Winner = document.getElementById('slide26-winner-name');
      const s26Score = document.getElementById('slide26-winner-score');

      if (s26Winner && top1) {
        s26Winner.textContent = top1.name;
        s26Score.textContent = `${top1.score.toLocaleString()} pts • ${top1.correctCount} / 18 acertos (${top1.turma})`;
      }

      if (s26Table && localLeaderboard.length > 0) {
        s26Table.innerHTML = localLeaderboard.slice(0, 6).map((p, i) => {
          const rank = i + 1;
          const medal = rank === 1 ? "🥇" : rank === 2 ? "🥈" : rank === 3 ? "🥉" : rank;
          return `<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
            <td style="padding: 0.35rem 0.2rem; font-weight:800;">${medal}</td>
            <td style="color:#fff;"><strong>${p.name}</strong></td>
            <td style="color:var(--cyan-light);">${p.turma}</td>
            <td style="color:var(--cyan-glow);">${p.score.toLocaleString()}</td>
            <td>${p.correctCount}/18</td>
          </tr>`;
        }).join('');
      }
    }

    function celebrateOnSlide() {
      if (typeof confetti === 'function') {
        confetti({ particleCount: 150, spread: 100, origin: { y: 0.6 } });
      }
    }

    /* Navigation Controls */
    function goToSlide(num) {
      if (num < 1) num = 1;
      if (num > TOTAL_SLIDES) num = TOTAL_SLIDES;
      currentSlide = num;

      document.querySelectorAll('.slide').forEach(s => s.classList.remove('active'));
      const activeSlide = document.querySelector(`.slide[data-slide="${num}"]`);
      if (activeSlide) {
        activeSlide.classList.add('active');
        activeSlide.scrollTop = 0;

        document.getElementById('footer-speaker').textContent = activeSlide.dataset.speaker || "Grupo 5";
        document.getElementById('footer-block').textContent = activeSlide.dataset.block || "Geral";
        document.getElementById('footer-time').textContent = activeSlide.dataset.time || "5 min";
      }

      document.getElementById('slide-num-indicator').textContent = `${num} / ${TOTAL_SLIDES}`;
      const pct = (num / TOTAL_SLIDES) * 100;
      document.getElementById('slide-progress-bar').style.width = `${pct}%`;

      document.getElementById('notes-slide-num').textContent = num;
      if (activeSlide) {
        document.getElementById('notes-speaker-name').textContent = `Orador: ${activeSlide.dataset.speaker} (Tempo: ${activeSlide.dataset.time})`;
      }
      document.getElementById('notes-content').textContent = speakerNotes[num] || "Sem notas cadastradas.";

      document.querySelectorAll('.slide-thumb').forEach(t => {
        t.classList.toggle('active', parseInt(t.dataset.slide) === num);
      });

      refreshSlideWidgets();
    }

    function nextSlide() { goToSlide(currentSlide + 1); }
    function prevSlide() { goToSlide(currentSlide - 1); }

    window.addEventListener('keydown', (e) => {
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;

      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {
        e.preventDefault();
        nextSlide();
      } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
        e.preventDefault();
        prevSlide();
      } else if (e.key === 'Home') {
        e.preventDefault();
        goToSlide(1);
      } else if (e.key === 'End') {
        e.preventDefault();
        goToSlide(TOTAL_SLIDES);
      } else if (e.key === 'n' || e.key === 'N') {
        toggleNotesDrawer();
      } else if (e.key === 'g' || e.key === 'G') {
        toggleGridModal();
      } else if (e.key === 'f' || e.key === 'F') {
        toggleFullscreen();
      } else if (e.key === 'Escape') {
        closeAllModals();
      }
    });

    function toggleNotesDrawer() {
      const drawer = document.getElementById('notes-drawer');
      const btn = document.getElementById('btn-notes');
      drawer.classList.toggle('open');
      btn.classList.toggle('active', drawer.classList.contains('open'));
    }

    function toggleGridModal() {
      const modal = document.getElementById('grid-modal');
      modal.classList.toggle('open');
    }

    function closeAllModals() {
      document.getElementById('notes-drawer').classList.remove('open');
      document.getElementById('btn-notes').classList.remove('active');
      document.getElementById('grid-modal').classList.remove('open');
    }

    function toggleFullscreen() {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(() => {});
      } else {
        document.exitFullscreen().catch(() => {});
      }
    }

    function buildThumbs() {
      const container = document.getElementById('thumbs-container');
      container.innerHTML = '';
      document.querySelectorAll('.slide').forEach(s => {
        const num = parseInt(s.dataset.slide);
        const titleEl = s.querySelector('.slide-title');
        const titleText = titleEl ? titleEl.textContent : `Slide ${num}`;
        const speaker = s.dataset.speaker || '';

        const thumb = document.createElement('div');
        thumb.className = `slide-thumb ${num === currentSlide ? 'active' : ''}`;
        thumb.dataset.slide = num;
        thumb.innerHTML = `
          <div class="thumb-num">Slide ${num}</div>
          <div class="thumb-title">${titleText}</div>
          <div class="thumb-speaker">👤 ${speaker}</div>
        `;
        thumb.onclick = () => {
          goToSlide(num);
          toggleGridModal();
        };
        container.appendChild(thumb);
      });
    }

    // Master 120-minute Clock
    let clockSeconds = 120 * 60;
    let clockRunning = false;
    let clockInterval = null;

    function toggleClock() {
      const btn = document.getElementById('clock-btn');
      const dot = document.getElementById('clock-dot');
      if (!clockRunning) {
        clockRunning = true;
        btn.textContent = '⏸';
        dot.style.background = 'var(--emerald-accent)';
        clockInterval = setInterval(() => {
          if (clockSeconds > 0) {
            clockSeconds--;
            updateClockDisplay();
          } else {
            clearInterval(clockInterval);
            clockRunning = false;
            btn.textContent = '▶';
            dot.style.background = 'var(--rose-accent)';
          }
        }, 1000);
      } else {
        clockRunning = false;
        clearInterval(clockInterval);
        btn.textContent = '▶';
        dot.style.background = 'var(--amber-accent)';
      }
    }

    function resetClock() {
      clockRunning = false;
      clearInterval(clockInterval);
      clockSeconds = 120 * 60;
      updateClockDisplay();
      document.getElementById('clock-btn').textContent = '▶';
      document.getElementById('clock-dot').style.background = 'var(--emerald-accent)';
    }

    function updateClockDisplay() {
      const m = Math.floor(clockSeconds / 60);
      const s = clockSeconds % 60;
      document.getElementById('clock-display').textContent = 
        `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
    }

    // Init
    window.addEventListener('DOMContentLoaded', () => {
      buildThumbs();
      goToSlide(1);
      updateLiveSlideSync();
      setInterval(updateLiveSlideSync, 1500);
    });
  </script>
</body>
</html>
'''

# Paths
dir_path = os.path.dirname(os.path.abspath(__file__))
index_path = os.path.join(dir_path, "index.html")
pres_path = os.path.join(dir_path, "apresentacao_seminario_ecossistema_pit.html")
gen_path = os.path.join(dir_path, "generate_deck.py")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(deck_code)

with open(pres_path, "w", encoding="utf-8") as f:
    f.write(deck_code)

with open(gen_path, "w", encoding="utf-8") as f:
    f.write(f'# -*- coding: utf-8 -*-\\nhtml_content = \'\'\'{deck_code}\'\'\'\\n\\nimport os\\noutput_path = os.path.join(os.path.dirname(__file__), "index.html")\\nwith open(output_path, "w", encoding="utf-8") as f:\\n    f.write(html_content)\\nprint("Deck generated successfully.")\\n')

print(f"Updated index.html ({os.path.getsize(index_path):,} bytes)")
print(f"Updated apresentacao_seminario_ecossistema_pit.html ({os.path.getsize(pres_path):,} bytes)")
print(f"Updated generate_deck.py ({os.path.getsize(gen_path):,} bytes)")
