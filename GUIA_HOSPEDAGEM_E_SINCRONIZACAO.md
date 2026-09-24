# 🚀 Guia de Hospedagem, Sincronização em Tempo Real e Operação do Kahoot RPG
**Seminário 5 — Gestão Estratégica da Inovação (GETI 2026)**  
*PPG-PIT • UNIFESP São José dos Campos*

---

## 📌 Sumário Executivo das Respostas

### 1. Formato RPG + Kahoot Integrado (O Avatar Anda no Mapa do PIT SJC)
- **Não abandonamos o RPG!** Pelo contrário: agora o aluno controla um **Avatar 2D interativo** andando pelo mapa do Parque Tecnológico de São José dos Campos.
- Ao se aproximar de cada estação temática (Nexus Hub, DCTA, Parque Tecnológico, Lab Net-Zero, etc.), o **portal do Kahoot** se abre automaticamente na tela do celular com:
  - 3 perguntas daquele bloco específico;
  - Cronômetro regressivo com pontuação regressiva por milissegundo (estilo Kahoot oficial);
  - Efeitos sonoros sintetizados via Web Audio API;
  - Botão de feedback imediato com a explicação científica de cada autor.
- Ao terminar a estação, o aluno volta a andar no mapa em direção à próxima estação desbloqueada pelo administrador.

---

### 2. Embaralhamento Dinâmico das Alternativas (Fisher-Yates Shuffle)
- No código anterior, a resposta certa estava fixa na primeira opção (`options[0]`).
- **Agora está 100% corrigido e embaralhado**: cada pergunta passa pelo algoritmo matemático de **Fisher-Yates Shuffle** no exato momento em que é renderizada na tela do jogador.
- A posição correta agora alterna aleatoriamente entre as posições **A, B e C** para cada aluno, impedindo "colas" ou padrões previsíveis.
- Internamente, o sistema mapeia a resposta escolhida para uma chave semântica de diagnóstico, garantindo que os **Gráficos de Pizza da Administração** registrem com 100% de exatidão quais foram os erros conceituais da turma.

---

### 3. Como Hospedar e Salvar os Dados das Respostas dos Celulares

Para que os 30+ alunos da sala joguem em seus smartphones (no 4G ou Wi-Fi da UNIFESP) e os dados apareçam instantaneamente no telão do projetor e no notebook do administrador, implementamos uma **Arquitetura Híbrida Inteligente**:

#### A. Onde Hospedar Gratuitamente (GitHub Pages - Recomendado)
1. Como a pasta `Seminário` já possui Git configurado, basta enviar para um repositório no seu GitHub:
   ```bash
   git add .
   git commit -m "Seminário GETI 2026: Slides, Kahoot RPG e Cockpit Admin"
   git branch -M main
   git remote add origin https://github.com/SEU_USUARIO/seminario-ecossistema-pit.git
   git push -u origin main
   ```
2. No GitHub: Acesse **Settings** > **Pages** > em *Branch*, selecione **main** e a pasta **/ (root)** ou **/Seminário**, e clique em **Save**.
3. Em 30 segundos, seu seminário estará online com HTTPS gratuito:
   - **Apresentação (Projetor):** `https://SEU_USUARIO.github.io/seminario-ecossistema-pit/index.html`
   - **Jogo dos Alunos (Smartphones):** `https://SEU_USUARIO.github.io/seminario-ecossistema-pit/jogo.html`
   - **Cockpit do Administrador:** `https://SEU_USUARIO.github.io/seminario-ecossistema-pit/admin.html`

---

#### B. Como Salvar e Sincronizar em Tempo Real (Firebase Realtime Database — Gratuito)
Para conectar dezenas de celulares diferentes pela internet sem precisar programar nenhum servidor backend:

1. Acesse o [Firebase Console](https://console.firebase.google.com/) (com sua conta Google).
2. Clique em **"Adicionar Projeto"** e dê um nome (ex: `geti-seminario-pit`).
3. No menu lateral esquerdo, vá em **Criação (Build)** > **Realtime Database** > **Criar Banco de Dados**.
   - Escolha o local padrão (`Estados Unidos`) e selecione **"Modo de Teste"** (permite leitura e escrita imediata).
4. No menu lateral, clique na engrenagem ⚙️ (**Configurações do Projeto**) > desça até **"Seus aplicativos"** > clique no ícone Web `</>`.
5. Copie os valores de `firebaseConfig` e cole dentro do arquivo [`firebase-config.js`](file:///c:/Users/jj/OneDrive/Estudos/Edital%20unifesp%20PIT%202026/Disciplinas%2002%202026/Gest%C3%A3o%20estrat%C3%A9gica%20da%20inova%C3%A7%C3%A3o/Semin%C3%A1rio/firebase-config.js):
   ```javascript
   window.FIREBASE_CONFIG = {
     apiKey: "AIzaSy...",
     authDomain: "geti-seminario-pit.firebaseapp.com",
     databaseURL: "https://geti-seminario-pit-default-rtdb.firebaseio.com",
     projectId: "geti-seminario-pit",
     storageBucket: "geti-seminario-pit.appspot.com",
     messagingSenderId: "123456789",
     appId: "1:123456789:web:..."
   };
   ```
6. **Pronto!** O script [`sync-service.js`](file:///c:/Users/jj/OneDrive/Estudos/Edital%20unifesp%20PIT%202026/Disciplinas%2002%202026/Gest%C3%A3o%20estrat%C3%A9gica%20da%20inova%C3%A7%C3%A3o/Semin%C3%A1rio/sync-service.js) conecta todos os celulares dos alunos ao projetor e ao admin instantaneamente via WebSockets de baixa latência (<50ms).
7. **Backup Local:** O painel `admin.html` possui os botões **"📥 Exportar CSV"** e **"📥 Exportar JSON"** para você salvar o histórico completo das notas e tempos no Excel ao final da aula!

> *Nota:* Se você abrir o projeto localmente no mesmo computador para testar em duas abas (sem internet), o sistema detecta que o Firebase está desativado e utiliza o **`BroadcastChannel`** nativo do navegador automaticamente!

---

### 4. Eliminação dos Espaços Vazios nos Slides
Na versão anterior, os cartões sofriam com estiramento vertical (`height: 100%` com `space-between`), deixando grandes vazios escuros quando o texto era enxuto.

**Soluções aplicadas:**
1. **Estrutura Visualmente Equilibrada:**
   - Adicionados chips conceituais, badges coloridos, ícones SVG e caixas de destaque em gradiente.
   - Adicionada a faixa de **Frase de Efeito (Punchline)** com aspas elegantes em todos os slides.
2. **Widgets de Interatividade:**
   - No Slide 1 e nos slides de encerramento de bloco (Checkpoints 6, 9, 12, 15, 17, 24), foi inserido o **Ticker de Status ao Vivo do Kahoot RPG**, preenchendo o espaço inferior de forma dinâmica e moderna.
3. **Diagramas e Gráficos:**
   - Slides teóricos agora contêm matrizes comparativas, fluxogramas de 4 etapas e barras de métricas visuais.

---

### 5. Ranking e Nomes Atualizando em Tempo Real no Telão
O slide do seminário agora se comporta como um verdadeiro painel de transmissão ao vivo:

- **Slide 1 (Abertura):** Mostra o indicador pulsante verde *"Transmissão ao Vivo do Kahoot RPG"* e atualiza a quantidade de participantes conectados e quem está liderando.
- **Slides 6, 9, 12, 15, 17 e 24 (Fim de cada Bloco):** Mostram o card de checkpoint com o líder parcial da sala em tempo real:
  `🥇 [Nome do Aluno] ([Pontuação] pts)`.
- **Slide 25 (Consolidação do Kahoot):** Exibe o **Pódio Dinâmico** com o Top 3 em destaque e o número de jogadores ativos.
- **Slide 26 (Premiação & Análise de Erros):** 
  - Projeta a tabela ao vivo com os 6 melhores colocados, suas turmas (Quarta ou Quinta), acertos sobre 18 e pontuação total.
  - Destaca o card do **Campeão Geral da Turma**.
  - Possui o botão para abrir diretamente o **Cockpit Admin** e analisar os Gráficos de Pizza de cada questão com a turma!

---

## 🗂️ Mapeamento de Arquivos da Solução

| Arquivo | Tamanho | Função |
| :--- | :--- | :--- |
| [`index.html`](file:///c:/Users/jj/OneDrive/Estudos/Edital%20unifesp%20PIT%202026/Disciplinas%2002%202026/Gest%C3%A3o%20estrat%C3%A9gica%20da%20inova%C3%A7%C3%A3o/Semin%C3%A1rio/index.html) | ~125 KB | Apresentação oficial dos 29 slides com ranking ao vivo, timer, notas (N) e navegação |
| [`jogo.html`](file:///c:/Users/jj/OneDrive/Estudos/Edital%20unifesp%20PIT%202026/Disciplinas%2002%202026/Gest%C3%A3o%20estrat%C3%A9gica%20da%20inova%C3%A7%C3%A3o/Semin%C3%A1rio/jogo.html) | ~53 KB | RPG 2D do Aluno (Avatar andando pelo PIT SJC + Kahoot nos portais com alternativas embaralhadas) |
| [`admin.html`](file:///c:/Users/jj/OneDrive/Estudos/Edital%20unifesp%20PIT%202026/Disciplinas%2002%202026/Gest%C3%A3o%20estrat%C3%A9gica%20da%20inova%C3%A7%C3%A3o/Semin%C3%A1rio/admin.html) | ~59 KB | Cockpit de Administração: liberação de fases, ranking, pódio com confetes e 18 gráficos de pizza |
| [`roteiro_falas_apresentadores.txt`](file:///c:/Users/jj/OneDrive/Estudos/Edital%20unifesp%20PIT%202026/Disciplinas%2002%202026/Gest%C3%A3o%20estrat%C3%A9gica%20da%20inova%C3%A7%C3%A3o/Semin%C3%A1rio/roteiro_falas_apresentadores.txt) | ~37 KB | Roteiro completo de falas slide a slide para os 29 slides, com speakers da 4ª e 5ª |
| [`firebase-config.js`](file:///c:/Users/jj/OneDrive/Estudos/Edital%20unifesp%20PIT%202026/Disciplinas%2002%202026/Gest%C3%A3o%20estrat%C3%A9gica%20da%20inova%C3%A7%C3%A3o/Semin%C3%A1rio/firebase-config.js) | ~1 KB | Configuração do Firebase para sincronização multi-celular em sala de aula |
| [`sync-service.js`](file:///c:/Users/jj/OneDrive/Estudos/Edital%20unifesp%20PIT%202026/Disciplinas%2002%202026/Gest%C3%A3o%20estrat%C3%A9gica%20da%20inova%C3%A7%C3%A3o/Semin%C3%A1rio/sync-service.js) | ~4 KB | Motor de sincronização em tempo real (Firebase Nuvem + BroadcastChannel Local) |
