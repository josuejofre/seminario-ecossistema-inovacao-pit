# -*- coding: utf-8 -*-
import os
import re
from bs4 import BeautifulSoup

def clean_deck(filepath):
    if not os.path.exists(filepath):
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    slides = soup.find_all('section', class_='slide')

    # Remove duplicated slides based on title
    seen_titles = set()
    cleaned_slides = []
    for s in slides:
        title_el = s.find('h2', class_='slide-title')
        title_txt = title_el.get_text(strip=True) if title_el else ''
        block = s.get('data-block', '')
        key = (title_txt, block)
        if key in seen_titles:
            # duplicate!
            s.decompose()
        else:
            seen_titles.add(key)
            cleaned_slides.append(s)

    # Renumber slides from 1 to N
    for idx, s in enumerate(cleaned_slides, 1):
        s['data-slide'] = str(idx)

    # Convert back to string
    # Replace the container with cleaned slides
    slides_container = soup.find('div', class_='deck-container') or soup.find('main') or soup.body
    # Re-save soup
    new_html = str(soup)

    # Ensure totalSlides is 39
    new_html = re.sub(r'const totalSlides = \d+;', f'const totalSlides = {len(cleaned_slides)};', new_html)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)

    print(f"Cleaned {filepath}: {len(cleaned_slides)} slides")

base_path = r"c:\Users\jj\OneDrive\Estudos\Edital unifesp PIT 2026\Disciplinas 02 2026\Gestão estratégica da inovação"
files = [
    os.path.join(base_path, "02 - Seminário 5 - Ecossistemas de Inovação", "Apresentação e Quiz Interativo", "index.html"),
    os.path.join(base_path, "02 - Seminário 5 - Ecossistemas de Inovação", "Apresentação e Quiz Interativo", "apresentacao_seminario_ecossistema_pit.html"),
    os.path.join(base_path, "Seminário", "index.html"),
    os.path.join(base_path, "Seminário", "apresentacao_seminario_ecossistema_pit.html")
]

for f in files:
    clean_deck(f)
