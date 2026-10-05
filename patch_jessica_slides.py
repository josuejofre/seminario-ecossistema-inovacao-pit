# -*- coding: utf-8 -*-
"""
Script para incorporar os 7 slides de Governança e Orquestração da Jéssica
no deck master oficial (index.html e apresentacao_seminario_ecossistema_pit.html).
Substitui os antigos slides 12, 13, 14 por 7 slides ricos baseados em Machado et al. (2025).
"""

import os
import re

jessica_slides_html = """
    <!-- SLIDE 12: BLOCO 3 - ABERTURA & MÉTODO (JÉSSICA SLIDE 1) -->
    <section class="slide" data-slide="12" data-block="Bloco 3" data-speaker="Jessica Pascotto David (4ª)" data-time="1 min">
      <div class="slide-tag">🏛️ BLOCO 3 • GOVERNANÇA E ORQUESTRAÇÃO</div>
      <h2 class="slide-title">Questão Central & Método: <span>Como Coordenar Atores Independentes?</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">🎯</span>
        <div class="punchline-quote">"Como coordenar atores independentes e quais mecanismos e competências permitem a orquestração do ecossistema?"</div>
      </div>

      <div class="grid-3" style="margin-bottom: 1rem;">
        <div class="card card-glow-cyan">
          <div class="card-title"><span>👤</span> 01 · QUEM</div>
          <div style="font-size: 1.1rem; font-weight: 800; color: #fff; margin: 0.4rem 0;">O Papel do Orquestrador</div>
          <p class="card-desc">Como conduzir atividades e coordenar a rede sem poder de chefia ou autoridade hierárquica.</p>
        </div>
        <div class="card card-glow-purple">
          <div class="card-title"><span>⚙️</span> 02 · COMO</div>
          <div style="font-size: 1.1rem; font-weight: 800; color: #fff; margin: 0.4rem 0;">Os 6 Mecanismos em Foco</div>
          <p class="card-desc">Agenda, Mobilização, Estabilização, Conhecimento, Coordenação e Comunicação.</p>
        </div>
        <div class="card card-glow-emerald">
          <div class="card-title"><span>🧠</span> 03 · COM O QUÊ</div>
          <div style="font-size: 1.1rem; font-weight: 800; color: #fff; margin: 0.4rem 0;">Competências (CHA)</div>
          <p class="card-desc">Conhecimentos, habilidades e atitudes mobilizados na ação situada em contexto.</p>
        </div>
      </div>

      <div class="card" style="padding: 0.9rem 1.4rem; background: rgba(6, 182, 212, 0.06); border-color: rgba(6, 182, 212, 0.3); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 0.8rem;">
        <div style="font-size: 0.88rem; color: #e2e8f0;">
          📚 <strong>Artigo-Base:</strong> Machado, Faccin & Bittencourt (2025). <em>Orchestration competence in innovation ecosystem</em>. INMR, 22(3).
        </div>
        <div class="chips-row" style="margin: 0;">
          <span class="chip-badge">Revisão Sistemática (RSL)</span>
          <span class="chip-badge">Scopus & Web of Science</span>
          <span class="chip-badge">670 ➔ 120 ➔ 10 Estudos</span>
        </div>
      </div>
    </section>

    <!-- SLIDE 13: BLOCO 3 - PAPEL DO ORQUESTRADOR (JÉSSICA SLIDE 2) -->
    <section class="slide" data-slide="13" data-block="Bloco 3" data-speaker="Jessica Pascotto David (4ª)" data-time="1.5 min">
      <div class="slide-tag">👑 BLOCO 3 • O PAPEL DO ORQUESTRADOR</div>
      <h2 class="slide-title">01 · O Papel do Orquestrador: <span>Coordenar sem Autoridade Hierárquica</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">⚖️</span>
        <div class="punchline-quote">"Atores interdependentes, mas hierarquicamente independentes: ninguém manda em ninguém."</div>
      </div>

      <div class="grid-2">
        <div class="card card-glow-amber">
          <div class="card-title"><span>⚠️</span> O Paradoxo do Ecossistema</div>
          <p class="card-desc" style="font-size: 0.95rem; line-height: 1.55;">
            Os participantes dependem uns dos outros para inovar (empresas, universidades, governo e sociedade civil), mas nenhum responde à chefia do outro.
          </p>
          <div style="margin-top: 1rem; padding: 0.85rem; background: rgba(0,0,0,0.3); border-radius: var(--radius-sm); border-left: 3px solid var(--amber-accent); font-size: 0.86rem; color: #cbd5e1;">
            <strong>Sem orquestração:</strong> dispersão, oportunismo e conflitos de interesse.<br>
            <strong>Com orquestrador:</strong> alinhamento estratégico, confiança relacional e co-criação.
          </div>
        </div>

        <div class="card card-glow-cyan">
          <div class="card-title"><span>🎭</span> Os 13 Papéis Consolidados pelo Artigo</div>
          <p class="card-desc" style="font-size: 0.92rem; margin-bottom: 0.75rem;">
            O papel do orquestrador não é fixo; ele assume múltiplos papéis dinâmicos e combinados ao longo do tempo (Dhanaraj & Parkhe, 2006; Pikkarainen et al., 2017):
          </p>
          <div style="display: flex; flex-wrap: wrap; gap: 0.45rem;">
            <span class="chip-badge" style="background: rgba(6, 182, 212, 0.2); color: #67e8f9;">🏛️ Arquiteto</span>
            <span class="chip-badge" style="background: rgba(139, 92, 246, 0.2); color: #c084fc;">🔨 Leiloeiro</span>
            <span class="chip-badge" style="background: rgba(16, 185, 129, 0.2); color: #6ee7b7;">🤝 Coordenador</span>
            <span class="chip-badge" style="background: rgba(245, 158, 11, 0.2); color: #fcd34d;">🧭 Líder</span>
            <span class="chip-badge" style="background: rgba(59, 130, 246, 0.2); color: #93c5fd;">🚪 Gatekeeper</span>
            <span class="chip-badge" style="background: rgba(244, 63, 94, 0.2); color: #fda4af;">📢 Representante</span>
            <span class="chip-badge" style="background: rgba(168, 85, 247, 0.2); color: #d8b4fe;">🎼 Regente</span>
            <span class="chip-badge" style="background: rgba(234, 179, 8, 0.2); color: #fef08a;">⚖️ Juiz</span>
            <span class="chip-badge" style="background: rgba(20, 184, 166, 0.2); color: #5eead4;">📡 Comunicador</span>
            <span class="chip-badge">Facilitador</span>
            <span class="chip-badge">Mediador</span>
            <span class="chip-badge">Promotor</span>
            <span class="chip-badge">Conector</span>
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 14: BLOCO 3 - AS DIMENSÕES DA ORQUESTRAÇÃO (JÉSSICA SLIDE 3) -->
    <section class="slide" data-slide="14" data-block="Bloco 3" data-speaker="Jessica Pascotto David (4ª)" data-time="1 min">
      <div class="slide-tag">📈 BLOCO 3 • EVOLUÇÃO TEÓRICA</div>
      <h2 class="slide-title">02 · As Dimensões da Orquestração: <span>Das 3 às 8 Dimensões na Literatura</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">📚</span>
        <div class="punchline-quote">"De 2006 a 2021: a orquestração expandiu da transferência tecnológica para a governança relacional."</div>
      </div>

      <div class="grid-4" style="margin-bottom: 1.25rem;">
        <div class="card" style="border-top: 3px solid #38bdf8;">
          <div style="font-size: 0.8rem; color: var(--blue-electric); font-weight: 700;">2006 • MARCO TEÓRICO</div>
          <div style="font-size: 1.15rem; font-weight: 800; color: #fff; margin: 0.25rem 0;">Dhanaraj & Parkhe</div>
          <div style="font-size: 0.85rem; color: var(--text-muted);"><strong>3 Dimensões Clássicas:</strong> Mobilidade do Conhecimento, Apropriabilidade da Inovação e Estabilidade da Rede.</div>
        </div>
        <div class="card" style="border-top: 3px solid #a855f7;">
          <div style="font-size: 0.8rem; color: var(--purple-glow); font-weight: 700;">2011 • EXPANSÃO</div>
          <div style="font-size: 1.15rem; font-weight: 800; color: #fff; margin: 0.25rem 0;">Hurmelinna-Laukkanen</div>
          <div style="font-size: 0.85rem; color: var(--text-muted);"><strong>6 Dimensões:</strong> Adiciona Definição de Agenda, Mobilização e Coordenação de Processos.</div>
        </div>
        <div class="card" style="border-top: 3px solid #34d399;">
          <div style="font-size: 0.8rem; color: #34d399; font-weight: 700;">2019 • COCRIAÇÃO</div>
          <div style="font-size: 1.15rem; font-weight: 800; color: #fff; margin: 0.25rem 0;">Da Silva & Bitencourt</div>
          <div style="font-size: 0.85rem; color: var(--text-muted);"><strong>7 Dimensões:</strong> Incorpora a Cocriação de Valor como processo relacional contínuo.</div>
        </div>
        <div class="card" style="border-top: 3px solid #f43f5e;">
          <div style="font-size: 0.8rem; color: var(--rose-accent); font-weight: 700;">2021 • COMUNICAÇÃO</div>
          <div style="font-size: 1.15rem; font-weight: 800; color: #fff; margin: 0.25rem 0;">Mignoni et al.</div>
          <div style="font-size: 0.85rem; color: var(--text-muted);"><strong>8 Dimensões:</strong> Acrescenta a Gestão da Comunicação e Engajamento Externo.</div>
        </div>
      </div>

      <div class="card card-glow-cyan" style="padding: 1rem 1.4rem;">
        <div style="font-weight: 800; color: #fff; margin-bottom: 0.4rem; font-size: 0.95rem;">
          🎯 Destaque de Machado et al. (2025): As 6 Dimensões Centrais em Foco
        </div>
        <div style="font-size: 0.88rem; color: #cbd5e1;">
          O seminário aprofunda as 6 dimensões operacionais do orquestrador: <strong>(1) Definição de Agenda, (2) Mobilização, (3) Estabilização da Rede, (4) Conhecimento, (5) Coordenação e (6) Comunicação</strong>. Apropriabilidade e Cocriação completam o mapa conceitual.
        </div>
      </div>
    </section>

    <!-- SLIDE 15: BLOCO 3 - MECANISMOS 1/2 (JÉSSICA SLIDE 4) -->
    <section class="slide" data-slide="15" data-block="Bloco 3" data-speaker="Jessica Pascotto David (4ª)" data-time="2 min">
      <div class="slide-tag">⚙️ BLOCO 3 • MECANISMOS EM AÇÃO (1/2)</div>
      <h2 class="slide-title">03 · Mecanismos (1/2): <span>Dar Direção, Reunir e Manter os Atores</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">🧭</span>
        <div class="punchline-quote">"Como atrair e manter unidos atores que não respondem à mesma hierarquia corporativa?"</div>
      </div>

      <div class="grid-3">
        <div class="card card-glow-cyan">
          <div class="card-title">1. Definição de Agenda</div>
          <p class="card-desc" style="font-size: 0.88rem; margin-bottom: 0.75rem;">
            Criar e comunicar uma agenda compartilhada que direcione e engaje os membros do ecossistema.
          </p>
          <div style="background: rgba(0,0,0,0.3); padding: 0.75rem; border-radius: var(--radius-sm); font-size: 0.82rem; line-height: 1.45;">
            <strong>Papéis do Orquestrador:</strong><br>
            • <strong>Arquiteto:</strong> identifica oportunidades e define metas;<br>
            • <strong>Leiloeiro:</strong> propõe a agenda e introduz a visão conjunta.
          </div>
        </div>

        <div class="card card-glow-purple">
          <div class="card-title">2. Mobilização</div>
          <p class="card-desc" style="font-size: 0.88rem; margin-bottom: 0.75rem;">
            Atrair e selecionar parceiros qualificados para o ecossistema, mapeando motivadores reais.
          </p>
          <div style="background: rgba(0,0,0,0.3); padding: 0.75rem; border-radius: var(--radius-sm); font-size: 0.82rem; line-height: 1.45;">
            <strong>Papéis do Orquestrador:</strong><br>
            • <strong>Arquiteto:</strong> seleciona os membros estratégicos da rede;<br>
            • <strong>Leiloeiro:</strong> cria e promove ativamente a visão conjunta.
          </div>
        </div>

        <div class="card card-glow-emerald">
          <div class="card-title">3. Estabilização da Rede</div>
          <p class="card-desc" style="font-size: 0.88rem; margin-bottom: 0.75rem;">
            Manter a colaboração duradoura por cultura, identidade e valores, evitando oportunismo e atritos.
          </p>
          <div style="background: rgba(0,0,0,0.3); padding: 0.75rem; border-radius: var(--radius-sm); font-size: 0.82rem; line-height: 1.45;">
            <strong>Papéis do Orquestrador:</strong><br>
            • <strong>Coordenador:</strong> administra interações para fortalecer laços;<br>
            • <strong>Líder:</strong> motiva a colaboração contínua de longo prazo.
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 16: BLOCO 3 - MECANISMOS 2/2 (JÉSSICA SLIDE 5) -->
    <section class="slide" data-slide="16" data-block="Bloco 3" data-speaker="Jessica Pascotto David (4ª)" data-time="2 min">
      <div class="slide-tag">📡 BLOCO 3 • MECANISMOS EM AÇÃO (2/2)</div>
      <h2 class="slide-title">04 · Mecanismos (2/2): <span>Fazer Conhecimento, Ação e Mensagem Circularem</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">🔄</span>
        <div class="punchline-quote">"Fazer o ecossistema respirar: absorver ciência, alinhar entregas e projetar valor para a sociedade."</div>
      </div>

      <div class="grid-3">
        <div class="card card-glow-blue">
          <div class="card-title">4. Conhecimento</div>
          <p class="card-desc" style="font-size: 0.88rem; margin-bottom: 0.75rem;">
            Compartilhar, adquirir, transferir e implementar conhecimento técnico no ecossistema.
          </p>
          <div style="background: rgba(0,0,0,0.3); padding: 0.75rem; border-radius: var(--radius-sm); font-size: 0.82rem; line-height: 1.45;">
            <strong>Papéis do Orquestrador:</strong><br>
            • <strong>Gatekeeper:</strong> extrai conhecimento de fora e dissemina;<br>
            • <strong>Representante:</strong> compartilha e filtra para fora;<br>
            • <strong>Regente:</strong> transforma informação em competência.
          </div>
        </div>

        <div class="card card-glow-amber">
          <div class="card-title">5. Coordenação</div>
          <p class="card-desc" style="font-size: 0.88rem; margin-bottom: 0.75rem;">
            Dirigir o planejamento, monitorar a execução e orientar todos os membros ao mesmo objetivo.
          </p>
          <div style="background: rgba(0,0,0,0.3); padding: 0.75rem; border-radius: var(--radius-sm); font-size: 0.82rem; line-height: 1.45;">
            <strong>Papéis do Orquestrador:</strong><br>
            • <strong>Regente:</strong> aloca tarefas e orquestra o ritmo;<br>
            • <strong>Juiz:</strong> monitora e ajusta padrões de desempenho;<br>
            • <strong>Líder:</strong> esclarece papéis e resolve gargalos.
          </div>
        </div>

        <div class="card card-glow-rose">
          <div class="card-title">6. Comunicação</div>
          <p class="card-desc" style="font-size: 0.88rem; margin-bottom: 0.75rem;">
            Divulgar ações, projetos institucionais e oportunidades, engajando a sociedade e stakeholders.
          </p>
          <div style="background: rgba(0,0,0,0.3); padding: 0.75rem; border-radius: var(--radius-sm); font-size: 0.82rem; line-height: 1.45;">
            <strong>Papel do Orquestrador:</strong><br>
            • <strong>Comunicador:</strong> conduz a estratégia de comunicação institucional, atrai visibilidade e mobiliza o território.
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 17: BLOCO 3 - COMPETÊNCIAS CHA (JÉSSICA SLIDE 6) -->
    <section class="slide" data-slide="17" data-block="Bloco 3" data-speaker="Jessica Pascotto David (4ª)" data-time="1.75 min">
      <div class="slide-tag">🧠 BLOCO 3 • O MODELO CHA</div>
      <h2 class="slide-title">05 · Competências de Orquestração: <span>O Modelo CHA em Ação</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">💡</span>
        <div class="punchline-quote">"Não se trata de pessoas competentes no abstrato, mas de ações competentes situadas no contexto."</div>
      </div>

      <div class="grid-2">
        <div class="card card-glow-purple">
          <div class="card-title"><span>🧩</span> O Tripé da Competência Individual</div>
          <div style="display: flex; gap: 0.8rem; margin: 1rem 0;">
            <div style="flex: 1; background: rgba(6, 182, 212, 0.15); border: 1px solid rgba(6, 182, 212, 0.3); padding: 0.75rem; border-radius: var(--radius-sm); text-align: center;">
              <strong style="color: var(--cyan-light); font-size: 1rem;">C</strong><br>
              <span style="font-size: 0.8rem; color: #cbd5e1;">Conhecimentos<br><em>(Saber)</em></span>
            </div>
            <div style="flex: 1; background: rgba(139, 92, 246, 0.15); border: 1px solid rgba(139, 92, 246, 0.3); padding: 0.75rem; border-radius: var(--radius-sm); text-align: center;">
              <strong style="color: var(--purple-glow); font-size: 1rem;">H</strong><br>
              <span style="font-size: 0.8rem; color: #cbd5e1;">Habilidades<br><em>(Saber Fazer)</em></span>
            </div>
            <div style="flex: 1; background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.3); padding: 0.75rem; border-radius: var(--radius-sm); text-align: center;">
              <strong style="color: #34d399; font-size: 1rem;">A</strong><br>
              <span style="font-size: 0.8rem; color: #cbd5e1;">Atitudes<br><em>(Saber Ser)</em></span>
            </div>
          </div>
          <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.5;">
            <strong>Evolução Teórica:</strong> Em Ruas (2005), <em>capacidade</em> é potencial; torna-se <em>competência</em> ao ser mobilizada na ação. Le Boterf (2003) e Antonello (2011) consolidam que a competência depende do contexto cultural e relacional.
          </p>
        </div>

        <div class="card card-glow-cyan">
          <div class="card-title"><span>🌟</span> Definição Proposta por Machado et al. (2025)</div>
          <blockquote style="font-size: 0.92rem; font-style: italic; color: #e2e8f0; border-left: 3px solid var(--cyan-glow); padding-left: 0.85rem; margin: 0.6rem 0 1rem;">
            "Combinação de conhecimentos, habilidades e atitudes que, mobilizada pelo orquestrador para desenvolver, gerenciar e coordenar o ecossistema, permite a interação colaborativa, interdependente e cocriativa entre os atores."
          </blockquote>
          <div style="background: rgba(0,0,0,0.3); padding: 0.85rem; border-radius: var(--radius-sm); font-size: 0.84rem; color: #cbd5e1;">
            📌 <strong>33 Atributos Mapeados:</strong> Incluem gerar confiança mútua, negociar interesses conflitantes, ter visão sistêmica, diplomacia relacional e resiliência política.
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 18: BLOCO 3 - SÍNTESE & AGENDA (JÉSSICA SLIDE 7) -->
    <section class="slide" data-slide="18" data-block="Bloco 3" data-speaker="Jessica Pascotto David (4ª)" data-time="1 min">
      <div class="slide-tag">🎯 BLOCO 3 • SÍNTESE & AGENDA</div>
      <h2 class="slide-title">06 · Síntese do Bloco: <span>"Ecossistema Não se Comanda: se Orquestra"</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">🎻</span>
        <div class="punchline-quote">"Ecossistema não se comanda: se orquestra."</div>
      </div>

      <div class="grid-2" style="margin-bottom: 1rem;">
        <div class="card card-glow-emerald">
          <div class="card-title"><span>🪜</span> A Resposta em Três Degraus</div>
          <ul class="bullet-list" style="margin-top: 0.6rem; font-size: 0.9rem;">
            <li><span class="bullet-dot">▸</span> <strong>Degrau 1 (O Orquestrador):</strong> Conduz atividades por influência, liderança adaptativa e legitimidade, sem hierarquia formal.</li>
            <li><span class="bullet-dot">▸</span> <strong>Degrau 2 (Os Mecanismos):</strong> Opera as 6 dimensões (agenda, mobilização, estabilização, conhecimento, coordenação, comunicação) com 13 papéis flexíveis.</li>
            <li><span class="bullet-dot">▸</span> <strong>Degrau 3 (A Competência):</strong> Mobiliza Conhecimentos, Habilidades e Atitudes (CHA) aplicados no contexto real.</li>
          </ul>
        </div>

        <div class="card card-glow-amber">
          <div class="card-title"><span>🔭</span> Limites do Estudo & Agenda Futura</div>
          <div style="font-size: 0.88rem; color: #cbd5e1; line-height: 1.55; margin-top: 0.5rem;">
            <p><strong>Limites Apontados pelos Autores:</strong> O modelo foi derivado teoricamente a partir de 10 estudos qualitativos de RSL, carecendo de validação empírica quantitativa com orquestradores em exercício.</p>
            <p style="margin-top: 0.6rem;"><strong>Agenda Proposta:</strong> Realização de entrevistas empíricas com orquestradores reais de parques e o desenvolvimento de <em>artefatos de formação executiva</em> para treinar futuros orquestradores.</p>
          </div>
        </div>
      </div>
    </section>
"""

jessica_notes = {
    12: "TEMPO: cerca de 1 minuto.\n1) Ler a questão do bloco em voz alta: Como coordenar atores independentes e quais mecanismos e competências permitem a orquestração do ecossistema?\n2) Apresentar o percurso em três camadas: QUEM orquestra (o papel do orquestrador), COMO se orquestra (os mecanismos) e COM O QUÊ (as competências de orquestração).\n3) Situar o artigo: Machado, Faccin e Bittencourt (2025) realizaram uma revisão sistemática da literatura (RSL), seguindo Tranfield et al. (2003), nas bases Scopus e Web of Science, de 2006 a 2024, tendo Dhanaraj e Parkhe (2006) como marco teórico. Foram 670 artigos encontrados, 120 após duplicados e 10 estudos incluídos.\n4) Destacar a escolha conceitual dos autores: capacidade, competência e habilidade referem-se ao indivíduo; capability, à organização.",
    13: "TEMPO: cerca de 1 minuto e 30 segundos.\n1) O PROBLEMA: ecossistemas de inovação são comunidades de participantes heterogêneos e interdependentes, mas hierarquicamente independentes. Eles dependem uns dos outros, mas ninguém responde a ninguém.\n2) A RESPOSTA: a orquestração. Para Dhanaraj e Parkhe (2006), orquestrar é um conjunto de atividades para desenvolver, gerenciar e coordenar a rede, criando e extraindo valor sem o benefício da autoridade hierárquica.\n3) O ORQUESTRADOR: é quem conduz essas atividades. O artigo consolida 13 papéis, como arquiteto, gatekeeper, juiz, coordenador, líder e comunicador. Um mesmo orquestrador pode assumir vários papéis, que mudam ao longo do tempo (Nilsen e Gausdal, 2017).",
    14: "TEMPO: cerca de 1 minuto.\nO artigo organiza a orquestração em dimensões que foram se acumulando na literatura:\n- 2006 (Dhanaraj e Parkhe): 3 dimensões seminais (mobilidade do conhecimento, apropriabilidade da inovação e estabilidade da rede);\n- 2011 (Hurmelinna-Laukkanen et al.): amplia para 6 dimensões (+ agenda, mobilização e coordenação);\n- 2019 (Da Silva e Bitencourt): acrescenta cocriação;\n- 2021 (Mignoni et al.): acrescenta gestão da comunicação, totalizando 8 dimensões.\nNeste bloco vamos aprofundar 6 delas em foco; apropriabilidade e cocriação completam o quadro conceitual.",
    15: "TEMPO: cerca de 2 minutos.\nOs três primeiros mecanismos respondem a como juntar atores que não respondem uns aos outros:\n1) DEFINIÇÃO DE AGENDA: criar e comunicar uma agenda que direcione os membros. Na prática, o arquiteto identifica oportunidades e define metas, e o leiloeiro propõe uma agenda que introduz a visão conjunta.\n2) MOBILIZAÇÃO: atrair e selecionar parceiros para o ecossistema. O arquiteto seleciona membros; o leiloeiro cria e promove a visão conjunta.\n3) ESTABILIZAÇÃO DA REDE: manter a colaboração entre os membros por cultura, valores e laços fortes, evitando individualismo e oportunismo. O coordenador administra interações; o líder motiva a colaboração com visão de longo prazo.",
    16: "TEMPO: cerca de 2 minutos.\nOs outros três mecanismos fazem o ecossistema funcionar no dia a dia:\n4) COMPARTILHAMENTO DE CONHECIMENTO: compartilhar, adquirir e implementar conhecimento. O gatekeeper extrai conhecimento de fora e dissemina; o representante compartilha e filtra para fora; o regente adquire e transforma informação para fortalecer competências.\n5) COORDENAÇÃO: planejar e monitorar a execução. O regente aloca tarefas, o juiz monitora e ajusta padrões de desempenho e o líder esclarece os papéis.\n6) COMUNICAÇÃO: conduzir a comunicação externa, divulgar projetos institucionais e engajar o público; papel do comunicador.",
    17: "TEMPO: cerca de 1 minuto e 45 segundos.\nEsta é a contribuição central do artigo.\n1) A LACUNA: a literatura avançou das dimensões da orquestração para os papéis do orquestrador. O próximo passo é entender a competência do indivíduo que orquestra.\n2) A BASE TEÓRICA: em Ruas (2005), capacidade é potencial; vira competência quando mobilizada na ação. Le Boterf (2003) organiza em saber (conhecimentos), saber fazer (habilidades) e saber ser (atitudes). Antonello (2011) completa: competência é ação situada em contexto.\n3) A DEFINIÇÃO: combinação de CHA mobilizada pelo orquestrador para permitir interação colaborativa, interdependente e cocriativa.\n4) O MODELO: 33 atributos de competência (confiança, alinhamento de interesses, visão sistêmica).",
    18: "TEMPO: cerca de 45 segundos.\n1) RESPOSTA À QUESTÃO DO BLOCO: atores independentes se coordenam por meio de um orquestrador que atua por influência e alinhamento, sem hierarquia; os mecanismos são as 6 dimensões operadas por diferentes papéis; e o que viabiliza tudo isso é a competência de orquestração (CHA em ação).\n2) LIMITES: 10 estudos incluídos na revisão sistemática, modelo puramente teórico ainda sem validação com orquestradores reais em exercício.\n3) AGENDA PROPOSTA: entrevistas com orquestradores reais e desenvolvimento de um artefato de formação executiva.\n4) FECHAMENTO: Ecossistema não se comanda, se orquestra!"
}

def update_file(filepath):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Localizar o bloco atual de slides 12, 13 e 14
    # Do início de <!-- SLIDE 12: até antes de <!-- SLIDE 15:
    pattern = r'(<!-- SLIDE 12:.*?)<!-- SLIDE 15:'
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        print(f"Pattern for Slide 12-14 not found in {filepath}")
        return

    # Substitui os slides 12, 13, 14 pelos 7 slides de Jéssica
    new_content = content[:match.start()] + jessica_slides_html.strip() + "\n\n    <!-- SLIDE 19:" + content[match.end():]

    # Agora precisamos renumerar os slides subsequentes que eram de 15 a 35 (agora 19 a 39)
    # A diferença é +4
    def renumber_slides(text):
        # Primeiro, ajustar os comentários <!-- SLIDE X:
        def repl_comment(m):
            num = int(m.group(1))
            if num >= 15:
                return f"<!-- SLIDE {num + 4}:"
            return m.group(0)
        text = re.sub(r'<!-- SLIDE (\d+):', repl_comment, text)

        # Ajustar data-slide="X"
        def repl_data_slide(m):
            num = int(m.group(1))
            if num >= 15:
                return f'data-slide="{num + 4}"'
            return m.group(0)
        text = re.sub(r'data-slide="(\d+)"', repl_data_slide, text)

        # Ajustar FASE 3 slide header
        text = text.replace('Desafio da Fase 3: <span>Centro de Governança do PIT</span>',
                            'Desafio da Fase 3: <span>Centro de Governança do PIT</span>')
        return text

    # Aplicar renumeração a partir de onde os slides subsequentes começam
    split_pt = new_content.find('<!-- SLIDE 19:')
    if split_pt != -1:
        before_s19 = new_content[:split_pt]
        after_s19 = new_content[split_pt:]
        after_s19 = renumber_slides(after_s19)
        new_content = before_s19 + after_s19

    # Atualizar totalSlides = 35 para 39
    new_content = re.sub(r'const totalSlides = \d+;', 'const totalSlides = 39;', new_content)

    # Atualizar notesMap no script JS
    # Vamos injetar as novas notas de 12 a 18 e remapear as antigas 15..35 para 19..39
    notes_match = re.search(r'const notesMap = \{(.*?)\};', new_content, re.DOTALL)
    if notes_match:
        old_notes_block = notes_match.group(1)
        # Parse old notes
        old_dict = {}
        for nm in re.finditer(r'(\d+):\s*"(.*?)"(?=,\s*\d+:|\s*$)', old_notes_block, re.DOTALL):
            s_num = int(nm.group(1))
            s_txt = nm.group(2)
            old_dict[s_num] = s_txt

        new_dict = {}
        for num in range(1, 12):
            if num in old_dict:
                new_dict[num] = old_dict[num]

        # Inserir as notas da Jéssica 12 a 18
        for num, txt in jessica_notes.items():
            # Escapar aspas e quebras de linha para JS string
            escaped = txt.replace('"', '\\"').replace('\n', '\\n')
            new_dict[num] = escaped

        # Remapear 15 a 35 para 19 a 39
        for num in range(15, 36):
            if num in old_dict:
                new_dict[num + 4] = old_dict[num]

        # Reconstruir notesMap string
        notes_lines = ["\n    const notesMap = {"]
        for num in sorted(new_dict.keys()):
            notes_lines.append(f'      {num}: "{new_dict[num]}",')
        notes_lines.append("    };\n")
        new_notes_block = "\n".join(notes_lines)

        new_content = new_content[:notes_match.start()] + new_notes_block.strip() + new_content[notes_match.end():]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Successfully updated: {filepath}")

# Atualizar todos os arquivos relevantes
base_path = r"c:\Users\jj\OneDrive\Estudos\Edital unifesp PIT 2026\Disciplinas 02 2026\Gestão estratégica da inovação"
files = [
    os.path.join(base_path, "02 - Seminário 5 - Ecossistemas de Inovação", "Apresentação e Quiz Interativo", "index.html"),
    os.path.join(base_path, "02 - Seminário 5 - Ecossistemas de Inovação", "Apresentação e Quiz Interativo", "apresentacao_seminario_ecossistema_pit.html"),
    os.path.join(base_path, "Seminário", "index.html"),
    os.path.join(base_path, "Seminário", "apresentacao_seminario_ecossistema_pit.html")
]

for f in files:
    update_file(f)
