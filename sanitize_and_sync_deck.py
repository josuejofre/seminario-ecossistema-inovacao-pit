import os, re, shutil

# Caminhos principais
BASE_DIR = r"c:\Users\jj\OneDrive\Estudos\Edital unifesp PIT 2026\Disciplinas 02 2026\Gestão estratégica da inovação"
DIR_SEM = os.path.join(BASE_DIR, "Seminário")
DIR_APRES = os.path.join(BASE_DIR, "02 - Seminário 5 - Ecossistemas de Inovação", "Apresentação e Quiz Interativo")

print("--- 1. ATUALIZANDO SLIDES DA ENTREVISTA NO HTML (INDEX.HTML) ---")

slide_30_clean = """<!-- SLIDE 30: ATIVIDADE DE CAMPO - ENTREVISTA PIT SJC -->
      <section class="slide" data-slide="30" data-block="Entrevista" data-speaker="Renato Paschoal (4ª e 5ª)" data-time="6 min">
        <div class="slide-tag">🎙️ ESTUDO EMPÍRICO • ATIVIDADE DE CAMPO NO PIT SJC</div>
        <h2 class="slide-title">Entrevista com a Liderança do Parque: <span>A Visão Prática do Orquestrador</span></h2>
        
        <div class="punchline-card">
          <span style="font-size: 1.4rem;">🎯</span>
          <div class="punchline-quote">"Investigando na prática os desafios reais de governança, conciliação de interesses e transferência tecnológica no PIT São José dos Campos."</div>
        </div>

        <div class="grid-2-stacked">
          <div class="card card-glow-purple">
            <div class="card-title"><span>📋</span> Eixos Investigados no Roteiro de Entrevista</div>
            <ul class="bullet-list" style="margin-top: 0.6rem;">
              <li><span class="bullet-dot">▸</span> <strong>Governança sem Hierarquia:</strong> Como o orquestrador equilibra o tempo ágil da indústria privada com os prazos de rigor acadêmico da universidade pública.</li>
              <li><span class="bullet-dot">▸</span> <strong>Gestão de PI &amp; Sigilo:</strong> Mecanismos contratuais para viabilizar transferência tecnológica aberta sem comprometer patentes e segredos industriais.</li>
              <li><span class="bullet-dot">▸</span> <strong>Estabilidade da Rede:</strong> Políticas para reter empresas âncoras, atrair startups deep tech e evitar comportamentos oportunistas.</li>
            </ul>
            <div class="chips-row" style="margin-top: 0.8rem;">
              <span class="chip-badge">Liderança PIT SJC</span>
              <span class="chip-badge">Atividade Empírica</span>
              <span class="chip-badge">Condução: Renato Paschoal</span>
            </div>
          </div>

          <div class="card card-glow-cyan" style="display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 2rem;">
            <div style="font-size: 3rem; margin-bottom: 0.8rem;">🎥</div>
            <div class="card-title" style="margin-bottom: 0.4rem;">Registro Audiovisual &amp; Relatos da Liderança</div>
            <p class="card-desc" style="max-width: 480px; font-size: 0.95rem; line-height: 1.5;">
              Espaço reservado para a exibição dos trechos gravados em vídeo e debate dos principais insights colhidos diretamente com a coordenação de inovação do Parque.
            </p>
            <div style="margin-top: 1rem; padding: 0.5rem 1.2rem; background: rgba(6,182,212,0.15); border: 1px dashed var(--cyan-glow); border-radius: 8px; font-size: 0.85rem; color: var(--cyan-glow);">
              ▶️ Condução e comentários ao vivo: Renato Paschoal
            </div>
          </div>
        </div>
      </section>"""

slide_31_clean = """<!-- SLIDE 31: 4 EIXOS DE GOVERNANÇA PRÁTICA -->
      <section class="slide" data-slide="31" data-block="Entrevista" data-speaker="Renato Paschoal (4ª e 5ª)" data-time="4 min">
        <div class="slide-tag">📋 SÍNTESE PRÁTICA • EIXOS DE ANÁLISE</div>
        <h2 class="slide-title">4 Eixos de Governança Analisados na <span>Prática do PIT SJC</span></h2>
        
        <div class="punchline-card">
          <span style="font-size: 1.4rem;">⚖️</span>
          <div class="punchline-quote">"A ponte universidade-empresa exige alinhamento prévio de governança, confiança relacional e domínio do marco regulatório."</div>
        </div>

        <div class="grid-4">
          <div class="card card-glow-cyan">
            <div class="card-title"><span>📝</span> 1. Contratos &amp; PI Antecipados</div>
            <p class="card-desc">Definição explícita de Propriedade Intelectual antes do início dos testes no laboratório.</p>
            <ul class="bullet-list" style="margin-top: 0.6rem;">
              <li><span class="bullet-dot">▸</span> Segurança jurídica para atrair capital de grandes corporações.</li>
              <li><span class="bullet-dot">▸</span> Preservação da autoria científica e patentes dos pesquisadores.</li>
            </ul>
          </div>

          <div class="card card-glow-emerald">
            <div class="card-title"><span>☕</span> 2. Confiança &amp; Capital Relacional</div>
            <p class="card-desc">A proximidade e os ritos de convivência diária resolvem mais impasses que disputas formais.</p>
            <ul class="bullet-list" style="margin-top: 0.6rem;">
              <li><span class="bullet-dot">▸</span> O Nexus Hub estimula o networking informal entre fundadores.</li>
              <li><span class="bullet-dot">▸</span> Redução de custos transacionais baseada em reputação e reciprocidade.</li>
            </ul>
          </div>

          <div class="card card-glow-amber">
            <div class="card-title"><span>⚖️</span> 3. Aplicação do Marco Legal de CTI</div>
            <p class="card-desc">Uso estratégico da Lei 13.243/16 para desbloquear parcerias entre universidades e empresas.</p>
            <ul class="bullet-list" style="margin-top: 0.6rem;">
              <li><span class="bullet-dot">▸</span> Compartilhamento ágil de infraestrutura laboratorial federal.</li>
              <li><span class="bullet-dot">▸</span> Remuneração e bolsas de estímulo à inovação aberta.</li>
            </ul>
          </div>

          <div class="card card-glow-purple">
            <div class="card-title"><span>🎓</span> 4. Formação Transdisciplinar</div>
            <p class="card-desc">O ecossistema demanda mestres e doutores com sólida visão acadêmica e mentalidade empreendedora.</p>
            <ul class="bullet-list" style="margin-top: 0.6rem;">
              <li><span class="bullet-dot">▸</span> O PPG-PIT capacita talentos bilíngues (ciência + negócios).</li>
              <li><span class="bullet-dot">▸</span> Capacidade de traduzir demandas industriais em projetos de pesquisa.</li>
            </ul>
          </div>
        </div>
      </section>"""

def update_html_file(file_path):
    if not os.path.exists(file_path):
        return
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # 1. Substituir Slide 30 / antigo 34
    pattern_s30 = r"<!-- SLIDE 34: ENTREVISTA EXCLUSIVA LUIZ FERNANDO -->[\s\S]*?</section>"
    if re.search(pattern_s30, content):
        content = re.sub(pattern_s30, slide_30_clean, content)
    else:
        # Tentar pegar por data-slide="30"
        pattern_s30_alt = r"<section class=\"slide\"[^>]*data-slide=\"30\"[\s\S]*?</section>"
        content = re.sub(pattern_s30_alt, slide_30_clean, content)

    # 2. Substituir Slide 31 / antigo 35
    pattern_s31 = r"<!-- SLIDE 35: 4 LIÇÕES DA ENTREVISTA -->[\s\S]*?</section>"
    if re.search(pattern_s31, content):
        content = re.sub(pattern_s31, slide_31_clean, content)
    else:
        pattern_s31_alt = r"<section class=\"slide\"[^>]*data-slide=\"31\"[\s\S]*?</section>"
        content = re.sub(pattern_s31_alt, slide_31_clean, content)

    # 3. Limpar menções no texto dos cards ou agenda
    content = content.replace("e a entrevista com o coordenador de inovação do Parque, Luiz Fernando Carvalho", "e a atividade de campo com a liderança do PIT SJC conduzida pelo Renato")
    content = content.replace("Luiz Fernando Carvalho", "Liderança do PIT SJC")

    # 4. Atualizar notesMap
    old_note_2 = 'Passaremos pela biologia de Moore, as 5 hélices, a orquestração de Machado et al., o benchmarking internacional de San Diego e as lições exclusivas da nossa entrevista técnica com o Coordenador de Inovação do PIT, Luiz Fernando Carvalho. Ao final de cada bloco, teremos a parada estratégica para o Kahoot RPG!'
    new_note_2 = 'Passaremos pela biologia de Moore, as 5 hélices, a orquestração de Machado et al., o benchmarking internacional de San Diego e a atividade empírica de campo no PIT SJC conduzida pelo Renato. Ao final de cada bloco, teremos a parada estratégica para o Kahoot RPG!'
    content = content.replace(old_note_2, new_note_2)

    old_note_34 = 'Tivemos a honra de entrevistar com exclusividade o Coordenador de Inovação do PIT, Luiz Fernando Carvalho. A frase dele resume a nossa disciplina: \'O orquestrador é o amortecedor de choques e o tradutor de dialetos entre universidade e corporação.\''
    new_note_34 = 'Neste momento, apresento a nossa atividade empírica no Parque Tecnológico de São José dos Campos. O objetivo desta atividade é confrontar os conceitos teóricos de governança e orquestração com a prática de quem atua na gestão do ecossistema. Vamos acompanhar os eixos investigados e as declarações da liderança do Parque.'
    content = content.replace(old_note_34, new_note_34)

    old_note_35 = 'Sintetizamos a entrevista em quatro lições práticas de ouro: alinhamento contratual no dia zero, construção contínua de confiança pessoal, domínio do Marco Legal de CTI e formação de mestres com mindset de negócios e agilidade.'
    new_note_35 = 'Estruturamos a análise de governança do PIT SJC em quatro eixos fundamentais: a antecipação contratual de propriedade intelectual, a construção do capital relacional e confiança mútua, a aplicação do Marco Legal de CTI e a formação de pesquisadores com visão de negócios no PPG-PIT.'
    content = content.replace(old_note_35, new_note_35)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[OK] Atualizado: {file_path}")

update_html_file(os.path.join(DIR_SEM, "index.html"))
update_html_file(os.path.join(DIR_SEM, "apresentacao_seminario_ecossistema_pit.html"))
update_html_file(os.path.join(DIR_APRES, "index.html"))
update_html_file(os.path.join(DIR_APRES, "apresentacao_seminario_ecossistema_pit.html"))

print("\n--- 2. ATUALIZANDO ROTEIRO DE FALAS DOS APRESENTADORES ---")
def update_roteiro_file(file_path):
    if not os.path.exists(file_path):
        return
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        rot = f.read()

    # Limpar slide 2
    rot = rot.replace("- Em seguida, traremos o caso concreto do PIT SJC e a entrevista exclusiva gravada pelo Renato com o coordenador de inovação do Parque, Luiz Fernando Carvalho;",
                      "- Em seguida, traremos o caso concreto do PIT SJC e a atividade de campo com a liderança do Parque conduzida pelo Renato;")

    # Limpar seção da entrevista
    pattern_entrevista_rot = r"SLIDE 26 \| ENTREVISTA EXCLUSIVA: LUIZ FERNANDO CARVALHO[\s\S]*?SLIDE 28 \| BLOCO 6"
    new_entrevista_rot = """SLIDE 30 | ATIVIDADE DE CAMPO: ENTREVISTA COM A LIDERANÇA DO PIT SJC
Tema: A Visão Prática do Orquestrador no Parque Tecnológico
Apresentador(a): Renato Paschoal (Quarta e Quinta)
Tempo sugerido: 6 min
Frase de Efeito no Slide: "Investigando na prática os desafios reais de governança e transferência tecnológica no PIT São José dos Campos."

FALA SUGERIDA DO APRESENTADOR (RENATO PASCHOAL):
"Caros colegas e professores, para trazer a voz da realidade ao nosso seminário, desenvolvemos uma atividade prática de campo com a liderança do Parque Tecnológico de São José dos Campos.
Nosso objetivo central não é apenas ilustrar o seminário, mas testar se as teorias que estudamos — como a coordenação sem hierarquia de Machado et al. e as lições do caso San Diego — se sustentam na prática cotidiana do orquestrador.

Organizamos nossa investigação em três eixos críticos:
1. Primeiro: como equilibrar a urgência da indústria por entregas imediatas com o tempo necessário para a pesquisa científica e a formação acadêmica;
2. Segundo: como estruturar a partilha de propriedade intelectual e sigilo sem inviabilizar publicações e patentes dos pesquisadores;
3. Terceiro: quais mecanismos relacionais mantêm empresas âncoras e startups engajadas no longo prazo.

[RENATO: Espaço para exibição do vídeo gravado com a liderança do PIT SJC e comentários dos destaques mais expressivos da fala do entrevistado]."

--------------------------------------------------------------------------------
SLIDE 31 | 4 EIXOS DE GOVERNANÇA ANALISADOS NA PRÁTICA DO PIT SJC
Tema: Alinhamento Contratual, Confiança, Marco Legal de CTI e Formação
Apresentador(a): Renato Paschoal (Quarta e Quinta)
Tempo sugerido: 4 min
Frase de Efeito no Slide: "A ponte universidade-empresa exige alinhamento prévio de governança, confiança relacional e domínio do marco regulatório."

FALA SUGERIDA DO APRESENTADOR (RENATO PASCHOAL):
"A partir da análise teórica e da nossa imersão de campo, estruturamos quatro eixos de governança fundamentais para a atuação do orquestrador no PIT SJC:
1. Contratos e Propriedade Intelectual Antecipados: O alinhamento de titularidade desde o primeiro dia dá segurança para que grandes corporações invistam sem temor de judicialização futura, ao mesmo tempo em que protege o pesquisador;
2. Confiança e Capital Relacional: Em ecossistemas onde não há subordinação hierárquica, a reputação e a convivência no Nexus Hub constroem pontes mais fortes do que exigências punitivas;
3. Aplicação Estratégica do Marco Legal de CTI (Lei 13.243/16): Dominar as ferramentas jurídicas permite compartilhar laboratórios públicos e conceder bolsas de inovação com total respaldo legal;
4. Formação Transdisciplinar de Talentos: O ecossistema não necessita apenas de cientistas de bancada ou administradores comerciais; ele demanda profissionais que falem os dois idiomas — exatamente o perfil que nosso programa de mestrado e doutorado no PPG-PIT desenvolve."

--------------------------------------------------------------------------------
SLIDE 32 | BLOCO 6"""

    if "SLIDE 26 | ENTREVISTA EXCLUSIVA: LUIZ FERNANDO CARVALHO" in rot:
        rot = re.sub(pattern_entrevista_rot, new_entrevista_rot, rot)
    elif "SLIDE 30 | ATIVIDADE DE CAMPO" not in rot:
        # Se os números forem diferentes, procurar pelo título
        pattern_alt = r"SLIDE \d+ \| ENTREVISTA EXCLUSIVA[\s\S]*?SLIDE \d+ \| BLOCO 6"
        rot = re.sub(pattern_alt, new_entrevista_rot, rot)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(rot)
    print(f"[OK] Roteiro atualizado: {file_path}")

update_roteiro_file(os.path.join(DIR_SEM, "roteiro_falas_apresentadores.txt"))
update_roteiro_file(os.path.join(DIR_APRES, "roteiro_falas_apresentadores.txt"))

print("\n--- 3. ATUALIZANDO PERGUNTAS DO BLOCO 3 NO ADMIN.HTML E JOGO.HTML COM AS SUGESTÕES DA JÉSSICA ---")

# Perguntas oficiais da Jéssica da planilha:
# Q1: A orquestração de redes de inovação ocorre sem o apoio de: b) autoridade hierárquica
# Q4: Qual papel do orquestrador traz conhecimento de fora da rede e o dissemina entre os membros? c) gatekeeper
# Q5: A competência de orquestração combina: b) conhecimentos, habilidades e atitudes (CHA)
# Q2: Atrair e selecionar parceiros para o ecossistema corresponde a qual dimensão? b) mobilização
# Q3: Qual dimensão busca manter a colaboração entre os membros e evitar individualismo e oportunismo? a) estabilização da rede
# Q6: Uma capacidade se torna competência quando: c) é mobilizada em uma ação num contexto específico

# Vamos atualizar admin.html
admin_path = os.path.join(DIR_SEM, "admin.html")
with open(admin_path, "r", encoding="utf-8", errors="ignore") as f:
    admin_content = f.read()

# Substituir o Bloco 3 em admin.html
bloco3_admin_new = """      // BLOCO 3 (Oficial - Perguntas formuladas por Jéssica Pascotto David)
      {
        id: "b3_q1",
        block: 3,
        blockName: "Bloco 3: Governança e Orquestração",
        title: "Coordenação sem Hierarquia",
        question: "A orquestração de redes de inovação ocorre sem o apoio de:",
        options: [
          { key: "A", text: "Autoridade hierárquica", correct: true },
          { key: "B", text: "Recursos financeiros", correct: false },
          { key: "C", text: "Troca de conhecimento", correct: false },
          { key: "D", text: "Parceiros externos", correct: false }
        ],
        insight: "A orquestração ocorre por meio de coordenação e influência entre os participantes da rede, e não pelo uso de autoridade hierárquica direta (Dhanaraj & Parkhe, 2006; Machado et al., 2025)."
      },
      {
        id: "b3_q2",
        block: 3,
        blockName: "Bloco 3: Governança e Orquestração",
        title: "Papéis do Orquestrador (Gatekeeper)",
        question: "Qual papel do orquestrador traz conhecimento de fora da rede e o dissemina entre os membros?",
        options: [
          { key: "A", text: "Gatekeeper (Porta de entrada)", correct: true },
          { key: "B", text: "Juiz (Monitor de conformidade)", correct: false },
          { key: "C", text: "Leiloeiro (Criador da agenda)", correct: false },
          { key: "D", text: "Comunicador externo", correct: false }
        ],
        insight: "O gatekeeper funciona como uma porta de entrada para conhecimentos externos, extraindo informações relevantes de fora da rede e disseminando-as entre os participantes."
      },
      {
        id: "b3_q3",
        block: 3,
        blockName: "Bloco 3: Governança e Orquestração",
        title: "Modelo CHA de Competências",
        question: "Segundo o modelo consolidado por Machado, Faccin & Bittencourt, a competência de orquestração combina:",
        options: [
          { key: "A", text: "Conhecimentos, habilidades e atitudes (Saber, Saber Fazer e Saber Ser)", correct: true },
          { key: "B", text: "Recursos, processos e tecnologia da informação", correct: false },
          { key: "C", text: "Poder formal, hierarquia e controle de metas", correct: false },
          { key: "D", text: "Papéis, contratos punitivos e cotas de mercado", correct: false }
        ],
        insight: "A competência é formada pela combinação entre saber (conhecimentos), saber fazer (habilidades) e saber ser (atitudes) mobilizados em ação contextual (Ruas; Le Boterf; Antonello)."
      },"""

# Localizar bloco 3 em admin.html
bloco3_pattern_admin = r"// BLOCO 3[\s\S]*?// BLOCO 4"
if re.search(bloco3_pattern_admin, admin_content):
    admin_content = re.sub(bloco3_pattern_admin, bloco3_admin_new + "\n\n      // BLOCO 4", admin_content)
    with open(admin_path, "w", encoding="utf-8") as f:
        f.write(admin_content)
    # Copiar para pasta Apresentação
    # shutil.copy2(admin_path, os.path.join(DIR_APRES, "admin.html"))
    print("[OK] admin.html atualizado com as perguntas da Jéssica!")

# Atualizar jogo.html
jogo_path = os.path.join(DIR_SEM, "jogo.html")
with open(jogo_path, "r", encoding="utf-8", errors="ignore") as f:
    jogo_content = f.read()

bloco3_jogo_new = """      // BLOCO 3 (Perguntas Oficiais da Jéssica Pascotto David)
      {
        id: "b3_q1",
        block: 3,
        stationName: "Centro de Governança do PIT",
        question: "A orquestração de redes de inovação ocorre sem o apoio de:",
        correctOption: "Autoridade hierárquica",
        distractors: [
          "Recursos financeiros",
          "Troca de conhecimento"
        ],
        explanation: "A orquestração ocorre por meio de coordenação e influência mútua entre os participantes da rede, e não pelo uso de autoridade hierárquica direta."
      },
      {
        id: "b3_q2",
        block: 3,
        stationName: "Centro de Governança do PIT",
        question: "Qual papel do orquestrador traz conhecimento de fora da rede e o dissemina entre os membros?",
        correctOption: "Gatekeeper (Porta de entrada)",
        distractors: [
          "Juiz (Monitor de padrões)",
          "Leiloeiro (Propositor de agenda)"
        ],
        explanation: "O gatekeeper funciona como uma porta de entrada para conhecimentos externos, extraindo dados relevantes de fora e disseminando-os aos parceiros."
      },
      {
        id: "b3_q3",
        block: 3,
        stationName: "Centro de Governança do PIT",
        question: "A competência de orquestração do indivíduo combina quais elementos fundamentais?",
        correctOption: "Conhecimentos, habilidades e atitudes (Modelo CHA)",
        distractors: [
          "Recursos, processos e tecnologia da informação",
          "Poder formal, hierarquia e controle contratual"
        ],
        explanation: "A competência individual é formada pela tríade CHA: saber (conhecimentos), saber fazer (habilidades) e saber ser (atitudes) mobilizados em contexto prático."
      },"""

bloco3_pattern_jogo = r"// BLOCO 3[\s\S]*?// BLOCO 4"
if re.search(bloco3_pattern_jogo, jogo_content):
    jogo_content = re.sub(bloco3_pattern_jogo, bloco3_jogo_new + "\n\n      // BLOCO 4", jogo_content)
    with open(jogo_path, "w", encoding="utf-8") as f:
        f.write(jogo_content)
    # Copiar para pasta Apresentação
    # shutil.copy2(jogo_path, os.path.join(DIR_APRES, "jogo.html"))
    print("[OK] jogo.html atualizado com as perguntas da Jéssica!")

print("\n--- SANITIZAÇÃO E ATUALIZAÇÃO CONCLUÍDAS COM SUCESSO! ---")
