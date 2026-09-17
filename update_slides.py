# -*- coding: utf-8 -*-
import re
import os
import shutil

path_gen = r"C:\Users\jj\OneDrive\Estudos\Edital unifesp PIT 2026\Disciplinas 02 2026\Gestão estratégica da inovação\Seminário\generate_deck.py"
with open(path_gen, 'r', encoding='utf-8') as f:
    code = f.read()

slide_25_26_pattern = re.compile(r'<!-- SLIDE 25: Apresentação da Dinâmica.*?<!-- SLIDE 27: Conclusões', re.DOTALL)

new_slides = '''<!-- SLIDE 25: Apresentação da Dinâmica Interativa com QR Code -->
    <section class="slide" data-slide="25" data-block="Dinâmica" data-speaker="Grupo Inteiro" data-time="5 min">
      <div class="slide-tag">🎮 ATIVIDADE DINÂMICA • GAME INTERATIVO NO CELULAR</div>
      <h2 class="slide-title">Dinâmica Interativa: <span>O Orquestrador do Ecossistema</span></h2>
      <p class="slide-subtitle">
        Todos os participantes da sala assumem agora a liderança estratégica do PIT São José dos Campos. Sem certo ou errado: cada decisão revela um arquétipo de governança para nossa roda de conversa.
      </p>

      <div class="grid-2" style="align-items: center;">
        <!-- Left: QR Code Showcase Card -->
        <div class="card card-glow-cyan" style="display: flex; flex-direction: column; align-items: center; text-align: center; padding: 1.5rem; background: rgba(10, 19, 36, 0.9);">
          <div style="font-family: var(--font-display); font-size: 1.15rem; font-weight: 800; color: #fff; margin-bottom: 0.6rem;">
            📱 Aponte a Câmera do seu Celular
          </div>
          <div style="background: #ffffff; padding: 0.85rem; border-radius: 16px; box-shadow: 0 0 35px rgba(6, 182, 212, 0.35); margin-bottom: 0.85rem; border: 2px solid var(--cyan-light);">
            <img src="assets/qrcode_jogo.png" alt="QR Code para o jogo do PIT" style="width: 200px; height: 200px; display: block; object-fit: contain;">
          </div>
          <div style="font-family: var(--font-mono); font-size: 0.82rem; color: var(--cyan-light); margin-bottom: 0.75rem; word-break: break-all;">
            josuejofre.github.io/seminario-ecossistema-inovacao-pit/jogo.html
          </div>
          <a href="jogo.html" target="_blank" class="deck-btn" style="background: var(--blue-accent); color: #fff; text-decoration: none; padding: 0.5rem 1.1rem; font-size: 0.82rem;">
            <span>↗</span> Abrir Jogo no Navegador
          </a>
        </div>

        <!-- Right: Instructions & Timer -->
        <div style="display: flex; flex-direction: column; gap: 1rem;">
          <div class="card card-glow-purple">
            <div class="card-title" style="font-size: 1.1rem;">Como Funciona a Dinâmica (5 Rodadas):</div>
            <ul style="margin-left: 1.25rem; font-size: 0.88rem; color: #cbd5e1; line-height: 1.6;">
              <li><strong>Passo 1:</strong> Abra a câmera do smartphone e aponte para o QR Code ao lado.</li>
              <li><strong>Passo 2:</strong> Digite seu nome e enfrente 5 dilemas reais do PIT SJC (conflito de patentes, aceleração do Nexus, fundo soberano, sociedade e descarbonização).</li>
              <li><strong>Passo 3:</strong> Escolha com autonomia: cada opção prioriza uma Hélice e traz trade-offs reais.</li>
              <li><strong>Passo 4:</strong> Descubra seu <strong>Arquétipo de Orquestrador</strong> e sua <strong>Manchete de 2031</strong> para a nossa roda de debate!</li>
            </ul>
          </div>

          <div class="card card-glow-emerald" style="display: flex; align-items: center; justify-content: space-between; padding: 1.2rem;">
            <div>
              <div style="font-size: 0.85rem; color: var(--text-muted); font-weight: 600;">⏱ Tempo para Todos Jogarem:</div>
              <div id="countdown-game" style="font-family: var(--font-mono); font-size: 1.8rem; font-weight: 800; color: var(--emerald-accent);">05:00</div>
            </div>
            <button class="deck-btn" id="btn-timer-game" onclick="toggleGameTimer()" style="background: rgba(16, 185, 129, 0.2); border-color: var(--emerald-accent); color: #fff; padding: 0.6rem 1.1rem;">
              <span>▶</span> Iniciar Contagem
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 26: Roda de Conversa & Debriefing dos Arquétipos -->
    <section class="slide" data-slide="26" data-block="Dinâmica" data-speaker="Grupo Inteiro" data-time="15 min">
      <div class="slide-tag">🎤 RODA DE CONVERSA • DEBRIEFING ESTRATÉGICO</div>
      <h2 class="slide-title">Roda de Conversa: <span>Que Tipo de Orquestrador Você É?</span></h2>
      <p class="slide-subtitle">
        Veja a distribuição dos perfis na sala. Levantem a mão e debatam os motivos de cada decisão:
      </p>

      <!-- Archetypes Tally Grid -->
      <div class="grid-3" style="margin-bottom: 1.25rem;">
        <div class="card card-glow-cyan" style="padding: 1.1rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
            <span style="font-size: 1.75rem;">💼</span>
            <div style="display: flex; align-items: center; gap: 0.4rem;">
              <button class="deck-btn" style="padding: 0.15rem 0.45rem; font-size: 0.72rem;" onclick="adjustTally('corp', -1)">-</button>
              <span id="tally-corp" style="font-family: var(--font-mono); font-weight: 800; font-size: 1.1rem; color: var(--cyan-light);">0</span>
              <button class="deck-btn" style="padding: 0.15rem 0.45rem; font-size: 0.72rem;" onclick="adjustTally('corp', +1)">+</button>
            </div>
          </div>
          <div class="card-title" style="font-size: 1rem;">O Pragmático Corporativo</div>
          <p class="card-desc" style="font-size: 0.8rem;">Priorizou receita, grandes contratos da Embraer e sobrevivência financeira.</p>
        </div>

        <div class="card card-glow-purple" style="padding: 1.1rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
            <span style="font-size: 1.75rem;">🔬</span>
            <div style="display: flex; align-items: center; gap: 0.4rem;">
              <button class="deck-btn" style="padding: 0.15rem 0.45rem; font-size: 0.72rem;" onclick="adjustTally('academia', -1)">-</button>
              <span id="tally-academia" style="font-family: var(--font-mono); font-weight: 800; font-size: 1.1rem; color: var(--purple-accent);">0</span>
              <button class="deck-btn" style="padding: 0.15rem 0.45rem; font-size: 0.72rem;" onclick="adjustTally('academia', +1)">+</button>
            </div>
          </div>
          <div class="card-title" style="font-size: 1rem;">O Guardião da Ciência Aberta</div>
          <p class="card-desc" style="font-size: 0.8rem;">Defendeu a autonomia da UNIFESP, patentes públicas e publicação de teses.</p>
        </div>

        <div class="card card-glow-amber" style="padding: 1.1rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
            <span style="font-size: 1.75rem;">⚡</span>
            <div style="display: flex; align-items: center; gap: 0.4rem;">
              <button class="deck-btn" style="padding: 0.15rem 0.45rem; font-size: 0.72rem;" onclick="adjustTally('deeptech', -1)">-</button>
              <span id="tally-deeptech" style="font-family: var(--font-mono); font-weight: 800; font-size: 1.1rem; color: var(--amber-accent);">0</span>
              <button class="deck-btn" style="padding: 0.15rem 0.45rem; font-size: 0.72rem;" onclick="adjustTally('deeptech', +1)">+</button>
            </div>
          </div>
          <div class="card-title" style="font-size: 1rem;">O Acelerador de Deep Techs</div>
          <p class="card-desc" style="font-size: 0.8rem;">Apostou em hardware espacial, propulsão e risco tecnológico radical no Nexus.</p>
        </div>

        <div class="card card-glow-emerald" style="padding: 1.1rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
            <span style="font-size: 1.75rem;">🌱</span>
            <div style="display: flex; align-items: center; gap: 0.4rem;">
              <button class="deck-btn" style="padding: 0.15rem 0.45rem; font-size: 0.72rem;" onclick="adjustTally('esg', -1)">-</button>
              <span id="tally-esg" style="font-family: var(--font-mono); font-weight: 800; font-size: 1.1rem; color: var(--emerald-accent);">0</span>
              <button class="deck-btn" style="padding: 0.15rem 0.45rem; font-size: 0.72rem;" onclick="adjustTally('esg', +1)">+</button>
            </div>
          </div>
          <div class="card-title" style="font-size: 1rem;">O Pioneiro da Quíntupla Hélice</div>
          <p class="card-desc" style="font-size: 0.8rem;">Colocou a descarbonização, o SAF e o impacto na periferia como prioridade nº 1.</p>
        </div>

        <div class="card card-glow-cyan" style="padding: 1.1rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
            <span style="font-size: 1.75rem;">🏛️</span>
            <div style="display: flex; align-items: center; gap: 0.4rem;">
              <button class="deck-btn" style="padding: 0.15rem 0.45rem; font-size: 0.72rem;" onclick="adjustTally('diplomat', -1)">-</button>
              <span id="tally-diplomat" style="font-family: var(--font-mono); font-weight: 800; font-size: 1.1rem; color: var(--blue-electric);">0</span>
              <button class="deck-btn" style="padding: 0.15rem 0.45rem; font-size: 0.72rem;" onclick="adjustTally('diplomat', +1)">+</button>
            </div>
          </div>
          <div class="card-title" style="font-size: 1rem;">O Diplomata Sistêmico</div>
          <p class="card-desc" style="font-size: 0.8rem;">Construiu acordos híbridos, cotitularidades e manteve as 4 hélices dialogando.</p>
        </div>

        <div class="card card-glow-rose" style="padding: 1.1rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
            <span style="font-size: 1.75rem;">🤝</span>
            <div style="display: flex; align-items: center; gap: 0.4rem;">
              <button class="deck-btn" style="padding: 0.15rem 0.45rem; font-size: 0.72rem;" onclick="adjustTally('community', -1)">-</button>
              <span id="tally-community" style="font-family: var(--font-mono); font-weight: 800; font-size: 1.1rem; color: var(--rose-accent);">0</span>
              <button class="deck-btn" style="padding: 0.15rem 0.45rem; font-size: 0.72rem;" onclick="adjustTally('community', +1)">+</button>
            </div>
          </div>
          <div class="card-title" style="font-size: 1rem;">O Articulador Comunitário</div>
          <p class="card-desc" style="font-size: 0.8rem;">Derrubou os muros do parque e integrou São José dos Campos em living labs sociais.</p>
        </div>
      </div>

      <!-- Debate Provocations -->
      <div class="card" style="background: rgba(15, 23, 42, 0.85); border-left: 4px solid var(--purple-accent);">
        <div style="font-family: var(--font-display); font-size: 1.1rem; font-weight: 700; color: #fff; margin-bottom: 0.5rem;">
          💬 Provocações Abertas para a Turma e os Docentes (Profª Iraci & Prof. Ueta):
        </div>
        <div class="grid-2" style="gap: 1rem; font-size: 0.85rem; color: #cbd5e1;">
          <div>
            <strong>1. Para quem escolheu ceder a patente à multinacional:</strong><br>
            Como proteger o pesquisador da UNIFESP que passou anos desenvolvendo a tecnologia e agora vê seu artigo bloqueado por sigilo corporativo?
          </div>
          <div>
            <strong>2. Para quem escolheu a soberania radical e recusou o fundo asiático:</strong><br>
            Como manter o ritmo de inovação se os editais públicos de fomento (FAPESP/Finep) sofrerem contingenciamento orçamentário?
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 27: Conclusões'''

code = slide_25_26_pattern.sub(new_slides, code)

# Update speaker notes
notes_pattern = re.compile(r'25: \{.*?27: \{', re.DOTALL)
new_notes = '''25: {
        speaker: "Grupo Inteiro",
        time: "5 minutos",
        notes: `
          <strong>Lançamento do Jogo de Tomada de Decisões:</strong><br>
          • Convide a turma e os professores a apontarem a câmera do celular para o QR Code na tela.<br>
          • Enfatize a proposta do grupo: não é uma prova de múltipla escolha ou quiz convencional; é um game de dilemas sem resposta certa ou errada.<br>
          • Avise que cada um terá 5 minutos para responder individualmente aos 5 dilemas no smartphone e descobrir seu Arquétipo de Orquestrador.<br>
          • Inicie o cronômetro de 5 minutos na tela.
        `
      },
      26: {
        speaker: "Grupo Inteiro",
        time: "15 minutos",
        notes: `
          <strong>Roda de Conversa e Debriefing dos Arquétipos:</strong><br>
          • Com todos com os celulares em mãos, pergunte: 'Quem aqui tirou o perfil Pragmático Corporativo?'. Vá clicando nos botões '+' para registrar a contagem da sala na tela.<br>
          • Em seguida, chame alguns voluntários: 'Por que você decidiu ceder a patente para a Embraer?', 'E quem protegeu a UNIFESP, como justificou a perda de verba?'.<br>
          • Convide a Profª Iraci e o Prof. Ueta para comentarem como esses dilemas de arquétipos refletem a governança real dos parques tecnológicos no Brasil.
        `
      },
      27: {'''

code = notes_pattern.sub(new_notes, code)

helper_js = '''
    /* Game Countdown Timer on Slide 25 */
    let gameSec = 300;
    let gameRunning = false;
    let gameInterval = null;
    function toggleGameTimer() {
      const display = document.getElementById('countdown-game');
      const btn = document.getElementById('btn-timer-game');
      if (!gameRunning) {
        gameRunning = true;
        btn.innerHTML = '<span>⏸</span> Pausar';
        gameInterval = setInterval(() => {
          if (gameSec > 0) {
            gameSec--;
            const m = Math.floor(gameSec / 60);
            const s = gameSec % 60;
            display.textContent = (m < 10 ? '0' + m : m) + ':' + (s < 10 ? '0' + s : s);
          } else {
            clearInterval(gameInterval);
            display.textContent = 'TEMPO ESGOTADO!';
            btn.innerHTML = '<span>↺</span> Reiniciar';
            gameRunning = false;
          }
        }, 1000);
      } else {
        clearInterval(gameInterval);
        btn.innerHTML = '<span>▶</span> Continuar';
        gameRunning = false;
      }
    }

    /* Interactive Tally for Debriefing on Slide 26 */
    const tallyScores = {
      corp: 0,
      academia: 0,
      deeptech: 0,
      esg: 0,
      diplomat: 0,
      community: 0
    };

    function adjustTally(key, delta) {
      tallyScores[key] = Math.max(0, tallyScores[key] + delta);
      document.getElementById('tally-' + key).textContent = tallyScores[key];
    }
'''

if 'function toggleGameTimer()' not in code:
    code = code.replace('// Initialize presentation on load', helper_js + '\n    // Initialize presentation on load')

with open(path_gen, 'w', encoding='utf-8') as f:
    f.write(code)

print("generate_deck.py updated successfully!")
