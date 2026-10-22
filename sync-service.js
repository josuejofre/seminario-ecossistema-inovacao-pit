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
  const pageLoadTime = Date.now();
  const seenAnswerKeys = new Set();

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
            callbacks.onStateUpdate.forEach(cb => {
              try { cb(state); } catch(e) { console.error(e); }
            });
          }
        });

        // Escuta sinal de reset geral do jogo (apenas disparos recentes pós-carregamento)
        firebaseDb.ref('kahoot_rpg/resetSignal').on('value', (snapshot) => {
          const val = snapshot.val();
          if (val && val > pageLoadTime - 2000) {
            handleIncomingMessage({ type: 'GAME_RESET', state: window.SyncService.getLocalState() });
          }
        });

        // Escuta respostas de alunos com deduplicação
        firebaseDb.ref('kahoot_rpg/answers').limitToLast(100).on('child_added', (snapshot) => {
          const answer = snapshot.val();
          if (answer && answer.timestamp && (Date.now() - answer.timestamp < 1000 * 60 * 180)) { // 3 horas
            triggerAnswer(answer);
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

  function triggerAnswer(answer) {
    if (!answer || !answer.playerName || !answer.questionId) return;

    // Deduplicação temporal contra eco entre BroadcastChannel e Firebase
    const dedupeKey = `${answer.playerName}__q${answer.questionId}__${answer.optionKey}`;
    if (seenAnswerKeys.has(dedupeKey)) return;
    seenAnswerKeys.add(dedupeKey);
    setTimeout(() => seenAnswerKeys.delete(dedupeKey), 8000);

    callbacks.onAnswer.forEach(cb => {
      try { cb(answer); } catch (err) { console.error('[SyncService] Answer callback error:', err); }
    });
  }

  function handleIncomingMessage(data) {
    if (!data) return;
    if (data.type === 'PLAYER_ANSWER' && data.payload) {
      triggerAnswer(data.payload);
    } else if (data.type === 'STATE_UPDATE' && data.state) {
      localStorage.setItem('kahoot_rpg_state', JSON.stringify(data.state));
      callbacks.onStateUpdate.forEach(cb => {
        try { cb(data.state); } catch(e) { console.error(e); }
      });
    } else if (data.type === 'GAME_RESET') {
      seenAnswerKeys.clear();
      localStorage.removeItem('kahoot_rpg_current_player');
      if (data.state) {
        localStorage.setItem('kahoot_rpg_state', JSON.stringify(data.state));
      }
      callbacks.onReset.forEach(cb => {
        try { cb(data.state); } catch(e) { console.error(e); }
      });
      callbacks.onStateUpdate.forEach(cb => {
        try { cb(data.state); } catch(e) { console.error(e); }
      });
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
      this.hardResetDatabase(gameState);
    },

    // Hard reset: apaga do Firebase, limpa local storage e dispara sinal
    hardResetDatabase: function (gameState, callback) {
      localStorage.removeItem('kahoot_rpg_state');
      localStorage.removeItem('kahoot_rpg_current_player');
      seenAnswerKeys.clear();

      // 1. Envio Local
      if (broadcastChannel) {
        broadcastChannel.postMessage({
          type: 'GAME_RESET',
          state: gameState
        });
      }
      callbacks.onReset.forEach(cb => { try { cb(gameState); } catch(e){} });
      callbacks.onStateUpdate.forEach(cb => { try { cb(gameState); } catch(e){} });

      // 2. Envio Nuvem (Firebase)
      if (isFirebaseActive && firebaseDb) {
        Promise.all([
          firebaseDb.ref('kahoot_rpg/state').set(gameState),
          firebaseDb.ref('kahoot_rpg/answers').set(null),
          firebaseDb.ref('kahoot_rpg/resetSignal').set(Date.now())
        ]).then(() => {
          console.log('[SyncService] ✅ Hard reset completo no Firebase Realtime Database.');
          if (typeof callback === 'function') callback(true);
        }).catch((err) => {
          console.error('[SyncService] Erro no hard reset do Firebase:', err);
          if (typeof callback === 'function') callback(false, err);
        });
      } else {
        if (typeof callback === 'function') callback(true);
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
