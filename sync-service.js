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
    onReset: [],
    onPosition: []
  };

  const knownPositions = new Map();

  function sanitizeKey(str) {
    return (str || '').trim().replace(/[.#$\[\]\/]/g, '_');
  }

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

        // Escuta posições de todos os jogadores no mapa do campus
        firebaseDb.ref('kahoot_rpg/positions').on('value', (snapshot) => {
          const positions = snapshot.val() || {};
          Object.values(positions).forEach(p => {
            if (p && p.playerName) {
              knownPositions.set(p.playerName.trim().toLowerCase(), p);
            }
          });
          callbacks.onPosition.forEach(cb => {
            try { cb(positions); } catch(e) { console.error(e); }
          });
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
    } else if (data.type === 'PLAYER_POSITION' && data.payload) {
      const p = data.payload;
      if (p && p.playerName) {
        knownPositions.set(p.playerName.trim().toLowerCase(), p);
        callbacks.onPosition.forEach(cb => {
          try { cb({ [p.playerName]: p }); } catch(e) { console.error(e); }
        });
      }
    } else if (data.type === 'STATE_UPDATE' && data.state) {
      localStorage.setItem('kahoot_rpg_state', JSON.stringify(data.state));
      callbacks.onStateUpdate.forEach(cb => {
        try { cb(data.state); } catch(e) { console.error(e); }
      });
    } else if (data.type === 'GAME_RESET') {
      seenAnswerKeys.clear();
      knownPositions.clear();
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
      callbacks.onPosition.forEach(cb => {
        try { cb({}); } catch(e) { console.error(e); }
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

    onPosition: function (cb) {
      if (typeof cb === 'function') callbacks.onPosition.push(cb);
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

    // Verificação de nome duplicado na sala
    isPlayerNameTaken: function (name, currentName) {
      const clean = (name || '').trim().toLowerCase();
      if (!clean) return false;
      if (currentName && clean === currentName.trim().toLowerCase()) return false;

      // 1. Checa no estado salvo localmente (gameState.players)
      const state = this.getLocalState();
      if (state && state.players) {
        for (const k of Object.keys(state.players)) {
          if (k.trim().toLowerCase() === clean) return true;
        }
      }

      // 2. Checa no mapa de posições conhecidas
      if (knownPositions.has(clean)) {
        return true;
      }

      return false;
    },

    // Obter todas as posições atuais
    getPositions: function () {
      const out = {};
      knownPositions.forEach((v, k) => { out[v.playerName || k] = v; });
      return out;
    },

    // Enviar posição do avatar no mapa (chamado a cada 30 segundos ou em marcos)
    sendPosition: function (payload) {
      if (!payload || !payload.playerName) return;
      const enriched = {
        ...payload,
        timestamp: Date.now()
      };
      const key = sanitizeKey(payload.playerName);
      knownPositions.set(payload.playerName.trim().toLowerCase(), enriched);

      // 1. Envio Local
      if (broadcastChannel) {
        broadcastChannel.postMessage({
          type: 'PLAYER_POSITION',
          payload: enriched
        });
      }

      // 2. Envio Nuvem (Firebase)
      if (isFirebaseActive && firebaseDb) {
        try {
          firebaseDb.ref('kahoot_rpg/positions/' + key).set(enriched);
        } catch (e) {
          console.error('[SyncService] Erro ao enviar posição para Firebase:', e);
        }
      }
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
          firebaseDb.ref('kahoot_rpg/positions').set(null),
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
