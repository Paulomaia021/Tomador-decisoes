
# Simulador: SIMULADOR DE CARREIRA
# Grupo: Paulo, Kauê e Guilherme

from aluno1 import exibir_status, exibir_menu
from aluno2 import aplicar_decisao
from aluno3 import verificar_encerramento, verificar_limites
from aluno4 import registrar_historico, exibir_historico

# --- Estado do sistema ---
estado = {
    "variavel_1": 100,
    "variavel_2": 100,
    "variavel_3": 50,
    "variavel_4": 0,
    "variavel_5": 1      # ex: ciclo atual
}

historico = []
OPCOES = ("Opção A", "Opção B", "Opção C")  # tupla — dados fixos

# --- Loop principal ---
while not verificar_encerramento(estado):
    exibir_status(estado)
    exibir_menu(OPCOES)
    escolha = input("Sua escolha (1, 2 ou 3): ")
    aplicar_decisao(estado, escolha)
    verificar_limites(estado)
    registrar_historico(historico, escolha, estado)

exibir_historico(historico)
aluno1.pyexemplo
python
# Responsável: Kauê
# Responsabilidade: exibição de status e menu

def exibir_status(estado):
    """Exibe o estado atual do simulador."""
    print("\n=== STATUS ATUAL ===")
    for chave, valor in estado.items():
        print(f"  {chave}: {valor}")

def exibir_menu(opcoes):
    """Exibe as opções disponíveis para o usuário."""
    print("\n=== O QUE VOCÊ DESEJA FAZER? ===")
    for i, opcao in enumerate(opcoes, start=1):
        print(f"  {i}. {opcao}")




from _1Guilherme import  Iniciar 
from _1Guilherme import  decisao1
from _1Guilherme import Comeco
# Simulador: [Simulador de carreira]
# Grupo: Paulo Cézar, Kaue Souza, Guilherme Fonseca
from _1Guilherme import Iniciar, decisao1, chegada

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

# Mostra a transferência para o Palmeiras e atualiza os atributos passados por parâmetro
chegada(atributos) 

# 4. Mostra o placar de atributos finalizado do dia
print(f'\nAtributos atuais do jogador: {atributos}')