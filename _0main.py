# Simulador: [Simulador de carreira]
# Grupo: Paulo Cézar, Kaue Souza, Guilherme Fonseca
from _1Guilherme import Iniciar, decisao1
from _2Paulo import escolha_de_time,  chegada
from _3Kaue import mostrar_status, mostrar_menu, mostrar_resultado
# 1. Mensagem de Boas-Vindas inicial do jogo
print('--- SEJA BEM VINDO AO SIMULADOR DE CARREIRA  ---')
print('Você tem exatamente 10 dias pra construir o seu jogador com objetivo de ir pra copa do mundo')
input("\nAperte ENTER para continuar...\n")

# 2. Dicionário de atributos inicializado
atributos = {
    'habilidade': 50,
    'energia': 100,
    'fama': 0,
    'dia': 1,
    'reputacao': 50
}

# 3. Execução da história do jogo na ordem correta
# Pede o nome do jogador
Iniciar() 

# Realiza a primeira grande decisão (Jogo contra Arthur Nogueira)
decisao1() 

# ele escolhe qual time ele vai 
escolha_de_time()

# Mostra a transferência para o Palmeiras e atualiza os atributos passados por parâmetro
chegada(atributos) 

# 4. Mostra o placar de atributos finalizado do dia
print(f'\nAtributos atuais do jogador: {atributos}')
