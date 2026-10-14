# -*- coding: utf-8 -*-
"""
Script to patch Lilian's 9 slides into index.html and apresentacao_seminario_ecossistema_pit.html.
Replaces the old slides 24 and 25 with 9 comprehensive, beautifully styled slides,
updates Slide 26 into Slide 33 (Kahoot Fase 5), preserves UNIFESP as Slide 34,
and cleanly renumbers slides 35 to 44 with all notesMap entries intact.
"""

import os
import re
import sys
from lilian_slides_html import get_lilian_slides_html

sys.stdout.reconfigure(encoding='utf-8')

# The notes for Lilian's slides (24 to 32)
LILIAN_NOTES = {
    24: """TEMPO: cerca de 1 minuto e meio.
FALA SUGERIDA (LILIAN VEIGA VINHAS):
"O principal artigo do nosso bloco tratou do surgimento e dos fatores de sucesso do ecossistema de inovação de San Diego, na Califórnia, conduzido pelos pesquisadores Jukka Majava e Satu Rinkinen (revisão sistemática de 20 anos de estudos entre 2001 e 2021, complementados por entrevistas com especialistas).
Para termos dimensão do impacto, trago os dados oficiais da Organização Mundial da Propriedade Intelectual (WIPO / ONU) no Global Innovation Index 2025. San Diego ocupa o 14º lugar no ranking dos 100 maiores clusters mundiais de inovação (e o 7º lugar mundial por intensidade relativa à densidade populacional).
Entre 2020 e 2024, foram nada menos que 26.713 pedidos de patente PCT na cidade, com destaque absoluto para a Qualcomm (líder global de processadores móveis, semicondutores, 4G, 5G e Wi-Fi), que responde sozinha por 64% das patentes. Na produção científica, a UCSD lidera com quase 12 mil artigos (59% da cidade). No Brasil, apenas a região metropolitana de São Paulo figura entre os 100 clusters da WIPO. Além da Qualcomm, centros de P&D de gigantes farmacêuticas mundiais operam na cidade, como Eli Lilly, Pfizer, Janssen e a Illumina, líder global de sequenciamento genético." """,

    25: """TEMPO: cerca de 1 minuto e 45 segundos.
FALA SUGERIDA (LILIAN VEIGA VINHAS):
"Por que estudar San Diego? Porque muitos países e regiões tentam copiar o Vale do Silício sem sucesso. San Diego é um caso fascinante porque era uma cidade periférica, considerada pequena e isolada no extremo sul da Califórnia, e que a partir dos anos 90 tornou-se polo global em biotecnologia e telecomunicações sem fio.
Majava & Rinkinen definem ecossistema de inovação como um conjunto dinâmico e em evolução de atores, instituições, atividades e relações complementares que impulsionam o desempenho inovador.
E os autores identificam 6 pontos-chave estruturantes na trajetória de San Diego:
1º Ponto: A fundação da UCSD nos anos 60 com excelência em biologia e ciências naturais, recrutando mentes brilhantes que atraíram capital de risco e multinacionais.
2º Ponto: Vocação histórica prévia em hospitais e clínicas; e um isolamento geográfico que dificultava indústrias manufatureiras e pesadas.
3º Ponto: Decisões políticas deliberadas de zoneamento urbano nos anos 70 reservando áreas para ciências da vida próximas à universidade.
4º Ponto: Contingências que forçam ação: a cidade tinha base militar forte, mas com o término da Guerra Fria nos anos 80, o desemprego bélico aumentou, forçando a reconversão econômica.
5º Ponto: Criação de instituição mediadora: em 1985 nasce a CONNECT dentro da UCSD para acelerar empresas e construir confiança entre as partes.
6º Ponto: Proximidade geográfica dos atores: distâncias curtas facilitaram a colaboração e parcerias diárias." """,

    26: """TEMPO: cerca de 1 minuto e 45 segundos.
FALA SUGERIDA (LILIAN VEIGA VINHAS):
"O grande diferencial de San Diego foi a CONNECT, criada em 1985.
Ela não nasceu de cima para baixo por decreto governamental, mas de baixo para cima (bottom-up), numa união da universidade UCSD com lideranças privadas e cientistas para salvar a economia da cidade pós-crise militar.
A CONNECT atuou como uma verdadeira aceleradora através do seu consagrado Programa Springboard. Como funcionava? Os cientistas passavam por sabatinas com advogados de patentes, executivos e investidores, que lapidavam o plano de negócios e preparavam a startup para receber investimento institucional.
Ela cumpriu o papel crucial de reduzir a assimetria entre as ideias dos cientistas e as regras dos negócios, instaurando a cultura de doação de tempo (give-first) e mentoria voluntária.
Atores que compuseram a rede: UCSD, institutos Scripps e Salk, aceleradoras, incubadoras, investidores-anjo, venture capital, prestadores de serviços jurídicos e financeiros, e empresas pioneiras como Hybritech e Linkabit/Qualcomm, que serviram como raízes de árvores genealógicas para novas startups." """,

    27: """TEMPO: cerca de 1 minuto e 45 segundos.
FALA SUGERIDA (LILIAN VEIGA VINHAS):
"Para sistematizar as lições de San Diego, o artigo utilizou uma Análise PEST (Político, Econômico, Social e Tecnológico) — método que também utilizamos na disciplina com o professor Yukio:
No pilar Político (P): zoneamento urbano estratégico e programas federais contínuos de fomento como o SBIR/STTR e fundos do NIH.
No pilar Econômico (E): farta oferta de Venture Capital especializado, e um ciclo virtuoso onde aquisições por grandes farmacêuticas e IPOs na NASDAQ reinjetavam capital reciclado nos empreendedores locais.
No pilar Social e Cultural (S): cultura sem aversão ao risco, e altíssima mobilidade interempresarial de executivos, fazendo a expertise circular pelo ecossistema.
No pilar Tecnológico (T): a excelência da pesquisa da UCSD e o transbordamento das empresas pioneiras.
Como frase síntese do radar: a concentração simultânea de ideias (ciência básica) e capital viabilizou o milagre da Biotecnologia.
Mas o artigo traz também os contrapontos e efeitos colaterais com honestidade acadêmica: a alta tecnologia gerou expansão urbana descontrolada, congestionamentos viários, gentrificação e escassez de moradia acessível para profissionais de média e baixa qualificação." """,

    28: """TEMPO: cerca de 1 minuto e 45 segundos.
FALA SUGERIDA (LILIAN VEIGA VINHAS):
"Fazendo agora a ponte com o nosso ecossistema em São José dos Campos: como nasceu a nossa vocação tecnológica?
A trajetória de SJC tem raízes no início da década de 50. A cidade reuniu atributos geográficos privilegiados: localização estratégica no eixo Rio-SP pela recém-inaugurada Via Dutra, abundância de recursos hídricos, energia elétrica e relevo plano.
Mas a grande virada veio com o Planejamento de Estado. O governo federal decidiu instalar o Centro Técnico de Aeronáutica (CTA) e o Instituto Tecnológico de Aeronáutica (ITA), estruturado a partir da experiência do MIT norte-americano, seguido pelo INPE em 1961.
Um ponto essencial: no Brasil dos anos 50 e 60 não existia a figura do Venture Capital. O que financiou a inovação brasileira? O poder de compra do Ministério da Aeronáutica, que fez encomendas estratégicas viabilizando a Embraer, Avibras e uma sólida cadeia de fornecedores.
E assim como em San Diego, constatou-se que quando os fundadores das empresas eram pessoas físicas, na quase totalidade eram pesquisadores saídos dos próprios institutos." """,

    29: """TEMPO: cerca de 1 minuto e 45 segundos.
FALA SUGERIDA (LILIAN VEIGA VINHAS):
"A literatura sobre polos tecnológicos classifica essas aglomerações em três tipologias:
Polo Tipo 1 (Polo Orgânico): aglomeração espontânea sem estrutura formal de orquestração de rede.
Polo Tipo 2: existência de estrutura organizacional prévia formalizada entre academia, indústria e governo.
Polo Tipo 3 (Parque Tecnológico): além da estrutura organizacional formal de governança, contém terrenos, prédios e laboratórios compartilhados dedicados a abrigar indústrias e startups interagindo com centros de pesquisa.
Podemos afirmar categoricamente que São José dos Campos nasceu como um Polo Tipo 1 nos anos 50 a 90. E o que acontecia na prática? Havia barreiras: as empresas tinham enorme dificuldade de acessar os laboratórios do CTA e do INPE, faltava fluxo de informações e apoio em gestão tecnológica.
Com a fundação do PIT em 2009, SJC deu o salto para o Polo Tipo 3, assumindo a gestão formalizada por Organização Social — funcionando para a nossa região exatamente como a CONNECT funcionou para San Diego! E superando a dificuldade histórica de acesso a laboratórios." """,

    30: """TEMPO: cerca de 1 minuto e 45 segundos.
FALA SUGERIDA (LILIAN VEIGA VINHAS):
"Entrando na anatomia atual do PIT SJC, fundamentada no Relatório Anual 2025 e no estudo de Thiago Rubem (2018):
O Parque foi instituído em 2009 e sua administração é realizada pela Associação Parque Tecnológico de São José dos Campos (APTSJC), uma Organização Social privada sem fins lucrativos credenciada no Sistema Paulista de Parques Tecnológicos (SPTec/SPAI).
O conceito teórico central é o de spill-overs territoriais: a concentração espacial não é mero espaço físico, ela gera transbordamento de conhecimento tácito que não aconteceria à distância.
Vejam a matriz pentagonal do Relatório Anual do PIT projetada na tela: a Tríplice Hélice central (APTSJC articulando Universidade, Governo e Empresas) coordena cinco eixos estratégicos: Defesa e Aeroespacial, TIC Vale, Agropolo, Saúde e Biotecnologia, e Mobilidade Urbana.
E o grande avanço: o PIT resolveu o gargalo histórico dos laboratórios! Em 2025 foram 56 projetos prospectados, 22 executados e o ecossistema passou a contar com uma rede integrada de 57 laboratórios de instituições parceiras à disposição das empresas!" """,

    31: """TEMPO: cerca de 1 minuto e 45 segundos.
FALA SUGERIDA (LILIAN VEIGA VINHAS):
"Em recente entrevista publicada na Gazeta de São Paulo em maio de 2026, Jeferson Cheriegate, presidente do PIT, destacou que o Parque expandiu sua atuação para além da tecnologia pura: tornou-se articulador de cidades inteligentes, sustentabilidade, ESG e internacionalização.
Olhem para o painel de logos de parceiros corporativos e governamentais que confiam no PIT: Gerdau, Nestlé, Finep, Sebrae, Thales, Novelis, Governos de SP, GO, PR e dezenas de prefeituras!
Os APLs operam a pleno vapor: o Cluster Aeroespacial e Defesa brasileiro marcou presença em Dubai e Paris; o TIC Vale atingiu 137 empresas; o Agropolo cresceu mais de 21% com 90 empresas; a cadeia de saúde e biotecnologia realizou mais de 100 reuniões de negócios; e o hub de inovação Nexus acelerou 192 startups com 87 mentores seniores.
Isso comprova a tese central: inovação requer instituições que gerem pertencimento, confiança e encontros presenciais contínuos." """,

    32: """TEMPO: cerca de 2 minutos.
FALA SUGERIDA (LILIAN VEIGA VINHAS):
"Para consolidar este bloco de benchmarking internacional, apresento nossa matriz comparativa detalhada em 6 dimensões estratégicas:
1. Matriz Científica: San Diego ancorou-se em saúde e UCSD com demandas navais; SJC ancorou-se no planejamento de defesa aeroespacial do CTA/ITA/INPE.
2. Governança: San Diego operou bottom-up com a ONG CONNECT; SJC evoluiu do polo orgânico (Tipo 1) ao orquestrado (Tipo 3) pelo PIT gerido por Organização Social.
3. Território: Zoneamento urbano em 1970 em San Diego; Adensamento territorial no PIT gerando transbordamentos tácitos (spill-overs) em SJC.
4. Genealogia: Startups pioneiras Hybritech e Qualcomm em San Diego; Embraer, Avibras e spin-offs de pesquisadores em SJC.
5. Financiamento: Venture Capital e IPOs nos EUA; Encomendas estatais históricas de defesa e atual modelo híbrido de investimentos no PIT.
6. Diversificação: San Diego lidera em Biotecnologia e Telecom; SJC expandiu o aeroespacial para TIC Vale, Agropolo, Saúde, Mobilidade e Cidades Inteligentes.
Conclusão Geral: Não existem fórmulas prontas. Parques tecnológicos não são empreendimentos imobiliários, mas ecossistemas relacionais de confiança humana mútua!" """
}

def patch_html_file(filepath):
    print(f"Patching {filepath}...")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update <span id="slide-total">35</span> (or whatever) to 44
    content = re.sub(r'<span id="slide-total">\d+</span>', '<span id="slide-total">44</span>', content)

    # 2. Extract slides 1 to 23
    # Let's find slide 24 start
    m24 = re.search(r'(<section class=["\']slide["\'][^>]*data-slide=["\']24["\'].*?)(?=<section class=["\']slide["\'][^>]*data-slide=["\']26["\'])', content, re.DOTALL)
    if not m24:
        raise ValueError("Could not find slide 24 in file!")
    
    # Let's see what is between slide 23 and slide 26:
    # It contains slide 24 and 25.
    old_bloco5 = m24.group(0)

    # Lilian slides HTML
    lilian_html = get_lilian_slides_html()

    # Replace old slide 24 and 25 with Lilian's 9 slides
    content = content.replace(old_bloco5, lilian_html + "\n    ")

    # Now let's handle the slides after Lilian:
    # Currently we have:
    # data-slide="26" (Kahoot 5) -> should become data-slide="33"
    # data-slide="27" (Caso PIT Números) -> we can remove or keep; let's see: Lilian's slides already have the PIT numbers & partners in slides 30 & 31.
    # What about data-slide="28" (A Integração UNIFESP & PIT)? That should become data-slide="34"!
    # What about data-slide="29" (Benchmarking)? Lilian's slide 32 already is the complete official benchmarking matrix! We can remove old slide 27 and 29.
    # What about data-slide="30" (Entrevista Renato)? -> data-slide="35"
    # What about data-slide="31" (4 Eixos Renato)? -> data-slide="36"
    # What about data-slide="32" (Bloco 6 Shen et al.)? -> data-slide="37"
    # What about data-slide="33" (Bloco 6 Armadilhas)? -> data-slide="38"
    # What about data-slide="34" (Kahoot 6)? -> data-slide="39"
    # What about data-slide="35" (Pódio Provisório)? -> data-slide="40"
    # What about data-slide="36" (Diagnóstico Erros)? -> data-slide="41"
    # What about data-slide="37" (5 Leis)? -> data-slide="42"
    # What about data-slide="38" (Debate)? -> data-slide="43"
    # What about data-slide="39" (Referências)? -> data-slide="44"

    # Let's locate each slide and update them cleanly.
    # Slide 26 (Kahoot 5) -> 33
    content = re.sub(r'(<section class=["\']slide["\'][^>]*data-block=["\']Momento Kahoot 5["\'][^>]*data-slide=["\'])26(["\'])', r'\g<1>33\g<2>', content)
    # Also handle alternate attribute ordering
    content = re.sub(r'(<section class=["\']slide["\'][^>]*data-slide=["\'])26(["\'][^>]*data-block=["\']Momento Kahoot 5["\'])', r'\g<1>33\g<2>', content)

    # Old Slide 27 (O Parque Tecnológico em Números): remove it cleanly since Lilian slide 30/31 is much richer
    m_old27 = re.search(r'<section class=["\']slide["\'][^>]*data-slide=["\']27["\'].*?</section>', content, re.DOTALL)
    if m_old27:
        content = content.replace(m_old27.group(0), "")

    # Slide 28 (A Integração UNIFESP & PIT) -> 34
    content = re.sub(r'(<section class=["\']slide["\'][^>]*data-slide=["\'])28(["\'])', r'\g<1>34\g<2>', content)

    # Old Slide 29 (Benchmarking simples): remove it cleanly since Lilian slide 32 is the full official table
    m_old29 = re.search(r'<section class=["\']slide["\'][^>]*data-slide=["\']29["\'].*?</section>', content, re.DOTALL)
    if m_old29:
        content = content.replace(m_old29.group(0), "")

    # Slide 30 (Entrevista Renato) -> 35
    content = re.sub(r'(<section class=["\']slide["\'][^>]*data-slide=["\'])30(["\'])', r'\g<1>35\g<2>', content)

    # Slide 31 (4 Eixos Renato) -> 36
    content = re.sub(r'(<section class=["\']slide["\'][^>]*data-slide=["\'])31(["\'])', r'\g<1>36\g<2>', content)

    # Slide 32 (Bloco 6 Shen) -> 37
    content = re.sub(r'(<section class=["\']slide["\'][^>]*data-slide=["\'])32(["\'])', r'\g<1>37\g<2>', content)

    # Slide 33 (Bloco 6 Armadilhas) -> 38
    content = re.sub(r'(<section class=["\']slide["\'][^>]*data-slide=["\'])33(["\'])', r'\g<1>38\g<2>', content)

    # Slide 34 (Kahoot 6) -> 39
    content = re.sub(r'(<section class=["\']slide["\'][^>]*data-slide=["\'])34(["\'])', r'\g<1>39\g<2>', content)

    # Slide 35 (Pódio Provisório) -> 40
    content = re.sub(r'(<section class=["\']slide["\'][^>]*data-slide=["\'])35(["\'])', r'\g<1>40\g<2>', content)

    # Slide 36 (Diagnóstico Erros) -> 41
    content = re.sub(r'(<section class=["\']slide["\'][^>]*data-slide=["\'])36(["\'])', r'\g<1>41\g<2>', content)

    # Slide 37 (5 Leis) -> 42
    content = re.sub(r'(<section class=["\']slide["\'][^>]*data-slide=["\'])37(["\'])', r'\g<1>42\g<2>', content)

    # Slide 38 (Debate) -> 43
    content = re.sub(r'(<section class=["\']slide["\'][^>]*data-slide=["\'])38(["\'])', r'\g<1>43\g<2>', content)

    # Slide 39 (Referências) -> 44
    content = re.sub(r'(<section class=["\']slide["\'][^>]*data-slide=["\'])39(["\'])', r'\g<1>44\g<2>', content)

    # 3. Update totalSlides in script
    content = re.sub(r'const totalSlides = \d+;', 'const totalSlides = 44;', content)

    # 4. Update References in Slide 44 to include Lilian's citations
    ref_additions = """
          <li><span class="bullet-dot">▸</span> <strong>Majava, J. &amp; Rinkinen, S. (2024/2026):</strong> Twenty years, twenty studies: what can we learn from San Diego’s innovation ecosystem? <em>Technology Analysis &amp; Strategic Management</em>, 38(1), 49-64.</li>
          <li><span class="bullet-dot">▸</span> <strong>Rubem, T. C. (2018):</strong> Políticas de inovação, parques tecnológicos e a importância do território: o caso do Parque Tecnológico de São José dos Campos. <em>Anais das Semanas de Geografia da Unicamp</em>, 101-107.</li>
          <li><span class="bullet-dot">▸</span> <strong>WIPO (2025):</strong> Global Innovation Index 2025: Science &amp; Technology Clusters Ranking (San Diego, 14th). <em>World Intellectual Property Organization</em>, Genebra.</li>
          <li><span class="bullet-dot">▸</span> <strong>APTSJC (2025):</strong> <em>Relatório Anual de Atividades 2025</em>. Associação Parque Tecnológico de São José dos Campos.</li>
          <li><span class="bullet-dot">▸</span> <strong>Cheriegate, J. (2026):</strong> Parque Tecnológico fortalece São José como polo nacional de inovação. <em>Gazeta de São Paulo</em>, entrevista de 29.05.2026.</li>"""
    
    if "Twenty years, twenty studies" not in content:
        content = content.replace('<li><span class="bullet-dot">▸</span> <strong>Majava, J. &amp; Rinkinen, S. (2021):</strong>', ref_additions + '\n          <li><span class="bullet-dot">▸</span> <strong>Majava, J. &amp; Rinkinen, S. (2021):</strong>')

    # 5. Now update notesMap
    # Let's reconstruct notesMap cleanly
    # Find existing notesMap
    nm_match = re.search(r'const notesMap = \{(.*?)\n    \};', content, re.DOTALL)
    if not nm_match:
        raise ValueError("Could not find notesMap in file!")
    
    # We will build updated notesMap from 1 to 44
    # Slides 1 to 23 keep exact notes
    # Slides 24 to 32 get Lilian notes
    # Slide 33 gets Kahoot 5 note
    # Slide 34 gets UNIFESP note
    # Slide 35 gets Entrevista Renato note
    # Slide 36 gets 4 Eixos Renato note
    # Slide 37 gets Bloco 6 Shen note
    # Slide 38 gets Bloco 6 Armadilhas note
    # Slide 39 gets Kahoot 6 note
    # Slide 40 gets Pódio Provisório note
    # Slide 41 gets Diagnóstico Erros note
    # Slide 42 gets 5 Leis note
    # Slide 43 gets Debate note
    # Slide 44 gets Referências note

    old_notes_block = nm_match.group(1)
    
    # Parse existing notes from old_notes_block
    # Using regex to get entries like `26: \`...\`,` or `26: "...",`
    entries = re.findall(r'(\d+)\s*:\s*([`"].*?[`"])(?=\s*,\s*\d+\s*:|\s*[`"]?\s*\}\s*;|\s*$)', old_notes_block, re.DOTALL)
    old_notes_dict = {int(k): v.strip() for k, v in entries}

    new_notes_lines = []
    # 1 to 23
    for k in range(1, 24):
        val = old_notes_dict.get(k, '`Roteiro oficial do slide.`')
        new_notes_lines.append(f'      {k}: {val},')

    # 24 to 32: Lilian
    for k in range(24, 33):
        escaped_note = LILIAN_NOTES[k].replace('`', '\\`')
        new_notes_lines.append(f'      {k}: `{escaped_note}`,')

    # 33: Kahoot 5 (was 26)
    val33 = old_notes_dict.get(26, """`[APRESENTADOR: Ao projetar este slide, anuncie ao microfone: 'Atenção turma, fase liberada no celular! Respondam às 3 perguntas da estação Pavilhão Aeroespacial & San Diego! O ranking ao vivo no telão está computando as respostas!']`""")
    new_notes_lines.append(f'      33: {val33},')

    # 34: UNIFESP (was 28)
    val34 = old_notes_dict.get(28, """`TEMPO: cerca de 3 minutos.
FALA SUGERIDA:
"Como futuros mestres e doutores do PPG-PIT, este slide nos toca diretamente. A integração entre a UNIFESP e o Parque Tecnológico não é teórica: é simbiótica. Nossas pesquisas, dissertações e teses nascem dentro dos laboratórios do PIT, conectadas às demandas reais da indústria aeroespacial, de TIC e de saúde."`""")
    new_notes_lines.append(f'      34: {val34},')

    # 35: Entrevista Renato (was 30)
    val35 = old_notes_dict.get(30, """`TEMPO: cerca de 6 minutos.
FALA SUGERIDA (RENATO PASCHOAL):
"Caros colegas e professores, para trazer o rigor da investigação empírica ao nosso seminário, realizei uma atividade de campo exclusiva: uma entrevista em profundidade com a liderança do Parque Tecnológico de São José dos Campos. O objetivo foi investigar como a teoria de orquestração se traduz na prática diária do maior complexo de inovação da região. Vamos acompanhar os relatos colhidos diretamente na gestão do Parque."`""")
    new_notes_lines.append(f'      35: {val35},')

    # 36: 4 Eixos Renato (was 31)
    val36 = old_notes_dict.get(31, """`TEMPO: cerca de 4 minutos.
FALA SUGERIDA (RENATO PASCHOAL):
"Da nossa entrevista com a liderança do PIT, sintetizamos 4 eixos práticos fundamentais:
1. Como gerenciar a governança sem hierarquia entre empresas concorrentes;
2. Como equilibrar a velocidade do mercado com os prazos de publicação acadêmica;
3. As cláusulas contratuais de sigilo e partilha de royalties;
4. As estratégias de atração e retenção de empresas âncoras para garantir a sustentabilidade econômico-financeira do Parque."`""")
    new_notes_lines.append(f'      36: {val36},')

    # 37: Bloco 6 Shen (was 32)
    val37 = old_notes_dict.get(32, """`No Bloco 6, Shen et al. trazem o contraponto crítico necessário a qualquer análise acadêmica séria. Ecossistemas não são panaceia. Existem riscos severos: assimetria predatória de poder, onde uma grande empresa se apropria do valor gerado por startups vulneráveis; o risco de aprisionamento tecnológico (lock-in); e o perigoso 'teatro da inovação' — quando parques gastam milhões em eventos, cafés e marketing sem gerar nenhuma patente ou produto real.`""")
    new_notes_lines.append(f'      37: {val37},')

    # 38: Bloco 6 Armadilhas (was 33)
    val38 = old_notes_dict.get(33, """`Aprofundando as armadilhas: analisamos como mitigar o lock-in cognitivo e a predação de propriedade intelectual. O papel do orquestrador neutro (como o PIT SJC) é justamente criar salvaguardas contratuais para que os elos mais fracos da rede — como startups e pesquisadores individuais — não sejam engolidos por corporações multinacionais.`""")
    new_notes_lines.append(f'      38: {val38},')

    # 39: Kahoot 6 (was 34)
    val39 = old_notes_dict.get(34, """`[APRESENTADOR: 'Última rodada de perguntas individuais! Acessem a estação Living Lab Net-Zero & Fronteiras no mapa do jogo. São as 3 questões finais decisivas sobre limitações e teatro da inovação! Respondam com agilidade para pontuar no ranking geral!']`""")
    new_notes_lines.append(f'      39: {val39},')

    # 40: Pódio Provisório (was 35)
    val40 = old_notes_dict.get(35, """`Com as 18 perguntas concluídas, projetamos aqui a classificação consolidada da turma! Jéssica conduzirá o encerramento da dinâmica, parabenizando os melhores colocados e preparando a turma para a análise diagnóstica dos erros mais frequentes.`""")
    new_notes_lines.append(f'      40: {val40},')

    # 41: Diagnóstico Erros (was 36)
    val41 = old_notes_dict.get(36, """`Análise pedagógica dos erros: examinamos quais conceitos geraram mais dúvidas na turma (coopetição, risco de coinovação, orquestração sem autoridade ou modelo CONNECT) e conectamos essas dúvidas diretamente aos autores seminais estudados.`""")
    new_notes_lines.append(f'      41: {val41},')

    # 42: 5 Leis (was 37)
    val42 = old_notes_dict.get(37, """`Encaminhando para as conclusões finais do nosso grupo: sintetizamos as 5 leis fundamentais dos ecossistemas de inovação. A lição mestra é que nenhum ator inova sozinho; o território vivo importa; e sem uma orquestração generosa e neutra, a rede se dispersa ou vira mero condomínio empresarial.`""")
    new_notes_lines.append(f'      42: {val42},')

    # 43: Debate (was 38)
    val43 = old_notes_dict.get(38, """`Abrimos agora a palavra para a banca examinadora — professora Iraci e professor Yukio — e para os nossos colegas de pós-graduação. Convidamos todos a refletirem sobre as perguntas provocativas que deixamos na tela.`""")
    new_notes_lines.append(f'      43: {val43},')

    # 44: Referências (was 39)
    val44 = old_notes_dict.get(39, """`Agradecemos a atenção de todos em nome do Grupo 5! Encerramos projetando as referências bibliográficas oficiais que sustentaram cada gráfico, número e argumento deste seminário.`""")
    new_notes_lines.append(f'      44: {val44}')

    new_notes_code = "const notesMap = {\n" + "\n".join(new_notes_lines) + "\n    };"

    content = content[:nm_match.start()] + new_notes_code + content[nm_match.end():]

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully patched {filepath} ({len(content):,} bytes)")

if __name__ == "__main__":
    deck_dir = r"02 - Seminário 5 - Ecossistemas de Inovação\Apresentação e Quiz Interativo"
    idx_file = os.path.join(deck_dir, "index.html")
    apr_file = os.path.join(deck_dir, "apresentacao_seminario_ecossistema_pit.html")

    patch_html_file(idx_file)
    patch_html_file(apr_file)
    print("ALL FILES PATCHED SUCCESSFULLY!")
