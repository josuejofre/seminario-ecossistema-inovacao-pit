# -*- coding: utf-8 -*-
import re

with open('roteiro_falas_apresentadores.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update Slide 1 speaker
text = re.sub(
    r'(SLIDE 1 \| ABERTURA OFICIAL\nTema:[^\n]+\n)Apresentador\(a\):[^\n]+',
    r'\1Apresentador(a): Nathália Neves (Quarta) / Fernando Barreto (Quinta) [Apresentadores do Bloco 1]',
    text
)

# 2. Update Slide 2 speaker
text = re.sub(
    r'(SLIDE 2 \| AGENDA E CRONOGRAMA\nTema:[^\n]+\n)Apresentador\(a\):[^\n]+',
    r'\1Apresentador(a): Nathália Neves (Quarta) / Fernando Barreto (Quinta) [Apresentadores do Bloco 1]',
    text
)

# 3. Update Slide 31
text = re.sub(
    r'SLIDE 31 \| DINÂMICA INTERATIVA: PÓDIO E RANKING GERAL\nTema:[^\n]+\nApresentador\(a\):[^\n]+',
    '''SLIDE 31 | ATIVIDADE: DINÂMICA INTERATIVA, PÓDIO E RANKING GERAL
Tema: Apresentação dos Resultados do Kahoot RPG da Turma
Apresentador(a): Jéssica David (Condução da Atividade Oficial de Resultados)''',
    text
)

# 4. Update Slide 32
text = re.sub(
    r'SLIDE 32 \| PREMIAÇÃO E ANÁLISE DOS GRÁFICOS DE PIZZA\nTema:[^\n]+\nApresentador\(a\):[^\n]+',
    '''SLIDE 32 | ATIVIDADE: PREMIAÇÃO DO CAMPEÃO E ANÁLISE DOS GRÁFICOS DE PIZZA
Tema: Revelação do Vencedor Oficial e Análise Cienciométrica dos Erros da Turma
Apresentador(a): Jéssica David (Condução da Atividade Oficial de Premiação)''',
    text
)

# 5. Update speech of Slide 31 to reflect Jessica's voice
slide_31_old_speech = '''FALA SUGERIDA DO APRESENTADOR:
"Chegamos ao ápice da nossa dinâmica interativa! Ao longo das apresentações, vocês foram respondendo às fases liberadas pelo nosso painel de controle. Quem ainda não finalizou alguma fase, feche seu placar no celular.

Estamos projetando agora o pódio preliminar com os 3 primeiros colocados da turma! Esse sistema registrou em milissegundos a precisão e a velocidade de resposta de cada participante, refletindo o rigor analítico e a prontidão estratégica exigidos de um verdadeiro gestor de inovação!"'''

slide_31_new_speech = '''FALA SUGERIDA DE JÉSSICA DAVID (CONDUÇÃO DA ATIVIDADE PRÁTICA):
"Chegamos agora à Atividade Oficial do nosso seminário: a consolidação dos resultados da nossa dinâmica interativa! Ao longo de cada um dos blocos teóricos, nós fomos desafiados em tempo real nas 6 estações do Parque Tecnológico de São José dos Campos.

Como orquestradores em formação no PPG-PIT, nós sabemos que a velocidade de resposta associada à precisão científica é a chave para liderar ecossistemas complexos. Estamos projetando agora no telão o nosso Ranking Geral e o Pódio com os participantes que atingiram as maiores pontuações em tempo recorde! Parabéns a todos pelo engajamento e pelas respostas em cada fase!"'''

text = text.replace(slide_31_old_speech, slide_31_new_speech)

# 6. Update speech of Slide 32 to reflect Jessica's voice
slide_32_old_speech = '''FALA SUGERIDA DO APRESENTADOR:
"Vejam que fascinante: estamos projetando agora a nossa Interface Administrativa com os Gráficos de Pizza em tempo real de cada uma das 18 perguntas!
Observem, por exemplo, a pergunta sobre 'Ecossistema de Inovação vs Ecossistema de Negócios': 28% da turma escolheu a opção de que não há diferença conceitual. Isso ilustra com clareza a confusão apontada por Shen et al. entre criação coletiva de novo conhecimento e simples comercialização de produtos prontos!

E agora, o momento mais esperado: vamos revelar o PÓDIO e acionar o botão de premiação!
Em 3º lugar: [Nome do Aluno 3]!
Em 2º lugar: [Nome do Aluno 2]!
E o grande vencedor, o Orquestrador Mestre do Seminário 5, com maior pontuação e melhor tempo de resposta é... [NOME DO ALUNO 1]! Parabéns! (Aplausos da sala e acionamento dos confetes virtuais)."'''

slide_32_new_speech = '''FALA SUGERIDA DE JÉSSICA DAVID (CONDUÇÃO DA ATIVIDADE DE PREMIAÇÃO):
"Para fechar a nossa atividade prática com o rigor analítico que a disciplina exige, vamos olhar para os Gráficos de Pizza gerados pelas respostas de vocês em tempo real!

Vejam que dado riquíssimo: na pergunta sobre 'Ecossistema de Inovação versus Ecossistema de Negócios', uma parcela expressiva da sala ainda assinalou que ambos eram sinônimos. Isso comprova exatamente a tese de Shen et al.: na prática de mercado, há uma tendência de chamar qualquer arranjo comercial de 'ecossistema', quando na verdade o ecossistema de inovação exige co-criação de novidades e interdependência científica!

E agora, com muita honra, vamos celebrar o(a) grande vencedor(a) da dinâmica!
Em 3º lugar: [Nome do 3º Colocado]!
Em 2º lugar: [Nome do 2º Colocado]!
E o(a) grande Orquestrador(a) Mestre do Seminário 5, com a maior precisão e rapidez de resposta é... [NOME DO VENCEDOR]! Parabéns pelo desempenho brilhante! (Aplausos e acionamento da chuva de confetes virtuais)."'''

text = text.replace(slide_32_old_speech, slide_32_new_speech)

with open('roteiro_falas_apresentadores.txt', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated roteiro_falas_apresentadores.txt with Bloco 1 speakers on opening and Jessica on final activity!")
