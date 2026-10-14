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

    # If Lilian slide with images
    if 24 <= num <= 32:
        if num == 24: # San Diego Radar Global
            # Left img, right img
            p_img1 = os.path.join(deck_dir, "assets/lilian/slide_1_img_2.png")
            p_img2 = os.path.join(deck_dir, "assets/lilian/slide_1_img_4.png")
            if os.path.exists(p_img1):
                slide.shapes.add_picture(p_img1, Inches(0.8), Inches(curr_top), width=Inches(5.8))
            if os.path.exists(p_img2):
                slide.shapes.add_picture(p_img2, Inches(6.8), Inches(curr_top), width=Inches(5.7))
        elif num == 25: # 6 Pontos
            # 6 boxes
            tb = slide.shapes.add_textbox(Inches(0.8), Inches(curr_top), Inches(11.7), Inches(4.5))
            tf = tb.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.text = "Os 6 Pontos-Chave de San Diego (Majava & Rinkinen, 2024/2026):"
            p.font.size = Pt(14)
            p.font.bold = True
            p.font.color.rgb = COLOR_CYAN
            pts = [
                ("1º Ponto: Universidade com Pesquisa de Ponta", "Fundação da UCSD nos anos 60 com foco em biologia e ciências, atraindo VCs e multinacionais."),
                ("2º Ponto: Antecedentes Históricos & Vocação", "Investimento prévio em hospitais e clínicas; isolamento geográfico que impediu indústrias pesadas."),
                ("3º Ponto: Decisões Políticas para Favorecer", "Zoneamento urbano nos anos 70 garantindo proximidade física entre UCSD, institutos e empresas."),
                ("4º Ponto: Contingências que Geram Ações", "Crise na indústria militar pós-Guerra Fria elevou desemprego, forçando reconversão em biotec e telecom."),
                ("5º Ponto: Instituição Mediadora (Orquestrador)", "Criação da CONNECT (1985) na UCSD: aceleradora Springboard, mentoria e laços de confiança."),
                ("6º Ponto: Proximidade Geográfica dos Atores", "Distâncias curtas que facilitaram encontros de corredor, compartilhamento de conhecimento tácito.")
            ]
            for title_pt, desc_pt in pts:
                p_item = tf.add_paragraph()
                r_item1 = p_item.add_run()
                r_item1.text = f"• {title_pt}: "
                r_item1.font.bold = True
                r_item1.font.color.rgb = COLOR_WHITE
                r_item1.font.size = Pt(12)
                r_item2 = p_item.add_run()
                r_item2.text = desc_pt
                r_item2.font.color.rgb = COLOR_MUTED
                r_item2.font.size = Pt(11)
        elif num == 26: # CONNECT
            p_img = os.path.join(deck_dir, "assets/lilian/slide_3_img_1.png")
            if os.path.exists(p_img):
                slide.shapes.add_picture(p_img, Inches(1.5), Inches(curr_top), width=Inches(10.3))
        elif num == 27: # PEST
            p_img = os.path.join(deck_dir, "assets/lilian/slide_4_img_1.png")
            if os.path.exists(p_img):
                slide.shapes.add_picture(p_img, Inches(1.5), Inches(curr_top), width=Inches(10.3))
        elif num == 28: # SJC Gênese
            p_img = os.path.join(deck_dir, "assets/lilian/slide_5_img_1.png")
            if os.path.exists(p_img):
                slide.shapes.add_picture(p_img, Inches(0.8), Inches(curr_top), width=Inches(6.0))
            tb = slide.shapes.add_textbox(Inches(7.0), Inches(curr_top), Inches(5.5), Inches(4.5))
            tf = tb.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.text = "Fatores Estruturantes de São José dos Campos:"
            p.font.size = Pt(14)
            p.font.bold = True
            p.font.color.rgb = COLOR_CYAN
            items = [
                ("Fatores Atrativos Originais (Anos 50):", "Localização no Eixo Rio-SP (Via Dutra), energia elétrica abundante, recursos hídricos e relevo plano."),
                ("Instituições-Âncora Estratégicas:", "CTA e ITA criados nos anos 50 baseados no MIT; INPE criado em 1961 formando elite em P&D aeroespacial e defesa."),
                ("O Poder de Compra Estatal:", "Na ausência de Venture Capital, as encomendas do Ministério da Aeronáutica viabilizaram a Embraer, Avibras e fornecedores nacionais.")
            ]
            for t_sub, d_sub in items:
                p_it = tf.add_paragraph()
                r_it1 = p_it.add_run()
                r_it1.text = f"\n▸ {t_sub} "
                r_it1.font.bold = True
                r_it1.font.color.rgb = COLOR_EMERALD
                r_it1.font.size = Pt(12)
                r_it2 = p_it.add_run()
                r_it2.text = d_sub
                r_it2.font.color.rgb = COLOR_MUTED
                r_it2.font.size = Pt(11)
        elif num == 29: # Evolução Tipológica
            p_img = os.path.join(deck_dir, "assets/lilian/slide_6_img_1.png")
            if os.path.exists(p_img):
                slide.shapes.add_picture(p_img, Inches(1.5), Inches(curr_top), width=Inches(10.3))
        elif num == 30: # PIT SJC Pentagonal
            p_img = os.path.join(deck_dir, "assets/lilian/slide_7_img_2.png")
            if os.path.exists(p_img):
                slide.shapes.add_picture(p_img, Inches(0.8), Inches(curr_top), width=Inches(5.5))
            tb = slide.shapes.add_textbox(Inches(6.6), Inches(curr_top), Inches(5.9), Inches(4.5))
            tf = tb.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.text = "Governança e Modelo de Operação do PIT SJC:"
            p.font.size = Pt(14)
            p.font.bold = True
            p.font.color.rgb = COLOR_CYAN
            items_pit = [
                ("Gestão por Organização Social:", "Criado em 2009 pela Prefeitura de SJC; gerido pela APTSJC (OS privada sem fins lucrativos credenciada no SPTec/SPAI)."),
                ("Superação do Gargalo de P&D:", "56 projetos prospectados, 22 executados em 2025; acesso ampliado a 57 laboratórios parceiros multiusuários."),
                ("Os 5 Eixos da Matriz Pentagonal:", "Defesa e Aeroespacial, TIC, Agronegócio, Saúde/Biotecnologia e Mobilidade Urbana articulando a Tríplice Hélice central."),
                ("Spill-overs Territoriais (Thiago Rubem, 2018):", "A aglomeração física catalisa transbordamento espontâneo de conhecimento tácito e sinergia.")
            ]
            for t_sub, d_sub in items_pit:
                p_it = tf.add_paragraph()
                r_it1 = p_it.add_run()
                r_it1.text = f"\n▸ {t_sub} "
                r_it1.font.bold = True
                r_it1.font.color.rgb = COLOR_EMERALD
                r_it1.font.size = Pt(12)
                r_it2 = p_it.add_run()
                r_it2.text = d_sub
                r_it2.font.color.rgb = COLOR_MUTED
                r_it2.font.size = Pt(11)
        elif num == 31: # Parceiros PIT
            p_img = os.path.join(deck_dir, "assets/lilian/slide_8_img_3.png")
            if os.path.exists(p_img):
                slide.shapes.add_picture(p_img, Inches(0.8), Inches(curr_top), width=Inches(6.2))
            tb = slide.shapes.add_textbox(Inches(7.2), Inches(curr_top), Inches(5.3), Inches(4.5))
            tf = tb.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.text = "Expansão dos APLs & Nexus Hub em 2026:"
            p.font.size = Pt(14)
            p.font.bold = True
            p.font.color.rgb = COLOR_CYAN
            items_apl = [
                ("Cluster Aeroespacial & Defesa:", "Presença internacional em Dubai e Paris; conexões com +10 países e +120h de capacitação."),
                ("TIC Vale (137 Empresas):", "Arranjo produtivo em Indústria 4.0, Inteligência Artificial, Big Data e Smart Cities."),
                ("Agropolo (+21,6%) & Saúde/Mobilidade:", "90 empresas no Agropolo com foco em ESG; cadeia de saúde com +100 rodadas de negócios."),
                ("Nexus Hub (192 Startups):", "Comunidade com 23 entidades estratégicas e 87 mentores seniores no Nexus Circle.")
            ]
            for t_sub, d_sub in items_apl:
                p_it = tf.add_paragraph()
                r_it1 = p_it.add_run()
                r_it1.text = f"\n▸ {t_sub} "
                r_it1.font.bold = True
                r_it1.font.color.rgb = COLOR_EMERALD
                r_it1.font.size = Pt(12)
                r_it2 = p_it.add_run()
                r_it2.text = d_sub
                r_it2.font.color.rgb = COLOR_MUTED
                r_it2.font.size = Pt(11)
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
                p.font.size = Pt(12)
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
                p0.font.size = Pt(10)
                p0.font.color.rgb = COLOR_WHITE

                c1 = tbl.cell(r_idx, 1)
                c1.fill.solid()
                c1.fill.fore_color.rgb = COLOR_CARD
                p1 = c1.text_frame.paragraphs[0]
                p1.text = d_sd
                p1.font.size = Pt(9.5)
                p1.font.color.rgb = COLOR_MUTED

                c2 = tbl.cell(r_idx, 2)
                c2.fill.solid()
                c2.fill.fore_color.rgb = COLOR_CARD
                p2 = c2.text_frame.paragraphs[0]
                p2.text = d_sjc
                p2.font.size = Pt(9.5)
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

    # Set speaker notes
    if num in notes_dict:
        set_notes(slide, notes_dict[num])

out_pptx = os.path.join(deck_dir, "Seminario_5_Ecossistemas_Inovacao_Master.pptx")
prs.save(out_pptx)
print(f"Master PPTX saved successfully: {out_pptx} ({os.path.getsize(out_pptx):,} bytes)")
