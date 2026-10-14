# -*- coding: utf-8 -*-
"""
Builds a master PowerPoint (.pptx) file for the entire 44-slide presentation:
"Seminario_5_Ecossistemas_Inovacao_Master.pptx"
- 16:9 Widescreen layout
- Dark space theme: background #050A14
- Titles in #E6EEF5 with accents in #3FD0E6 (Cyan) and #10B981 (Emerald)
- Cards and content for all 44 slides
- Embeds official images from assets/lilian and assets/jessica
- Complete speaker notes for each slide matching notesMap
"""

import os
import sys
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

sys.stdout.reconfigure(encoding='utf-8')

prs = pptx.Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6] # blank layout

COLOR_BG = RGBColor(5, 10, 20)       # #050A14
COLOR_SURFACE = RGBColor(10, 19, 36) # #0A1324
COLOR_CARD = RGBColor(15, 23, 42)    # #0F172A
COLOR_TITLE = RGBColor(230, 238, 245)# #E6EEF5
COLOR_CYAN = RGBColor(63, 208, 230)  # #3FD0E6
COLOR_EMERALD = RGBColor(16, 185, 129)# #10B981
COLOR_AMBER = RGBColor(245, 158, 11) # #F59E0B
COLOR_PURPLE = RGBColor(168, 85, 247)# #A855F7
COLOR_MUTED = RGBColor(148, 163, 184)# #94A3B8
COLOR_WHITE = RGBColor(255, 255, 255)

def set_slide_background(slide):
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = COLOR_BG

def add_header(slide, tag_text, title_main, title_accent=""):
    # Tag
    tb_tag = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.4))
    tf_tag = tb_tag.text_frame
    tf_tag.word_wrap = True
    p_tag = tf_tag.paragraphs[0]
    p_tag.text = tag_text.upper()
    p_tag.font.size = Pt(11)
    p_tag.font.bold = True
    p_tag.font.color.rgb = COLOR_CYAN
    p_tag.font.name = "JetBrains Mono"

    # Title
    tb_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.7), Inches(0.8))
    tf_title = tb_title.text_frame
    tf_title.word_wrap = True
    p_title = tf_title.paragraphs[0]
    r1 = p_title.add_run()
    r1.text = title_main + " "
    r1.font.size = Pt(22)
    r1.font.bold = True
    r1.font.color.rgb = COLOR_TITLE
    r1.font.name = "Outfit"

    if title_accent:
        r2 = p_title.add_run()
        r2.text = title_accent
        r2.font.size = Pt(22)
        r2.font.bold = True
        r2.font.color.rgb = COLOR_CYAN
        r2.font.name = "Outfit"

def set_notes(slide, notes_text):
    notes_slide = slide.notes_slide
    tf = notes_slide.notes_text_frame
    tf.text = notes_text

# Load all slides info from verify_deck_integrity
import re
with open(r'02 - Seminário 5 - Ecossistemas de Inovação\Apresentação e Quiz Interativo\index.html', encoding='utf-8') as f:
    html_text = f.read()

slide_regex = re.compile(r'<section class=["\']slide.*?["\'](.*?)>(.*?)</section>', re.DOTALL)
slide_matches = list(slide_regex.finditer(html_text))

# Load notesMap
nm_match = re.search(r'const notesMap = \{(.*?)\n    \};', html_text, re.DOTALL)
notes_dict = {}
if nm_match:
    entries = re.findall(r'(\d+)\s*:\s*[`"](.*?)`(?=\s*,\s*\d+\s*:|\s*[`"]?\s*\}\s*;|\s*$)', nm_match.group(1), re.DOTALL)
    for k, v in entries:
        notes_dict[int(k)] = v.strip().replace('\\`', '`')

deck_dir = r"02 - Seminário 5 - Ecossistemas de Inovação\Apresentação e Quiz Interativo"

print(f"Generating Master PPTX with {len(slide_matches)} slides...")

for idx, match in enumerate(slide_matches, 1):
    attrs = match.group(1)
    body = match.group(2)
    num_m = re.search(r'data-slide=["\'](\d+)["\']', attrs)
    num = int(num_m.group(1)) if num_m else idx
    spk_m = re.search(r'data-speaker=["\']([^"\']+)["\']', attrs)
    spk = spk_m.group(1) if spk_m else 'Grupo 5'
    tag_m = re.search(r'<div class=["\']slide-tag["\']>(.*?)</div>', body)
    tag = tag_m.group(1) if tag_m else 'SEMINÁRIO 5 • ECOSSISTEMAS DE INOVAÇÃO'
    title_m = re.search(r'<h[12][^>]*>(.*?)</h[12]>', body, re.DOTALL)
    title_raw = title_m.group(1) if title_m else 'Slide ' + str(num)
    
    # Split main title and span accent
    span_m = re.search(r'<span>(.*?)</span>', title_raw, re.DOTALL)
    accent_txt = span_m.group(1).strip() if span_m else ''
    main_title = re.sub(r'<[^>]+>', '', title_raw).replace(accent_txt, '').strip()
    if not main_title:
        main_title = accent_txt
        accent_txt = ""

    slide = prs.slides.add_slide(blank_layout)
    set_slide_background(slide)
    add_header(slide, tag, main_title, accent_txt)

    # Add punchline if present
    punch_m = re.search(r'<div class=["\']punchline-quote["\']>(.*?)</div>', body, re.DOTALL)
    curr_top = 1.6
    if punch_m:
        punch_txt = re.sub(r'<[^>]+>', '', punch_m.group(1)).strip()
        tb_p = slide.shapes.add_textbox(Inches(0.8), Inches(curr_top), Inches(11.7), Inches(0.65))
        tf_p = tb_p.text_frame
        tf_p.word_wrap = True
        p_p = tf_p.paragraphs[0]
        p_p.text = f'"{punch_txt}"'
        p_p.font.size = Pt(13)
        p_p.font.italic = True
        p_p.font.color.rgb = COLOR_WHITE
        curr_top += 0.75

    # Check for images in body
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', body)
    # Check for tables in body
    has_table = '<table' in body

    # If Lilian slide with images (faithful to Apresentação1.pptx)
    if 24 <= num <= 32:
        if num == 24: # San Diego Radar Global (Lilian Slide 1 - Figuras e Texto Ampliados)
            p_card = os.path.join(deck_dir, "assets/lilian/slide_1_img_3.png")
            p_map = os.path.join(deck_dir, "assets/lilian/slide_1_img_2.png")
            p_gii = os.path.join(deck_dir, "assets/lilian/slide_1_img_4.png")
            
            # Imagem 3 (escrita da esquerda) ampliada
            if os.path.exists(p_card):
                slide.shapes.add_picture(p_card, Inches(0.8), Inches(1.6), width=Inches(3.6))
                # Callouts em texto nítido
                tb_c = slide.shapes.add_textbox(Inches(0.8), Inches(4.5), Inches(3.6), Inches(2.0))
                tf_c = tb_c.text_frame
                tf_c.word_wrap = True
                callouts = [
                    ("Patentes PCT (2020-2024):", "26.713"),
                    ("Artigos Científicos:", "19.862"),
                    ("Deals de Venture Capital:", "1.705")
                ]
                for i, (k_c, v_c) in enumerate(callouts):
                    p_cc = tf_c.paragraphs[0] if i == 0 else tf_c.add_paragraph()
                    r1 = p_cc.add_run()
                    r1.text = f"• {k_c} "
                    r1.font.size = Pt(11)
                    r1.font.color.rgb = COLOR_MUTED
                    r2 = p_cc.add_run()
                    r2.text = v_c
                    r2.font.size = Pt(12)
                    r2.font.bold = True
                    r2.font.color.rgb = COLOR_CYAN

            # Imagem 2 (Mapa Mundial)
            if os.path.exists(p_map):
                slide.shapes.add_picture(p_map, Inches(4.6), Inches(1.6), width=Inches(4.4), height=Inches(4.8))

            # Imagem 4 (GII 2025)
            if os.path.exists(p_gii):
                slide.shapes.add_picture(p_gii, Inches(9.2), Inches(1.6), width=Inches(3.3), height=Inches(4.8))

        elif num == 25: # O que é um ecossistema? & 6 Pontos (Lilian Slide 2 - Fontes Ampliadas)
            # Definição ampliada
            tb_def = slide.shapes.add_textbox(Inches(0.8), Inches(1.4), Inches(11.7), Inches(1.3))
            tf_def = tb_def.text_frame
            tf_def.word_wrap = True
            p_d1 = tf_def.paragraphs[0]
            p_d1.text = '"É conjunto dinâmico e em evolução de atores, instituições, atividades e relações complementares que impulsionam o desempenho inovador."'
            p_d1.font.size = Pt(15)
            p_d1.font.bold = True
            p_d1.font.italic = True
            p_d1.font.color.rgb = COLOR_WHITE
            p_d2 = tf_def.add_paragraph()
            p_d2.text = "— Jukka Majava & Satu Rinkinen (2026), Technology Analysis & Strategic Management, 38:1, 49-64."
            p_d2.font.size = Pt(11)
            p_d2.font.color.rgb = COLOR_CYAN

            # 6 Pontos em 2 colunas com fontes ampliadas
            pts_col1 = [
                "1º. Ponto: UNIVERSIDADE COM PESQUISA DE PONTA, ATRAÇÃO DE EMPRESAS",
                "2º. Ponto: ANTECEDENTES HISTÓRICOS, VOCAÇÃO DA CIDADE",
                "3º. Ponto: DECISÕES POLÍTICAS PARA FAVORECER O ECOSSISTEMA"
            ]
            pts_col2 = [
                "4º Ponto: CONTINGENCIAS QUE GERAM AÇÕES",
                "5º. Ponto: INSTITUIÇÃO MEDIADORA PARA PROPORCIONAR RELACIONAMENTOS",
                "6º Ponto: PROXIMIDADE GEOGRÁFICA DOS ATORES"
            ]
            tb_c1 = slide.shapes.add_textbox(Inches(0.8), Inches(2.9), Inches(5.7), Inches(3.6))
            tf_c1 = tb_c1.text_frame
            tf_c1.word_wrap = True
            for i, pt in enumerate(pts_col1):
                p_pt = tf_c1.paragraphs[0] if i == 0 else tf_c1.add_paragraph()
                p_pt.text = f"▸ {pt}\n"
                p_pt.font.size = Pt(13)
                p_pt.font.bold = True
                p_pt.font.color.rgb = COLOR_WHITE

            tb_c2 = slide.shapes.add_textbox(Inches(6.8), Inches(2.9), Inches(5.7), Inches(3.6))
            tf_c2 = tb_c2.text_frame
            tf_c2.word_wrap = True
            for i, pt in enumerate(pts_col2):
                p_pt = tf_c2.paragraphs[0] if i == 0 else tf_c2.add_paragraph()
                p_pt.text = f"▸ {pt}\n"
                p_pt.font.size = Pt(13)
                p_pt.font.bold = True
                p_pt.font.color.rgb = COLOR_WHITE

        elif num == 26: # CONNECT (Lilian Slide 3 Hero Infographic)
            p_img = os.path.join(deck_dir, "assets/lilian/slide_3_img_1.png")
            if os.path.exists(p_img):
                slide.shapes.add_picture(p_img, Inches(1.2), Inches(1.5), width=Inches(10.9), height=Inches(5.1))

        elif num == 27: # PEST Radar (Lilian Slide 4 Hero Infographic)
            p_img = os.path.join(deck_dir, "assets/lilian/slide_4_img_1.png")
            if os.path.exists(p_img):
                slide.shapes.add_picture(p_img, Inches(1.2), Inches(1.5), width=Inches(10.9), height=Inches(5.1))

        elif num == 28: # SJC Gênese (Lilian Slide 5 Hero Infographic)
            p_img = os.path.join(deck_dir, "assets/lilian/slide_5_img_1.png")
            if os.path.exists(p_img):
                slide.shapes.add_picture(p_img, Inches(1.2), Inches(1.5), width=Inches(10.9), height=Inches(5.1))

        elif num == 29: # Evolução Tipológica (Lilian Slide 6 Hero Infographic)
            p_img = os.path.join(deck_dir, "assets/lilian/slide_6_img_1.png")
            if os.path.exists(p_img):
                slide.shapes.add_picture(p_img, Inches(1.2), Inches(1.5), width=Inches(10.9), height=Inches(5.1))

        elif num == 30: # PIT SJC Pentagonal (Lilian Slide 7)
            p_img = os.path.join(deck_dir, "assets/lilian/slide_7_img_2.png")
            if os.path.exists(p_img):
                slide.shapes.add_picture(p_img, Inches(3.6), Inches(1.6), width=Inches(6.1), height=Inches(4.9))

        elif num == 31: # Parceiros PIT (Lilian Slide 8)
            p_img = os.path.join(deck_dir, "assets/lilian/slide_8_img_3.png")
            if os.path.exists(p_img):
                slide.shapes.add_picture(p_img, Inches(1.1), Inches(1.6), width=Inches(11.1), height=Inches(4.9))
        elif num == 32: # Tabela Comparativa Completa
            # Add table
            rows = 7
            cols = 3
            left = Inches(0.8)
            top = Inches(curr_top)
            width = Inches(11.7)
            height = Inches(4.5)
            tbl_shape = slide.shapes.add_table(rows, cols, left, top, width, height)
            tbl = tbl_shape.table
            tbl.columns[0].width = Inches(2.2)
            tbl.columns[1].width = Inches(4.75)
            tbl.columns[2].width = Inches(4.75)

            headers = ["Dimensão", "San Diego (EUA)", "São José dos Campos (Brasil)"]
            for col_idx, h in enumerate(headers):
                cell = tbl.cell(0, col_idx)
                cell.fill.solid()
                cell.fill.fore_color.rgb = COLOR_SURFACE
                p = cell.text_frame.paragraphs[0]
                p.text = h
                p.font.bold = True
                p.font.size = Pt(13)
                p.font.color.rgb = COLOR_CYAN

            data = [
                ("Matriz Científica e Origem", "Pesquisa em saúde (Scripps, Salk), UCSD e demandas da Marinha/Aeronáutica civil.", "Planejamento estatal/militar em defesa e aeroespacial (CTA, ITA, INPE)."),
                ("Evolução da Governança", "Modelo Bottom-Up: Liderança privada e universidade criaram a ONG CONNECT em 1985.", "De Orgânico (Tipo 1) a Orquestrado (Tipo 3): De polo sem gestão formal (anos 90) ao PIT em 2009 (Organização Social)."),
                ("Papel do Território", "Zoneamento urbano em 1970 garantiu proximidade física entre universidade, institutos e startups.", "Aglomeração territorial no PIT gerando sinergia e transbordamento de conhecimento tácito (spill-overs)."),
                ("Atores-Âncora e Genealogia", "Startups pioneiras em ciências (Hybritech em biotec e Linkabit/Qualcomm em sem fio).", "Embraer, Avibras e vasta rede de fornecedores e spin-offs de pesquisadores do CTA/INPE."),
                ("Modelo de Financiamento", "Investimento federal em pesquisa (NIH, SBIR/STTR), Capital de Risco (Venture Capital) e IPOs.", "Histórico de encomendas estatais de defesa e transição atual para modelo híbrido (investimentos públicos e privados no PIT)."),
                ("Diversificação Setorial", "Liderança mundial em Biotecnologia, Ciências da Vida e Telecomunicações Sem Fio.", "Matriz aeroespacial/defesa expandida para TIC Vale, Agropolo, Saúde, Mobilidade e Smart Cities.")
            ]
            for r_idx, (d_name, d_sd, d_sjc) in enumerate(data, 1):
                c0 = tbl.cell(r_idx, 0)
                c0.fill.solid()
                c0.fill.fore_color.rgb = COLOR_CARD
                p0 = c0.text_frame.paragraphs[0]
                p0.text = d_name
                p0.font.bold = True
                p0.font.size = Pt(11.5)
                p0.font.color.rgb = COLOR_WHITE

                c1 = tbl.cell(r_idx, 1)
                c1.fill.solid()
                c1.fill.fore_color.rgb = COLOR_CARD
                p1 = c1.text_frame.paragraphs[0]
                p1.text = d_sd
                p1.font.size = Pt(11)
                p1.font.color.rgb = COLOR_MUTED

                c2 = tbl.cell(r_idx, 2)
                c2.fill.solid()
                c2.fill.fore_color.rgb = COLOR_CARD
                p2 = c2.text_frame.paragraphs[0]
                p2.text = d_sjc
                p2.font.size = Pt(11)
                p2.font.color.rgb = COLOR_WHITE

    else:
        # Default card rendering for other slides
        # If image in body, add image
        if imgs:
            img_rel = imgs[0]
            img_path = os.path.join(deck_dir, img_rel)
            if os.path.exists(img_path):
                slide.shapes.add_picture(img_path, Inches(1.5), Inches(curr_top), width=Inches(10.3))
            else:
                # Add text content
                clean_body = re.sub(r'<[^>]+>', ' ', body).strip()
                tb = slide.shapes.add_textbox(Inches(0.8), Inches(curr_top), Inches(11.7), Inches(4.5))
                tf = tb.text_frame
                tf.word_wrap = True
                p = tf.paragraphs[0]
                p.text = clean_body[:500]
                p.font.size = Pt(13)
                p.font.color.rgb = COLOR_MUTED
        else:
            # Extract bullet points or cards
            clean_body = re.sub(r'<[^>]+>', '\n', body)
            clean_lines = [l.strip() for l in clean_body.splitlines() if l.strip()]
            tb = slide.shapes.add_textbox(Inches(0.8), Inches(curr_top), Inches(11.7), Inches(4.5))
            tf = tb.text_frame
            tf.word_wrap = True
            for i, l in enumerate(clean_lines[:8]):
                p = tf.add_paragraph() if i > 0 else tf.paragraphs[0]
                p.text = f"• {l}"
                p.font.size = Pt(13)
                p.font.color.rgb = COLOR_WHITE if i % 2 == 0 else COLOR_MUTED

    # Add bottom footer bar: Presenters (left) and Reference Citation (right)
    ref_m = re.search(r'<div class=["\']slide-footer-ref["\']>(.*?)</div>', body, re.DOTALL)
    ref_txt = re.sub(r'<[^>]+>', ' ', ref_m.group(1)).strip() if ref_m else ""
    if ref_txt.startswith("📚"):
        ref_txt = ref_txt.replace("📚", "").strip()

    tb_foot = slide.shapes.add_textbox(Inches(0.8), Inches(6.9), Inches(11.733), Inches(0.45))
    tf_foot = tb_foot.text_frame
    tf_foot.word_wrap = True
    p_foot = tf_foot.paragraphs[0]
    
    r_spk = p_foot.add_run()
    r_spk.text = f"🎤 {spk}   |   "
    r_spk.font.size = Pt(8.5)
    r_spk.font.bold = True
    r_spk.font.color.rgb = COLOR_CYAN
    r_spk.font.name = "JetBrains Mono"

    if ref_txt:
        r_ref = p_foot.add_run()
        r_ref.text = f"📚 {ref_txt}"
        r_ref.font.size = Pt(8.5)
        r_ref.font.color.rgb = COLOR_MUTED
        r_ref.font.name = "JetBrains Mono"

    # Set speaker notes
    if num in notes_dict:
        set_notes(slide, notes_dict[num])

out_pptx = os.path.join(deck_dir, "Seminario_5_Ecossistemas_Inovacao_Master.pptx")
prs.save(out_pptx)
print(f"Master PPTX saved successfully: {out_pptx} ({os.path.getsize(out_pptx):,} bytes)")
