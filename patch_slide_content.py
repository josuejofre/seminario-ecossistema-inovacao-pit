# -*- coding: utf-8 -*-
import re

with open('generate_35_slide_deck.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update Slide 1 & 2 speaker tags
code = re.sub(
    r'(<section class="slide" data-slide="1"[^>]*data-speaker=")[^"]*(")',
    r'\g<1>Nathalia (4ª) / Fernando Barreto (5ª)\g<2>',
    code
)
code = re.sub(
    r'(<section class="slide" data-slide="2"[^>]*data-speaker=")[^"]*(")',
    r'\g<1>Nathalia (4ª) / Fernando Barreto (5ª)\g<2>',
    code
)

# 2. Update Slide 31 & 32 speaker tags
code = re.sub(
    r'(<section class="slide" data-slide="31"[^>]*data-speaker=")[^"]*(")',
    r'\g<1>Jéssica David (Atividade Oficial)\g<2>',
    code
)
code = re.sub(
    r'(<section class="slide" data-slide="32"[^>]*data-speaker=")[^"]*(")',
    r'\g<1>Jéssica David (Atividade Oficial)\g<2>',
    code
)

# 3. Enrich Slide 6 cards
slide6_old = '''      <div class="grid-4">
        <div class="card">
          <div class="card-title">Cluster (Porter)</div>
          <p class="card-desc">Concentração geográfica de firmas similares para ganho de escala e redução de custos operacionais.</p>
        </div>
        <div class="card">
          <div class="card-title">Sistema de Inovação</div>
          <p class="card-desc">Foco nas instituições públicas, leis de incentivo, ministérios e agências reguladoras do Estado.</p>
        </div>
        <div class="card">
          <div class="card-title">Ecossistema de Negócios</div>
          <p class="card-desc">Foco na captura de valor presente, canais de distribuição e monetização comercial de produtos.</p>
        </div>
        <div class="card card-glow-cyan">
          <div class="card-title" style="color: var(--cyan-light);">Ecossistema de Inovação</div>
          <p class="card-desc">Foco na <strong>co-criação de novo conhecimento</strong> e geração coletiva de tecnologias inéditas.</p>
        </div>
      </div>'''

slide6_new = '''      <div class="grid-4">
        <div class="card card-glow-cyan">
          <div class="card-title"><span>🏭</span> Cluster (Porter)</div>
          <p class="card-desc">Concentração geográfica de firmas do mesmo setor que buscam ganho de escala produtiva e redução de custos logísticos.</p>
          <ul class="bullet-list" style="margin-top: 0.8rem;">
            <li><span class="bullet-dot">▸</span> <strong>Foco Central:</strong> Eficiência de custos e aglomeração de cadeia tradicional.</li>
            <li><span class="bullet-dot">▸</span> <strong>Limitação:</strong> Não exige interdependência nem co-criação de novidades tecnológicas.</li>
          </ul>
        </div>
        <div class="card card-glow-purple">
          <div class="card-title"><span>🏛️</span> Sistema de Inovação</div>
          <p class="card-desc">Arcabouço institucional formal do Estado: leis de incentivo, ministérios, agências reguladoras e fomento público.</p>
          <ul class="bullet-list" style="margin-top: 0.8rem;">
            <li><span class="bullet-dot">▸</span> <strong>Foco Central:</strong> Políticas públicas de C&T, subsídios e infraestrutura básica regional.</li>
            <li><span class="bullet-dot">▸</span> <strong>Limitação:</strong> Dinâmica predominantemente macro, institucional e regulatória.</li>
          </ul>
        </div>
        <div class="card card-glow-amber">
          <div class="card-title"><span>💼</span> Ecossistema de Negócios</div>
          <p class="card-desc">Rede de parceiros, fornecedores e canais de distribuição voltada à monetização e entrega de valor existente.</p>
          <ul class="bullet-list" style="margin-top: 0.8rem;">
            <li><span class="bullet-dot">▸</span> <strong>Foco Central:</strong> Captura de valor comercial no curto prazo e market share.</li>
            <li><span class="bullet-dot">▸</span> <strong>Limitação:</strong> Não prioriza a pesquisa científica de ponta nem coevolução em incerteza.</li>
          </ul>
        </div>
        <div class="card card-glow-emerald">
          <div class="card-title" style="color: #34d399;"><span>🚀</span> Ecossistema de Inovação</div>
          <p class="card-desc">Comunidade interdependente de atores heterogêneos focada na <strong>co-criação de novo conhecimento</strong>.</p>
          <ul class="bullet-list" style="margin-top: 0.8rem;">
            <li><span class="bullet-dot">▸</span> <strong>Foco Central:</strong> Geração conjunta de soluções inéditas que nenhum ator geraria isolado.</li>
            <li><span class="bullet-dot">▸</span> <strong>Diferencial:</strong> Orquestração relacional, simbiose e coevolução contínua.</li>
          </ul>
        </div>
      </div>'''

code = code.replace(slide6_old, slide6_new)

# 4. Enrich Slide 27 cards
slide27_old = '''      <div class="grid-4">
        <div class="card">
          <div class="card-title">1. Contratos Claros</div>
          <p class="card-desc">Propriedade Intelectual decidida antes de ligar o primeiro computador do laboratório.</p>
        </div>
        <div class="card card-glow-cyan">
          <div class="card-title">2. Confiança Humana</div>
          <p class="card-desc">Café semanal e convivência informal resolvem mais impasses do que notificações judiciais.</p>
        </div>
        <div class="card">
          <div class="card-title">3. Marco de CTI</div>
          <p class="card-desc">Usar com maestria a Lei 13.243/16 para viabilizar compartilhamento de laboratórios federais.</p>
        </div>
        <div class="card card-glow-purple">
          <div class="card-title">4. Formação Mista</div>
          <p class="card-desc">O PIT busca na UNIFESP mestres que saibam equacionar problemas e formular planos de negócios.</p>
        </div>
      </div>'''

slide27_new = '''      <div class="grid-4">
        <div class="card card-glow-cyan">
          <div class="card-title"><span>📝</span> 1. Contratos & PI Antecipados</div>
          <p class="card-desc">Definição explícita de Propriedade Intelectual antes do início dos testes no laboratório.</p>
          <ul class="bullet-list" style="margin-top: 0.6rem;">
            <li><span class="bullet-dot">▸</span> Segurança jurídica para atrair capital de grandes corporações.</li>
            <li><span class="bullet-dot">▸</span> Preservação da autoria científica e patentes dos pesquisadores.</li>
          </ul>
        </div>
        <div class="card card-glow-emerald">
          <div class="card-title"><span>☕</span> 2. Confiança & Capital Relacional</div>
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
            <li><span class="bullet-dot">▸</span> Remuneração de pesquisadores em projetos de inovação aberta.</li>
          </ul>
        </div>
        <div class="card card-glow-purple">
          <div class="card-title"><span>🎓</span> 4. Formação Transdisciplinar</div>
          <p class="card-desc">O ecossistema demanda mestres e doutores com sólida visão acadêmica e mentalidade empreendedora.</p>
          <ul class="bullet-list" style="margin-top: 0.6rem;">
            <li><span class="bullet-dot">▸</span> Alinhamento do PPG-PIT UNIFESP aos desafios reais das deep techs.</li>
            <li><span class="bullet-dot">▸</span> Capacidade de traduzir descobertas científicas em modelos de negócio.</li>
          </ul>
        </div>
      </div>'''

code = code.replace(slide27_old, slide27_new)

with open('generate_35_slide_deck.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Slide content enriched successfully in generate_35_slide_deck.py!")
