/**
 * ==============================================================================
 * SYNC SERVICE - KAKOOT RPG SEMINÁRIO GETI 2026 (PPG-PIT UNIFESP)
 * Sincronização Híbrida: Firebase Realtime Database (Nuvem) + BroadcastChannel (Local)
 * ==============================================================================
 */

(function (window) {
  const CHANNEL_NAME = 'kahoot_rpg_channel';
  let broadcastChannel = null;
  let firebaseDb = null;
  let isFirebaseActive = false;

  const callbacks = {
    onAnswer: [],
    onStateUpdate: [],
    onReset: []
  };

  // 1. Inicialização do BroadcastChannel Local
  try {
    if (typeof BroadcastChannel !== 'undefined') {
      broadcastChannel = new BroadcastChannel(CHANNEL_NAME);
      broadcastChannel.onmessage = (event) => {
        handleIncomingMessage(event.data);
      };
    }
  } catch (e) {
    console.warn('[SyncService] BroadcastChannel indisponível:', e);
  }

  // 2. Inicialização do Firebase se configurado
  function initFirebase() {
    const config = window.FIREBASE_CONFIG;
    if (config && config.apiKey && (config.databaseURL || config.projectId) && typeof firebase !== 'undefined') {
      try {
        if (!config.databaseURL && config.projectId) {
          config.databaseURL = `https://${config.projectId}-default-rtdb.firebaseio.com`;
        }
        if (!firebase.apps.length) {
          firebase.initializeApp(config);
        }
        firebaseDb = firebase.database();
        isFirebaseActive = true;
        console.log('[SyncService] ✅ Conectado com sucesso ao Firebase Realtime Database! URL:', config.databaseURL);

        // Escuta atualizações de estado do jogo (liberação de fases)
        firebaseDb.ref('kahoot_rpg/state').on('value', (snapshot) => {
          const state = snapshot.val();
          if (state) {
            localStorage.setItem('kahoot_rpg_state', JSON.stringify(state));
            callbacks.onStateUpdate.forEach(cb => cb(state));
          }
        });

        // Escuta sinal de reset geral do jogo
        firebaseDb.ref('kahoot_rpg/resetSignal').on('value', (snapshot) => {
          const val = snapshot.val();
          if (val && (Date.now() - val < 1000 * 60 * 30)) { // últimos 30 min
            handleIncomingMessage({ type: 'GAME_RESET', state: window.SyncService.getLocalState() });
          }
        });

        // Escuta novas respostas de alunos
        firebaseDb.ref('kahoot_rpg/answers').limitToLast(50).on('child_added', (snapshot) => {
          const answer = snapshot.val();
          if (answer && answer.timestamp && (Date.now() - answer.timestamp < 1000 * 60 * 180)) { // 3 horas
            callbacks.onAnswer.forEach(cb => cb(answer));
          }
        });

      } catch (err) {
        console.warn('[SyncService] Falha ao inicializar Firebase (usando modo local):', err);
        isFirebaseActive = false;
      }
    } else {
      console.log('[SyncService] Firebase não configurado. Operando em modo Local (BroadcastChannel + LocalStorage).');
    }
  }

  function handleIncomingMessage(data) {
    if (!data) return;
    if (data.type === 'PLAYER_ANSWER' && data.payload) {
      callbacks.onAnswer.forEach(cb => cb(data.payload));
    } else if (data.type === 'STATE_UPDATE' && data.state) {
      localStorage.setItem('kahoot_rpg_state', JSON.stringify(data.state));
      callbacks.onStateUpdate.forEach(cb => cb(data.state));
    } else if (data.type === 'GAME_RESET') {
      localStorage.removeItem('kahoot_rpg_current_player');
      if (data.state) {
        localStorage.setItem('kahoot_rpg_state', JSON.stringify(data.state));
      }
      callbacks.onReset.forEach(cb => cb(data.state));
      callbacks.onStateUpdate.forEach(cb => cb(data.state));
    }
  }

  // API Pública do SyncService
  window.SyncService = {
    isCloudActive: () => isFirebaseActive,

    init: function () {
      initFirebase();
      return this;
    },

    onAnswer: function (cb) {
      if (typeof cb === 'function') callbacks.onAnswer.push(cb);
      return this;
    },

    onStateUpdate: function (cb) {
      if (typeof cb === 'function') callbacks.onStateUpdate.push(cb);
      return this;
    },

    onReset: function (cb) {
      if (typeof cb === 'function') callbacks.onReset.push(cb);
      return this;
    },

    // Enviar resposta do aluno
    sendAnswer: function (payload) {
      // payload: { playerName, turma, questionId, optionKey, isCorrect, timeMs }
      const enrichedPayload = {
        ...payload,
        timestamp: Date.now()
      };

      // 1. Envio Local
      if (broadcastChannel) {
        broadcastChannel.postMessage({
          type: 'PLAYER_ANSWER',
          payload: enrichedPayload
        });
      }

      // 2. Envio Nuvem (Firebase)
      if (isFirebaseActive && firebaseDb) {
        try {
          firebaseDb.ref('kahoot_rpg/answers').push(enrichedPayload);
        } catch (e) {
          console.error('[SyncService] Erro ao enviar resposta para Firebase:', e);
        }
      }
    },

    // Enviar atualização de estado (Admin)
    sendState: function (gameState) {
      localStorage.setItem('kahoot_rpg_state', JSON.stringify(gameState));

      // 1. Envio Local
      if (broadcastChannel) {
        broadcastChannel.postMessage({
          type: 'STATE_UPDATE',
          state: gameState
        });
      }

      // 2. Envio Nuvem (Firebase)
      if (isFirebaseActive && firebaseDb) {
        try {
          firebaseDb.ref('kahoot_rpg/state').set(gameState);
        } catch (e) {
          console.error('[SyncService] Erro ao enviar estado para Firebase:', e);
        }
      }
    },

    // Resetar jogo completo (Admin)
    sendReset: function (gameState) {
      localStorage.setItem('kahoot_rpg_state', JSON.stringify(gameState));
      localStorage.removeItem('kahoot_rpg_current_player');

      // 1. Envio Local
      if (broadcastChannel) {
        broadcastChannel.postMessage({
          type: 'GAME_RESET',
          state: gameState
        });
      }

      // 2. Envio Nuvem (Firebase)
      if (isFirebaseActive && firebaseDb) {
        try {
          firebaseDb.ref('kahoot_rpg/state').set(gameState);
          firebaseDb.ref('kahoot_rpg/answers').remove();
          firebaseDb.ref('kahoot_rpg/resetSignal').set(Date.now());
        } catch (e) {
          console.error('[SyncService] Erro ao resetar Firebase:', e);
        }
      }
    },

    // Carregar estado salvo
    getLocalState: function () {
      try {
        const raw = localStorage.getItem('kahoot_rpg_state');
        return raw ? JSON.parse(raw) : null;
      } catch (e) {
        return null;
      }
    }
  };

  // Auto-init ao carregar página
  window.addEventListener('DOMContentLoaded', () => {
    window.SyncService.init();
  });

})(window);
