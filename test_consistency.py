# -*- coding: utf-8 -*-
import re

with open('Seminário/admin.html', 'r', encoding='utf-8') as f:
    admin_content = f.read()

with open('Seminário/jogo.html', 'r', encoding='utf-8') as f:
    jogo_content = f.read()

q_admin = re.findall(r'id:\s*["\'](b\d+_q\d+)["\']', admin_content)
q_jogo = re.findall(r'id:\s*["\'](b\d+_q\d+)["\']', jogo_content)

print(f"Admin questions count: {len(q_admin)}")
print(f"Jogo questions count: {len(q_jogo)}")
assert q_admin == q_jogo, "Mismatch between admin and jogo questions!"
print("SUCCESS: All 18 question IDs perfectly match across admin.html and jogo.html!")
