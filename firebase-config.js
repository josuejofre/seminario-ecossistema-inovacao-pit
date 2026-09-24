// ==============================================================================
// CONFIGURAÇÃO DO FIREBASE (OPCIONAL, MAS RECOMENDADO PARA USO EM SALA DE AULA)
// ==============================================================================
// Para que 30+ celulares na sala sincronizem em tempo real com o projetor e o
// painel de administração via 4G/Wi-Fi:
//
// 1. Crie um projeto gratuito no Firebase Console: https://console.firebase.google.com/
// 2. Vá em "Build" -> "Realtime Database" -> "Criar Banco de Dados" (Escolha modo teste).
// 3. Em Configurações do Projeto (ícone de engrenagem) -> "Seus aplicativos" -> Web (</>).
// 4. Copie o objeto 'firebaseConfig' e cole abaixo substituindo os valores:
// ==============================================================================

window.FIREBASE_CONFIG = {
  // Cole suas credenciais aqui se desejar sincronização na nuvem (4G/Wi-Fi da sala).
  // Se deixar vazio ou não preencher, o sistema funciona normalmente usando
  // BroadcastChannel nativo do navegador (ótimo para testes locais na mesma máquina).
  
  apiKey: "",
  authDomain: "",
  databaseURL: "",
  projectId: "",
  storageBucket: "",
  messagingSenderId: "",
  appId: ""
};
