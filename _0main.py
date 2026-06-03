# Simulador: Simulador de carreira
# Grupo: Paulo Cézar, Kaue Souza, Guilherme Fonseca
from colorama import Fore, init
from _2Paulo import escolha_de_time, chegada
from _3Kaue import mostrar_menu, mostrar_resultado, mostrar_status
from _1Guilherme import Iniciar, decisao1

# 1. Mensagem inicial
init()
print('--- SEJA BEM VINDO AO SIMULADOR DE CARREIRA ---')
print('Você tem exatamente 10 meses pra construir o seu jogador com objetivo de ir pra copa do mundo')
input("\nAperte ENTER para continuar...\n")

# 2. Estado do jogo
atributos = {
    'habilidade': 50,
    'energia': 100,
    'fama': 0,
    'mes': 1,
    'reputacao': 50

}

color = {
    'yellow': Fore.YELLOW,
    'blue': Fore.BLUE,
    'green': Fore.GREEN,
    'reset': Fore.RESET,
}

# CLASSE DE HISTÓRICO
class Historico:
    def __init__(self):
        self.decisoes = []
    
    def adicionar(self, acao):
        self.decisoes.append(acao)
    
    def exibir(self):
        if not self.decisoes:
            print("\nNenhuma decisão foi registrada ainda.\n")
        else:
            print("\n===== HISTÓRICO DE DECISÕES =====")
            for i, acao in enumerate(self.decisoes, 1):
                print(f"{i}. {acao}")
            print("==================================\n")

# INSTÂNCIA DE HISTÓRICO
historico = Historico()

# 3. Início do jogo
nome = Iniciar()

# 4. Primeira decisão
decisao1(nome, atributos, historico)

atributos['mes'] += 1

# 5. Escolha de time
escolha_de_time(historico)

atributos['mes'] += 1

# 6. Chegada no time
chegada(atributos, historico)

atributos['mes'] += 1

mostrar_status(atributos)
input('Aperte ENTER para prosseguir...')
mostrar_resultado('Você está pronto para a próxima fase!')
input('Aperte ENTER para prosseguir...')

mostrar_menu()
input('Aperte ENTER para prosseguir...')

# 8. MOSTRAR HISTÓRICO FINAL
historico.exibir()
