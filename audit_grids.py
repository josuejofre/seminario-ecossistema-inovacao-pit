# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

slides = re.findall(r'<section class="slide" data-slide="(\d+)"[^>]*>(.*?)</section>', html, re.DOTALL)
print(f"Total slides found: {len(slides)}")

for num, body in slides:
    grids = re.findall(r'class="(grid-[^"]+)"', body)
    cards = len(re.findall(r'class="card', body))
    has_admin_btn = "Abrir Cockpit Admin" in body or "Cockpit Admin" in body
    print(f"Slide {num}: Grids={grids} | Cards={cards} | HasAdminBtn={has_admin_btn}")
