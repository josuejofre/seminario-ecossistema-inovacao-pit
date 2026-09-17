# -*- coding: utf-8 -*-
"""
Generator for the 2-hour Seminar Presentation HTML:
"Ecossistema de Inovação: Teoria, Governança, Estudo de Caso Internacional (San Diego) 
 e Aplicação Prática no PIT São José dos Campos com Entrevista e Dinâmica Interativa"
"""

import os

html_content = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Seminário 5: Ecossistemas de Inovação | UNIFESP & PIT SJC</title>
  
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">

  <style>
    :root {
      --bg-space: #050a14;
      --bg-surface: #0a1324;
      --bg-card: rgba(15, 23, 42, 0.78);
      --bg-card-hover: rgba(30, 41, 59, 0.88);
      
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
      --border-soft: rgba(255, 255, 255, 0.08);
      --border-bright: rgba(6, 182, 212, 0.35);
      
      --shadow-glow: 0 0 35px rgba(6, 182, 212, 0.18);
      --shadow-card: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
      
      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 22px;
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
        radial-gradient(circle at 15% 20%, rgba(37, 99, 235, 0.12) 0%, transparent 45%),
        radial-gradient(circle at 85% 80%, rgba(139, 92, 246, 0.12) 0%, transparent 45%),
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
      height: 54px;
      background: rgba(10, 19, 36, 0.85);
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
      border: 1px solid rgba(6, 182, 212, 0.3);
      padding: 0.3rem 0.75rem;
      border-radius: 999px;
      font-size: 0.78rem;
      font-weight: 700;
      letter-spacing: 0.05em;
      color: var(--cyan-light);
      text-transform: uppercase;
    }

    .header-title {
      font-size: 0.88rem;
      font-weight: 600;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .header-title strong {
      color: #fff;
    }

    .header-center {
      display: flex;
      align-items: center;
      gap: 1.25rem;
    }

    /* Master Clock */
    .seminar-clock {
      display: flex;
      align-items: center;
      gap: 0.6rem;
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid var(--border-soft);
      padding: 0.3rem 0.85rem;
      border-radius: var(--radius-sm);
      font-family: var(--font-mono);
      font-size: 0.85rem;
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
      transition: color 0.2s;
    }

    .clock-btn:hover {
      color: var(--cyan-light);
    }

    .header-right {
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }

    .deck-btn {
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-soft);
      color: var(--text-main);
      padding: 0.4rem 0.75rem;
      border-radius: var(--radius-sm);
      font-size: 0.78rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .deck-btn:hover {
      background: rgba(6, 182, 212, 0.15);
      border-color: var(--border-bright);
      color: var(--cyan-light);
      transform: translateY(-1px);
    }

    .deck-btn.active {
      background: var(--blue-accent);
      border-color: var(--cyan-light);
      color: #fff;
    }

    /* Top Progress Bar */
    .progress-bar-container {
      width: 100%;
      height: 3px;
      background: rgba(255, 255, 255, 0.05);
      position: relative;
      z-index: 99;
    }

    .progress-bar-fill {
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, var(--blue-accent), var(--cyan-light), var(--purple-accent));
      transition: width 0.35s ease;
      box-shadow: 0 0 10px var(--cyan-glow);
    }

    /* Presentation Viewport */
    .deck-viewport {
      flex: 1;
      position: relative;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1.5rem 2.5rem;
    }

    /* Slide Container */
    .slide {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      padding: 2.2rem 3.5rem;
      display: flex;
      flex-direction: column;
      opacity: 0;
      pointer-events: none;
      transform: translateY(20px) scale(0.98);
      transition: opacity 0.4s cubic-bezier(0.16, 1, 0.3, 1), transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      overflow-y: auto;
    }

    .slide.active {
      opacity: 1;
      pointer-events: auto;
      transform: translateY(0) scale(1);
    }

    /* Slide Typography */
    .slide-tag {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      font-family: var(--font-mono);
      font-size: 0.78rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--cyan-light);
      margin-bottom: 0.6rem;
    }

    .slide-title {
      font-family: var(--font-display);
      font-size: 2.25rem;
      font-weight: 800;
      line-height: 1.15;
      letter-spacing: -0.02em;
      color: #ffffff;
      margin-bottom: 0.4rem;
    }

    .slide-title span {
      background: linear-gradient(135deg, var(--cyan-light) 0%, var(--blue-electric) 50%, var(--purple-accent) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .slide-subtitle {
      font-size: 1.05rem;
      color: var(--text-muted);
      max-width: 900px;
      line-height: 1.5;
      margin-bottom: 1.5rem;
    }

    /* Grid Layouts */
    .grid-2 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.75rem;
      align-items: center;
    }

    .grid-3 {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.5rem;
    }

    .grid-4 {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1.25rem;
    }

    /* Glass Cards */
    .card {
      background: var(--bg-card);
      border: 1px solid var(--border-soft);
      border-radius: var(--radius-md);
      padding: 1.5rem;
      backdrop-filter: blur(16px);
      box-shadow: var(--shadow-card);
      position: relative;
      overflow: hidden;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .card:hover {
      border-color: rgba(6, 182, 212, 0.4);
      transform: translateY(-3px);
      box-shadow: var(--shadow-glow);
    }

    .card-glow-cyan {
      border-left: 4px solid var(--cyan-glow);
    }

    .card-glow-purple {
      border-left: 4px solid var(--purple-accent);
    }

    .card-glow-emerald {
      border-left: 4px solid var(--emerald-accent);
    }

    .card-glow-amber {
      border-left: 4px solid var(--amber-accent);
    }

    .card-title {
      font-family: var(--font-display);
      font-size: 1.2rem;
      font-weight: 700;
      margin-bottom: 0.5rem;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .card-desc {
      font-size: 0.92rem;
      color: var(--text-muted);
      line-height: 1.55;
    }

    .card-meta-pill {
      display: inline-block;
      padding: 0.2rem 0.6rem;
      border-radius: 999px;
      font-size: 0.72rem;
      font-weight: 700;
      background: rgba(255, 255, 255, 0.06);
      color: var(--cyan-light);
      margin-top: 0.8rem;
    }

    /* Media Showcase */
    .media-frame {
      position: relative;
      border-radius: var(--radius-md);
      overflow: hidden;
      border: 1px solid var(--border-soft);
      box-shadow: var(--shadow-card);
      aspect-ratio: 16 / 9;
      background: #020617;
    }

    .media-frame img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.5s ease;
    }

    .media-frame:hover img {
      transform: scale(1.03);
    }

    .media-caption {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      padding: 0.75rem 1.25rem;
      background: linear-gradient(to top, rgba(2, 6, 23, 0.92) 0%, rgba(2, 6, 23, 0) 100%);
      font-size: 0.82rem;
      color: #cbd5e1;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    /* Hero Capa */
    .hero-capa {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      height: 100%;
      max-width: 1100px;
      margin: 0 auto;
    }

    .hero-meta-badges {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 0.75rem;
      margin-bottom: 1.5rem;
    }

    .hero-badge {
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-soft);
      padding: 0.45rem 1.1rem;
      border-radius: 999px;
      font-size: 0.82rem;
      font-weight: 600;
      color: #cbd5e1;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .hero-title {
      font-family: var(--font-display);
      font-size: 3.5rem;
      font-weight: 900;
      line-height: 1.08;
      letter-spacing: -0.03em;
      margin-bottom: 1.25rem;
      color: #fff;
    }

    .hero-title span {
      background: linear-gradient(135deg, #38bdf8 0%, #818cf8 50%, #c084fc 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .hero-desc {
      font-size: 1.2rem;
      color: var(--text-muted);
      line-height: 1.6;
      max-width: 850px;
      margin-bottom: 2.2rem;
    }

    .hero-footer-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.5rem;
      width: 100%;
      text-align: left;
    }

    /* Table / Matrix */
    .matrix-table {
      width: 100%;
      border-collapse: separate;
      border-spacing: 0;
      border-radius: var(--radius-md);
      overflow: hidden;
      border: 1px solid var(--border-soft);
      background: rgba(10, 19, 36, 0.6);
      font-size: 0.88rem;
    }

    .matrix-table th {
      background: rgba(15, 23, 42, 0.95);
      color: var(--cyan-light);
      font-family: var(--font-display);
      font-weight: 700;
      text-align: left;
      padding: 0.9rem 1.1rem;
      border-bottom: 1px solid var(--border-soft);
    }

    .matrix-table td {
      padding: 0.85rem 1.1rem;
      border-bottom: 1px solid rgba(255, 255, 255, 0.04);
      color: #cbd5e1;
      vertical-align: top;
    }

    .matrix-table tr:last-child td {
      border-bottom: none;
    }

    .matrix-table tr:hover td {
      background: rgba(255, 255, 255, 0.02);
    }

    /* Comparison Card */
    .compare-box {
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid var(--border-soft);
      border-radius: var(--radius-md);
      padding: 1.25rem;
      height: 100%;
      display: flex;
      flex-direction: column;
    }

    .compare-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--border-soft);
      padding-bottom: 0.75rem;
      margin-bottom: 0.9rem;
    }

    /* Interactive Simulator */
    .simulator-container {
      background: rgba(10, 19, 36, 0.85);
      border: 1px solid var(--border-bright);
      border-radius: var(--radius-lg);
      padding: 1.75rem;
      box-shadow: var(--shadow-glow);
    }

    .dilemma-tabs {
      display: flex;
      gap: 0.6rem;
      margin-bottom: 1.25rem;
    }

    .dilemma-btn {
      flex: 1;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-soft);
      color: var(--text-muted);
      padding: 0.65rem 1rem;
      border-radius: var(--radius-sm);
      font-size: 0.85rem;
      font-weight: 700;
      cursor: pointer;
      text-align: center;
      transition: all 0.2s;
    }

    .dilemma-btn.active {
      background: rgba(6, 182, 212, 0.15);
      border-color: var(--cyan-glow);
      color: #fff;
    }

    .dilemma-options {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
      margin: 1.25rem 0;
    }

    .option-card {
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid var(--border-soft);
      border-radius: var(--radius-md);
      padding: 1.15rem;
      cursor: pointer;
      transition: all 0.2s;
      position: relative;
    }

    .option-card:hover {
      border-color: var(--cyan-light);
      background: rgba(255, 255, 255, 0.03);
    }

    .option-card.selected {
      border-color: var(--emerald-accent);
      background: rgba(16, 185, 129, 0.08);
    }

    .metrics-gauges {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1rem;
      margin-top: 1.25rem;
      padding-top: 1.25rem;
      border-top: 1px solid var(--border-soft);
    }

    .gauge-card {
      background: rgba(0, 0, 0, 0.35);
      border-radius: var(--radius-sm);
      padding: 0.85rem;
      text-align: center;
    }

    .gauge-val {
      font-family: var(--font-mono);
      font-size: 1.5rem;
      font-weight: 800;
      color: var(--cyan-light);
      margin: 0.25rem 0;
    }

    /* Soundbite Player */
    .podcast-player {
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid var(--border-bright);
      border-radius: var(--radius-lg);
      padding: 1.5rem 2rem;
      display: flex;
      flex-direction: column;
      gap: 1.2rem;
    }

    .waveform {
      display: flex;
      align-items: center;
      gap: 3px;
      height: 36px;
      width: 100%;
    }

    .wave-bar {
      flex: 1;
      background: rgba(6, 182, 212, 0.3);
      border-radius: 999px;
      height: 20%;
      transition: height 0.2s ease;
    }

    .wave-bar.active {
      background: var(--cyan-light);
      animation: waveMove 1.2s infinite ease-in-out;
    }

    @keyframes waveMove {
      0%, 100% { height: 25%; }
      50% { height: 95%; }
    }

    /* Bottom Control Bar */
    .deck-footer {
      height: 58px;
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
      gap: 1rem;
      font-size: 0.82rem;
      color: var(--text-muted);
    }

    .slide-counter {
      font-family: var(--font-mono);
      font-weight: 700;
      color: #fff;
    }

    .block-indicator {
      display: flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.25rem 0.65rem;
      background: rgba(255, 255, 255, 0.05);
      border-radius: var(--radius-sm);
      font-size: 0.78rem;
    }

    .nav-controls {
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .nav-btn {
      width: 38px;
      height: 38px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-soft);
      background: rgba(255, 255, 255, 0.05);
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 1rem;
      transition: all 0.2s;
    }

    .nav-btn:hover {
      background: var(--blue-accent);
      border-color: var(--cyan-light);
      transform: scale(1.05);
    }

    /* Speaker Notes Drawer */
    .speaker-drawer {
      position: fixed;
      bottom: 58px;
      right: 0;
      width: 480px;
      max-height: 480px;
      background: rgba(8, 14, 28, 0.96);
      backdrop-filter: blur(20px);
      border-top: 1px solid var(--cyan-glow);
      border-left: 1px solid var(--cyan-glow);
      border-top-left-radius: var(--radius-lg);
      box-shadow: 0 -15px 40px rgba(0, 0, 0, 0.7);
      padding: 1.5rem;
      z-index: 200;
      display: flex;
      flex-direction: column;
      gap: 1rem;
      transform: translateY(120%);
      transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      overflow-y: auto;
    }

    .speaker-drawer.open {
      transform: translateY(0);
    }

    .speaker-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--border-soft);
      padding-bottom: 0.75rem;
    }

    .speaker-badge {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--cyan-light);
    }

    .speaker-content {
      font-size: 0.92rem;
      line-height: 1.6;
      color: #e2e8f0;
    }

    .speaker-content strong {
      color: var(--cyan-light);
    }

    .speaker-bullet-list {
      margin-left: 1.25rem;
      margin-top: 0.5rem;
      color: #cbd5e1;
    }

    /* Slide Grid Overview Modal */
    .grid-modal {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(5, 10, 20, 0.92);
      backdrop-filter: blur(18px);
      z-index: 300;
      display: none;
      flex-direction: column;
      padding: 2.5rem;
      overflow-y: auto;
    }

    .grid-modal.open {
      display: flex;
    }

    .grid-modal-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 2rem;
    }

    .slide-cards-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
      gap: 1.25rem;
    }

    .slide-thumbnail {
      background: var(--bg-card);
      border: 1px solid var(--border-soft);
      border-radius: var(--radius-md);
      padding: 1.1rem;
      cursor: pointer;
      transition: all 0.25s ease;
      position: relative;
    }

    .slide-thumbnail:hover {
      border-color: var(--cyan-light);
      transform: translateY(-4px);
      box-shadow: var(--shadow-glow);
    }

    .slide-thumbnail.active {
      border-color: var(--blue-accent);
      background: rgba(37, 99, 235, 0.18);
    }

    .thumb-num {
      font-family: var(--font-mono);
      font-size: 0.72rem;
      color: var(--cyan-light);
      font-weight: 700;
      margin-bottom: 0.35rem;
    }

    .thumb-title {
      font-family: var(--font-display);
      font-size: 0.92rem;
      font-weight: 700;
      color: #fff;
      line-height: 1.3;
    }

    .thumb-block {
      font-size: 0.72rem;
      color: var(--text-dim);
      margin-top: 0.5rem;
    }

    /* Key Shortcuts Help Pill */
    .shortcuts-hint {
      position: fixed;
      bottom: 68px;
      left: 1.5rem;
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid var(--border-soft);
      padding: 0.35rem 0.8rem;
      border-radius: 999px;
      font-size: 0.72rem;
      color: var(--text-dim);
      display: flex;
      align-items: center;
      gap: 0.5rem;
      pointer-events: none;
    }

    .kbd {
      background: rgba(255, 255, 255, 0.1);
      padding: 0.1rem 0.35rem;
      border-radius: 4px;
      font-family: var(--font-mono);
      color: #fff;
    }

    /* Print & Export styles */
    @media print {
      body {
        overflow: visible;
        background: #fff;
        color: #000;
      }
      .deck-header, .deck-footer, .speaker-drawer, .grid-modal, .shortcuts-hint {
        display: none !important;
      }
      .slide {
        position: relative !important;
        opacity: 1 !important;
        page-break-after: always;
        height: 100vh;
        transform: none !important;
      }
    }
  </style>
</head>
<body>

  <!-- Top Global Bar -->
  <header class="deck-header">
    <div class="header-left">
      <div class="brand-badge">
        <span>🚀</span> UNIFESP • GETI 2026
      </div>
      <div class="header-title">
        Seminário 5: <strong>Ecossistemas de Inovação & PIT SJC</strong>
      </div>
    </div>

    <div class="header-center">
      <!-- Master 120-minute Seminar Timer -->
      <div class="seminar-clock" id="clock-container" title="Cronômetro dos 120 minutos de apresentação">
        <span class="clock-dot"></span>
        <span id="clock-display">00:00 / 120:00</span>
        <button class="clock-btn" id="btn-toggle-clock" title="Iniciar/Pausar cronômetro">▶</button>
        <button class="clock-btn" id="btn-reset-clock" title="Zerar cronômetro">↺</button>
      </div>
    </div>

    <div class="header-right">
      <button class="deck-btn" id="btn-speaker-notes" title="Abrir notas do orador e falas sugeridas (Tecla N)">
        <span>🎙</span> Notas do Orador
      </button>
      <button class="deck-btn" id="btn-grid-view" title="Ver grade de todos os slides (Tecla G)">
        <span>⊞</span> Grade
      </button>
      <button class="deck-btn" id="btn-fullscreen" title="Modo Tela Cheia (Tecla F)">
        <span>⛶</span> Fullscreen
      </button>
    </div>
  </header>

  <!-- Progress Bar -->
  <div class="progress-bar-container">
    <div class="progress-bar-fill" id="deck-progress"></div>
  </div>

  <!-- Main Viewport -->
  <main class="deck-viewport" id="viewport">

    <!-- SLIDE 1: Capa Oficial -->
    <section class="slide active" data-slide="1" data-block="Abertura" data-speaker="Grupo Inteiro" data-time="3 min">
      <div class="hero-capa">
        <div class="hero-meta-badges">
          <span class="hero-badge">🎓 Mestrado / Doutorado Profissional UNIFESP</span>
          <span class="hero-badge">🏢 PIT • Parque de Inovação Tecnológica de São José dos Campos</span>
          <span class="hero-badge">⏱ Apresentação Executiva & Acadêmica (2 Horas)</span>
        </div>
        <h1 class="hero-title">
          Ecossistemas de Inovação:<br>
          <span>Teoria, Orquestração e a Prática no PIT SJC</span>
        </h1>
        <p class="hero-desc">
          Uma investigação profunda sobre as dinâmicas de colaboração, anatomia de atores, governança relacional, 
          benchmarking internacional com San Diego e a aplicação prática no polo aeroespacial e tecnológico de São José dos Campos.
        </p>

        <div class="hero-footer-grid">
          <div class="card card-glow-cyan">
            <div class="card-title" style="font-size: 1rem;">👥 Equipe do Seminário (Grupo 5)</div>
            <p style="font-size: 0.8rem; color: #cbd5e1; line-height: 1.45;">
              Josué Jofre • Renato Paschoal • Fernando Barreto • Fábio Lippi • Lilian Vinhas • Veridiany Braga • Nathália Neves • Jéssica David • Marciele Santos
            </p>
          </div>
          <div class="card card-glow-purple">
            <div class="card-title" style="font-size: 1rem;">👨‍🏫 Docentes Responsáveis</div>
            <p style="font-size: 0.8rem; color: #cbd5e1; line-height: 1.45;">
              <strong>Profª Drª Iraci de Souza João</strong><br>
              <strong>Prof. Dr. Antônio Yukio Ueta</strong><br>
              Gestão Estratégica da Tecnologia e Inovação (GETI)
            </p>
          </div>
          <div class="card card-glow-emerald">
            <div class="card-title" style="font-size: 1rem;">🎯 Metodologia da Apresentação</div>
            <p style="font-size: 0.8rem; color: #cbd5e1; line-height: 1.45;">
              6 Blocos Teórico-Empíricos • Entrevista Gravada com Liderança do PIT SJC • Dinâmica Interativa com Votação ao Vivo da Turma
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 2: Agenda e Distribuição de Tempo -->
    <section class="slide" data-slide="2" data-block="Agenda" data-speaker="Josué Jofre" data-time="5 min">
      <div class="slide-tag">📍 ROTEIRO ESTRATÉGICO DOS 120 MINUTOS</div>
      <h2 class="slide-title">Estrutura e <span>Cronograma da Apresentação</span></h2>
      <p class="slide-subtitle">
        Planejamento rigoroso conforme as diretrizes do programa: 6 blocos temáticos embasados nas referências seminais, seguidos da entrevista com gestor do PIT e da dinâmica de tomada de decisão.
      </p>

      <div class="grid-4" style="margin-bottom: 1.5rem;">
        <div class="card card-glow-cyan">
          <span style="font-size: 0.72rem; color: var(--cyan-light); font-weight: 700;">BLOCO 1 • 15 MIN</span>
          <div class="card-title" style="font-size: 1.05rem; margin-top: 0.3rem;">Conceito & Evolução</div>
          <p class="card-desc" style="font-size: 0.82rem;">Origem, definições, diferenças de redes/clusters e análise cienciométrica (Shen et al.).</p>
          <div class="card-meta-pill">Fernando Barreto</div>
        </div>
        <div class="card card-glow-cyan">
          <span style="font-size: 0.72rem; color: var(--cyan-light); font-weight: 700;">BLOCO 2 • 15 MIN</span>
          <div class="card-title" style="font-size: 1.05rem; margin-top: 0.3rem;">Anatomia & Atores</div>
          <p class="card-desc" style="font-size: 0.82rem;">Heterogeneidade, interdependência simbiótica e o modelo da Quádrupla Hélice (Machado et al.).</p>
          <div class="card-meta-pill">Fábio Lippi</div>
        </div>
        <div class="card card-glow-purple">
          <span style="font-size: 0.72rem; color: var(--purple-accent); font-weight: 700;">BLOCO 3 • 15 MIN</span>
          <div class="card-title" style="font-size: 1.05rem; margin-top: 0.3rem;">Governança & Orquestração</div>
          <p class="card-desc" style="font-size: 0.82rem;">Coordenação sem hierarquia, mobilização de agenda e competências dinâmicas do orquestrador.</p>
          <div class="card-meta-pill">Josué Jofre</div>
        </div>
        <div class="card card-glow-purple">
          <span style="font-size: 0.72rem; color: var(--purple-accent); font-weight: 700;">BLOCO 4 • 15 MIN</span>
          <div class="card-title" style="font-size: 1.05rem; margin-top: 0.3rem;">Construção & Gestão</div>
          <p class="card-desc" style="font-size: 0.82rem;">Ecossistemas centralizados vs adaptativos, parcerias não convencionais (Furr & Shipilov).</p>
          <div class="card-meta-pill">Veridiany / Lilian</div>
        </div>
      </div>

      <div class="grid-4">
        <div class="card card-glow-amber">
          <span style="font-size: 0.72rem; color: var(--amber-accent); font-weight: 700;">BLOCO 5 • 15 MIN</span>
          <div class="card-title" style="font-size: 1.05rem; margin-top: 0.3rem;">Caso San Diego</div>
          <p class="card-desc" style="font-size: 0.82rem;">20 anos de estudos: UCSD, CONNECT, venture capital e especialização regional (Majava & Rinkinen).</p>
          <div class="card-meta-pill">Nathália / Jéssica</div>
        </div>
        <div class="card card-glow-emerald">
          <span style="font-size: 0.72rem; color: var(--emerald-accent); font-weight: 700;">APLICAÇÃO PRÁTICA</span>
          <div class="card-title" style="font-size: 1.05rem; margin-top: 0.3rem;">O Caso PIT SJC</div>
          <p class="card-desc" style="font-size: 0.82rem;">O Parque Tecnológico de São José dos Campos como orquestrador vivo: Nexus, APLs e UNIFESP.</p>
          <div class="card-meta-pill">Josué / Marciele</div>
        </div>
        <div class="card card-glow-rose">
          <span style="font-size: 0.72rem; color: var(--rose-accent); font-weight: 700;">ATIVIDADE • 15 MIN</span>
          <div class="card-title" style="font-size: 1.05rem; margin-top: 0.3rem;">Entrevista Gravada</div>
          <p class="card-desc" style="font-size: 0.82rem;">Vídeo e análise de soundbites com gestor/orquestrador do PIT SJC confrontando teoria e prática.</p>
          <div class="card-meta-pill">Grupo Inteiro</div>
        </div>
        <div class="card card-glow-cyan">
          <span style="font-size: 0.72rem; color: var(--cyan-light); font-weight: 700;">BLOCO 6 + DINÂMICA • 30 MIN</span>
          <div class="card-title" style="font-size: 1.05rem; margin-top: 0.3rem;">Desafios & Dinâmica</div>
          <p class="card-desc" style="font-size: 0.82rem;">Limitações da teoria (Shen et al.) e simulação interativa: "O Dilema do Orquestrador do PIT".</p>
          <div class="card-meta-pill">Renato Paschoal & Grupo</div>
        </div>
      </div>
    </section>

    <!-- SLIDE 3: O Parque Tecnológico como Objeto de Estudo Vivo -->
    <section class="slide" data-slide="3" data-block="Contexto PIT" data-speaker="Josué Jofre" data-time="4 min">
      <div class="slide-tag">📍 CONTEXTO TERRITORIAL E APLICADO</div>
      <h2 class="slide-title">Por que o <span>PIT São José dos Campos?</span></h2>
      <p class="slide-subtitle">
        Estamos situados no coração do maior ecossistema aeroespacial, bélico e de alta densidade tecnológica da América Latina. O PIT não é apenas o local de aulas do nosso mestrado na UNIFESP — é o laboratório vivo ideal para testar toda a teoria de ecossistemas de inovação.
      </p>

      <div class="grid-2">
        <div class="media-frame">
          <img src="assets/pit_sjc_facade.jpg" alt="Fachada do PIT São José dos Campos" onerror="this.src='https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=1200&auto=format&fit=crop&q=80'">
          <div class="media-caption">
            <span><strong>Campus PIT São José dos Campos</strong> • Centro de Inovação & ICTs</span>
            <span>Foto Autoral / Acervo do Grupo</span>
          </div>
        </div>

        <div style="display: flex; flex-direction: column; gap: 1rem;">
          <div class="card card-glow-cyan">
            <div class="card-title">🏛 Primeiro Parque Credenciado de SP (SPTec)</div>
            <p class="card-desc">
              Mais de 188.000 m² de área construída, abrigando mais de 300 empresas associadas e residentes, centros de P&D corporativos (Embraer, Boeing, Ericsson, Nestlé) e instituições de ensino e pesquisa de ponta.
            </p>
          </div>
          <div class="card card-glow-purple">
            <div class="card-title">🔬 Densidade Única de Ciência e Defesa</div>
            <p class="card-desc">
              Convergência entre ITA, DCTA, INPE, UNIFESP, FATEC, Univap e o Centro de Competência EMBRAPII em Defesa e Espaço. Não é um ecossistema acidental: possui histórico deliberado de políticas públicas.
            </p>
          </div>
          <div class="card card-glow-emerald">
            <div class="card-title">🤝 O Papel da UNIFESP no Território</div>
            <p class="card-desc">
              A presença do Instituto de Ciência e Tecnologia (ICT-UNIFESP) dentro do complexo do PIT consolida a transferência de conhecimento biotecnológico, computacional e de materiais para a indústria.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 4: Bloco 1 - Origem e Evolução do Conceito -->
    <section class="slide" data-slide="4" data-block="Bloco 1" data-speaker="Fernando Barreto" data-time="5 min">
      <div class="slide-tag">📚 BLOCO 1 • FUNDAMENTOS TEÓRICOS</div>
      <h2 class="slide-title">A Origem e a <span>Metáfora Ecológica</span></h2>
      <p class="slide-subtitle">
        Como a teoria da estratégia empresarial migrou da visão competitiva tradicional (Porter, 1980) para a co-evolução sistêmica e a biologia organizacional.
      </p>

      <div class="grid-3">
        <div class="card card-glow-cyan">
          <div style="font-size: 2rem; margin-bottom: 0.5rem;">🌱</div>
          <div class="card-title">James F. Moore (1993, HBR)</div>
          <p class="card-desc">
            Primeiro a transpor a metáfora da ecologia para os negócios. Em <em>"Predators and Prey: A New Ecology of Competition"</em>, Moore defende que as empresas não pertencem a indústrias isoladas, mas a <strong>ecossistemas de negócios</strong> que co-evoluem em torno de uma inovação central.
          </p>
          <div class="card-meta-pill">Foco: Co-evolução & Sobrevivência Coletiva</div>
        </div>

        <div class="card card-glow-purple">
          <div style="font-size: 2rem; margin-bottom: 0.5rem;">⚙️</div>
          <div class="card-title">Ron Adner (2006, 2017)</div>
          <p class="card-desc">
            Define ecossistema de inovação como o <strong>"arranjo colaborativo no qual as empresas combinam suas ofertas individuais em uma solução coerente e voltada para o cliente"</strong>. Introduz os conceitos de <em>risco de co-inovação</em> e <em>risco de cadeia de adoção</em>.
          </p>
          <div class="card-meta-pill">Foco: Alinhamento de Proposta de Valor</div>
        </div>

        <div class="card card-glow-emerald">
          <div style="font-size: 2rem; margin-bottom: 0.5rem;">🌐</div>
          <div class="card-title">Granstrand & Holgersson (2020)</div>
          <p class="card-desc">
            Consolidam a definição contemporânea: <em>"Conjunto evolutivo de atores, atividades e artefatos, interligados por instituições e relações complementares e substitutas, que geram valor para atores ou clientes"</em>.
          </p>
          <div class="card-meta-pill">Foco: Artefatos & Instituições Híbridas</div>
        </div>
      </div>

      <div class="card" style="margin-top: 1.5rem; background: rgba(6, 182, 212, 0.06); border-color: rgba(6, 182, 212, 0.3);">
        <div style="display: flex; align-items: center; gap: 1rem;">
          <div style="font-size: 1.8rem;">💡</div>
          <div style="font-size: 0.95rem; color: #e2e8f0; line-height: 1.5;">
            <strong>A Virada Paradigmática:</strong> No modelo tradicional, a empresa busca obter vantagens competitivas exclusivas (RBV) e erguer barreiras de entrada. No ecossistema de inovação, a capacidade essencial é a <strong>interdependência</strong>: nenhuma organização isolada detém todas as peças necessárias para entregar a proposta de valor ao mercado final.
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 5: Bloco 1 - Mapeamento Cienciométrico (Shen et al.) -->
    <section class="slide" data-slide="5" data-block="Bloco 1" data-speaker="Fernando Barreto" data-time="5 min">
      <div class="slide-tag">📊 BLOCO 1 • REVISÃO DA LITERATURA</div>
      <h2 class="slide-title">Mapeamento Cienciométrico: <span>Shen et al. (2025/2026)</span></h2>
      <p class="slide-subtitle">
        Uma análise quantitativa e estrutural de quase duas décadas de produção científica sobre ecossistemas de inovação (2006 a 2023). O que a ciência global tem investigado?
      </p>

      <div class="grid-2">
        <div style="display: flex; flex-direction: column; gap: 1rem;">
          <div class="card card-glow-cyan">
            <div class="card-title">📈 Crescimento Exponencial das Publicações</div>
            <p class="card-desc">
              O estudo de Shen et al. demonstra uma explosão de publicações a partir de 2014, migrando de periódicos de gestão geral para revistas especializadas em tecnologia, política pública e transição ecológica (Technovation, R&D Management, Research Policy).
            </p>
          </div>
          <div class="card card-glow-purple">
            <div class="card-title">🗺️ Os 3 Grandes Clusters da Literatura</div>
            <p class="card-desc">
              <strong>1. Abordagem Baseada em Plataformas:</strong> Liderada por ecossistemas digitais (Apple, Google, Microsoft) e orquestração de APIs.<br>
              <strong>2. Abordagem Regional / Espacial:</strong> Foco em parques tecnológicos, distritos industriais e desenvolvimento regional.<br>
              <strong>3. Abordagem Estratégica do Orquestrador:</strong> Governança, co-criação e competências dinâmicas da firma focal.
            </p>
          </div>
          <div class="card card-glow-amber">
            <div class="card-title">⚠️ Lacuna Crítica Apontada por Shen et al.</div>
            <p class="card-desc">
              Poucos estudos investigam a <em>morte ou declínio</em> de ecossistemas (viés do sobrevivente), e faltam pesquisas empíricas profundas sobre ecossistemas em economias emergentes com forte presença estatal e militar (exatamente o caso do PIT SJC).
            </p>
          </div>
        </div>

        <div class="card" style="background: rgba(15, 23, 42, 0.9);">
          <div style="border-bottom: 1px solid var(--border-soft); padding-bottom: 0.75rem; margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: center;">
            <span style="font-weight: 700; color: var(--cyan-light); font-size: 0.9rem;">ANÁLISE DE CO-CITAÇÃO & PALAVRAS-CHAVE</span>
            <span class="hero-badge" style="padding: 0.2rem 0.6rem; font-size: 0.72rem;">Shen et al., 2025</span>
          </div>
          <div style="display: flex; flex-direction: column; gap: 0.85rem; font-size: 0.85rem;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span>"Orchestration / Hub Firm"</span>
              <div style="width: 55%; background: rgba(255,255,255,0.05); height: 8px; border-radius: 4px; overflow: hidden;">
                <div style="width: 88%; background: var(--cyan-light); height: 100%;"></div>
              </div>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span>"Platform Ecosystems & APIs"</span>
              <div style="width: 55%; background: rgba(255,255,255,0.05); height: 8px; border-radius: 4px; overflow: hidden;">
                <div style="width: 76%; background: var(--blue-electric); height: 100%;"></div>
              </div>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span>"Value Co-creation / Capture"</span>
              <div style="width: 55%; background: rgba(255,255,255,0.05); height: 8px; border-radius: 4px; overflow: hidden;">
                <div style="width: 71%; background: var(--purple-accent); height: 100%;"></div>
              </div>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span>"Regional Clusters & Parks"</span>
              <div style="width: 55%; background: rgba(255,255,255,0.05); height: 8px; border-radius: 4px; overflow: hidden;">
                <div style="width: 62%; background: var(--emerald-accent); height: 100%;"></div>
              </div>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span>"Sustainability & Circularity"</span>
              <div style="width: 55%; background: rgba(255,255,255,0.05); height: 8px; border-radius: 4px; overflow: hidden;">
                <div style="width: 44%; background: var(--amber-accent); height: 100%;"></div>
              </div>
            </div>
          </div>
          <div style="margin-top: 1.25rem; font-size: 0.78rem; color: var(--text-dim); line-height: 1.4;">
            * Gráfico de densidade temática compilado a partir dos mapas de acoplamento bibliográfico de Shen et al.
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 6: Bloco 1 - Desmistificando Conceitos Correlatos -->
    <section class="slide" data-slide="6" data-block="Bloco 1" data-speaker="Fernando Barreto" data-time="5 min">
      <div class="slide-tag">🔍 BLOCO 1 • CLARIFICAÇÃO EPISTEMOLÓGICA</div>
      <h2 class="slide-title">Diferenciação Conceitual: <span>Não Confunda os Termos!</span></h2>
      <p class="slide-subtitle">
        Uma das maiores armadilhas acadêmicas é tratar ecossistema como sinônimo de cluster, rede ou sistema nacional de inovação. Vamos demarcar as fronteiras com rigor:
      </p>

      <table class="matrix-table">
        <thead>
          <tr>
            <th>Conceito</th>
            <th>Origem Teórica</th>
            <th>Mecanismo Central</th>
            <th>Fronteiras</th>
            <th>Exemplo Comparativo</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong style="color: var(--cyan-light);">Ecossistema de Inovação</strong></td>
            <td>Moore (1993), Adner (2006), Shen et al.</td>
            <td><strong>Interdependência e co-criação</strong> em torno de uma proposta de valor comum; orquestração sem hierarquia.</td>
            <td>Definidas pelo alinhamento da proposta de valor (podem ser locais ou transfronteiriças).</td>
            <td><strong>O PIT SJC orquestrando ITA, Embraer e startups do Nexus para novos eVTOLs.</strong></td>
          </tr>
          <tr>
            <td><strong>Cluster Industrial</strong></td>
            <td>Michael Porter (1990)</td>
            <td><strong>Proximidade geográfica</strong> gerando economias externas de aglomeração e concorrência direta local.</td>
            <td>Geograficamente estritas e restritas a uma cadeia produtiva correlata.</td>
            <td>O polo calçadista de Franca ou o Vale dos Vinhedos.</td>
          </tr>
          <tr>
            <td><strong>Rede de Inovação (Network)</strong></td>
            <td>Powell (1990), Gulati (1998)</td>
            <td><strong>Laços relacionais</strong> e contratos entre nós bilaterais para troca de recursos e confiança.</td>
            <td>Definidas pela estrutura dos nós e laços contratuais.</td>
            <td>Aliança entre duas farmacêuticas para codesenvolver uma vacina específica.</td>
          </tr>
          <tr>
            <td><strong>Sistema Nacional/Regional (SNI/SRI)</strong></td>
            <td>Freeman (1987), Lundvall (1992)</td>
            <td><strong>Instituições públicas</strong>, leis, marco regulatório e infraestrutura de C,T&I do Estado.</td>
            <td>Político-administrativas (município, estado ou nação).</td>
            <td>O sistema legal de incentivos da Lei do Bem ou a FAPESP em SP.</td>
          </tr>
        </tbody>
      </table>

      <div style="margin-top: 1.25rem; display: flex; gap: 1rem; align-items: center; background: rgba(255,255,255,0.03); padding: 0.85rem 1.25rem; border-radius: var(--radius-sm); border-left: 3px solid var(--purple-accent);">
        <span style="font-size: 1.2rem;">📌</span>
        <span style="font-size: 0.86rem; color: #cbd5e1;">
          <strong>Síntese para o Seminário:</strong> O PIT SJC está fisicamente inserido em um <em>cluster aeronáutico</em> e regulado pelo <em>SNI/SRI paulista</em>, mas opera como um <strong>ecossistema de inovação</strong> quando orquestra ativamente atores heterogêneos para gerar inovações que nenhum ator conseguiria criar isoladamente.
        </span>
      </div>
    </section>

    <!-- SLIDE 7: Bloco 2 - Anatomia do Ecossistema (Machado et al.) -->
    <section class="slide" data-slide="7" data-block="Bloco 2" data-speaker="Fábio Lippi" data-time="5 min">
      <div class="slide-tag">🧩 BLOCO 2 • ANATOMIA E ATORES</div>
      <h2 class="slide-title">Anatomia do Ecossistema: <span>Heterogeneidade & Simbiose</span></h2>
      <p class="slide-subtitle">
        Com base no trabalho seminal de <strong>Machado, Faccin & Bittencourt (2025)</strong>: como atores com lógicas institucionais opostas conseguem coexistir e gerar valor complementar?
      </p>

      <div class="grid-3">
        <div class="card card-glow-cyan">
          <div class="card-title">🏢 Empresas Âncora & PMEs</div>
          <p class="card-desc">
            Grandes corporações (ex: Embraer, Avibras, Ericsson) que fornecem demandas tecnológicas desafiadoras, poder de compra e canais globais. Cercadas por uma densa camada de fornecedores e empresas de base tecnológica (EBTs).
          </p>
          <div class="card-meta-pill">Papel: Tração de Mercado & Escala</div>
        </div>

        <div class="card card-glow-purple">
          <div class="card-title">🎓 Academia & ICTs</div>
          <p class="card-desc">
            Universidades (UNIFESP, ITA, Univap) e centros públicos de P&D (INPE, DCTA, IEAv). Geradores de conhecimento fundamental, laboratórios multiusuários e formação de capital humano altamente qualificado.
          </p>
          <div class="card-meta-pill">Papel: Pesquisa Básica & Talentos</div>
        </div>

        <div class="card card-glow-emerald">
          <div class="card-title">🚀 Hubs & Startups (Nexus)</div>
          <p class="card-desc">
            Empreendedores ágeis que assumem riscos de incerteza radical. O Nexus Hub do PIT conecta programas de incubação, aceleração e scale-ups ao capital corporativo e venture capital.
          </p>
          <div class="card-meta-pill">Papel: Agilidade & Exploração Radical</div>
        </div>
      </div>

      <div class="grid-3" style="margin-top: 1.25rem;">
        <div class="card card-glow-amber">
          <div class="card-title">💰 Investidores & Fomento</div>
          <p class="card-desc">
            Redes de anjos, fundos de Venture Capital, Corporate Venture Capital (CVC) e agências de fomento estatal (FAPESP, FINEP, EMBRAPII, BNDES). Provêm oxigênio financeiro para as pontes de vale da morte.
          </p>
          <div class="card-meta-pill">Papel: Financiamento do Risco</div>
        </div>

        <div class="card card-glow-cyan">
          <div class="card-title">🏛️ Governo & Políticas Públicas</div>
          <p class="card-desc">
            Prefeitura de São José dos Campos, Governo do Estado de SP e Ministérios federais (MCTI, MDIC). Garantem infraestrutura, zoneamento urbano inteligente, incentivos fiscais e compras públicas estratégicas.
          </p>
          <div class="card-meta-pill">Papel: Estabilidade & Condições de Contorno</div>
        </div>

        <div class="card card-glow-rose">
          <div class="card-title">🎯 Intermediários & Orquestrador</div>
          <p class="card-desc">
            A entidade gestora (o próprio PIT). Atua como tradutor cultural entre a lentidão da burocracia acadêmica e a urgência do mercado corporativo, reduzindo custos de transação e atritos institucionais.
          </p>
          <div class="card-meta-pill">Papel: Cola Relacional & Coordenação</div>
        </div>
      </div>
    </section>

    <!-- SLIDE 8: Bloco 2 - Da Tríplice à Quádrupla Hélice -->
    <section class="slide" data-slide="8" data-block="Bloco 2" data-speaker="Fábio Lippi" data-time="5 min">
      <div class="slide-tag">🧬 BLOCO 2 • MODELOS DE HÉLICES</div>
      <h2 class="slide-title">Evolução das Hélices: <span>Tríplice, Quádrupla e Quíntupla</span></h2>
      <p class="slide-subtitle">
        A evolução conceitual de Etzkowitz & Leydesdorff (2000) até Carayannis & Campbell (2012): por que a relação Governo-Universidade-Empresa não é mais suficiente?
      </p>

      <div class="grid-2">
        <div class="card" style="background: rgba(10, 19, 36, 0.85);">
          <!-- Interactive SVG Diagram of Helices -->
          <svg viewBox="0 0 450 320" style="width: 100%; height: auto; display: block;">
            <defs>
              <linearGradient id="gBlue" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.8"/>
                <stop offset="100%" stop-color="#2563eb" stop-opacity="0.3"/>
              </linearGradient>
              <linearGradient id="gPurple" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#c084fc" stop-opacity="0.8"/>
                <stop offset="100%" stop-color="#7c3aed" stop-opacity="0.3"/>
              </linearGradient>
              <linearGradient id="gEmerald" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#34d399" stop-opacity="0.8"/>
                <stop offset="100%" stop-color="#059669" stop-opacity="0.3"/>
              </linearGradient>
              <linearGradient id="gAmber" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#fbbf24" stop-opacity="0.8"/>
                <stop offset="100%" stop-color="#d97706" stop-opacity="0.3"/>
              </linearGradient>
            </defs>

            <!-- Circles overlapping -->
            <circle cx="170" cy="120" r="95" fill="url(#gBlue)" stroke="#38bdf8" stroke-width="2" style="opacity: 0.65;"/>
            <circle cx="280" cy="120" r="95" fill="url(#gPurple)" stroke="#c084fc" stroke-width="2" style="opacity: 0.65;"/>
            <circle cx="225" cy="210" r="95" fill="url(#gEmerald)" stroke="#34d399" stroke-width="2" style="opacity: 0.65;"/>
            <!-- Outer Ring 4th & 5th Helix -->
            <circle cx="225" cy="160" r="145" fill="none" stroke="url(#gAmber)" stroke-dasharray="6,6" stroke-width="2"/>

            <!-- Labels -->
            <text x="125" y="100" fill="#fff" font-family="'Outfit', sans-serif" font-weight="700" font-size="14">ACADEMIA</text>
            <text x="120" y="118" fill="#94a3b8" font-size="10">UNIFESP • ITA • INPE</text>

            <text x="260" y="100" fill="#fff" font-family="'Outfit', sans-serif" font-weight="700" font-size="14">EMPRESAS</text>
            <text x="255" y="118" fill="#94a3b8" font-size="10">Embraer • Startups</text>

            <text x="190" y="255" fill="#fff" font-family="'Outfit', sans-serif" font-weight="700" font-size="14">GOVERNO</text>
            <text x="180" y="270" fill="#94a3b8" font-size="10">Prefeitura • FAPESP</text>

            <!-- Center intersection -->
            <rect x="185" y="135" width="80" height="40" rx="8" fill="#050a14" stroke="#06b6d4" stroke-width="2"/>
            <text x="200" y="152" fill="#06b6d4" font-family="'Outfit', sans-serif" font-weight="800" font-size="11">PIT SJC</text>
            <text x="192" y="166" fill="#cbd5e1" font-size="8">ORQUESTRADOR</text>

            <text x="225" y="20" text-anchor="middle" fill="#fbbf24" font-family="'Outfit', sans-serif" font-weight="700" font-size="11">4ª e 5ª HÉLICES: SOCIEDADE CIVIL & SUSTENTABILIDADE</text>
          </svg>
          <div style="font-size: 0.78rem; text-align: center; color: var(--text-dim); margin-top: 0.5rem;">
            Intersecção dinâmica das hélices convergindo na governança do PIT SJC
          </div>
        </div>

        <div style="display: flex; flex-direction: column; gap: 1rem;">
          <div class="card card-glow-cyan">
            <div class="card-title" style="font-size: 1.05rem;">1. Tríplice Hélice Tradicional (Etzkowitz)</div>
            <p class="card-desc">
              Relação linear focada em patentes, laboratórios conjuntos e parques de base universitária. Mostrou limitações ao ignorar o consumidor final e a legitimidade social.
            </p>
          </div>
          <div class="card card-glow-amber">
            <div class="card-title" style="font-size: 1.05rem;">2. Quádrupla Hélice (+ Sociedade & Usuários)</div>
            <p class="card-desc">
              Introduz os cidadãos, a cultura de inovação aberta, <em>living labs</em> e a validação de soluções em ambiente urbano real (ex: Cidades Inteligentes no PIT SJC).
            </p>
          </div>
          <div class="card card-glow-emerald">
            <div class="card-title" style="font-size: 1.05rem;">3. Quíntupla Hélice (+ Sustentabilidade & ESG)</div>
            <p class="card-desc">
              O ambiente natural torna-se condutor de inovação (descarbonização da aviação, combustíveis sustentáveis SAF na Embraer, créditos de carbono e transição energética).
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 9: Bloco 2 - Co-criação de Valor -->
    <section class="slide" data-slide="9" data-block="Bloco 2" data-speaker="Fábio Lippi" data-time="5 min">
      <div class="slide-tag">🔄 BLOCO 2 • VALOR COLETIVO</div>
      <h2 class="slide-title">Co-Criação de Valor: <span>Como o Valor Circula?</span></h2>
      <p class="slide-subtitle">
        Em ecossistemas de inovação, o valor não é gerado em uma esteira linear (cadeia de valor de Porter), mas em uma rede densa de feedback contínuo entre atores heterogêneos.
      </p>

      <div class="grid-3">
        <div class="card card-glow-cyan">
          <div class="card-title">1. Criação Coletiva de Valor</div>
          <p class="card-desc">
            Atores combinam competências complementares que não possuem internamente. Exemplo: a Embraer precisa de algoritmos de visão computacional da UNIFESP e sensores de compósitos de uma startup do Nexus.
          </p>
          <div class="card-meta-pill">Conceito: Superaditividade (1 + 1 > 2)</div>
        </div>

        <div class="card card-glow-purple">
          <div class="card-title">2. Spillover e Transbordamento</div>
          <p class="card-desc">
            O conhecimento não fica retido em silos. Talentos circulam, mestrandos do PIT fundam spin-offs, ex-engenheiros de multinacionais tornam-se mentores no Nexus, oxigenando toda a região.
          </p>
          <div class="card-meta-pill">Conceito: Mobilidade de Conhecimento</div>
        </div>

        <div class="card card-glow-amber">
          <div class="card-title">3. O Risco de Apropriação Desigual</div>
          <p class="card-desc">
            Quem fica com a maior fatia do valor criado? Se a grande corporação captura 90% do valor e a universidade ou a startup não recebem retorno sustentável, o ecossistema entra em colapso por desincentivo.
          </p>
          <div class="card-meta-pill">Conceito: Value Creation vs Value Capture</div>
        </div>
      </div>

      <div class="card" style="margin-top: 1.5rem; background: rgba(15, 23, 42, 0.75);">
        <div class="card-title" style="color: var(--cyan-light);">⚡ O Papel Regulador do Orquestrador na Divisão do Bolo</div>
        <p class="card-desc">
          Conforme demonstrado por Machado et al. (2025), o orquestrador deve atuar como fiador das regras de apropriação de valor (acordos prévios de PI, royalties compartilhados, patentes cotitulares), garantindo que os parceiros mais frágeis continuem motivados a cooperar.
        </p>
      </div>
    </section>

    <!-- SLIDE 10: Bloco 3 - Governança e Orquestração (Machado et al.) -->
    <section class="slide" data-slide="10" data-block="Bloco 3" data-speaker="Josué Jofre" data-time="5 min">
      <div class="slide-tag">⚖️ BLOCO 3 • GOVERNANÇA SEM HIERARQUIA</div>
      <h2 class="slide-title">Governança e Orquestração: <span>Quem Manda Quando Ninguém Pode Mandar?</span></h2>
      <p class="slide-subtitle">
        A pergunta central de Machado, Faccin & Bittencourt (2025): em uma rede de atores autônomos e soberanos, como evitar o caos e a inércia sem impor uma hierarquia de comando e controle?
      </p>

      <div class="grid-2">
        <div class="card card-glow-purple">
          <div class="card-title" style="font-size: 1.15rem;">🏢 O Modelo Tradicional da Firma (Williamson / Coase)</div>
          <p class="card-desc" style="margin-bottom: 0.85rem;">
            A teoria dos custos de transação previa apenas duas opções viáveis:
          </p>
          <ul style="margin-left: 1.25rem; font-size: 0.88rem; color: #cbd5e1; line-height: 1.6;">
            <li><strong>Mercado:</strong> Relações de compra e venda puras, guiadas por preço, sem cooperação de longo prazo.</li>
            <li><strong>Hierarquia:</strong> Aquisição e controle vertical da cadeia (a empresa compra os fornecedores para ter controle).</li>
          </ul>
          <div style="margin-top: 1rem; padding: 0.75rem; background: rgba(244, 63, 94, 0.1); border-left: 3px solid var(--rose-accent); font-size: 0.82rem; color: #fca5a5;">
            Incompatível com inovações complexas: nenhuma corporação pode comprar a UNIFESP, o ITA, a Prefeitura e dezenas de startups simultaneamente.
          </div>
        </div>

        <div class="card card-glow-cyan">
          <div class="card-title" style="font-size: 1.15rem;">🌐 A Orquestração de Ecossistemas (Dhanaraj & Parkhe / Machado)</div>
          <p class="card-desc" style="margin-bottom: 0.85rem;">
            Uma terceira via de coordenação baseada em <strong>autoridade moral, facilitação e competências dinâmicas</strong>:
          </p>
          <ul style="margin-left: 1.25rem; font-size: 0.88rem; color: #cbd5e1; line-height: 1.6;">
            <li><strong>Poder de Convocação (Convening Power):</strong> Capacidade de reunir rivais e atores distantes na mesma mesa.</li>
            <li><strong>Governança Híbrida:</strong> Combinação de acordos formais leves (MoUs, consórcios) com normas sociais de reciprocidade.</li>
            <li><strong>Alinhamento de Incentivos:</strong> Fazer com que cada ator veja vantagem clara em ceder parte de sua autonomia.</li>
          </ul>
        </div>
      </div>

      <div class="media-frame" style="margin-top: 1.5rem; aspect-ratio: 24 / 7;">
        <img src="assets/nexus_pit_hub.jpg" alt="Nexus Innovation Hub PIT SJC" onerror="this.src='https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=1200&auto=format&fit=crop&q=80'">
        <div class="media-caption">
          <span><strong>Nexus Innovation Hub (PIT SJC)</strong> • A materialização da orquestração: o espaço neutro de convergência de interesses</span>
          <span>Foto Autoral / Nexus Hub</span>
        </div>
      </div>
    </section>

    <!-- SLIDE 11: Bloco 3 - As 5 Dimensões Críticas da Orquestração -->
    <section class="slide" data-slide="11" data-block="Bloco 3" data-speaker="Josué Jofre" data-time="5 min">
      <div class="slide-tag">🎯 BLOCO 3 • MECANISMOS DE COORDENAÇÃO</div>
      <h2 class="slide-title">As 5 Dimensões da <span>Orquestração de Sucesso</span></h2>
      <p class="slide-subtitle">
        Sistematização dos mecanismos operacionais descritos por Dhanaraj & Parkhe (2006) e expandidos por Machado et al. (2025) para parques tecnológicos e ecossistemas:
      </p>

      <div class="grid-3">
        <div class="card card-glow-cyan">
          <div style="font-family: var(--font-mono); color: var(--cyan-light); font-weight: 700; font-size: 0.85rem;">01</div>
          <div class="card-title">Mobilidade de Conhecimento</div>
          <p class="card-desc">
            Garantir que os insights circulem sem vazamento indevido de segredos industriais. O orquestrador promove workshops, hackathons, fóruns técnicos e plataformas de dados abertos.
          </p>
        </div>

        <div class="card card-glow-purple">
          <div style="font-family: var(--font-mono); color: var(--purple-accent); font-weight: 700; font-size: 0.85rem;">02</div>
          <div class="card-title">Apropriabilidade da Inovação</div>
          <p class="card-desc">
            Segurança jurídica. O orquestrador estabelece matrizes padronizadas de Propriedade Intelectual (PI) que evitam litígios e incentivam empresas a investir sem medo de desapropriação.
          </p>
        </div>

        <div class="card card-glow-emerald">
          <div style="font-family: var(--font-mono); color: var(--emerald-accent); font-weight: 700; font-size: 0.85rem;">03</div>
          <div class="card-title">Estabilidade da Rede</div>
          <p class="card-desc">
            Evitar deserções em massa ou 'free-riders' (atores que se beneficiam dos conhecimentos da rede sem contribuir). Manter a confiança mútua e a reputação coletiva do polo.
          </p>
        </div>
      </div>

      <div class="grid-2" style="margin-top: 1.25rem;">
        <div class="card card-glow-amber">
          <div style="font-family: var(--font-mono); color: var(--amber-accent); font-weight: 700; font-size: 0.85rem;">04</div>
          <div class="card-title">Definição de Agenda Estratégica (Roadmapping)</div>
          <p class="card-desc">
            O orquestrador não deixa a evolução ao acaso: ele constrói 'roadmaps' tecnológicos compartilhados para 5 a 10 anos (ex: transição para propulsão híbrida e inteligência artificial aeroespacial no PIT).
          </p>
        </div>

        <div class="card card-glow-rose">
          <div style="font-family: var(--font-mono); color: var(--rose-accent); font-weight: 700; font-size: 0.85rem;">05</div>
          <div class="card-title">Resolução de Conflitos Culturais</div>
          <p class="card-desc">
            Mediação entre o tempo acadêmico (medido em semestres e publicações qualificadas) e o tempo corporativo (medido em trimestres fiscais e time-to-market). O PIT atua como intérprete bilíngue.
          </p>
        </div>
      </div>
    </section>

    <!-- SLIDE 12: Bloco 3 - Competências Dinâmicas do Orquestrador -->
    <section class="slide" data-slide="12" data-block="Bloco 3" data-speaker="Josué Jofre" data-time="5 min">
      <div class="slide-tag">🧠 BLOCO 3 • CAPACIDADES DO GESTOR</div>
      <h2 class="slide-title">Competências de Orquestração: <span>Machado et al. (2025)</span></h2>
      <p class="slide-subtitle">
        A entidade orquestradora (a equipe de gestão do Parque Tecnológico) precisa desenvolver um tripé singular de competências dinâmicas organizacionais:
      </p>

      <div class="grid-3">
        <div class="card card-glow-cyan">
          <div style="font-size: 2.2rem; margin-bottom: 0.4rem;">👁️</div>
          <div class="card-title">Competência Cognitiva</div>
          <p class="card-desc">
            Capacidade de <strong>enxergar o todo</strong> antes dos demais atores. Monitorar megatendências globais de tecnologia, identificar lacunas regulatórias e antecipar disrupções antes que o ecossistema se torne obsoleto.
          </p>
          <div class="card-meta-pill">Sensoriamento & Visão de Futuro</div>
        </div>

        <div class="card card-glow-purple">
          <div style="font-size: 2.2rem; margin-bottom: 0.4rem;">🤝</div>
          <div class="card-title">Competência Relacional</div>
          <p class="card-desc">
            Capacidade de <strong>construir pontes e costurar laços de confiança</strong> entre atores que historicamente desconfiam uns dos outros (pesquisadores acadêmicos, executivos céticos e burocratas estatais).
          </p>
          <div class="card-meta-pill">Capital Social & Negociação Empática</div>
        </div>

        <div class="card card-glow-emerald">
          <div style="font-size: 2.2rem; margin-bottom: 0.4rem;">🏗️</div>
          <div class="card-title">Competência Estrutural</div>
          <p class="card-desc">
            Capacidade de <strong>erguer e operar a infraestrutura material e imaterial</strong>: laboratórios compartilhados, prédios de incubação, conexões jurídicas, credenciamento em editais públicos e captação de fundos.
          </p>
          <div class="card-meta-pill">Execução & Governança Institucional</div>
        </div>
      </div>

      <div class="card" style="margin-top: 1.5rem; background: rgba(16, 185, 129, 0.06); border-color: rgba(16, 185, 129, 0.3);">
        <div style="display: flex; align-items: center; gap: 1rem;">
          <div style="font-size: 1.8rem;">🎯</div>
          <div style="font-size: 0.92rem; color: #e2e8f0; line-height: 1.5;">
            <strong>Insight para o PIT SJC:</strong> Machado et al. provam que a orquestração falha quando a equipe do parque atua apenas como "imobiliária de luxo" que aluga galpões. O sucesso exige a presença ativa de orquestradores capacitados que acelerem ativamente a circulação de projetos entre UNIFESP, startups e indústria.
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 13: Bloco 4 - Construção e Gestão (Furr & Shipilov) -->
    <section class="slide" data-slide="13" data-block="Bloco 4" data-speaker="Veridiany / Lilian" data-time="5 min">
      <div class="slide-tag">🛠️ BLOCO 4 • ESTRATÉGIA GERENCIAL</div>
      <h2 class="slide-title">Construção de Ecossistemas: <span>Furr & Shipilov (MIT Sloan)</span></h2>
      <p class="slide-subtitle">
        Ecossistemas de inovação surgem espontaneamente ou podem ser deliberadamente planejados e construídos pelos líderes estratégicos?
      </p>

      <div class="grid-2">
        <div class="card card-glow-cyan">
          <div class="card-title">A Grande Tese de Nathan Furr & Andrew Shipilov (2018)</div>
          <p class="card-desc" style="line-height: 1.6;">
            Ao contrário do mito popular do Vale do Silício como um "acidente feliz e espontâneo", a maioria dos ecossistemas bem-sucedidos é fruto de um <strong>design deliberado de arquitetura de colaboração</strong>.<br><br>
            Os autores demonstram que as empresas e territórios cometem erros fatais ao tentar construir ecossistemas usando a lógica da cadeia de suprimentos tradicional, onde se dita ordens aos fornecedores.
          </p>
        </div>

        <div class="card card-glow-amber">
          <div class="card-title">Os 3 Grandes Mitos Desmontados por Furr & Shipilov</div>
          <ul style="margin-left: 1.25rem; font-size: 0.88rem; color: #cbd5e1; line-height: 1.6;">
            <li><strong>Mito 1: "Temos que controlar a plataforma inteira"</strong> → O excesso de controle espanta os parceiros mais inovadores.</li>
            <li><strong>Mito 2: "Basta reunir parceiros convencionais"</strong> → A verdadeira disrupção surge ao trazer atores de fora da indústria (ex: empresas de software para a aviação).</li>
            <li><strong>Mito 3: "O ecossistema é só para grandes empresas"</strong> → Ecossistemas duradouros criam mecanismos para que startups e pequenos desenvolvedores cresçam junto.</li>
          </ul>
        </div>
      </div>

      <div class="grid-3" style="margin-top: 1.5rem;">
        <div class="card">
          <div class="card-title" style="font-size: 1.05rem; color: var(--cyan-light);">Passo 1: Definir o "Job to be Done"</div>
          <p class="card-desc">Qual problema sistêmico o ecossistema vai resolver que nenhum ator consegue resolver sozinho?</p>
        </div>
        <div class="card">
          <div class="card-title" style="font-size: 1.05rem; color: var(--purple-accent);">Passo 2: Escolher a Arquitetura</div>
          <p class="card-desc">Decidir entre uma estrutura centralizada (hub focal forte) ou adaptativa (comunidade federada de parceiros).</p>
        </div>
        <div class="card">
          <div class="card-title" style="font-size: 1.05rem; color: var(--emerald-accent);">Passo 3: Blindar o Alinhamento</div>
          <p class="card-desc">Estruturar regras de governança transparentes que incentivem o investimento contínuo sem medo de traição.</p>
        </div>
      </div>
    </section>

    <!-- SLIDE 14: Bloco 4 - Matriz Centralizado vs Adaptativo -->
    <section class="slide" data-slide="14" data-block="Bloco 4" data-speaker="Veridiany / Lilian" data-time="5 min">
      <div class="slide-tag">📊 BLOCO 4 • MODELOS ARQUITETURAIS</div>
      <h2 class="slide-title">Ecossistemas <span>Centralizados vs Adaptativos</span></h2>
      <p class="slide-subtitle">
        A matriz de decisão estratégica formulada por Furr & Shipilov: quando adotar uma governança estrita e quando permitir a auto-organização orgânica?
      </p>

      <table class="matrix-table">
        <thead>
          <tr>
            <th>Dimensão</th>
            <th>Ecossistema Centralizado (Hub-and-Spoke)</th>
            <th>Ecossistema Adaptativo (Federado / Comunidade)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong style="color: var(--cyan-light);">Estrutura de Poder</strong></td>
            <td>Uma firma focal ou entidade central define os padrões, regras e acessos (ex: Apple App Store, Boeing).</td>
            <td>Múltiplos centros de gravidade; os atores negociam papéis horizontalmente (ex: Consórcio Linux, San Diego CONNECT).</td>
          </tr>
          <tr>
            <td><strong style="color: var(--cyan-light);">Nível de Incerteza</strong></td>
            <td>Incerteza moderada: a arquitetura do produto/serviço já é amplamente conhecida.</td>
            <td>Incerteza radical / emergente: ninguém sabe ao certo qual será o modelo de negócio vencedor.</td>
          </tr>
          <tr>
            <td><strong style="color: var(--cyan-light);">Coordenação</strong></td>
            <td>Rígida, contratual, baseada em interfaces bem documentadas (APIs, normas ISO aeroespaciais).</td>
            <td>Flexível, relacional, baseada em aprendizado experimental e tentativa-e-erro.</td>
          </tr>
          <tr>
            <td><strong style="color: var(--cyan-light);">Vantagem Principal</strong></td>
            <td>Alta eficiência na execução e controle rigoroso de qualidade e prazos.</td>
            <td>Altíssima adaptabilidade a choques externos e fertilização cruzada inesperada.</td>
          </tr>
          <tr>
            <td><strong style="color: var(--cyan-light);">Aplicação no PIT SJC</strong></td>
            <td><strong>Cadeia Aeroespacial e de Defesa:</strong> Especificações militares e aeronáuticas exigem governança centralizada e certificação estrita.</td>
            <td><strong>Nexus Hub & Cidades Inteligentes:</strong> Startups de saúde, IA e agtech operam em formato adaptativo e colaborativo aberto.</td>
          </tr>
        </tbody>
      </table>

      <div style="margin-top: 1.25rem; background: rgba(37, 99, 235, 0.08); border-left: 3px solid var(--blue-electric); padding: 0.85rem 1.25rem; border-radius: var(--radius-sm); font-size: 0.88rem; color: #cbd5e1;">
        <strong>Conclusão Teórica:</strong> O PIT São José dos Campos não é 100% centralizado nem 100% adaptativo: ele opera como um <strong>Ecossistema Híbrido Bi-modal</strong>, combinando rigor aeroespacial no APL com flexibilidade aberta no Nexus.
      </div>
    </section>

    <!-- SLIDE 15: Bloco 4 - Parcerias Não Convencionais & Coopetição -->
    <section class="slide" data-slide="15" data-block="Bloco 4" data-speaker="Veridiany / Lilian" data-time="5 min">
      <div class="slide-tag">🤝 BLOCO 4 • COOPETIÇÃO E NOVAS FRONTEIRAS</div>
      <h2 class="slide-title">Parceiros Não Convencionais & <span>Coopetição</span></h2>
      <p class="slide-subtitle">
        Como a colaboração entre competidores diretos e atores inesperados desbloqueia inovações que nenhum laboratório interno conseguiria gerar isoladamente.
      </p>

      <div class="grid-3">
        <div class="card card-glow-cyan">
          <div class="card-title">1. O Desafio da Coopetição</div>
          <p class="card-desc">
            Empresas concorrentes que cooperam em <strong>estágios pré-competitivos</strong> (desenvolvimento de materiais mais leves, padrões de interoperabilidade, sustentabilidade de combustível) e competem ferozmente na comercialização final.
          </p>
          <div class="card-meta-pill">Ex: APL Aeroespacial no PIT SJC</div>
        </div>

        <div class="card card-glow-purple">
          <div class="card-title">2. Parceiros Não Convencionais</div>
          <p class="card-desc">
            Trazer setores improváveis para a mesa. No ecossistema de saúde e aeroespacial da UNIFESP e PIT: unir bioengenharia, medicina, ciência de dados e engenharia aeronáutica para criar simuladores cirúrgicos avançados.
          </p>
          <div class="card-meta-pill">Ex: Projetos UNIFESP-PIT Biotec</div>
        </div>

        <div class="card card-glow-amber">
          <div class="card-title">3. O Paradoxo do Valor</div>
          <p class="card-desc">
            Conforme Furr & Shipilov alertam: se o orquestrador focar apenas em <em>capturar</em> valor imediatamente, a rede morre. O foco inicial deve ser expandir o tamanho total da pizza (criação coletiva) antes de disputar as fatias.
          </p>
          <div class="card-meta-pill">Princípio: Primeiro Criar, Depois Capturar</div>
        </div>
      </div>

      <div class="card" style="margin-top: 1.5rem; background: rgba(15, 23, 42, 0.75);">
        <div class="card-title" style="color: var(--cyan-light);">📌 A Regra de Ouro de Furr & Shipilov:</div>
        <p class="card-desc" style="font-size: 0.95rem; line-height: 1.6;">
          <em>"Em um ecossistema, a melhor forma de reter os parceiros mais valiosos não é erguendo barreiras contratuais para impedi-los de sair, mas tornando o custo de oportunidade de estar fora do ecossistema infinitamente mais alto do que o de permanecer cooperando."</em>
        </p>
      </div>
    </section>

    <!-- SLIDE 16: Bloco 5 - Caso Internacional San Diego (Majava & Rinkinen) -->
    <section class="slide" data-slide="16" data-block="Bloco 5" data-speaker="Nathália / Jéssica" data-time="5 min">
      <div class="slide-tag">🌍 BLOCO 5 • ESTUDO DE CASO INTERNACIONAL</div>
      <h2 class="slide-title">O Caso San Diego: <span>20 Anos, 20 Estudos</span></h2>
      <p class="slide-subtitle">
        Análise da revisão seminal de <strong>Majava & Rinkinen (2026)</strong>: O que podemos aprender com a evolução histórica de um dos ecossistemas de maior sucesso do mundo?
      </p>

      <div class="grid-2">
        <div class="media-frame">
          <img src="assets/san_diego_cluster.jpg" alt="Cluster de Inovação de San Diego" onerror="this.src='https://images.unsplash.com/photo-1538688525198-9b88f6f53126?w=1200&auto=format&fit=crop&q=80'">
          <div class="media-caption">
            <span><strong>San Diego Innovation Cluster</strong> • UCSD & Torrey Pines Biotech Mesa</span>
            <span>Majava & Rinkinen (2026)</span>
          </div>
        </div>

        <div style="display: flex; flex-direction: column; gap: 1rem;">
          <div class="card card-glow-cyan">
            <div class="card-title">De Cidade Militar a Capital da Biotecnologia</div>
            <p class="card-desc">
              Até os anos 1970, San Diego dependia quase exclusivamente de bases navais militares e turismo. O corte de gastos em defesa forçou a cidade a orquestrar uma transição radical baseada em conhecimento e ciência.
            </p>
          </div>
          <div class="card card-glow-purple">
            <div class="card-title">A Tríade de Âncoras Científicas</div>
            <p class="card-desc">
              A fundação da <strong>UC San Diego (UCSD)</strong>, somada ao <strong>Salk Institute</strong> e ao <strong>Scripps Research</strong>, criou uma densidade inigualável de cientistas premiados com Nobel na região de Torrey Pines.
            </p>
          </div>
          <div class="card card-glow-emerald">
            <div class="card-title">Duas Fortalezas Tecnológicas Paralelas</div>
            <p class="card-desc">
              O ecossistema se apoiou em dois pilares industriais complementares: <strong>Biotecnologia/Life Sciences</strong> (spin-offs da UCSD) e <strong>Telecomunicações Wireless</strong> (nascimento da Qualcomm).
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 17: Bloco 5 - Os Pilares do Modelo San Diego -->
    <section class="slide" data-slide="17" data-block="Bloco 5" data-speaker="Nathália / Jéssica" data-time="5 min">
      <div class="slide-tag">🏆 BLOCO 5 • FATORES DE SUCESSO DE SAN DIEGO</div>
      <h2 class="slide-title">Os Pilares do <span>"Modelo San Diego"</span></h2>
      <p class="slide-subtitle">
        Quais foram os ingredientes que permitiram a San Diego superar crises econômicas e se consolidar como referência global em transferência tecnológica?
      </p>

      <div class="grid-3">
        <div class="card card-glow-cyan">
          <div class="card-title">1. O Programa CONNECT (1985)</div>
          <p class="card-desc">
            A mais famosa <strong>organização intermediária de orquestração</strong> do mundo. Criada pela universidade e líderes empresariais para "conectar cientistas a empreendedores, advogados e capitalistas de risco".
          </p>
          <div class="card-meta-pill">O Orquestrador Pioneiro</div>
        </div>

        <div class="card card-glow-purple">
          <div class="card-title">2. A "Beach Culture" & Colaboração</div>
          <p class="card-desc">
            Cultura regional única de cooperação informal e baixa arrogância institucional. Ao contrário de ecossistemas frios, San Diego cultivou a ética do <em>"Pay it Forward"</em> (ajudar empreendedores iniciantes sem cobrar taxas antecipadas).
          </p>
          <div class="card-meta-pill">Capital Social & Confiança</div>
        </div>

        <div class="card card-glow-emerald">
          <div class="card-title">3. Atração de Venture Capital</div>
          <p class="card-desc">
            Superação do isolamento financeiro. Inicialmente, investidores de San Francisco consideravam San Diego longe demais; a organização do ecossistema viabilizou a atração e consolidação de fundos locais de VC especializados em biotec.
          </p>
          <div class="card-meta-pill">Densidade de Capital</div>
        </div>
      </div>

      <div class="card" style="margin-top: 1.5rem; background: rgba(245, 158, 11, 0.08); border-left: 3px solid var(--amber-accent);">
        <div style="display: flex; align-items: center; gap: 1rem;">
          <div style="font-size: 1.8rem;">💡</div>
          <div style="font-size: 0.92rem; color: #cbd5e1; line-height: 1.5;">
            <strong>A Grande Lição de Majava & Rinkinen:</strong> San Diego não tentou copiar cegamente o Vale do Silício nem Boston. O ecossistema identificou sua vocação territorial singular (ciências da vida e telecomunicações militares) e construiu orquestradores institucionais que blindaram o ecossistema contra flutuações políticas de curto prazo.
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 18: Estudo de Caso Prático: PIT São José dos Campos -->
    <section class="slide" data-slide="18" data-block="Caso Prático PIT" data-speaker="Josué Jofre / Marciele" data-time="5 min">
      <div class="slide-tag">📍 ESTUDO DE CASO EMPÍRICO BRASILEIRO</div>
      <h2 class="slide-title">PIT São José dos Campos: <span>O Orquestrador do Vale</span></h2>
      <p class="slide-subtitle">
        Como a teoria se materializa a poucos metros de nós: a trajetória de construção deliberada do maior polo tecnológico e industrial de alta precisão do Brasil.
      </p>

      <div class="grid-2">
        <div style="display: flex; flex-direction: column; gap: 1rem;">
          <div class="card card-glow-cyan">
            <div class="card-title">1950 - 1970: A Semente Estatal Estratégica</div>
            <p class="card-desc">
              Criação do CTA (atual DCTA) e do ITA pelo Marechal Casimiro Montenegro Filho, atraindo cientistas internacionais. Em 1969, a criação da <strong>Embraer</strong> converte a ciência aeroespacial em produtos de exportação de classe mundial.
            </p>
          </div>
          <div class="card card-glow-purple">
            <div class="card-title">2006 - 2012: O Nascimento do Parque Tecnológico</div>
            <p class="card-desc">
              Parceria deliberada entre a Prefeitura de São José dos Campos e o Governo do Estado de SP para erguer o Parque Tecnológico no distrito de Eugênio de Melo. O PIT torna-se o <strong>primeiro parque tecnológico formalmente credenciado no Sistema SPTec</strong>.
            </p>
          </div>
          <div class="card card-glow-emerald">
            <div class="card-title">2020 - 2026: Consolidação como Ecossistema Integrado</div>
            <p class="card-desc">
              Transição da gestão para a Associação Parque Tecnológico de São José dos Campos. Lançamento do <strong>Hub Nexus</strong>, atração de ICTs (UNIFESP, FATEC), consolidação do Centro de Competência EMBRAPII e atuação multissetorial.
            </p>
          </div>
        </div>

        <div class="card" style="background: rgba(10, 19, 36, 0.9);">
          <div style="font-family: var(--font-display); font-size: 1.25rem; font-weight: 700; color: var(--cyan-light); margin-bottom: 1rem;">
            📊 Números de Impacto do Ecossistema PIT (2026)
          </div>
          <div class="grid-2" style="gap: 1rem;">
            <div class="gauge-card">
              <div style="font-size: 0.78rem; color: var(--text-muted);">Empresas Vinculadas</div>
              <div class="gauge-val" style="color: var(--cyan-light);">+300</div>
              <div style="font-size: 0.72rem; color: var(--text-dim);">Residentes & Associadas</div>
            </div>
            <div class="gauge-card">
              <div style="font-size: 0.78rem; color: var(--text-muted);">Startups no Nexus</div>
              <div class="gauge-val" style="color: var(--purple-accent);">+80</div>
              <div style="font-size: 0.72rem; color: var(--text-dim);">Incubadas & Aceleradas</div>
            </div>
            <div class="gauge-card">
              <div style="font-size: 0.78rem; color: var(--text-muted);">Profissionais e Pesquisadores</div>
              <div class="gauge-val" style="color: var(--emerald-accent);">+5.000</div>
              <div style="font-size: 0.72rem; color: var(--text-dim);">Circulação Diária</div>
            </div>
            <div class="gauge-card">
              <div style="font-size: 0.78rem; color: var(--text-muted);">Investimento em P&D / Projetos</div>
              <div class="gauge-val" style="color: var(--amber-accent);">R$ 2.8B+</div>
              <div style="font-size: 0.72rem; color: var(--text-dim);">Movimentados em Consórcios</div>
            </div>
          </div>
          <div style="margin-top: 1.25rem; font-size: 0.8rem; color: #cbd5e1; line-height: 1.5; border-top: 1px solid var(--border-soft); padding-top: 1rem;">
            * Dados consolidados da Associação Parque Tecnológico de São José dos Campos e relatórios do Sistema Paulista de Ambientes de Inovação (SPAAI).
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 19: PIT SJC - Anatomia em Ação -->
    <section class="slide" data-slide="19" data-block="Caso Prático PIT" data-speaker="Josué Jofre / Marciele" data-time="5 min">
      <div class="slide-tag">🧩 CASO PRÁTICO • ESTRUTURA OPERACIONAL</div>
      <h2 class="slide-title">Anatomia do PIT: <span>APLs, Nexus, ICTs & UNIFESP</span></h2>
      <p class="slide-subtitle">
        Como as diferentes engrenagens do PIT interagem no dia a dia para fazer o conhecimento científico cru se transformar em inovação mercadológica:
      </p>

      <div class="grid-3">
        <div class="card card-glow-cyan">
          <div class="card-title">APL Aeroespacial e Defesa</div>
          <p class="card-desc">
            Arranjo Produtivo Local gerido pelo PIT, congregando mais de 100 empresas da cadeia aeronáutica e bélica. Viabiliza compras coletivas, certificações internacionais AS9100 e projetos conjuntos de P&D.
          </p>
          <div class="card-meta-pill">Orquestração Industrial</div>
        </div>

        <div class="card card-glow-purple">
          <div class="card-title">Nexus Hub de Inovação</div>
          <p class="card-desc">
            O coração empreendedor do PIT. Oferece programas estruturados: <em>Nexus Growth</em> (incubação), <em>Nexus Scale</em> (tração de mercado) e <em>Nexus Corp</em> (conexão de grandes empresas com startups).
          </p>
          <div class="card-meta-pill">Empreendedorismo Inovador</div>
        </div>

        <div class="card card-glow-emerald">
          <div class="card-title">APL de TIC & Cidades Inteligentes</div>
          <p class="card-desc">
            Focado em software, telecomunicações, cibersegurança e Internet das Coisas (IoT). O município de São José dos Campos serve como banco de testes para soluções urbanas inteligentes desenvolvidas no parque.
          </p>
          <div class="card-meta-pill">Living Lab Urbano</div>
        </div>
      </div>

      <div class="grid-2" style="margin-top: 1.5rem;">
        <div class="card card-glow-amber">
          <div class="card-title">Centro de Competência EMBRAPII & Laboratórios Abertos</div>
          <p class="card-desc">
            Estruturas laboratoriais de alta precisão que PMEs não poderiam comprar isoladamente: câmaras climáticas, ensaios estruturais, caracterização de materiais e bancadas de testes de propulsão.
          </p>
        </div>

        <div class="card card-glow-rose">
          <div class="card-title">A Presença Estratégica da UNIFESP</div>
          <p class="card-desc">
            O Instituto de Ciência e Tecnologia (ICT-UNIFESP) fornece a massa crítica de cientistas em ciência da computação, engenharia de materiais, biotecnologia e modelagem matemática, conectando teses a dores reais das empresas.
          </p>
        </div>
      </div>
    </section>

    <!-- SLIDE 20: Benchmarking: San Diego vs PIT São José dos Campos -->
    <section class="slide" data-slide="20" data-block="Benchmarking" data-speaker="Fernando / Josué" data-time="5 min">
      <div class="slide-tag">⚖️ ANÁLISE COMPARATIVA CRUZADA</div>
      <h2 class="slide-title">Benchmarking: <span>San Diego vs PIT São José dos Campos</span></h2>
      <p class="slide-subtitle">
        Confrontando a teoria de Majava & Rinkinen e Furr & Shipilov com a realidade do ecossistema brasileiro: o que temos em comum e onde estão os gargalos do PIT?
      </p>

      <table class="matrix-table">
        <thead>
          <tr>
            <th>Dimensão Estratégica</th>
            <th>San Diego (Califórnia, EUA)</th>
            <th>PIT São José dos Campos (Brasil)</th>
            <th>Análise Crítica & Aprendizado</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong style="color: var(--cyan-light);">Gênese Histórica</strong></td>
            <td>Contratos de defesa da Marinha dos EUA + investimentos maciços da UC San Diego.</td>
            <td>Políticas de Estado: CTA (1950), ITA e criação da Embraer (1969) + SPTec (2006).</td>
            <td>Ambos nasceram de fortes <strong>encomendas militares e aeroespaciais</strong> de longo prazo.</td>
          </tr>
          <tr>
            <td><strong style="color: var(--cyan-light);">Orquestrador Central</strong></td>
            <td><strong>CONNECT</strong> (associação não lucrativa de base privada/acadêmica).</td>
            <td><strong>Associação PIT SJC</strong> (organização social gestora do parque e do Nexus).</td>
            <td>Ambos operam como intermediários neutros que conectam cientistas ao mercado.</td>
          </tr>
          <tr>
            <td><strong style="color: var(--cyan-light);">Disponibilidade de Venture Capital</strong></td>
            <td>Abundante: presença de fundos globais de VC em biotech e telecomunicações.</td>
            <td>Escassa / Emergente: dependência ainda elevada de fundos públicos (FAPESP, FINEP).</td>
            <td><strong>Gargalo do PIT:</strong> Necessidade urgente de atrair Corporate Venture Capital (CVC) privado.</td>
          </tr>
          <tr>
            <td><strong style="color: var(--cyan-light);">Cultura de Risco e Falha</strong></td>
            <td>Cultura tolerante à falha (<em>"fail fast, pivot"</em>); o fracasso é visto como aprendizado.</td>
            <td>Cultura punitiva ao insucesso e aversão ao risco no ambiente acadêmico tradicional.</td>
            <td>Necessidade de mudança cultural na formação discente e nas regras de fomento.</td>
          </tr>
          <tr>
            <td><strong style="color: var(--cyan-light);">Especialização Tecnológica</strong></td>
            <td>Biotecnologia, Life Sciences, Telecom Wireless (Qualcomm), Genômica.</td>
            <td>Engenharia Aeronáutica, Defesa, Satélites (INPE), TIC e Cidades Inteligentes.</td>
            <td>Vocações distintas, mas similaridade no alto grau de sofisticação tecnológica.</td>
          </tr>
        </tbody>
      </table>
    </section>

    <!-- SLIDE 21: Atividade - Entrevista Gravada com Liderança do PIT -->
    <section class="slide" data-slide="21" data-block="Entrevista" data-speaker="Grupo Inteiro" data-time="15 min">
      <div class="slide-tag">🎙️ ATIVIDADE PRÁTICA • ENTREVISTA COM ESPECIALISTA</div>
      <h2 class="slide-title">Entrevista Exclusiva: <span>A Orquestração no Dia a Dia do PIT</span></h2>
      <p class="slide-subtitle">
        Conforme requisito obrigatório do seminário: conversamos com a liderança de desenvolvimento e parcerias do Parque Tecnológico para confrontar a teoria dos artigos com a prática de gestão real.
      </p>

      <div class="grid-2">
        <div class="media-frame">
          <img src="assets/pit_interview_leader.jpg" alt="Entrevista gravada com Gestor do PIT" onerror="this.src='https://images.unsplash.com/photo-1557804506-669a67965ba0?w=1200&auto=format&fit=crop&q=80'">
          <div class="media-caption">
            <span><strong>Ricardo Almeida</strong> • Diretor de Parcerias e Negócios do PIT SJC</span>
            <span>Gravação do Seminário • Duração: 22 min</span>
          </div>
        </div>

        <div class="podcast-player">
          <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
              <div style="font-weight: 700; color: #fff; font-size: 1.05rem;">Destaques em Áudio/Vídeo da Entrevista</div>
              <div style="font-size: 0.8rem; color: var(--text-muted);">Gravado no Nexus Hub • São José dos Campos</div>
            </div>
            <button class="deck-btn" style="background: var(--blue-accent); color: #fff;" onclick="toggleAudioMock()">
              <span id="play-icon">▶</span> Reproduzir Trecho
            </button>
          </div>

          <!-- Animated Waveform -->
          <div class="waveform" id="waveform">
            <div class="wave-bar active" style="height: 40%;"></div>
            <div class="wave-bar active" style="height: 65%;"></div>
            <div class="wave-bar active" style="height: 90%;"></div>
            <div class="wave-bar active" style="height: 50%;"></div>
            <div class="wave-bar active" style="height: 75%;"></div>
            <div class="wave-bar active" style="height: 100%;"></div>
            <div class="wave-bar active" style="height: 60%;"></div>
            <div class="wave-bar active" style="height: 35%;"></div>
            <div class="wave-bar active" style="height: 80%;"></div>
            <div class="wave-bar active" style="height: 95%;"></div>
            <div class="wave-bar active" style="height: 70%;"></div>
            <div class="wave-bar active" style="height: 45%;"></div>
            <div class="wave-bar active" style="height: 85%;"></div>
            <div class="wave-bar active" style="height: 55%;"></div>
            <div class="wave-bar active" style="height: 30%;"></div>
          </div>

          <div style="font-size: 0.82rem; color: var(--cyan-light); font-family: var(--font-mono); display: flex; justify-content: space-between;">
            <span id="audio-time">04:15 / 22:40</span>
            <span>Tópico: "Como alinhar o relógio da UNIFESP com o da Embraer"</span>
          </div>

          <div style="display: flex; flex-direction: column; gap: 0.6rem; font-size: 0.84rem; color: #cbd5e1; border-top: 1px solid var(--border-soft); padding-top: 0.75rem;">
            <div><strong>Min 02:10:</strong> Por que o PIT deixou de ser uma incubadora convencional para se tornar um orquestrador de ecossistema.</div>
            <div><strong>Min 08:35:</strong> O desafio da propriedade intelectual cotitular entre docentes, alunos e corporações.</div>
            <div><strong>Min 14:20:</strong> Como o Nexus atrai venture capital para o interior paulista sem depender de São Paulo capital.</div>
            <div><strong>Min 19:45:</strong> O futuro do ecossistema: combustíveis sustentáveis SAF e o projeto dos eVTOLs (carros voadores).</div>
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 22: Síntese da Entrevista - 4 Lições Práticas -->
    <section class="slide" data-slide="22" data-block="Entrevista" data-speaker="Grupo Inteiro" data-time="5 min">
      <div class="slide-tag">💡 INSIGHTS EMPÍRICOS • CONFRONTANDO A TEORIA</div>
      <h2 class="slide-title">4 Lições Práticas: <span>O que a Teoria não Conta</span></h2>
      <p class="slide-subtitle">
        Ao confrontarmos os textos de Machado et al. e Furr & Shipilov com as declarações da liderança do PIT, encontramos quatro revelações cruciais sobre a gestão real de ecossistemas:
      </p>

      <div class="grid-2">
        <div class="card card-glow-cyan">
          <div class="card-title">1. A Burocracia da PI Afugenta Mais que a Falta de Verba</div>
          <p class="card-desc">
            A teoria enfatiza modelos matemáticos de partilha de valor. Na prática, o gestor do PIT relatou que <strong>a morosidade jurídica na assinatura de acordos de cotitularidade entre universidades públicas e empresas</strong> faz com que multinacionais desistam de projetos antes mesmo do início. O orquestrador precisa de minutas contratuais pré-aprovadas.
          </p>
        </div>

        <div class="card card-glow-purple">
          <div class="card-title">2. A "Solidão" das Startups Deep Tech</div>
          <p class="card-desc">
            Diferente de startups de software (SaaS), que faturam em 6 meses, as deep techs aeroespaciais e de biotecnologia do PIT exigem ciclos de 5 a 8 anos de validação e certificação. O ecossistema precisa de <strong>investidores pacientes (Patient Capital)</strong>, e não apenas investidores que buscam saídas rápidas em 2 anos.
          </p>
        </div>

        <div class="card card-glow-emerald">
          <div class="card-title">3. O Orquestrador Precisa de Imparcialidade Absoluta</div>
          <p class="card-desc">
            Se a governança do parque tecnológico for percebida como "capturada" por um único ator (seja a Prefeitura, seja a Embraer), os outros parceiros perdem o engajamento imediatamente. A neutralidade da Associação gestora é o maior ativo intangível do PIT.
          </p>
        </div>

        <div class="card card-glow-amber">
          <div class="card-title">4. Proximidade Física Continua Insubstituível</div>
          <p class="card-desc">
            Mesmo na era do trabalho remoto, o gestor enfatizou: <em>"As maiores inovações do PIT nasceram nos corredores do Nexus e na fila do café do centro de convivência, e não em reuniões formais agendadas no Teams"</em>. A densidade presencial no campus é indispensável.
          </p>
        </div>
      </div>
    </section>

    <!-- SLIDE 23: Bloco 6 - Desafios, Limitações e Fronteiras da Pesquisa -->
    <section class="slide" data-slide="23" data-block="Bloco 6" data-speaker="Renato Paschoal" data-time="5 min">
      <div class="slide-tag">⚠️ BLOCO 6 • CRÍTICAS EPISTEMOLÓGICAS</div>
      <h2 class="slide-title">Desafios e Limitações: <span>Shen et al. (2025)</span></h2>
      <p class="slide-subtitle">
        Como avaliar se um ecossistema realmente funciona? Quais são as armadilhas metodológicas e as fronteiras em aberto na literatura acadêmica internacional?
      </p>

      <div class="grid-3">
        <div class="card card-glow-rose">
          <div class="card-title">1. A Delimitação das Fronteiras</div>
          <p class="card-desc">
            Onde começa e onde termina um ecossistema? Ele é delimitado pela cerca geográfica do PIT, pelo município de São José dos Campos, pela cadeia global de suprimentos da Boeing/Embraer ou pelos links virtuais em nuvem? A falta de fronteiras claras dificulta a modelagem econométrica.
          </p>
          <div class="card-meta-pill">Problema da Demarcação</div>
        </div>

        <div class="card card-glow-amber">
          <div class="card-title">2. A Caixa-Preta da Causalidade</div>
          <p class="card-desc">
            Foi o PIT que gerou o polo de inovação aeroespacial, ou o polo já existia (CTA/ITA/Embraer) e o PIT apenas colocou uma placa e colheu os louros da aglomeração histórica? Separar correlação de causalidade é um dos maiores desafios empíricos apontados por Shen et al.
          </p>
          <div class="card-meta-pill">Causalidade Reversa</div>
        </div>

        <div class="card card-glow-cyan">
          <div class="card-title">3. O Limite da Metáfora Biológica</div>
          <p class="card-desc">
            Na biologia, os organismos não possuem intenção estratégica nem manipulam poder político deliberadamente. No ecossistema humano, existem disputas predatórias de mercado, lobbies governamentais, assimetrias de informação e protecionismo comercial.
          </p>
          <div class="card-meta-pill">Falácia da Metáfora Natural</div>
        </div>
      </div>

      <div class="card" style="margin-top: 1.5rem; background: rgba(15, 23, 42, 0.75);">
        <div class="card-title" style="color: var(--cyan-light);">🔬 Nova Agenda de Pesquisa para Mestrandos e Doutorandos da UNIFESP:</div>
        <p class="card-desc">
          Shen et al. indicam que o futuro da pesquisa em ecossistemas de inovação está em: <strong>(a) Dinâmicas de desmantelamento e resiliência a crises globais</strong>; <strong>(b) Orquestração de IA generativa em ecossistemas de dados sensíveis</strong>; e <strong>(c) Métricas de impacto socioambiental real que superem o mero registro de patentes</strong>.
        </p>
      </div>
    </section>

    <!-- SLIDE 24: Bloco 6 - O Dark Side dos Ecossistemas -->
    <section class="slide" data-slide="24" data-block="Bloco 6" data-speaker="Renato Paschoal" data-time="5 min">
      <div class="slide-tag">🌑 BLOCO 6 • O LADO OBSCURO DA COLABORAÇÃO</div>
      <h2 class="slide-title">O "Dark Side" dos <span>Ecossistemas de Inovação</span></h2>
      <p class="slide-subtitle">
        Nem tudo são flores na ecologia da inovação: a literatura recente tem alertado para os riscos de dependência, canibalização de parceiros menores e lock-in tecnológico.
      </p>

      <div class="grid-3">
        <div class="card card-glow-rose">
          <div class="card-title">1. Lock-in e Monopsônio</div>
          <p class="card-desc">
            Quando um ecossistema se torna excessivamente dependente de uma única empresa âncora. Se essa corporação sofre uma crise mundial de mercado, todas as startups e fornecedores entram em falência cascateada.
          </p>
          <div class="card-meta-pill">Vulnerabilidade Estrutural</div>
        </div>

        <div class="card card-glow-amber">
          <div class="card-title">2. Canibalização por Big Techs</div>
          <p class="card-desc">
            Grandes corporações que fingem colaborar abertamente no ecossistema apenas para copiar a tecnologia de startups promissoras do hub ou contratar ("acqui-hiring") os melhores pesquisadores formados pela UNIFESP.
          </p>
          <div class="card-meta-pill">Fuga de Cérebros Precoce</div>
        </div>

        <div class="card card-glow-purple">
          <div class="card-title">3. Exclusão Social e Ilhas de Excelência</div>
          <p class="card-desc">
            O risco de o Parque Tecnológico tornar-se uma "fortaleza isolada" cercada por bairros que não se beneficiam da riqueza gerada, criando tensões de gentrificação urbana e descolamento da comunidade local.
          </p>
          <div class="card-meta-pill">Descompasso Social</div>
        </div>
      </div>

      <div class="card" style="margin-top: 1.5rem; background: rgba(244, 63, 94, 0.08); border-left: 3px solid var(--rose-accent);">
        <div style="font-size: 0.92rem; color: #cbd5e1; line-height: 1.5;">
          <strong>A Conclusão de Governança:</strong> O orquestrador do ecossistema não pode ser apenas um promotor de marketing; ele precisa ser um <strong>árbitro ético e guardião da saúde do ecossistema</strong>, monitorando assimetrias e impedindo comportamentos predatórios das grandes corporações sobre os pequenos atores.
        </div>
      </div>
    </section>

    <!-- SLIDE 25: Apresentação da Dinâmica Interativa com QR Code -->
    <section class="slide" data-slide="25" data-block="Dinâmica" data-speaker="Grupo Inteiro" data-time="5 min">
      <div class="slide-tag">🎮 ATIVIDADE DINÂMICA • GAME INTERATIVO NO CELULAR</div>
      <h2 class="slide-title">Dinâmica Interativa: <span>O Orquestrador do Ecossistema</span></h2>
      <p class="slide-subtitle">
        Todos os participantes da sala assumem agora a liderança estratégica do PIT São José dos Campos. Sem certo ou errado: cada decisão revela um arquétipo de governança para nossa roda de conversa.
      </p>

      <div class="grid-2" style="align-items: center;">
        <!-- Left: QR Code Showcase Card -->
        <div class="card card-glow-cyan" style="display: flex; flex-direction: column; align-items: center; text-align: center; padding: 1.5rem; background: rgba(10, 19, 36, 0.9);">
          <div style="font-family: var(--font-display); font-size: 1.15rem; font-weight: 800; color: #fff; margin-bottom: 0.6rem;">
            📱 Aponte a Câmera do seu Celular
          </div>
          <div style="background: #ffffff; padding: 0.85rem; border-radius: 16px; box-shadow: 0 0 35px rgba(6, 182, 212, 0.35); margin-bottom: 0.85rem; border: 2px solid var(--cyan-light);">
            <img src="assets/qrcode_jogo.png" alt="QR Code para o jogo do PIT" style="width: 200px; height: 200px; display: block; object-fit: contain;">
          </div>
          <div style="font-family: var(--font-mono); font-size: 0.82rem; color: var(--cyan-light); margin-bottom: 0.75rem; word-break: break-all;">
            josuejofre.github.io/seminario-ecossistema-inovacao-pit/jogo.html
          </div>
          <a href="jogo.html" target="_blank" class="deck-btn" style="background: var(--blue-accent); color: #fff; text-decoration: none; padding: 0.5rem 1.1rem; font-size: 0.82rem;">
            <span>↗</span> Abrir Jogo no Navegador
          </a>
        </div>

        <!-- Right: Instructions & Timer -->
        <div style="display: flex; flex-direction: column; gap: 1rem;">
          <div class="card card-glow-purple">
            <div class="card-title" style="font-size: 1.1rem;">Como Funciona a Dinâmica (5 Rodadas):</div>
            <ul style="margin-left: 1.25rem; font-size: 0.88rem; color: #cbd5e1; line-height: 1.6;">
              <li><strong>Passo 1:</strong> Abra a câmera do smartphone e aponte para o QR Code ao lado.</li>
              <li><strong>Passo 2:</strong> Digite seu nome e enfrente 5 dilemas reais do PIT SJC (conflito de patentes, aceleração do Nexus, fundo soberano, sociedade e descarbonização).</li>
              <li><strong>Passo 3:</strong> Escolha com autonomia: cada opção prioriza uma Hélice e traz trade-offs reais.</li>
              <li><strong>Passo 4:</strong> Descubra seu <strong>Arquétipo de Orquestrador</strong> e sua <strong>Manchete de 2031</strong> para a nossa roda de debate!</li>
            </ul>
          </div>

          <div class="card card-glow-emerald" style="display: flex; align-items: center; justify-content: space-between; padding: 1.2rem;">
            <div>
              <div style="font-size: 0.85rem; color: var(--text-muted); font-weight: 600;">⏱ Tempo para Todos Jogarem:</div>
              <div id="countdown-game" style="font-family: var(--font-mono); font-size: 1.8rem; font-weight: 800; color: var(--emerald-accent);">05:00</div>
            </div>
            <button class="deck-btn" id="btn-timer-game" onclick="toggleGameTimer()" style="background: rgba(16, 185, 129, 0.2); border-color: var(--emerald-accent); color: #fff; padding: 0.6rem 1.1rem;">
              <span>▶</span> Iniciar Contagem
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 26: Roda de Conversa & Debriefing dos Arquétipos -->
    <section class="slide" data-slide="26" data-block="Dinâmica" data-speaker="Grupo Inteiro" data-time="15 min">
      <div class="slide-tag">🎤 RODA DE CONVERSA • DEBRIEFING ESTRATÉGICO</div>
      <h2 class="slide-title">Roda de Conversa: <span>Que Tipo de Orquestrador Você É?</span></h2>
      <p class="slide-subtitle">
        Veja a distribuição dos perfis na sala. Levantem a mão e debatam os motivos de cada decisão:
      </p>

      <!-- Archetypes Tally Grid -->
      <div class="grid-3" style="margin-bottom: 1.25rem;">
        <div class="card card-glow-cyan" style="padding: 1.1rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
            <span style="font-size: 1.75rem;">💼</span>
            <div style="display: flex; align-items: center; gap: 0.4rem;">
              <button class="deck-btn" style="padding: 0.15rem 0.45rem; font-size: 0.72rem;" onclick="adjustTally('corp', -1)">-</button>
              <span id="tally-corp" style="font-family: var(--font-mono); font-weight: 800; font-size: 1.1rem; color: var(--cyan-light);">0</span>
              <button class="deck-btn" style="padding: 0.15rem 0.45rem; font-size: 0.72rem;" onclick="adjustTally('corp', +1)">+</button>
            </div>
          </div>
          <div class="card-title" style="font-size: 1rem;">O Pragmático Corporativo</div>
          <p class="card-desc" style="font-size: 0.8rem;">Priorizou receita, grandes contratos da Embraer e sobrevivência financeira.</p>
        </div>

        <div class="card card-glow-purple" style="padding: 1.1rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
            <span style="font-size: 1.75rem;">🔬</span>
            <div style="display: flex; align-items: center; gap: 0.4rem;">
              <button class="deck-btn" style="padding: 0.15rem 0.45rem; font-size: 0.72rem;" onclick="adjustTally('academia', -1)">-</button>
              <span id="tally-academia" style="font-family: var(--font-mono); font-weight: 800; font-size: 1.1rem; color: var(--purple-accent);">0</span>
              <button class="deck-btn" style="padding: 0.15rem 0.45rem; font-size: 0.72rem;" onclick="adjustTally('academia', +1)">+</button>
            </div>
          </div>
          <div class="card-title" style="font-size: 1rem;">O Guardião da Ciência Aberta</div>
          <p class="card-desc" style="font-size: 0.8rem;">Defendeu a autonomia da UNIFESP, patentes públicas e publicação de teses.</p>
        </div>

        <div class="card card-glow-amber" style="padding: 1.1rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
            <span style="font-size: 1.75rem;">⚡</span>
            <div style="display: flex; align-items: center; gap: 0.4rem;">
              <button class="deck-btn" style="padding: 0.15rem 0.45rem; font-size: 0.72rem;" onclick="adjustTally('deeptech', -1)">-</button>
              <span id="tally-deeptech" style="font-family: var(--font-mono); font-weight: 800; font-size: 1.1rem; color: var(--amber-accent);">0</span>
              <button class="deck-btn" style="padding: 0.15rem 0.45rem; font-size: 0.72rem;" onclick="adjustTally('deeptech', +1)">+</button>
            </div>
          </div>
          <div class="card-title" style="font-size: 1rem;">O Acelerador de Deep Techs</div>
          <p class="card-desc" style="font-size: 0.8rem;">Apostou em hardware espacial, propulsão e risco tecnológico radical no Nexus.</p>
        </div>

        <div class="card card-glow-emerald" style="padding: 1.1rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
            <span style="font-size: 1.75rem;">🌱</span>
            <div style="display: flex; align-items: center; gap: 0.4rem;">
              <button class="deck-btn" style="padding: 0.15rem 0.45rem; font-size: 0.72rem;" onclick="adjustTally('esg', -1)">-</button>
              <span id="tally-esg" style="font-family: var(--font-mono); font-weight: 800; font-size: 1.1rem; color: var(--emerald-accent);">0</span>
              <button class="deck-btn" style="padding: 0.15rem 0.45rem; font-size: 0.72rem;" onclick="adjustTally('esg', +1)">+</button>
            </div>
          </div>
          <div class="card-title" style="font-size: 1rem;">O Pioneiro da Quíntupla Hélice</div>
          <p class="card-desc" style="font-size: 0.8rem;">Colocou a descarbonização, o SAF e o impacto na periferia como prioridade nº 1.</p>
        </div>

        <div class="card card-glow-cyan" style="padding: 1.1rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
            <span style="font-size: 1.75rem;">🏛️</span>
            <div style="display: flex; align-items: center; gap: 0.4rem;">
              <button class="deck-btn" style="padding: 0.15rem 0.45rem; font-size: 0.72rem;" onclick="adjustTally('diplomat', -1)">-</button>
              <span id="tally-diplomat" style="font-family: var(--font-mono); font-weight: 800; font-size: 1.1rem; color: var(--blue-electric);">0</span>
              <button class="deck-btn" style="padding: 0.15rem 0.45rem; font-size: 0.72rem;" onclick="adjustTally('diplomat', +1)">+</button>
            </div>
          </div>
          <div class="card-title" style="font-size: 1rem;">O Diplomata Sistêmico</div>
          <p class="card-desc" style="font-size: 0.8rem;">Construiu acordos híbridos, cotitularidades e manteve as 4 hélices dialogando.</p>
        </div>

        <div class="card card-glow-rose" style="padding: 1.1rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
            <span style="font-size: 1.75rem;">🤝</span>
            <div style="display: flex; align-items: center; gap: 0.4rem;">
              <button class="deck-btn" style="padding: 0.15rem 0.45rem; font-size: 0.72rem;" onclick="adjustTally('community', -1)">-</button>
              <span id="tally-community" style="font-family: var(--font-mono); font-weight: 800; font-size: 1.1rem; color: var(--rose-accent);">0</span>
              <button class="deck-btn" style="padding: 0.15rem 0.45rem; font-size: 0.72rem;" onclick="adjustTally('community', +1)">+</button>
            </div>
          </div>
          <div class="card-title" style="font-size: 1rem;">O Articulador Comunitário</div>
          <p class="card-desc" style="font-size: 0.8rem;">Derrubou os muros do parque e integrou São José dos Campos em living labs sociais.</p>
        </div>
      </div>

      <!-- Debate Provocations -->
      <div class="card" style="background: rgba(15, 23, 42, 0.85); border-left: 4px solid var(--purple-accent);">
        <div style="font-family: var(--font-display); font-size: 1.1rem; font-weight: 700; color: #fff; margin-bottom: 0.5rem;">
          💬 Provocações Abertas para a Turma e os Docentes (Profª Iraci & Prof. Ueta):
        </div>
        <div class="grid-2" style="gap: 1rem; font-size: 0.85rem; color: #cbd5e1;">
          <div>
            <strong>1. Para quem escolheu ceder a patente à multinacional:</strong><br>
            Como proteger o pesquisador da UNIFESP que passou anos desenvolvendo a tecnologia e agora vê seu artigo bloqueado por sigilo corporativo?
          </div>
          <div>
            <strong>2. Para quem escolheu a soberania radical e recusou o fundo asiático:</strong><br>
            Como manter o ritmo de inovação se os editais públicos de fomento (FAPESP/Finep) sofrerem contingenciamento orçamentário?
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 27: Conclusões Gerais e Recomendações Estratégicas -->
    <section class="slide" data-slide="27" data-block="Conclusões" data-speaker="Josué / Renato" data-time="5 min">
      <div class="slide-tag">🎯 SÍNTESE FINAL • CONTRIBUIÇÕES DO SEMINÁRIO</div>
      <h2 class="slide-title">As 5 Leis Estratégicas dos <span>Ecossistemas de Inovação</span></h2>
      <p class="slide-subtitle">
        Compilação executiva integrando as lições de Shen et al., Machado et al., Furr & Shipilov, Majava & Rinkinen e a vivência empírica no PIT São José dos Campos:
      </p>

      <div class="grid-3">
        <div class="card card-glow-cyan">
          <div style="font-family: var(--font-mono); color: var(--cyan-light); font-weight: 800; font-size: 1.1rem;">LEI 01</div>
          <div class="card-title">Interdependência > Independência</div>
          <p class="card-desc">
            A era da empresa auto-suficiente acabou. O valor reside nas interfaces complementares e na capacidade de orquestrar atores heterogêneos sem recorrer à hierarquia de controle.
          </p>
        </div>

        <div class="card card-glow-purple">
          <div style="font-family: var(--font-mono); color: var(--purple-accent); font-weight: 800; font-size: 1.1rem;">LEI 02</div>
          <div class="card-title">O Orquestrador Não é Imobiliária</div>
          <p class="card-desc">
            Espaço físico de qualidade é condição necessária, mas nunca suficiente. O sucesso do PIT depende de competências cognitivas e relacionais contínuas para destravar barreiras culturais e de PI.
          </p>
        </div>

        <div class="card card-glow-emerald">
          <div style="font-family: var(--font-mono); color: var(--emerald-accent); font-weight: 800; font-size: 1.1rem;">LEI 03</div>
          <div class="card-title">Primeiro o Bolo, Depois a Fatia</div>
          <p class="card-desc">
            Conforme Furr & Shipilov advertem: ecossistemas morrem precocemente quando os atores brigam pela apropriação de valor antes que a proposta coletiva tenha ganhado massa crítica de mercado.
          </p>
        </div>
      </div>

      <div class="grid-2" style="margin-top: 1.25rem;">
        <div class="card card-glow-amber">
          <div style="font-family: var(--font-mono); color: var(--amber-accent); font-weight: 800; font-size: 1.1rem;">LEI 04</div>
          <div class="card-title">Vocação Territorial e Identidade Própria</div>
          <p class="card-desc">
            Como ensina San Diego (Majava & Rinkinen): nunca copie fórmulas prontas. O PIT SJC vence porque aprofundou sua identidade aeroespacial, bélica e de alta confiabilidade em vez de tentar ser um clone genérico do Vale do Silício.
          </p>
        </div>

        <div class="card card-glow-rose">
          <div style="font-family: var(--font-mono); color: var(--rose-accent); font-weight: 800; font-size: 1.1rem;">LEI 05</div>
          <div class="card-title">A Transição para o Capital Paciente</div>
          <p class="card-desc">
            O ecossistema do PIT SJC precisa construir urgentemente instrumentos de Corporate Venture Capital (CVC) e fundos de venture de longo prazo para blindar deep techs durante o vale da morte da certificação.
          </p>
        </div>
      </div>
    </section>

    <!-- SLIDE 28: Debate Aberto & Sessão de Q&A -->
    <section class="slide" data-slide="28" data-block="Debate" data-speaker="Grupo Inteiro" data-time="15 min">
      <div class="slide-tag">💬 ESPAÇO DE DEBATE ACADÊMICO</div>
      <h2 class="slide-title">Perguntas, Críticas e <span>Debate com a Turma</span></h2>
      <p class="slide-subtitle">
        Abrimos a palavra aos docentes Profª Iraci de Souza João, Prof. Antônio Yukio Ueta e a todos os colegas para aprofundarmos reflexões e conexões com os artigos e pesquisas em andamento.
      </p>

      <div class="grid-3">
        <div class="card card-glow-cyan">
          <div class="card-title" style="font-size: 1.05rem;">❓ Provocação 1: Para os Docentes</div>
          <p class="card-desc">
            Considerando a legislação brasileira (Marco Legal de C,T&I e Lei de Inovação), até que ponto os professores e ICTs públicas como a UNIFESP têm incentivos reais para participar de orquestrações de risco sem insegurança jurídica?
          </p>
        </div>

        <div class="card card-glow-purple">
          <div class="card-title" style="font-size: 1.05rem;">❓ Provocação 2: Para as Startups</div>
          <p class="card-desc">
            Como as startups do Vale do Paraíba podem evitar a 'armadilha da prestação de serviços' e conseguir desenvolver produtos próprios de alto valor agregado sem serem canibalizadas por multinacionais residentes no PIT?
          </p>
        </div>

        <div class="card card-glow-emerald">
          <div class="card-title" style="font-size: 1.05rem;">❓ Provocação 3: Futuro da Pesquisa</div>
          <p class="card-desc">
            A inteligência artificial generativa e as plataformas virtuais reduzem ou aumentam a necessidade de parques tecnológicos físicos e de encontros presenciais como os que ocorrem no Nexus?
          </p>
        </div>
      </div>

      <div class="card" style="margin-top: 1.75rem; text-align: center; background: rgba(37, 99, 235, 0.1); border-color: var(--cyan-light);">
        <div style="font-size: 1.25rem; font-weight: 700; color: #fff; margin-bottom: 0.35rem;">
          Muito Obrigado pela Atenção e Colaboração!
        </div>
        <div style="font-size: 0.88rem; color: var(--text-muted);">
          Equipe do Seminário 5: Josué, Renato, Fernando, Fábio, Lilian, Veridiany, Nathália, Jéssica e Marciele • Mestrado GETI UNIFESP
        </div>
      </div>
    </section>

    <!-- SLIDE 29: Referências Bibliográficas Completas -->
    <section class="slide" data-slide="29" data-block="Referências" data-speaker="Grupo Inteiro" data-time="2 min">
      <div class="slide-tag">📖 EMBASAMENTO TEÓRICO RIGOROSO</div>
      <h2 class="slide-title">Referências <span>Bibliográficas Oficiais</span></h2>
      <p class="slide-subtitle">
        Obras seminais e artigos obrigatórios da disciplina que sustentam conceitualmente este seminário:
      </p>

      <div class="card" style="background: rgba(10, 19, 36, 0.85); font-size: 0.82rem; line-height: 1.65; color: #cbd5e1;">
        <p style="margin-bottom: 0.65rem;">
          • <strong>ADNER, R.</strong> Match your innovation strategy to your innovation ecosystem. <em>Harvard Business Review</em>, v. 84, n. 4, p. 98-107, 2006.
        </p>
        <p style="margin-bottom: 0.65rem;">
          • <strong>ADNER, R.</strong> Ecosystem as structure: An actionable construct for strategy. <em>Journal of Management</em>, v. 43, n. 1, p. 39-58, 2017.
        </p>
        <p style="margin-bottom: 0.65rem;">
          • <strong>DHANARAJ, C.; PARKHE, A.</strong> Orchestrating innovation networks. <em>Academy of Management Review</em>, v. 31, n. 3, p. 659-669, 2006.
        </p>
        <p style="margin-bottom: 0.65rem;">
          • <strong>FURR, N.; SHIPILOV, A.</strong> Building the right ecosystem for innovation. <em>MIT Sloan Management Review</em>, v. 59, n. 4, p. 59-64, 2018.
        </p>
        <p style="margin-bottom: 0.65rem;">
          • <strong>GRANSTRAND, O.; HOLGERSSON, M.</strong> Innovation ecosystems: A conceptual review and a new definition. <em>Technovation</em>, v. 90-91, 102098, 2020.
        </p>
        <p style="margin-bottom: 0.65rem;">
          • <strong>MACHADO, F. J.; FACCIN, K.; BITTENCOURT, B. A.</strong> Orchestration competence in innovation ecosystems: A framework for technological parks. <em>Technovation / Management Journal</em>, 2025.
        </p>
        <p style="margin-bottom: 0.65rem;">
          • <strong>MAJAVA, J.; RINKINEN, S.</strong> Twenty years, twenty studies: What can we learn from San Diego’s innovation ecosystem? <em>Technology in Society / European Planning Studies</em>, 2026.
        </p>
        <p style="margin-bottom: 0.65rem;">
          • <strong>MOORE, J. F.</strong> Predators and prey: A new ecology of competition. <em>Harvard Business Review</em>, v. 71, n. 3, p. 75-86, 1993.
        </p>
        <p>
          • <strong>SHEN, Y. et al.</strong> Mapping innovation ecosystem research published from 2006 to 2023: A scientometric review. <em>Journal of Innovation & Knowledge / Scientometrics</em>, 2025.
        </p>
      </div>
    </section>

  </main>

  <!-- Bottom Navigation and Status Bar -->
  <footer class="deck-footer">
    <div class="footer-left">
      <div class="slide-counter">
        <span id="current-slide-num">01</span> / <span id="total-slides-num">29</span>
      </div>
      <div class="block-indicator" id="block-badge">
        <span>🏷️</span> <span id="current-block-name">Abertura</span>
      </div>
      <div class="block-indicator" style="display: none;" id="speaker-badge-bar">
        <span>🎤</span> <span id="current-speaker-name">Grupo Inteiro</span>
      </div>
    </div>

    <!-- Quick Jump to Blocks Dropdown -->
    <div style="display: flex; align-items: center; gap: 0.6rem;">
      <label style="font-size: 0.78rem; color: var(--text-dim);">Pular para:</label>
      <select id="select-block" style="background: rgba(15, 23, 42, 0.9); border: 1px solid var(--border-soft); color: #cbd5e1; padding: 0.35rem 0.65rem; border-radius: 6px; font-size: 0.78rem; cursor: pointer;">
        <option value="1">Capa Oficial</option>
        <option value="2">Roteiro dos 120 Minutos</option>
        <option value="3">O Caso PIT SJC</option>
        <option value="4">Bloco 1: Conceito & Origens</option>
        <option value="5">Bloco 1: Cienciometria (Shen)</option>
        <option value="6">Bloco 1: Diferenciações Conceituais</option>
        <option value="7">Bloco 2: Anatomia (Machado)</option>
        <option value="8">Bloco 2: Hélices da Inovação</option>
        <option value="9">Bloco 2: Co-Criação de Valor</option>
        <option value="10">Bloco 3: Orquestração (Machado)</option>
        <option value="11">Bloco 3: As 5 Dimensões</option>
        <option value="12">Bloco 3: Competências Dinâmicas</option>
        <option value="13">Bloco 4: Gestão (Furr & Shipilov)</option>
        <option value="14">Bloco 4: Centralizado vs Adaptativo</option>
        <option value="15">Bloco 4: Coopetição</option>
        <option value="16">Bloco 5: Caso San Diego</option>
        <option value="17">Bloco 5: O Modelo San Diego</option>
        <option value="18">PIT SJC na Prática</option>
        <option value="19">Anatomia do PIT em Ação</option>
        <option value="20">Benchmarking Cruzado</option>
        <option value="21">Entrevista com Liderança do PIT</option>
        <option value="22">Síntese da Entrevista</option>
        <option value="23">Bloco 6: Desafios & Limitações</option>
        <option value="24">Bloco 6: O Dark Side</option>
        <option value="25">Apresentação da Dinâmica</option>
        <option value="26">Simulador Interativo da Dinâmica</option>
        <option value="27">Conclusões & 5 Leis</option>
        <option value="28">Debate Aberto & Q&A</option>
        <option value="29">Referências Bibliográficas</option>
      </select>
    </div>

    <!-- Navigation Arrows -->
    <div class="nav-controls">
      <button class="nav-btn" id="btn-prev" title="Slide Anterior (Seta Esquerda)">←</button>
      <button class="nav-btn" id="btn-next" title="Próximo Slide (Seta Direita / Espaço)">→</button>
    </div>
  </footer>

  <!-- Speaker Notes Drawer (Toggled with 'N') -->
  <aside class="speaker-drawer" id="speaker-drawer">
    <div class="speaker-header">
      <div class="speaker-badge">
        <span>🎙️</span> NOTAS DO APRESENTADOR & ROTEIRO
      </div>
      <button style="background: none; border: none; color: var(--text-muted); cursor: pointer; font-size: 1.1rem;" id="btn-close-notes">✕</button>
    </div>
    <div style="display: flex; gap: 0.6rem; font-size: 0.78rem;">
      <span class="hero-badge" id="notes-speaker-pill">Orador: Josué Jofre</span>
      <span class="hero-badge" id="notes-time-pill" style="color: var(--amber-accent);">Tempo Recomendado: 4 min</span>
    </div>
    <div class="speaker-content" id="speaker-notes-body">
      Selecione um slide para visualizar as recomendações de oratória, pontos-chave de ênfase e ganchos para manter as 2 horas dinâmicas e envolventes.
    </div>
  </aside>

  <!-- Slide Grid Modal (Toggled with 'G') -->
  <div class="grid-modal" id="grid-modal">
    <div class="grid-modal-header">
      <div style="font-family: var(--font-display); font-size: 1.5rem; font-weight: 800; color: #fff;">
        ⊞ Visão Geral dos 29 Slides do Seminário
      </div>
      <button class="deck-btn" id="btn-close-grid">✕ Fechar Grade (Esc)</button>
    </div>
    <div class="slide-cards-grid" id="slide-thumbnails-grid">
      <!-- Generated via JS -->
    </div>
  </div>

  <!-- Keyboard hints -->
  <div class="shortcuts-hint">
    <span>Atalhos:</span>
    <span class="kbd">←</span> <span class="kbd">→</span> Navegar
    <span class="kbd">N</span> Notas
    <span class="kbd">G</span> Grade
    <span class="kbd">F</span> Tela Cheia
  </div>

  <!-- Interactive JavaScript -->
  <script>
    /* Speaker notes dictionary for each of the 29 slides */
    const speakerNotesData = {
      1: {
        speaker: "Grupo Inteiro / Josué Jofre",
        time: "3 minutos",
        notes: `
          <strong>Abertura e Boas-Vindas:</strong><br>
          • Cumprimente a Profª Iraci, o Prof. Ueta e todos os colegas da turma.<br>
          • Apresente a equipe do Grupo 5 e ressalte a singularidade desta apresentação: vamos unir o rigor das teorias seminais com a experiência viva e empírica do PIT São José dos Campos.<br>
          • Alerte que o seminário é interativo e que haverá uma dinâmica de tomada de decisão com votação ao vivo da turma.
        `
      },
      2: {
        speaker: "Josué Jofre",
        time: "5 minutos",
        notes: `
          <strong>Gestão dos 120 Minutos:</strong><br>
          • Explique a disciplina de tempo: 6 blocos teóricos (15 min cada), 1 bloco de entrevista prática (15 min), 1 bloco de dinâmica interativa (15-20 min) e sessão de debate.<br>
          • Demonstre para os professores o cumprimento integral de todas as referências exigidas na ementa e na planilha de divisão do seminário.
        `
      },
      3: {
        speaker: "Josué Jofre",
        time: "4 minutos",
        notes: `
          <strong>Por que o PIT SJC?</strong><br>
          • Conecte a sala à nossa realidade imediata: o campus da UNIFESP onde temos aulas é parte indissociável do PIT.<br>
          • Destaque que o PIT não é uma incubadora comum, mas o maior ecossistema de alta complexidade e densidade militar-aeroespacial do hemisfério sul.
        `
      },
      4: {
        speaker: "Fernando Barreto",
        time: "5 minutos",
        notes: `
          <strong>Bloco 1 - Raízes Teóricas:</strong><br>
          • Explique a virada de Moore (1993): as empresas não competem como ilhas isoladas; elas co-evoluem como predadores e presas em simbiose.<br>
          • Destaque Adner (2006): o risco da inovação não é só técnico; é o risco de co-inovação e de adoção em cadeia.<br>
          • Defina Granstrand & Holgersson (2020) para dar sustentação formal contemporânea.
        `
      },
      5: {
        speaker: "Fernando Barreto",
        time: "5 minutos",
        notes: `
          <strong>Bloco 1 - Cienciometria (Shen et al.):</strong><br>
          • Mostre o mapa cienciométrico: o campo explodiu após 2014.<br>
          • Destaque os 3 grandes clusters: plataformas digitais, sistemas espaciais/regionais e governança do orquestrador.<br>
          • Provoque a sala sobre a lacuna apontada por Shen: quase ninguém estuda como ecossistemas morrem ou enfrentam crises severas.
        `
      },
      6: {
        speaker: "Fernando Barreto",
        time: "5 minutos",
        notes: `
          <strong>Bloco 1 - Diferenciação Conceitual Rígida:</strong><br>
          • Atenção redobrada para a banca docente: diferencie claramente ecossistema de cluster (Porter), de rede contratual (Powell) e de sistema nacional (Lundvall).<br>
          • Enfatize: o PIT é cluster geograficamente, mas só é ecossistema porque há interdependência na proposta de valor de novos produtos aeroespaciais.
        `
      },
      7: {
        speaker: "Fábio Lippi",
        time: "5 minutos",
        notes: `
          <strong>Bloco 2 - Anatomia do Ecossistema (Machado et al.):</strong><br>
          • Apresente a heterogeneidade: empresas âncora (Embraer), EBTs, universidades e fundos têm lógicas institucionais opostas.<br>
          • O papel do orquestrador é criar uma "linguagem comum" que permita a esses atores dialogarem sem fricção destrutiva.
        `
      },
      8: {
        speaker: "Fábio Lippi",
        time: "5 minutos",
        notes: `
          <strong>Bloco 2 - As Hélices:</strong><br>
          • Passeie pelo diagrama SVG interativo na tela.<br>
          • Mostre como a Tríplice Hélice clássica (governo-academia-empresa) precisou ser ampliada para a Quádrupla (sociedade/cidadão) e Quíntupla (sustentabilidade/SAF).
        `
      },
      9: {
        speaker: "Fábio Lippi",
        time: "5 minutos",
        notes: `
          <strong>Bloco 2 - Co-criação de Valor:</strong><br>
          • Explique o conceito de superaditividade (1+1 > 2).<br>
          • Alerte sobre o dilema crucial: se uma grande corporação tenta capturar 100% dos ganhos, as startups e a universidade abandonam o ecossistema.
        `
      },
      10: {
        speaker: "Josué Jofre",
        time: "5 minutos",
        notes: `
          <strong>Bloco 3 - Governança e Orquestração (Machado et al.):</strong><br>
          • O cerne do Bloco 3: quem manda quando ninguém pode mandar?<br>
          • Explique por que a teoria de custos de transação de Williamson falha aqui: a Embraer não pode comprar a UNIFESP nem a Prefeitura. A resposta é a orquestração relacional.
        `
      },
      11: {
        speaker: "Josué Jofre",
        time: "5 minutos",
        notes: `
          <strong>Bloco 3 - As 5 Dimensões de Dhanaraj & Parkhe:</strong><br>
          • Detalhe cada uma das 5 dimensões: Mobilidade do conhecimento, Apropriabilidade, Estabilidade da rede, Roadmapping e Resolução de conflitos culturais.<br>
          • Exemplifique como o PIT atua como tradutor cultural entre o tempo acadêmico e o corporativo.
        `
      },
      12: {
        speaker: "Josué Jofre",
        time: "5 minutos",
        notes: `
          <strong>Bloco 3 - Competências Dinâmicas do Orquestrador:</strong><br>
          • Destaque o tripé de Machado et al.: Competência Cognitiva (enxergar o futuro), Relacional (construir confiança) e Estrutural (gerir laboratórios e recursos).<br>
          • Conclusão de impacto: o parque que é apenas imobiliária que aluga salas está fadado ao fracasso.
        `
      },
      13: {
        speaker: "Veridiany / Lilian",
        time: "5 minutos",
        notes: `
          <strong>Bloco 4 - Construção Deliberada (Furr & Shipilov):</strong><br>
          • Desmonte o mito de que o Vale do Silício surgiu ao acaso.<br>
          • Apresente os passos estratégicos de Furr & Shipilov para desenhar a arquitetura certa de um ecossistema.
        `
      },
      14: {
        speaker: "Veridiany / Lilian",
        time: "5 minutos",
        notes: `
          <strong>Bloco 4 - Centralizado vs Adaptativo:</strong><br>
          • Explique a tabela 2x2: ecossistemas centralizados (alta coordenação, incerteza moderada) vs adaptativos (federados, incerteza radical).<br>
          • Mostre que o PIT SJC adota modelo bi-modal: centralizado na certificação de defesa e adaptativo nas startups do Nexus.
        `
      },
      15: {
        speaker: "Veridiany / Lilian",
        time: "5 minutos",
        notes: `
          <strong>Bloco 4 - Coopetição e Parceiros Não Convencionais:</strong><br>
          • Explique como concorrentes diretos cooperam no estágio pré-competitivo do APL Aeroespacial.<br>
          • Cite a regra de ouro de Furr & Shipilov sobre criar valor antes de tentar capturá-lo.
        `
      },
      16: {
        speaker: "Nathália / Jéssica",
        time: "5 minutos",
        notes: `
          <strong>Bloco 5 - Caso San Diego (Majava & Rinkinen):</strong><br>
          • Apresente a transformação histórica de San Diego: de base naval militar em crise nos anos 1970 para capital global de biotecnologia e telecomunicações sem fio.<br>
          • Ressalte o papel da UC San Diego, Salk Institute e Scripps Research.
        `
      },
      17: {
        speaker: "Nathália / Jéssica",
        time: "5 minutos",
        notes: `
          <strong>Bloco 5 - O Programa CONNECT e a Beach Culture:</strong><br>
          • Enfatize o papel pioneiro do CONNECT em orquestrar a região.<br>
          • Explique a 'Beach Culture': baixa formalidade, informalidade cooperativa e a ética do "Pay it Forward" como alavancas de capital social.
        `
      },
      18: {
        speaker: "Josué Jofre / Marciele",
        time: "5 minutos",
        notes: `
          <strong>Caso PIT São José dos Campos:</strong><br>
          • Mostre a linha do tempo brasileira: do sonho visionário de Casimiro Montenegro (CTA/ITA) à criação da Embraer e ao credenciamento como 1º Parque Tecnológico de SP no SPTec em 2006.<br>
          • Exiba os números robustos: mais de 300 empresas, 80 startups no Nexus, R$ 2.8B em projetos.
        `
      },
      19: {
        speaker: "Josué Jofre / Marciele",
        time: "5 minutos",
        notes: `
          <strong>Anatomia Operacional do PIT:</strong><br>
          • Explique como operam os APLs Aeroespacial e de TIC, o Nexus Hub e os laboratórios multiusuários da EMBRAPII.<br>
          • Destaque o papel do ICT-UNIFESP como fornecedor de ciência de fronteira em computação, materiais e saúde.
        `
      },
      20: {
        speaker: "Fernando / Josué",
        time: "5 minutos",
        notes: `
          <strong>Benchmarking Cruzado (San Diego vs PIT SJC):</strong><br>
          • Compare ponto a ponto na tabela.<br>
          • Destaque a semelhança na gênese de defesa e no orquestrador neutro.<br>
          • Aponte o grande desafio do PIT em relação a San Diego: a atração de capital de risco privado e a superação da aversão cultural ao erro acadêmico.
        `
      },
      21: {
        speaker: "Grupo Inteiro",
        time: "15 minutos",
        notes: `
          <strong>Exibição dos Destaques da Entrevista Gravada:</strong><br>
          • Apresente a entrevista com Ricardo Almeida (Diretor de Parcerias do PIT).<br>
          • Toque os trechos selecionados no player interativo da tela.<br>
          • Chame a atenção da Profª Iraci e do Prof. Ueta para como a teoria de orquestração se confirma nas palavras do diretor.
        `
      },
      22: {
        speaker: "Grupo Inteiro",
        time: "5 minutos",
        notes: `
          <strong>Síntese dos 4 Ensinamentos Práticos da Entrevista:</strong><br>
          • Enfatize a denúncia prática: a morosidade burocrática dos contratos de PI afasta mais empresas que a falta de dinheiro.<br>
          • Explique a solidão das Deep Techs e a necessidade de capital paciente.<br>
          • Reafirme: o contato presencial no café do PIT ainda é o maior catalisador de inovação.
        `
      },
      23: {
        speaker: "Renato Paschoal",
        time: "5 minutos",
        notes: `
          <strong>Bloco 6 - Desafios e Limitações (Shen et al.):</strong><br>
          • Análise crítica e rigorosa: o problema de demarcar fronteiras difusas.<br>
          • O desafio da causalidade reversa: foi o PIT que criou as empresas ou foram as empresas que criaram o PIT?<br>
          • Os limites da metáfora biológica: ecossistemas humanos têm jogos de poder e interesses assimétricos.
        `
      },
      24: {
        speaker: "Renato Paschoal",
        time: "5 minutos",
        notes: `
          <strong>Bloco 6 - O Dark Side dos Ecossistemas:</strong><br>
          • Alerte sobre os perigos reais: monopólio e dependência excessiva de uma corporação âncora.<br>
          • O risco de predação de talentos (fuga de cérebros) e a gentrificação do entorno.<br>
          • A necessidade do orquestrador atuar como árbitro ético e protetor dos atores mais vulneráveis.
        `
      },
      25: {
        speaker: "Grupo Inteiro",
        time: "5 minutos",
        notes: `
          <strong>Lançamento do Jogo de Tomada de Decisões:</strong><br>
          • Convide a turma e os professores a apontarem a câmera do celular para o QR Code na tela.<br>
          • Enfatize a proposta do grupo: não é uma prova de múltipla escolha ou quiz convencional; é um game de dilemas sem resposta certa ou errada.<br>
          • Avise que cada um terá 5 minutos para responder individualmente aos 5 dilemas no smartphone e descobrir seu Arquétipo de Orquestrador.<br>
          • Inicie o cronômetro de 5 minutos na tela.
        `
      },
      26: {
        speaker: "Grupo Inteiro",
        time: "15 minutos",
        notes: `
          <strong>Roda de Conversa e Debriefing dos Arquétipos:</strong><br>
          • Com todos com os celulares em mãos, pergunte: 'Quem aqui tirou o perfil Pragmático Corporativo?'. Vá clicando nos botões '+' para registrar a contagem da sala na tela.<br>
          • Em seguida, chame alguns voluntários: 'Por que você decidiu ceder a patente para a Embraer?', 'E quem protegeu a UNIFESP, como justificou a perda de verba?'.<br>
          • Convide a Profª Iraci e o Prof. Ueta para comentarem como esses dilemas de arquétipos refletem a governança real dos parques tecnológicos no Brasil.
        `
      },
      27: {
        speaker: "Josué / Renato",
        time: "5 minutos",
        notes: `
          <strong>As 5 Leis Estratégicas:</strong><br>
          • Conclua o seminário amarrando todas as pontas da teoria à prática.<br>
          • Reafirme as 5 teses que resumem o seminário de forma executiva e acadêmica impecável.
        `
      },
      28: {
        speaker: "Grupo Inteiro",
        time: "15 minutos",
        notes: `
          <strong>Sessão de Perguntas e Debate (Q&A):</strong><br>
          • Convide expressamente a Profª Iraci de Souza João e o Prof. Antônio Yukio Ueta para seus comentários e questionamentos.<br>
          • Abra para as perguntas dos colegas de mestrado e distribua as respostas de forma articulada entre os integrantes do grupo.
        `
      },
      29: {
        speaker: "Grupo Inteiro",
        time: "2 minutos",
        notes: `
          <strong>Encerramento Formal e Referências:</strong><br>
          • Exiba a bibliografia completa padronizada em ABNT/APA, comprovando o cumprimento de todas as referências exigidas no plano de ensino e na planilha.
        `
      }
    };

    let currentSlide = 1;
    const totalSlides = 29;
    const slides = document.querySelectorAll('.slide');
    const progressBar = document.getElementById('deck-progress');
    const curSlideNumEl = document.getElementById('current-slide-num');
    const blockBadgeEl = document.getElementById('current-block-name');
    const selectBlockEl = document.getElementById('select-block');
    const speakerDrawer = document.getElementById('speaker-drawer');
    const notesSpeakerPill = document.getElementById('notes-speaker-pill');
    const notesTimePill = document.getElementById('notes-time-pill');
    const speakerNotesBody = document.getElementById('speaker-notes-body');
    const gridModal = document.getElementById('grid-modal');
    const thumbnailsGrid = document.getElementById('slide-thumbnails-grid');

    /* Initialize slide display */
    function goToSlide(n) {
      if (n < 1) n = 1;
      if (n > totalSlides) n = totalSlides;
      currentSlide = n;

      slides.forEach((s, idx) => {
        if (idx + 1 === currentSlide) {
          s.classList.add('active');
        } else {
          s.classList.remove('active');
        }
      });

      // Update progress bar
      const pct = ((currentSlide - 1) / (totalSlides - 1)) * 100;
      progressBar.style.width = pct + '%';

      // Update footer info
      curSlideNumEl.textContent = currentSlide < 10 ? '0' + currentSlide : currentSlide;
      
      const activeSlideEl = slides[currentSlide - 1];
      const blockName = activeSlideEl.getAttribute('data-block') || 'Geral';
      const speakerName = activeSlideEl.getAttribute('data-speaker') || 'Grupo';
      blockBadgeEl.textContent = blockName;
      selectBlockEl.value = currentSlide;

      // Update speaker notes
      const noteData = speakerNotesData[currentSlide] || { speaker: speakerName, time: "5 min", notes: "Sem notas específicas cadastradas." };
      notesSpeakerPill.textContent = 'Orador: ' + noteData.speaker;
      notesTimePill.textContent = 'Tempo Recomendado: ' + noteData.time;
      speakerNotesBody.innerHTML = noteData.notes;

      // Update thumbnails active state
      document.querySelectorAll('.slide-thumbnail').forEach(t => {
        if (parseInt(t.dataset.slideNum) === currentSlide) {
          t.classList.add('active');
        } else {
          t.classList.remove('active');
        }
      });
    }

    function nextSlide() {
      goToSlide(currentSlide + 1);
    }

    function prevSlide() {
      goToSlide(currentSlide - 1);
    }

    /* Event Listeners for Nav buttons */
    document.getElementById('btn-next').addEventListener('click', nextSlide);
    document.getElementById('btn-prev').addEventListener('click', prevSlide);

    selectBlockEl.addEventListener('change', (e) => {
      goToSlide(parseInt(e.target.value));
    });

    /* Keyboard Navigation */
    window.addEventListener('keydown', (e) => {
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA' || e.target.tagName === 'SELECT') return;

      switch(e.key) {
        case 'ArrowRight':
        case 'ArrowDown':
        case ' ':
        case 'PageDown':
          e.preventDefault();
          nextSlide();
          break;
        case 'ArrowLeft':
        case 'ArrowUp':
        case 'PageUp':
          e.preventDefault();
          prevSlide();
          break;
        case 'Home':
          e.preventDefault();
          goToSlide(1);
          break;
        case 'End':
          e.preventDefault();
          goToSlide(totalSlides);
          break;
        case 'n':
        case 'N':
          e.preventDefault();
          toggleSpeakerNotes();
          break;
        case 'g':
        case 'G':
          e.preventDefault();
          toggleGridView();
          break;
        case 'f':
        case 'F':
          e.preventDefault();
          toggleFullscreen();
          break;
        case 'Escape':
          gridModal.classList.remove('open');
          speakerDrawer.classList.remove('open');
          break;
      }
    });

    /* Speaker Notes Drawer Toggling */
    function toggleSpeakerNotes() {
      speakerDrawer.classList.toggle('open');
      document.getElementById('btn-speaker-notes').classList.toggle('active', speakerDrawer.classList.contains('open'));
    }

    document.getElementById('btn-speaker-notes').addEventListener('click', toggleSpeakerNotes);
    document.getElementById('btn-close-notes').addEventListener('click', () => {
      speakerDrawer.classList.remove('open');
      document.getElementById('btn-speaker-notes').classList.remove('active');
    });

    /* Grid View Modal */
    function buildThumbnailsGrid() {
      thumbnailsGrid.innerHTML = '';
      slides.forEach((s, idx) => {
        const num = idx + 1;
        const block = s.getAttribute('data-block') || '';
        const titleEl = s.querySelector('.slide-title');
        const titleText = titleEl ? titleEl.innerText.replace(/\\n/g, ' ') : ('Slide ' + num);
        
        const card = document.createElement('div');
        card.className = 'slide-thumbnail' + (num === currentSlide ? ' active' : '');
        card.dataset.slideNum = num;
        card.innerHTML = `
          <div class="thumb-num">SLIDE \${num < 10 ? '0' + num : num}</div>
          <div class="thumb-title">\${titleText.length > 48 ? titleText.substring(0, 48) + '...' : titleText}</div>
          <div class="thumb-block">🏷️ \${block}</div>
        `;
        card.addEventListener('click', () => {
          goToSlide(num);
          gridModal.classList.remove('open');
        });
        thumbnailsGrid.appendChild(card);
      });
    }

    function toggleGridView() {
      gridModal.classList.toggle('open');
      if (gridModal.classList.contains('open')) {
        buildThumbnailsGrid();
      }
    }

    document.getElementById('btn-grid-view').addEventListener('click', toggleGridView);
    document.getElementById('btn-close-grid').addEventListener('click', () => {
      gridModal.classList.remove('open');
    });

    /* Fullscreen Toggle */
    function toggleFullscreen() {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(err => {
          console.warn('Fullscreen error:', err);
        });
      } else {
        if (document.exitFullscreen) {
          document.exitFullscreen();
        }
      }
    }
    document.getElementById('btn-fullscreen').addEventListener('click', toggleFullscreen);

    /* Master 120-minute Seminar Clock */
    let clockSeconds = 0;
    let clockRunning = false;
    let clockInterval = null;
    const clockDisplay = document.getElementById('clock-display');
    const clockBtn = document.getElementById('btn-toggle-clock');
    const clockResetBtn = document.getElementById('btn-reset-clock');

    function formatTime(sec) {
      const m = Math.floor(sec / 60);
      const s = sec % 60;
      return (m < 10 ? '0' + m : m) + ':' + (s < 10 ? '0' + s : s);
    }

    function updateClockDisplay() {
      clockDisplay.textContent = formatTime(clockSeconds) + ' / 120:00';
    }

    clockBtn.addEventListener('click', () => {
      if (clockRunning) {
        clearInterval(clockInterval);
        clockRunning = false;
        clockBtn.textContent = '▶';
      } else {
        clockRunning = true;
        clockBtn.textContent = '⏸';
        clockInterval = setInterval(() => {
          clockSeconds++;
          updateClockDisplay();
        }, 1000);
      }
    });

    clockResetBtn.addEventListener('click', () => {
      clearInterval(clockInterval);
      clockRunning = false;
      clockBtn.textContent = '▶';
      clockSeconds = 0;
      updateClockDisplay();
    });

    /* Mock Podcast / Audio Player */
    let audioPlaying = false;
    let audioSec = 255; // 04:15
    let audioInterval = null;
    function toggleAudioMock() {
      const icon = document.getElementById('play-icon');
      const timeEl = document.getElementById('audio-time');
      const waves = document.querySelectorAll('.wave-bar');
      
      if (!audioPlaying) {
        audioPlaying = true;
        icon.textContent = '⏸';
        waves.forEach(w => w.classList.add('active'));
        audioInterval = setInterval(() => {
          audioSec++;
          const m = Math.floor(audioSec / 60);
          const s = audioSec % 60;
          timeEl.textContent = (m < 10 ? '0' + m : m) + ':' + (s < 10 ? '0' + s : s) + ' / 22:40';
        }, 1000);
      } else {
        audioPlaying = false;
        icon.textContent = '▶';
        waves.forEach(w => w.classList.remove('active'));
        clearInterval(audioInterval);
      }
    }

    /* Interactive Dilemma Simulator Logic */
    const dilemmas = {
      1: {
        title: "Cenário 1: Conflito de Propriedade Intelectual (Patente Fechada vs Publicação Aberta)",
        desc: "Um laboratório da UNIFESP e uma startup do Nexus desenvolveram um algoritmo de rota para drones que reduz em 40% a bateria. A Embraer oferece financiar R$ 5 milhões para transformar o projeto em escala industrial, porém exige exclusividade total mundial de 10 anos e cláusula de sigilo estrito que proíbe o mestrando de publicar sua dissertação nos próximos 3 anos. O que o PIT faz?",
        optA: {
          title: "Opção A: Aceitar a Exigência da Grande Corporação",
          desc: "Garante os R$ 5 milhões imediatos e o produto voando em escala real, mas sacrifica a dissertação acadêmica e gera revolta entre os pesquisadores da universidade.",
          cohesion: 48,
          innovation: 70,
          finance: 92,
          feedback: "⚠️ A corporação financiou o projeto, mas docentes e alunos da UNIFESP romperam parcerias por sensação de desapropriação predatória."
        },
        optB: {
          title: "Opção B: Orquestrar Acordo de Inovação Aberta Híbrido",
          desc: "O PIT negocia: a corporação tem licença preferencial comercial, o código-fonte essencial é patenteado em cotitularidade e a dissertação é publicada com dados anonimizados após 6 meses.",
          cohesion: 94,
          innovation: 89,
          finance: 84,
          feedback: "🌟 Sucesso de Orquestração! O PIT equilibrou os interesses da Hélice: ciência preservada, royalties garantidos e tecnologia no mercado."
        }
      },
      2: {
        title: "Cenário 2: Fundo de Investimento Estrangeiro com Cláusula de Lock-in",
        desc: "Um grande fundo de Venture Capital da Ásia propõe injetar R$ 30 milhões no Nexus para selecionar 10 startups de cibersegurança e defesa, sob a condição de que toda a PI futura seja transferida para uma holding no exterior. Como o PIT deve se posicionar?",
        optA: {
          title: "Opção A: Aprovar o Fundo Sem Restrições",
          desc: "Injeta capital massivo no Nexus e atrai holofotes globais, mas arrisca evasão de propriedade intelectual crítica e desmonte da soberania tecnológica brasileira.",
          cohesion: 55,
          innovation: 65,
          finance: 95,
          feedback: "🚨 Alerta de Soberania! O DCTA e as Forças Armadas bloquearam projetos no parque por vazamento de tecnologias sensíveis."
        },
        optB: {
          title: "Opção B: Condicionar o Investimento a Consórcio Mútuo Nacional",
          desc: "Exigir que a holding mantenha a cotitularidade de patentes no Brasil e atrair a Finep / BNDES para co-investir na rodada com direitos de golden share.",
          cohesion: 90,
          innovation: 92,
          finance: 80,
          feedback: "✅ Equilíbrio Estratégico! O ecossistema protegeu seus ativos críticos e garantiu liquidez internacional sustentável."
        }
      },
      3: {
        title: "Cenário 3: Colapso do Fundo Público de Subvenção no Nexus",
        desc: "Um corte orçamentário federal extingue o edital de subvenção que financiava as bolsas de 25 startups de biotecnologia e materiais avançados no Nexus. Como o PIT evita a falência em massa dessas deep techs?",
        optA: {
          title: "Opção A: Cobrar Mensalidades das Startups para Manter o Hub",
          desc: "Preserva a receita imediata da associação gestora do PIT, mas força 80% das startups em estágio inicial a fecharem as portas ou migrarem de cidade.",
          cohesion: 35,
          innovation: 40,
          finance: 72,
          feedback: "❌ Desastre Sistêmico! O Vale da Morte ceifou as deep techs mais promissoras do parque por falta de oxigênio financeiro."
        },
        optB: {
          title: "Opção B: Criar Fundo Mútuo de CVC com o APL Aeroespacial e TIC",
          desc: "O PIT reúne Embraer, Ericsson e multinacionais para cotizarem um fundo de Corporate Venture com abatimento de ISS e contrapartida de fornecimento tecnológico.",
          cohesion: 96,
          innovation: 94,
          finance: 88,
          feedback: "🚀 Vitória do Ecossistema! As startups sobreviveram e as grandes empresas ganharam acesso prioritário a tecnologias de ponta."
        }
      }
    };

    let activeDilemma = 1;

    function selectDilemma(id) {
      activeDilemma = id;
      document.querySelectorAll('.dilemma-btn').forEach((b, idx) => {
        b.classList.toggle('active', idx + 1 === id);
      });

      const d = dilemmas[id];
      document.getElementById('dilemma-title').textContent = d.title;
      document.getElementById('dilemma-desc').textContent = d.desc;

      const optAEl = document.getElementById('opt-a');
      const optBEl = document.getElementById('opt-b');
      optAEl.classList.remove('selected');
      optBEl.classList.remove('selected');

      optAEl.querySelector('strong').textContent = d.optA.title;
      optAEl.querySelector('p').textContent = d.optA.desc;

      optBEl.querySelector('strong').textContent = d.optB.title;
      optBEl.querySelector('p').textContent = d.optB.desc;

      document.getElementById('sim-feedback').textContent = "Aguardando deliberação da sala para o Cenário " + id + "...";
    }

    function chooseOption(opt) {
      const d = dilemmas[activeDilemma];
      const optData = opt === 'A' ? d.optA : d.optB;

      document.getElementById('opt-a').classList.toggle('selected', opt === 'A');
      document.getElementById('opt-b').classList.toggle('selected', opt === 'B');

      document.getElementById('metric-cohesion').textContent = optData.cohesion + '%';
      document.getElementById('metric-innovation').textContent = optData.innovation + '%';
      document.getElementById('metric-finance').textContent = optData.finance + '%';

      document.getElementById('sim-feedback').innerHTML = optData.feedback;
    }

    /* Debate timer for classroom activity */
    let debateSec = 120;
    let debateRunning = false;
    let debateInterval = null;
    function toggleDebateTimer() {
      const display = document.getElementById('debate-timer');
      if (!debateRunning) {
        debateRunning = true;
        debateInterval = setInterval(() => {
          if (debateSec > 0) {
            debateSec--;
            const m = Math.floor(debateSec / 60);
            const s = debateSec % 60;
            display.textContent = (m < 10 ? '0' + m : m) + ':' + (s < 10 ? '0' + s : s);
            if (debateSec <= 20) {
              display.style.color = 'var(--rose-accent)';
            }
          } else {
            clearInterval(debateInterval);
            display.textContent = 'TEMPO ESGOTADO!';
            debateRunning = false;
          }
        }, 1000);
      } else {
        clearInterval(debateInterval);
        debateRunning = false;
      }
    }

    
    /* Game Countdown Timer on Slide 25 */
    let gameSec = 300;
    let gameRunning = false;
    let gameInterval = null;
    function toggleGameTimer() {
      const display = document.getElementById('countdown-game');
      const btn = document.getElementById('btn-timer-game');
      if (!gameRunning) {
        gameRunning = true;
        btn.innerHTML = '<span>⏸</span> Pausar';
        gameInterval = setInterval(() => {
          if (gameSec > 0) {
            gameSec--;
            const m = Math.floor(gameSec / 60);
            const s = gameSec % 60;
            display.textContent = (m < 10 ? '0' + m : m) + ':' + (s < 10 ? '0' + s : s);
          } else {
            clearInterval(gameInterval);
            display.textContent = 'TEMPO ESGOTADO!';
            btn.innerHTML = '<span>↺</span> Reiniciar';
            gameRunning = false;
          }
        }, 1000);
      } else {
        clearInterval(gameInterval);
        btn.innerHTML = '<span>▶</span> Continuar';
        gameRunning = false;
      }
    }

    /* Interactive Tally for Debriefing on Slide 26 */
    const tallyScores = {
      corp: 0,
      academia: 0,
      deeptech: 0,
      esg: 0,
      diplomat: 0,
      community: 0
    };

    function adjustTally(key, delta) {
      tallyScores[key] = Math.max(0, tallyScores[key] + delta);
      document.getElementById('tally-' + key).textContent = tallyScores[key];
    }

    // Initialize presentation on load
    window.addEventListener('DOMContentLoaded', () => {
      goToSlide(1);
    });
  </script>
</body>
</html>
'''

output_path = r"C:\Users\jj\OneDrive\Estudos\Edital unifesp PIT 2026\Disciplinas 02 2026\Gestão estratégica da inovação\Seminário\apresentacao_seminario_ecossistema_pit.html"

with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Presentation generated successfully at: {output_path}")
print(f"File size: {os.path.getsize(output_path):,} bytes")
