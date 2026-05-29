# Simulador: Simulador de carreira
# Grupo: Paulo Cézar, Kaue Souza, Guilherme Fonseca

from _1Guilherme import Iniciar, decisao1
from _2Paulo import escolha_de_time, chegada

# 1. Mensagem inicial
print('--- SEJA BEM VINDO AO SIMULADOR DE CARREIRA ---')
print('Você tem exatamente 10 dias pra construir o seu jogador com objetivo de ir pra copa do mundo')
input("\nAperte ENTER para continuar...\n")

# 2. Estado do jogo
atributos = {
    'habilidade': 50,
    'energia': 100,
    'fama': 0,
    'dia': 1,
    'reputacao': 50
}

# LISTA DE HISTÓRICO
historico = []

# 3. Início do jogo
Iniciar()

# 4. Primeira decisão
decisao1(atributos)  # AGORA PASSA ATRIBUTOS
historico.append("Dia 1: Jogou partida contra Arthur Nogueira")

atributos['dia'] += 1

# 5. Escolha de time
escolha_de_time()
historico.append("Dia 2: Escolheu um time")

atributos['dia'] += 1

# 6. Chegada no time
chegada(atributos)
historico.append("Dia 3: Chegou ao novo clube")

atributos['dia'] += 1

# 7. Mostrar atributos finais
print(f'\nAtributos atuais do jogador: {atributos}')

# 8. MOSTRAR HISTÓRICO
print("\n===== HISTÓRICO DE DECISÕES =====")
for acao in historico:
    print("-", acao)