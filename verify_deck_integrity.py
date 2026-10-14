import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open(r'02 - Seminário 5 - Ecossistemas de Inovação\Apresentação e Quiz Interativo\index.html', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# 1. Check all slide tags
slides = re.findall(r'<section class=["\']slide.*?["\'](.*?)>(.*?)</section>', text, re.DOTALL)
print(f"Total slides found in HTML: {len(slides)}")

found_slides = []
for idx, (attrs, body) in enumerate(slides, 1):
    num_m = re.search(r'data-slide=["\'](\d+)["\']', attrs)
    num = int(num_m.group(1)) if num_m else idx
    found_slides.append(num)
    block_m = re.search(r'data-block=["\']([^"\']+)["\']', attrs)
    block = block_m.group(1) if block_m else ''
    spk_m = re.search(r'data-speaker=["\']([^"\']+)["\']', attrs)
    spk = spk_m.group(1) if spk_m else ''
    tag_m = re.search(r'<div class=["\']slide-tag["\']>(.*?)</div>', body)
    tag = tag_m.group(1) if tag_m else ''
    title_m = re.search(r'<h[12] class=["\']slide-title["\']>(.*?)</h[12]>', body, re.DOTALL)
    title = re.sub(r'<[^>]+>', '', title_m.group(1)).strip() if title_m else ''
    if not title:
        # maybe Jessica custom title
        j_title = re.search(r'<h2[^>]*>(.*?)</h2>', body, re.DOTALL)
        if j_title:
            title = re.sub(r'<[^>]+>', '', j_title.group(1)).strip()
    print(f"Slide {num:>2}: [{block:<15}] ({spk:<24}) | {title[:60]}")

print("\nChecking slide numbers:")
expected = list(range(1, 45))
print(f"Sequence matches 1 to 44? {found_slides == expected}")
if found_slides != expected:
    print(f"Discrepancy: found={found_slides}")

# 2. Check notesMap
nm_match = re.search(r'const notesMap = \{(.*?)\n    \};', text, re.DOTALL)
if nm_match:
    nm_text = nm_match.group(1)
    keys = [int(k) for k in re.findall(r'(\d+)\s*:', nm_text)]
    print(f"NotesMap total entries: {len(keys)}")
    print(f"NotesMap keys match 1 to 44? {keys == expected}")

# 3. Check totalSlides variable
ts_match = re.search(r'const totalSlides = (\d+);', text)
print(f"const totalSlides in JS: {ts_match.group(1) if ts_match else 'NOT FOUND'}")
