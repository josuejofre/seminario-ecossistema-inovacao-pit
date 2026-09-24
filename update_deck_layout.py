# -*- coding: utf-8 -*-
import re

with open('generate_35_slide_deck.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove Cockpit Admin from top header
content = re.sub(
    r'<a href="admin\.html" target="_blank" class="deck-btn"><span>⚙️</span> Cockpit Admin</a>\s*',
    '',
    content
)

# 2. Remove Cockpit Admin card from the Kahoot slides (Slide 7, 13, 19, 24, 29, 34)
kahoot_admin_card_regex = r'<div class="card" style="padding: 1rem; display: flex; flex-direction: column; gap: 0\.6rem;">\s*<div style="font-family: var\(--font-display\); font-size: 0\.85rem; font-weight: 700; color: #fff; display: flex; align-items: center; gap: 0\.5rem;">\s*<span>⚡</span> Painel do Apresentador\s*</div>\s*<a href="admin\.html" target="_blank" class="deck-btn" style="[^"]*">\s*<span>⚙️</span> Abrir Cockpit Admin \(Fase \d+\)\s*</a>\s*<div style="font-size: 0\.7rem; color: var\(--text-muted\); text-align: center;">\s*Pressione <strong>N</strong> para ver suas anotações de fala\.\s*</div>\s*</div>'

student_help_card = '''<div class="card" style="padding: 1.25rem; display: flex; flex-direction: column; justify-content: center; gap: 0.65rem; border-color: rgba(6, 182, 212, 0.3); background: rgba(6, 182, 212, 0.05);">
            <div style="font-family: var(--font-display); font-size: 1.05rem; font-weight: 800; color: #fff; display: flex; align-items: center; gap: 0.6rem;">
              <span>📱</span> Como Responder no Celular:
            </div>
            <div style="font-size: 0.95rem; color: #cbd5e1; line-height: 1.5;">
              1. Abra <strong>jogo.html</strong> no seu smartphone<br>
              2. Caminhe até a estação ativa no campus<br>
              3. Responda antes do tempo esgotar!
            </div>
            <div style="font-size: 0.82rem; color: var(--cyan-light); font-weight: 700; margin-top: 0.2rem;">
              ⚡ Sincronizado ao vivo via Firebase!
            </div>
          </div>'''

content = re.sub(kahoot_admin_card_regex, student_help_card, content)

# 3. Update CSS in generate_35_slide_deck.py for maximum space usage and large typography
old_css_grids = '''    /* Layout Grids */
    .grid-2 { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1.1rem; }
    .grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.1rem; }
    .grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; }

    /* Cards */
    .card {
      background: var(--bg-card);
      border: 1px solid var(--border-soft);
      border-radius: var(--radius-md);
      padding: 1.15rem 1.35rem;
      backdrop-filter: blur(12px);
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
      transition: all 0.2s ease;
      position: relative;
      overflow: hidden;
    }'''

new_css_grids = '''    /* Dynamic Full-Height Layout Grids */
    .slide {
      position: absolute;
      inset: 1.25rem 2.5rem;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      gap: 1.15rem;
      opacity: 0;
      transform: scale(0.98) translateY(12px);
      pointer-events: none;
      transition: opacity 0.35s cubic-bezier(0.16, 1, 0.3, 1), transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      overflow-y: auto;
      max-width: 1440px;
      margin: 0 auto;
      height: calc(100% - 2.5rem);
    }

    .slide-title {
      font-family: var(--font-display);
      font-size: 2.35rem;
      font-weight: 800;
      line-height: 1.15;
      letter-spacing: -0.02em;
      color: #fff;
    }

    .punchline-card {
      background: linear-gradient(90deg, rgba(6, 182, 212, 0.15), rgba(37, 99, 235, 0.12));
      border-left: 4px solid var(--cyan-glow);
      border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
      padding: 0.75rem 1.4rem;
      display: flex;
      align-items: center;
      gap: 0.9rem;
    }

    .punchline-quote {
      font-family: var(--font-display);
      font-size: 1.22rem;
      font-weight: 700;
      color: #fff;
      font-style: italic;
    }

    /* 4 Blocks -> 2x2 Grid filling 100% of vertical and horizontal space */
    .grid-4, .grid-2x2 {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      grid-template-rows: repeat(2, 1fr);
      gap: 1.35rem;
      flex: 1;
      min-height: 0;
      width: 100%;
    }

    /* 2 Blocks -> 2 Horizontal Rectangular Banners stacked vertically */
    .grid-2-stacked {
      display: flex;
      flex-direction: column;
      gap: 1.35rem;
      flex: 1;
      min-height: 0;
      width: 100%;
    }

    .grid-2-stacked .card {
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: center;
      padding: 1.8rem 2.4rem;
    }

    .grid-2-stacked .card-title {
      font-size: 1.6rem;
      font-weight: 800;
      margin-bottom: 0.75rem;
    }

    .grid-2-stacked .card-desc {
      font-size: 1.25rem;
      line-height: 1.6;
    }

    .grid-2-stacked .bullet-list li {
      font-size: 1.2rem;
      line-height: 1.55;
    }

    /* 2 Columns Split (Kahoot slides / side-by-side) */
    .grid-2, .grid-split {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 1.35rem;
      flex: 1;
      min-height: 0;
      width: 100%;
    }

    /* 3 Blocks -> 3 Large Columns filling 100% height */
    .grid-3 {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.35rem;
      flex: 1;
      min-height: 0;
      width: 100%;
    }

    .grid-3 .card {
      display: flex;
      flex-direction: column;
      justify-content: center;
      padding: 1.6rem 1.8rem;
    }

    .grid-3 .card-title {
      font-size: 1.4rem;
      font-weight: 800;
      margin-bottom: 0.65rem;
    }

    .grid-3 .card-desc {
      font-size: 1.15rem;
      line-height: 1.5;
    }

    .grid-3 .bullet-list li {
      font-size: 1.08rem;
      line-height: 1.45;
    }

    /* Cards Base */
    .card {
      background: var(--bg-card);
      border: 1px solid var(--border-soft);
      border-radius: var(--radius-md);
      padding: 1.6rem 2rem;
      backdrop-filter: blur(12px);
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
      transition: all 0.2s ease;
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }

    .card-title {
      font-family: var(--font-display);
      font-size: 1.45rem;
      font-weight: 800;
      color: #fff;
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }

    .card-desc {
      font-size: 1.2rem;
      color: var(--text-muted);
      line-height: 1.55;
    }'''

content = content.replace(old_css_grids, new_css_grids)

# 4. In slides with 2 cards that should be stacked horizontally:
# Replace <div class="grid-2"> with <div class="grid-2-stacked"> EXCEPT where grid-template-columns is explicitly defined (like Kahoot slides: style="grid-template-columns: 380px 1fr;...")
content = re.sub(r'<div class="grid-2">(?!\s*style=)', '<div class="grid-2-stacked">', content)

with open('generate_35_slide_deck.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated generate_35_slide_deck.py successfully!")
