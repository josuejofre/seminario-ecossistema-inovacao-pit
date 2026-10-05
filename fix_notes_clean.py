import os

for fname in ['index.html', 'apresentacao_seminario_ecossistema_pit.html']:
    p = os.path.join(r"c:\Users\jj\OneDrive\Estudos\Edital unifesp PIT 2026\Disciplinas 02 2026\Gestão estratégica da inovação\Seminário", fname)
    with open(p, 'rb') as f:
        data = f.read()
    target = b'amortecedor de choques'
    idx = data.find(target)
    if idx != -1:
        line_start = data.rfind(b'\n', 0, idx) + 1
        line_end = data.find(b'\n', idx) + 1
        replacement = '      30: "Neste momento, apresentamos a nossa atividade empírica de campo no Parque Tecnológico de São José dos Campos, conduzida pelo Renato Paschoal. O objetivo é confrontar os conceitos teóricos de governança e orquestração com a prática real de quem atua na gestão do ecossistema.",\r\n'.encode('utf-8')
        data = data[:line_start] + replacement + data[line_end:]
        with open(p, 'wb') as f:
            f.write(data)
        print(f"Fixed {fname} successfully!")
    else:
        print(f"Not found in {fname}")
