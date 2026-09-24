# -*- coding: utf-8 -*-
import re
import json

with open('jogo.html', 'r', encoding='utf-8') as f:
    jogo_content = f.read()

# Extract question block
q_match = re.search(r'const rawQuestions = (\[.*?\]);\s*/\*\s*Station Coordinates', jogo_content, re.DOTALL)
if not q_match:
    print('Failed to find rawQuestions')
    exit(1)

# Use Node to cleanly parse the JavaScript array into JSON
import subprocess
node_cmd = ["node", "-e", f"""
const fs = require('fs');
const html = fs.readFileSync('jogo.html', 'utf8');
const match = html.match(/const rawQuestions = (\[[\\s\\S]*?\\]);\\s*\\/\\*\\s*Station Coordinates/);
const qs = eval(match[1]);
fs.writeFileSync('temp_qs.json', JSON.stringify(qs, null, 2), 'utf8');
"""]
subprocess.run(node_cmd, check=True)

with open('temp_qs.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

print(f"Loaded {len(questions)} questions")

# Build formatted questions section
lines = []
lines.append("\n" + "=" * 80)
lines.append("BANCO COMPLETO DE PERGUNTAS E RESPOSTAS DO KAHOOT RPG (FASES 1 A 6)")
lines.append("Para revisão da equipe, validação dos professores e conferência dos gabaritos")
lines.append("=" * 80 + "\n")

phase_titles = {
    1: "FASE 1: BLOCO ACADÊMICO UNIFESP (Fundamentos Teóricos & Moore)",
    2: "FASE 2: PRAÇA CENTRAL DAS HÉLICES (As 5 Hélices & Interdependência)",
    3: "FASE 3: CENTRO DE GOVERNANÇA DO PIT (Orquestração & Machado et al.)",
    4: "FASE 4: NEXUS HUB DE STARTUPS (Furr & Shipilov / Criação de Ecossistemas)",
    5: "FASE 5: PAVILHÃO AEROESPACIAL & SAN DIEGO (Benchmarking Internacional & Majava)",
    6: "FASE 6: LIVING LAB NET-ZERO & FRONTEIRAS (Shen et al. / Gargalos & Fronteiras)"
}

for b in range(1, 7):
    b_qs = [q for q in questions if q['block'] == b]
    lines.append("-" * 80)
    lines.append(f"📌 {phase_titles[b].upper()}")
    lines.append("-" * 80)
    for idx, q in enumerate(b_qs):
        lines.append(f"\n[QUESTÃO {idx + 1} - CÓDIGO: {q['id'].upper()}]")
        lines.append(f"ENUNCIADO: {q['question']}")
        lines.append(f"  ✓ [RESPOSTA CORRETA]: {q['correctOption']}")
        lines.append(f"  ✗ [DISTRAÇÃO 1]   : {q['distractors'][0]}")
        lines.append(f"  ✗ [DISTRAÇÃO 2]   : {q['distractors'][1]}")
        lines.append(f"  💡 JUSTIFICATIVA / GABARITO COMENTADO: {q['explanation']}")
    lines.append("")

formatted_q_text = "\n".join(lines)

# Read existing roteiro
with open('roteiro_falas_apresentadores.txt', 'r', encoding='utf-8') as f:
    roteiro = f.read()

# Replace any occurrence of 'fase liberada' in the speeches so the presenter announces it when clicking
roteiro_cleaned = re.sub(
    r"'Atenção turma, fase liberada no seu celular!",
    "'Atenção turma, o desafio está pronto no seu celular!",
    roteiro,
    flags=re.IGNORECASE
)
roteiro_cleaned = re.sub(
    r"Atenção turma, fase liberada",
    "Atenção turma, desafio aberto",
    roteiro_cleaned,
    flags=re.IGNORECASE
)

# Check if the bank is already in roteiro; if so, replace it, else append at end
if "BANCO COMPLETO DE PERGUNTAS E RESPOSTAS DO KAHOOT RPG" in roteiro_cleaned:
    parts = roteiro_cleaned.split("================================================================================\nBANCO COMPLETO DE PERGUNTAS E RESPOSTAS DO KAHOOT RPG")
    final_roteiro = parts[0].rstrip() + "\n\n" + formatted_q_text
else:
    final_roteiro = roteiro_cleaned.rstrip() + "\n\n" + formatted_q_text

with open('roteiro_falas_apresentadores.txt', 'w', encoding='utf-8') as f:
    f.write(final_roteiro)

print("Updated roteiro_falas_apresentadores.txt successfully!")
