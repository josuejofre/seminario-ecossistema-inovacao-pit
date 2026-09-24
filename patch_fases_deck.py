# -*- coding: utf-8 -*-
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
gen_path = os.path.join(script_dir, "generate_35_slide_deck.py")

with open(gen_path, "r", encoding="utf-8") as f:
    code = f.read()

replacements = [
    ("🎮 MOMENTO KAHOOT RPG • BLOCO 1", "🎮 MOMENTO KAHOOT RPG • FASE 1"),
    ("Desafio da Estação: <span>Bloco Acadêmico UNIFESP</span>", "Desafio da Fase 1: <span>Bloco Acadêmico UNIFESP</span>"),
    ("Estação 1 de 6 • Teoria & Moore (1993)", "FASE 1 DE 6 • Bloco Acadêmico UNIFESP"),
    ("Aguardando respostas da turma para o Bloco 1...", "Aguardando respostas da turma para a Fase 1..."),

    ("🎮 MOMENTO KAHOOT RPG • BLOCO 2", "🎮 MOMENTO KAHOOT RPG • FASE 2"),
    ("Desafio da Estação: <span>Praça Central das Hélices</span>", "Desafio da Fase 2: <span>Praça Central das Hélices</span>"),
    ("Estação 2 de 6 • Heterogeneidade & Redes", "FASE 2 DE 6 • Praça Central das Hélices"),
    ("Aguardando respostas da turma para o Bloco 2...", "Aguardando respostas da turma para a Fase 2..."),

    ("🎮 MOMENTO KAHOOT RPG • BLOCO 3", "🎮 MOMENTO KAHOOT RPG • FASE 3"),
    ("Desafio da Estação: <span>Centro de Governança do PIT</span>", "Desafio da Fase 3: <span>Centro de Governança do PIT</span>"),
    ("Estação 3 de 6 • Machado et al. (2025)", "FASE 3 DE 6 • Centro de Governança do PIT"),
    ("Aguardando respostas da turma para o Bloco 3...", "Aguardando respostas da turma para a Fase 3..."),

    ("🎮 MOMENTO KAHOOT RPG • BLOCO 4", "🎮 MOMENTO KAHOOT RPG • FASE 4"),
    ("Desafio da Estação: <span>Nexus Hub de Startups</span>", "Desafio da Fase 4: <span>Nexus Hub de Startups</span>"),
    ("Estação 4 de 6 • Furr & Shipilov (MIT)", "FASE 4 DE 6 • Nexus Hub de Startups"),
    ("Aguardando respostas da turma para o Bloco 4...", "Aguardando respostas da turma para a Fase 4..."),

    ("🎮 MOMENTO KAHOOT RPG • BLOCO 5", "🎮 MOMENTO KAHOOT RPG • FASE 5"),
    ("Desafio da Estação: <span>Pavilhão Aeroespacial & San Diego</span>", "Desafio da Fase 5: <span>Pavilhão Aeroespacial & San Diego</span>"),
    ("Estação 5 de 6 • Benchmarking San Diego", "FASE 5 DE 6 • Pavilhão Aeroespacial & San Diego"),
    ("Aguardando respostas da turma para o Bloco 5...", "Aguardando respostas da turma para a Fase 5..."),

    ("🎮 MOMENTO KAHOOT RPG • BLOCO 6", "🎮 MOMENTO KAHOOT RPG • FASE 6"),
    ("Desafio da Estação: <span>Living Lab Net-Zero & Fronteiras</span>", "Desafio da Fase 6: <span>Living Lab Net-Zero & Fronteiras</span>"),
    ("Estação 6 de 6 • Shen et al. & Fronteiras", "FASE 6 DE 6 • Living Lab Net-Zero & Fronteiras"),
    ("Aguardando respostas da turma para o Bloco 6...", "Aguardando respostas da turma para a Fase 6..."),

    # Slide 2 Agenda badges
    ("<div class=\"chips-row\"><span class=\"chip-badge\">Bloco 1 • 15 min</span></div>", "<div class=\"chips-row\"><span class=\"chip-badge\">Bloco 1 • Fase 1 RPG • 15 min</span></div>"),
    ("<div class=\"chips-row\"><span class=\"chip-badge\">Bloco 2 • 15 min</span></div>", "<div class=\"chips-row\"><span class=\"chip-badge\">Bloco 2 • Fase 2 RPG • 15 min</span></div>"),
    ("<div class=\"chips-row\"><span class=\"chip-badge\">Bloco 3 • 15 min</span></div>", "<div class=\"chips-row\"><span class=\"chip-badge\">Bloco 3 • Fase 3 RPG • 15 min</span></div>"),
    ("<div class=\"chips-row\"><span class=\"chip-badge\">Bloco 4 • 15 min</span></div>", "<div class=\"chips-row\"><span class=\"chip-badge\">Bloco 4 • Fase 4 RPG • 15 min</span></div>"),
    ("<div class=\"chips-row\"><span class=\"chip-badge\">Bloco 5 • 20 min</span></div>", "<div class=\"chips-row\"><span class=\"chip-badge\">Bloco 5 • Fase 5 RPG • 20 min</span></div>"),
    ("<div class=\"chips-row\"><span class=\"chip-badge\">Bloco 6 • 15 min</span></div>", "<div class=\"chips-row\"><span class=\"chip-badge\">Bloco 6 • Fase 6 RPG • 15 min</span></div>")
]

for old, new in replacements:
    code = code.replace(old, new)

with open(gen_path, "w", encoding="utf-8") as f:
    f.write(code)

print(f"Updated {gen_path}")
