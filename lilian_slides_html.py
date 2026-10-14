# -*- coding: utf-8 -*-
"""
Helper that returns the HTML markup for Lilian's 9 slides (Slides 24 to 32)
maintaining 100% fidelity to her PPTX content and presentation visual identity.
"""

def get_lilian_slides_html():
    return """
    <!-- ======================================================================= -->
    <!-- BLOCO 5: CASO SAN DIEGO & SÃO JOSÉ DOS CAMPOS (LILIAN VEIGA VINHAS)     -->
    <!-- 9 SLIDES COMPLETOS E LITERAIS BASEADOS NO PPTX DA LILIAN                -->
    <!-- ======================================================================= -->

    <!-- SLIDE 24: BLOCO 5 (1/9) - SAN DIEGO NO RADAR GLOBAL (WIPO GII 2025) -->
    <section class="slide" data-slide="24" data-block="Bloco 5" data-speaker="Lilian Veiga Vinhas (4ª)" data-time="1.5 min">
      <div class="slide-tag">🌍 BLOCO 5 • BENCHMARKING INTERNACIONAL (1/9)</div>
      <h2 class="slide-title">San Diego no Radar Global: <span>14º Maior Polo de Inovação do Mundo</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">🏆</span>
        <div class="punchline-quote">"San Diego é o 14º maior polo mundial de inovação (7º por intensidade populacional): 26.713 pedidos de patente PCT liderados pela Qualcomm e 19.862 artigos pela UCSD."</div>
      </div>

      <div class="grid-2" style="grid-template-columns: 1.15fr 1fr; gap: 1.25rem; align-items: stretch;">
        <!-- Coluna Esquerda: MAPA GLOBAL WIPO -->
        <div class="card card-glow-cyan" style="display: flex; flex-direction: column; justify-content: space-between;">
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.5rem;">
            <div class="card-title" style="margin-bottom: 0;"><span>🗺️</span> Mapeamento Global de Clusters (WIPO)</div>
            <span class="chip-badge" style="background: rgba(63, 208, 230, 0.15); color: var(--cyan-light);">PCT 2020-2024</span>
          </div>
          <div style="background: rgba(5, 10, 20, 0.85); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 0.4rem; text-align: center;">
            <img src="assets/lilian/slide_1_img_2.png" alt="Mapa Mundial de Clusters de Inovação WIPO" style="width: 100%; max-height: 220px; object-fit: contain; border-radius: 6px;">
          </div>
          <div style="font-size: 0.78rem; color: var(--text-muted); line-height: 1.4; margin-top: 0.5rem;">
            📍 <em>WIPO / ONU:</em> Os pontos destacam densidade inventiva. <strong>Nota:</strong> No Brasil, apenas São Paulo figura entre os 100 maiores clusters de inovação do mundo.
          </div>
        </div>

        <!-- Coluna Direita: DADOS SAN DIEGO GII 2025 -->
        <div class="card card-glow-emerald" style="display: flex; flex-direction: column; justify-content: space-between;">
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.5rem;">
            <div class="card-title" style="margin-bottom: 0;"><span>📊</span> Global Innovation Index 2025</div>
            <span class="chip-badge" style="background: rgba(16, 185, 129, 0.15); color: var(--emerald-accent);">Rank 14 Global</span>
          </div>
          <div style="background: rgba(5, 10, 20, 0.85); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 0.4rem; text-align: center;">
            <img src="assets/lilian/slide_1_img_4.png" alt="Dados San Diego WIPO GII 2025" style="width: 100%; max-height: 190px; object-fit: contain; border-radius: 6px;">
          </div>
          <div class="grid-2" style="gap: 0.5rem; margin-top: 0.5rem;">
            <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.06); border-radius: 6px; padding: 0.4rem 0.6rem;">
              <div style="font-size: 0.7rem; color: var(--text-dim); text-transform: uppercase;">Líder em Patentes</div>
              <div style="font-size: 0.85rem; font-weight: 700; color: #fff;">Qualcomm (17.205 • 64%)</div>
              <div style="font-size: 0.72rem; color: var(--cyan-light);">Illumina (442) • UC (436)</div>
            </div>
            <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.06); border-radius: 6px; padding: 0.4rem 0.6rem;">
              <div style="font-size: 0.7rem; color: var(--text-dim); text-transform: uppercase;">Líder Científico</div>
              <div style="font-size: 0.85rem; font-weight: 700; color: #fff;">UCSD (11.696 art. • 59%)</div>
              <div style="font-size: 0.72rem; color: var(--emerald-accent);">SDSU (1.320) • Scripps (1.041)</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 25: BLOCO 5 (2/9) - CONCEITO & OS 6 PONTOS-CHAVE DE SAN DIEGO -->
    <section class="slide" data-slide="25" data-block="Bloco 5" data-speaker="Lilian Veiga Vinhas (4ª)" data-time="1.75 min">
      <div class="slide-tag">🧬 BLOCO 5 • CONCEITO & GÊNESE (2/9)</div>
      <h2 class="slide-title">O que é um Ecossistema? <span>Os 6 Pontos-Chave de San Diego</span></h2>

      <div class="punchline-card" style="border-left: 3px solid var(--cyan-light);">
        <span style="font-size: 1.4rem;">📖</span>
        <div class="punchline-quote">
          "É conjunto dinâmico e em evolução de atores, instituições, atividades e relações complementares que impulsionam o desempenho inovador."
          <div style="font-size: 0.8rem; font-weight: 400; color: var(--text-muted); margin-top: 0.2rem;">
            — <strong>Jukka Majava & Satu Rinkinen (2024/2026)</strong> • <em>Twenty years, twenty studies: what can we learn from San Diego’s innovation ecosystem?</em> (Tech. Analysis & Strategic Management, 38:1)
          </div>
        </div>
      </div>

      <!-- Grid dos 6 Pontos Oficiais do PPTX -->
      <div class="grid-3" style="gap: 0.85rem; margin-top: 0.5rem;">
        <div class="card card-glow-cyan" style="padding: 0.9rem;">
          <div style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--cyan-light); font-weight: 700;">1º PONTO</div>
          <div style="font-size: 0.95rem; font-weight: 800; color: #fff; margin: 0.2rem 0;">Universidade com Pesquisa de Ponta</div>
          <p style="font-size: 0.8rem; color: var(--text-muted); line-height: 1.4; margin: 0;">Fundação da UCSD (anos 60) recrutando cientistas de elite em biologia/ciências e atraindo empresas globais e VCs.</p>
        </div>

        <div class="card card-glow-purple" style="padding: 0.9rem;">
          <div style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--purple-accent); font-weight: 700;">2º PONTO</div>
          <div style="font-size: 0.95rem; font-weight: 800; color: #fff; margin: 0.2rem 0;">Antecedentes Históricos & Vocação</div>
          <p style="font-size: 0.8rem; color: var(--text-muted); line-height: 1.4; margin: 0;">Investimento prévio em hospitais e clínicas; isolamento geográfico que impediu indústrias pesadas poluentes.</p>
        </div>

        <div class="card card-glow-emerald" style="padding: 0.9rem;">
          <div style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--emerald-accent); font-weight: 700;">3º PONTO</div>
          <div style="font-size: 0.95rem; font-weight: 800; color: #fff; margin: 0.2rem 0;">Decisões Políticas para Favorecer</div>
          <p style="font-size: 0.8rem; color: var(--text-muted); line-height: 1.4; margin: 0;">Zoneamento urbano na década de 70 garantindo contiguidade física entre UCSD, institutos de pesquisa e empresas.</p>
        </div>

        <div class="card card-glow-amber" style="padding: 0.9rem;">
          <div style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--amber-accent); font-weight: 700;">4º PONTO</div>
          <div style="font-size: 0.95rem; font-weight: 800; color: #fff; margin: 0.2rem 0;">Contingências que Geram Ações</div>
          <p style="font-size: 0.8rem; color: var(--text-muted); line-height: 1.4; margin: 0;">Redução de gastos militares na década de 80 elevou o desemprego, forçando a cidade a se reinventar em biotec e telecom.</p>
        </div>

        <div class="card card-glow-cyan" style="padding: 0.9rem;">
          <div style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--cyan-light); font-weight: 700;">5º PONTO</div>
          <div style="font-size: 0.95rem; font-weight: 800; color: #fff; margin: 0.2rem 0;">Instituição Mediadora (Orquestrador)</div>
          <p style="font-size: 0.8rem; color: var(--text-muted); line-height: 1.4; margin: 0;">Criação da CONNECT (1985) na UCSD: aceleradora pioneira de treinamento, mentoria e construção de confiança mútua.</p>
        </div>

        <div class="card card-glow-emerald" style="padding: 0.9rem;">
          <div style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--emerald-accent); font-weight: 700;">6º PONTO</div>
          <div style="font-size: 0.95rem; font-weight: 800; color: #fff; margin: 0.2rem 0;">Proximidade Geográfica dos Atores</div>
          <p style="font-size: 0.8rem; color: var(--text-muted); line-height: 1.4; margin: 0;">Distâncias curtas que facilitaram encontros de corredor, compartilhamento de conhecimento tácito e laços relacionais.</p>
        </div>
      </div>
    </section>

    <!-- SLIDE 26: BLOCO 5 (3/9) - CONNECT: A ENGENHARIA DA CONFIANÇA -->
    <section class="slide" data-slide="26" data-block="Bloco 5" data-speaker="Lilian Veiga Vinhas (4ª)" data-time="1.75 min">
      <div class="slide-tag">🌉 BLOCO 5 • O ORQUESTRADOR REGIONAL (3/9)</div>
      <h2 class="slide-title">CONNECT: A Engenharia da Confiança <span>A Ponte entre Ciência e Capital</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">🤝</span>
        <div class="punchline-quote">"Criada de baixo para cima (Bottom-Up) na UCSD em resposta à crise militar, a CONNECT reduziu a assimetria entre as 'ideias' dos cientistas e as 'regras' dos negócios."</div>
      </div>

      <!-- Infográfico Oficial CONNECT -->
      <div class="card" style="background: rgba(10, 19, 36, 0.9); border: 1px solid rgba(63, 208, 230, 0.3); padding: 0.8rem; margin-bottom: 0.85rem; text-align: center;">
        <img src="assets/lilian/slide_3_img_1.png" alt="CONNECT: A Engenharia da Confiança - Diagrama Oficial" style="width: 100%; max-height: 230px; object-fit: contain; border-radius: 8px;">
      </div>

      <!-- 3 Pilares Estruturados do PPTX -->
      <div class="grid-3" style="gap: 0.85rem;">
        <div class="card card-glow-cyan" style="padding: 0.9rem;">
          <div class="card-title" style="font-size: 0.92rem; margin-bottom: 0.3rem;"><span>🌱</span> Movimento Bottom-Up</div>
          <p style="font-size: 0.8rem; color: var(--text-muted); line-height: 1.4; margin: 0;">Lideranças empresariais privadas e a universidade UCSD fundaram a ONG em 1985 para mitigar o desemprego do setor bélico.</p>
        </div>
        <div class="card card-glow-emerald" style="padding: 0.9rem;">
          <div class="card-title" style="font-size: 0.92rem; margin-bottom: 0.3rem;"><span>🚀</span> Programa Springboard</div>
          <p style="font-size: 0.8rem; color: var(--text-muted); line-height: 1.4; margin: 0;">Aceleradora pioneira com sabatinas de cientistas por investidores, CEOs experientes e especialistas em patentes e mercado.</p>
        </div>
        <div class="card card-glow-purple" style="padding: 0.9rem;">
          <div class="card-title" style="font-size: 0.92rem; margin-bottom: 0.3rem;"><span>🔗</span> Redução de Assimetrias</div>
          <p style="font-size: 0.8rem; color: var(--text-muted); line-height: 1.4; margin: 0;">Traduziu a ciência básica em propostas de valor investíveis, fundando uma cultura de mentoria gratuita e desinteressada ('give-first').</p>
        </div>
      </div>
    </section>

    <!-- SLIDE 27: BLOCO 5 (4/9) - ANÁLISE PEST: O RADAR DE SUCESSO -->
    <section class="slide" data-slide="27" data-block="Bloco 5" data-speaker="Lilian Veiga Vinhas (4ª)" data-time="1.75 min">
      <div class="slide-tag">🎯 BLOCO 5 • DIAGNÓSTICO METODOLÓGICO (4/9)</div>
      <h2 class="slide-title">Análise PEST: O Radar de Sucesso <span>As Forças que Impulsionaram San Diego</span></h2>

      <div class="grid-2" style="grid-template-columns: 1.05fr 1.15fr; gap: 1.25rem; align-items: stretch;">
        <!-- Coluna Esquerda: IMAGEM OFICIAL RADAR PEST -->
        <div class="card card-glow-amber" style="display: flex; flex-direction: column; justify-content: space-between;">
          <div class="card-title" style="margin-bottom: 0.4rem;"><span>🧭</span> Radar PEST de San Diego</div>
          <div style="background: rgba(5, 10, 20, 0.9); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 0.4rem; text-align: center;">
            <img src="assets/lilian/slide_4_img_1.png" alt="Análise PEST: Radar de Sucesso de San Diego" style="width: 100%; max-height: 240px; object-fit: contain; border-radius: 6px;">
          </div>
          <div style="font-size: 0.8rem; color: var(--amber-accent); font-weight: 700; line-height: 1.4; margin-top: 0.5rem; text-align: center;">
            "A concentração simultânea de ideias (ciência básica) e capital viabilizou o milagre da Biotecnologia."
          </div>
        </div>

        <!-- Coluna Direita: 4 QUADRANTES PEST DETALHADOS -->
        <div style="display: flex; flex-direction: column; gap: 0.65rem;">
          <div class="card card-glow-cyan" style="padding: 0.75rem 0.9rem;">
            <div style="display: flex; align-items: center; justify-content: space-between;">
              <span style="font-weight: 800; color: #fff; font-size: 0.9rem;">🏛️ Político (P)</span>
              <span class="chip-badge" style="font-size: 0.68rem;">Zoneamento & SBIR</span>
            </div>
            <p style="font-size: 0.78rem; color: var(--text-muted); margin: 0.2rem 0 0 0; line-height: 1.35;">Zoneamento urbano favorável; fomento federal contínuo a pequenas empresas inovadoras (SBIR/STTR e fundos NIH).</p>
          </div>

          <div class="card card-glow-emerald" style="padding: 0.75rem 0.9rem;">
            <div style="display: flex; align-items: center; justify-content: space-between;">
              <span style="font-weight: 800; color: #fff; font-size: 0.9rem;">💰 Econômico (E)</span>
              <span class="chip-badge" style="font-size: 0.68rem;">Venture Capital & IPOs</span>
            </div>
            <p style="font-size: 0.78rem; color: var(--text-muted); margin: 0.2rem 0 0 0; line-height: 1.35;">Ampla oferta de Venture Capital; aquisições por farmacêuticas globais e aberturas de capital (IPOs) reciclando liquidez.</p>
          </div>

          <div class="card card-glow-purple" style="padding: 0.75rem 0.9rem;">
            <div style="display: flex; align-items: center; justify-content: space-between;">
              <span style="font-weight: 800; color: #fff; font-size: 0.9rem;">🤝 Social / Cultural (S)</span>
              <span class="chip-badge" style="font-size: 0.68rem;">Cultura de Risco & Mobilidade</span>
            </div>
            <p style="font-size: 0.78rem; color: var(--text-muted); margin: 0.2rem 0 0 0; line-height: 1.35;">Cultura sem estigma ao erro; intensa mobilidade interempresarial de executivos conectando laboratórios e mercado.</p>
          </div>

          <div class="card card-glow-cyan" style="padding: 0.75rem 0.9rem;">
            <div style="display: flex; align-items: center; justify-content: space-between;">
              <span style="font-weight: 800; color: #fff; font-size: 0.9rem;">🔬 Tecnológico (T)</span>
              <span class="chip-badge" style="font-size: 0.68rem;">UCSD & Spin-offs Pioneiras</span>
            </div>
            <p style="font-size: 0.78rem; color: var(--text-muted); margin: 0.2rem 0 0 0; line-height: 1.35;">Excelência acadêmica da UCSD/Scripps; efeito genealógico de startups âncoras (Hybritech gerando dezenas de biotechs).</p>
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 28: BLOCO 5 (5/9) - SÃO JOSÉ DOS CAMPOS: A GÊNESE DE UMA VOCAÇÃO -->
    <section class="slide" data-slide="28" data-block="Bloco 5" data-speaker="Lilian Veiga Vinhas (4ª)" data-time="1.75 min">
      <div class="slide-tag">🇧🇷 BLOCO 5 • SÃO JOSÉ DOS CAMPOS: RAÍZES HISTÓRICAS (5/9)</div>
      <h2 class="slide-title">São José dos Campos: A Gênese de uma Vocação <span>Planejamento de Estado & Instituições-Âncora</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">✈️</span>
        <div class="punchline-quote">"Na ausência de capital de risco privado no Brasil dos anos 50/60, o poder de compra estatal do Ministério da Aeronáutica atuou como indutor, viabilizando a Embraer e fornecedores locais."</div>
      </div>

      <div class="grid-2" style="grid-template-columns: 1.15fr 1fr; gap: 1.25rem; align-items: stretch;">
        <!-- Coluna Esquerda: IMAGEM OFICIAL GÊNESE SJC -->
        <div class="card card-glow-cyan" style="display: flex; flex-direction: column; justify-content: space-between;">
          <div class="card-title" style="margin-bottom: 0.4rem;"><span>🗺️</span> Vocação Territorial & Adensamento</div>
          <div style="background: rgba(5, 10, 20, 0.9); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 0.4rem; text-align: center;">
            <img src="assets/lilian/slide_5_img_1.png" alt="São José dos Campos: A Gênese de uma Vocação" style="width: 100%; max-height: 235px; object-fit: contain; border-radius: 6px;">
          </div>
          <div style="font-size: 0.76rem; color: var(--text-muted); line-height: 1.4; margin-top: 0.4rem;">
            🎯 <em>Convergência Territorial:</em> O Eixo Rio-SP (Via Dutra) associado a recursos hídricos e relevo plano canalizou investimentos industriais e de defesa.
          </div>
        </div>

        <!-- Coluna Direita: FATORES ESTRUTURANTES -->
        <div style="display: flex; flex-direction: column; gap: 0.7rem;">
          <div class="card card-glow-emerald" style="padding: 0.9rem;">
            <div class="card-title" style="font-size: 0.95rem; margin-bottom: 0.3rem;"><span>📍</span> Fatores Atrativos Originais (Anos 50)</div>
            <ul class="bullet-list">
              <li><span class="bullet-dot">▸</span> Localização entre as duas maiores metrópoles do país (Rio-São Paulo).</li>
              <li><span class="bullet-dot">▸</span> Abundância de energia elétrica, lençol freático rico e topografia favorável.</li>
              <li><span class="bullet-dot">▸</span> Atração precoce de multinacionais de base tecnológica ao longo da Via Dutra.</li>
            </ul>
          </div>

          <div class="card card-glow-purple" style="padding: 0.9rem;">
            <div class="card-title" style="font-size: 0.95rem; margin-bottom: 0.3rem;"><span>🏛️</span> Planejamento de Estado & Instituições-Âncora</div>
            <ul class="bullet-list">
              <li><span class="bullet-dot">▸</span> <strong>CTA e ITA (anos 50):</strong> Institutos estruturados com base no modelo do MIT norte-americano para forjar excelência em engenharia aeronáutica.</li>
              <li><span class="bullet-dot">▸</span> <strong>INPE (1961):</strong> Polo de pesquisa aeroespacial e ciências espaciais.</li>
              <li><span class="bullet-dot">▸</span> <strong>Gênese de Spin-offs:</strong> Pesquisadores fundadores da quase totalidade das empresas de base tecnológica da região.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 29: BLOCO 5 (6/9) - EVOLUÇÃO TIPOLÓGICA: DE ORGÂNICO À ORQUESTRAÇÃO -->
    <section class="slide" data-slide="29" data-block="Bloco 5" data-speaker="Lilian Veiga Vinhas (4ª)" data-time="1.75 min">
      <div class="slide-tag">🔄 BLOCO 5 • EVOLUÇÃO ESTRUTURAL (6/9)</div>
      <h2 class="slide-title">A Evolução Tipológica: De Orgânico à Orquestração <span>Da Proximidade Física à Gestão Formal do PIT</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">🏛️</span>
        <div class="punchline-quote">"Da dificuldade histórica de acesso da indústria aos laboratórios de P&D para a gestão orquestrada de inovação de 25 milhões de m²."</div>
      </div>

      <!-- Infográfico Oficial Evolução Tipológica -->
      <div class="card" style="background: rgba(10, 19, 36, 0.9); border: 1px solid rgba(63, 208, 230, 0.3); padding: 0.8rem; margin-bottom: 0.85rem; text-align: center;">
        <img src="assets/lilian/slide_6_img_1.png" alt="A Evolução Tipológica: De Orgânico à Orquestração" style="width: 100%; max-height: 230px; object-fit: contain; border-radius: 8px;">
      </div>

      <!-- Comparativo Tipo 1 vs Tipo 3 -->
      <div class="grid-2" style="gap: 1rem;">
        <div class="card card-glow-amber" style="padding: 0.9rem;">
          <div class="card-title" style="font-size: 0.95rem; margin-bottom: 0.3rem;"><span>⏳</span> Polo Tipo 1 · Anos 90 (Polo Orgânico)</div>
          <p style="font-size: 0.8rem; color: var(--text-muted); line-height: 1.4; margin-bottom: 0.4rem;">Proximidade física natural entre CTA, INPE, Embraer e Avibras, mas sem estrutura formal de orquestração.</p>
          <div style="background: rgba(245, 158, 11, 0.1); border-left: 2px solid var(--amber-accent); padding: 0.4rem 0.6rem; font-size: 0.74rem; color: #fde68a;">
            <strong>Gargalos:</strong> Barreiras de acesso a laboratórios, assimetria de informações e carência de gestão em contratos e PI.
          </div>
        </div>

        <div class="card card-glow-emerald" style="padding: 0.9rem;">
          <div class="card-title" style="font-size: 0.95rem; margin-bottom: 0.3rem;"><span>🎯</span> Polo Tipo 3 · 2009 em Diante (Polo Orquestrado)</div>
          <p style="font-size: 0.8rem; color: var(--text-muted); line-height: 1.4; margin-bottom: 0.4rem;">Criação do Parque Tecnológico com estrutura formal de governança gerida por Organização Social (APTSJC).</p>
          <div style="background: rgba(16, 185, 129, 0.1); border-left: 2px solid var(--emerald-accent); padding: 0.4rem 0.6rem; font-size: 0.74rem; color: #a7f3d0;">
            <strong>Solução:</strong> Acesso compartilhado a 57 laboratórios parceiros, APLs consolidados e incubação de base tecnológica (Nexus).
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 30: BLOCO 5 (7/9) - O PIT SJC: GOVERNANÇA E TERRITÓRIO -->
    <section class="slide" data-slide="30" data-block="Bloco 5" data-speaker="Lilian Veiga Vinhas (4ª)" data-time="1.75 min">
      <div class="slide-tag">🏛️ BLOCO 5 • ANATOMIA DO PIT SJC (7/9)</div>
      <h2 class="slide-title">O PIT SJC: Governança e Território <span>Relatório Anual 2025 & Políticas de Inovação</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">🌐</span>
        <div class="punchline-quote">"Spill-overs territoriais: em áreas de grande aglomeração, a proximidade física catalisa o transbordamento espontâneo de conhecimento tácito e sinergia." — <strong>Thiago Chiquetto Rubem (2018)</strong></div>
      </div>

      <div class="grid-2" style="grid-template-columns: 1.05fr 1.15fr; gap: 1.25rem; align-items: stretch;">
        <!-- Coluna Esquerda: DIAGRAMA PENTAGONAL DO PIT -->
        <div class="card card-glow-emerald" style="display: flex; flex-direction: column; justify-content: space-between;">
          <div class="card-title" style="margin-bottom: 0.4rem;"><span>🌀</span> Matriz Pentagonal do PIT (Relatório 2025)</div>
          <div style="background: rgba(5, 10, 20, 0.9); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 0.4rem; text-align: center;">
            <img src="assets/lilian/slide_7_img_2.png" alt="Diagrama Pentagonal do Relatório Anual PIT 2025" style="width: 100%; max-height: 235px; object-fit: contain; border-radius: 6px;">
          </div>
          <div style="font-size: 0.76rem; color: var(--text-muted); line-height: 1.4; margin-top: 0.4rem;">
            📌 <em>Núcleo APTSJC:</em> Tríplice Hélice (Academia, Governo, Empresas) articulando as 5 cadeias setoriais fundamentais.
          </div>
        </div>

        <!-- Coluna Direita: MECANISMOS DE OPERAÇÃO -->
        <div style="display: flex; flex-direction: column; gap: 0.65rem;">
          <div class="card card-glow-cyan" style="padding: 0.85rem;">
            <div class="card-title" style="font-size: 0.92rem; margin-bottom: 0.25rem;"><span>🏢</span> Modelo de Gestão por Organização Social (OS)</div>
            <p style="font-size: 0.79rem; color: var(--text-muted); line-height: 1.35; margin: 0;">Fundado em 2009 pela Prefeitura de SJC; gerido pela Associação Parque Tecnológico (OS privada sem fins lucrativos credenciada no SPTec/SPAI).</p>
          </div>

          <div class="card card-glow-purple" style="padding: 0.85rem;">
            <div class="card-title" style="font-size: 0.92rem; margin-bottom: 0.25rem;"><span>🧪</span> Superação do Gargalo de P&D: Rede de Laboratórios</div>
            <p style="font-size: 0.79rem; color: var(--text-muted); line-height: 1.35; margin: 0;">56 projetos prospectados e 22 executados em 2025; acesso ampliado a uma rede integrada de <strong>57 laboratórios parceiros</strong> multiusuários.</p>
          </div>

          <div class="card card-glow-emerald" style="padding: 0.85rem;">
            <div class="card-title" style="font-size: 0.92rem; margin-bottom: 0.25rem;"><span>🎯</span> O Papel Integrador do Orquestrador</div>
            <p style="font-size: 0.79rem; color: var(--text-muted); line-height: 1.35; margin: 0;">Conexão contínua: empresas apresentam demandas e o PIT conecta pesquisadores, startups, investidores e infraestrutura tecnológica.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 31: BLOCO 5 (8/9) - O PIT SJC EM 2026: CONSOLIDAÇÃO & REDES DE CONFIANÇA -->
    <section class="slide" data-slide="31" data-block="Bloco 5" data-speaker="Lilian Veiga Vinhas (4ª)" data-time="1.75 min">
      <div class="slide-tag">🤝 BLOCO 5 • CONEXÕES & MERCADO (8/9)</div>
      <h2 class="slide-title">O PIT SJC em 2026: Consolidação & Parcerias <span>Construção de Redes de Confiança e Diversificação</span></h2>

      <div class="punchline-card">
        <span style="font-size: 1.4rem;">✨</span>
        <div class="punchline-quote">"Parque Tecnológico não é mero empreendimento imobiliário: é um ambiente catalisador de confiança, pontes relacionais e encontros humanos." — <strong>Jeferson Cheriegate (Gazeta de SP, 2026)</strong></div>
      </div>

      <div class="grid-2" style="grid-template-columns: 1.15fr 1fr; gap: 1.25rem; align-items: stretch;">
        <!-- Coluna Esquerda: LOGOS PARCEIROS PIT -->
        <div class="card card-glow-cyan" style="display: flex; flex-direction: column; justify-content: space-between;">
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.4rem;">
            <div class="card-title" style="margin-bottom: 0;"><span>🤝</span> Quem Confiou em Nosso Trabalho</div>
            <span class="chip-badge" style="background: rgba(63, 208, 230, 0.15); color: var(--cyan-light);">Parceiros & Municípios</span>
          </div>
          <div style="background: rgba(255, 255, 255, 0.95); border: 1px solid rgba(255,255,255,0.2); border-radius: 8px; padding: 0.6rem; text-align: center;">
            <img src="assets/lilian/slide_8_img_3.png" alt="Parceiros e Municípios do PIT SJC" style="width: 100%; max-height: 215px; object-fit: contain;">
          </div>
          <div style="font-size: 0.75rem; color: var(--text-muted); line-height: 1.35; margin-top: 0.4rem;">
            🌐 <em>Grandes Contratantes & Governos:</em> Gerdau, Nestlé, Finep, Sebrae-SP, Thales, Governos de SP, GO, PR e prefeituras em inovação aberta.
          </div>
        </div>

        <!-- Coluna Direita: APLS EM EXPANSÃO -->
        <div style="display: flex; flex-direction: column; gap: 0.6rem;">
          <div class="card card-glow-purple" style="padding: 0.75rem 0.85rem;">
            <div style="font-size: 0.86rem; font-weight: 800; color: #fff;">✈️ Aeroespacial & Defesa (DNA Regional)</div>
            <p style="font-size: 0.76rem; color: var(--text-muted); margin: 0.2rem 0 0 0;">Cluster brasileiro ativo em feiras mundiais (Paris, Dubai, LAAD); conexões com mais de 10 países.</p>
          </div>
          <div class="card card-glow-cyan" style="padding: 0.75rem 0.85rem;">
            <div style="font-size: 0.86rem; font-weight: 800; color: #fff;">💻 TIC Vale (137 Empresas)</div>
            <p style="font-size: 0.76rem; color: var(--text-muted); margin: 0.2rem 0 0 0;">Soluções integradas em Indústria 4.0, Inteligência Artificial, Big Data e Smart Cities.</p>
          </div>
          <div class="card card-glow-emerald" style="padding: 0.75rem 0.85rem;">
            <div style="font-size: 0.86rem; font-weight: 800; color: #fff;">🌾 Agropolo (+21,6%) & Saúde/Mobilidade</div>
            <p style="font-size: 0.76rem; color: var(--text-muted); margin: 0.2rem 0 0 0;">90 empresas no Agropolo com foco em ESG; cadeia de saúde e mobilidade urbana em expansão.</p>
          </div>
          <div class="card card-glow-amber" style="padding: 0.75rem 0.85rem;">
            <div style="font-size: 0.86rem; font-weight: 800; color: #fff;">🚀 Nexus Hub (192 Startups)</div>
            <p style="font-size: 0.76rem; color: var(--text-muted); margin: 0.2rem 0 0 0;">Comunidade ativa com 23 entidades estratégicas e 87 mentores seniores no Nexus Circle.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 32: BLOCO 5 (9/9) - SÍNTESE COMPARATIVA: SAN DIEGO VS SÃO JOSÉ DOS CAMPOS -->
    <section class="slide" data-slide="32" data-block="Bloco 5" data-speaker="Lilian Veiga Vinhas (4ª)" data-time="2 min">
      <div class="slide-tag">⚖️ BLOCO 5 • MATRIZ DE BENCHMARKING (9/9)</div>
      <h2 class="slide-title">Síntese Comparativa: <span>San Diego (EUA) vs São José dos Campos (Brasil)</span></h2>

      <!-- Tabela Oficial Transcrita Literalmente do PPTX de Lilian -->
      <div class="card card-glow-cyan" style="padding: 0.75rem 1rem; margin-bottom: 0.75rem; overflow-x: auto;">
        <table style="width: 100%; border-collapse: collapse; font-size: 0.82rem; text-align: left;">
          <thead>
            <tr style="border-bottom: 2px solid var(--cyan-light); color: var(--cyan-light); font-family: var(--font-display); font-size: 0.88rem; text-transform: uppercase;">
              <th style="padding: 0.45rem 0.6rem; width: 19%;">Dimensão</th>
              <th style="padding: 0.45rem 0.6rem; width: 40.5%;">San Diego (EUA)</th>
              <th style="padding: 0.45rem 0.6rem; width: 40.5%;">São José dos Campos (Brasil)</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
              <td style="padding: 0.45rem 0.6rem; font-weight: 700; color: #fff;">Matriz Científica e Origem</td>
              <td style="padding: 0.45rem 0.6rem; color: var(--text-muted);">Pesquisa em saúde (Scripps, Salk), UCSD e demandas da Marinha/Aeronáutica civil.</td>
              <td style="padding: 0.45rem 0.6rem; color: #cbd5e1;">Planejamento estatal/militar em defesa e aeroespacial (CTA, ITA, INPE).</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.06); background: rgba(255,255,255,0.02);">
              <td style="padding: 0.45rem 0.6rem; font-weight: 700; color: #fff;">Evolução da Governança</td>
              <td style="padding: 0.45rem 0.6rem; color: var(--text-muted);"><strong>Modelo Bottom-Up:</strong> Liderança privada e universidade criaram a ONG CONNECT em 1985.</td>
              <td style="padding: 0.45rem 0.6rem; color: #cbd5e1;"><strong>De Orgânico (Tipo 1) a Orquestrado (Tipo 3):</strong> De polo sem gestão formal (anos 90) ao PIT em 2009 (Organização Social).</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
              <td style="padding: 0.45rem 0.6rem; font-weight: 700; color: #fff;">Papel do Território</td>
              <td style="padding: 0.45rem 0.6rem; color: var(--text-muted);">Zoneamento urbano em 1970 garantiu proximidade física entre universidade, institutos e startups.</td>
              <td style="padding: 0.45rem 0.6rem; color: #cbd5e1;">Aglomeração territorial no PIT gerando sinergia e transbordamento de conhecimento tácito (spill-overs).</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.06); background: rgba(255,255,255,0.02);">
              <td style="padding: 0.45rem 0.6rem; font-weight: 700; color: #fff;">Atores-Âncora e Genealogia</td>
              <td style="padding: 0.45rem 0.6rem; color: var(--text-muted);">Startups pioneiras em ciências (Hybritech em biotec e Linkabit/Qualcomm em sem fio).</td>
              <td style="padding: 0.45rem 0.6rem; color: #cbd5e1;">Embraer, Avibras e vasta rede de fornecedores e spin-offs de pesquisadores do CTA/INPE.</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
              <td style="padding: 0.45rem 0.6rem; font-weight: 700; color: #fff;">Modelo de Financiamento</td>
              <td style="padding: 0.45rem 0.6rem; color: var(--text-muted);">Investimento federal em pesquisa (NIH, SBIR/STTR), Capital de Risco (Venture Capital) e IPOs.</td>
              <td style="padding: 0.45rem 0.6rem; color: #cbd5e1;">Histórico de encomendas estatais de defesa e transição atual para modelo híbrido (investimentos públicos e privados no PIT).</td>
            </tr>
            <tr style="background: rgba(255,255,255,0.02);">
              <td style="padding: 0.45rem 0.6rem; font-weight: 700; color: #fff;">Diversificação Setorial</td>
              <td style="padding: 0.45rem 0.6rem; color: var(--text-muted);">Liderança mundial em Biotecnologia, Ciências da Vida e Telecomunicações Sem Fio.</td>
              <td style="padding: 0.45rem 0.6rem; color: #cbd5e1;">Matriz aeroespacial/defesa expandida para TIC Vale, Agropolo, Saúde, Mobilidade e Smart Cities.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="punchline-card" style="border-left: 3px solid var(--emerald-accent); margin-bottom: 0;">
        <span style="font-size: 1.25rem;">💡</span>
        <div class="punchline-quote" style="font-size: 0.88rem;">
          <strong>Conclusão Estratégica:</strong> Não existem fórmulas prontas, mas sim princípios universais: excelência acadêmica, visão territorial e entidades orquestradoras que geram laços de confiança humana indispensáveis à coinovação.
        </div>
      </div>
    </section>
"""
