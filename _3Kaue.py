# Responsável: Kauê
# Funções de exibição (interface)
from colorama import Fore, init, Style 

init()

def mostrar_status(atributos):
    """Função para exibir o status atual do jogador"""
    print(f"{Fore.GREEN}===== STATUS DO JOGADOR =====")
    print(f"Habilidade: {atributos['habilidade']}")
    print(f"Energia: {atributos['energia']}")
    print(f"Fama: {atributos['fama']}")
    print(f"Dia: {atributos['mes']}")
    print(f"Reputação: {atributos['reputacao']}")
    print(f"============================={Fore.RESET}")


def mostrar_menu():
    """Função para exibir menu de opções"""
    print("\n===== O QUE VOCÊ QUER FAZER? =====")
    print("1 - Jogar partida")
    print("2 - Treinar")
    print("3 - Descansar")
    print("==================================")


def mostrar_resultado(texto):
    """Função para exibir resultado de uma ação"""
    print("\n===== RESULTADO =====")
    print(texto)
    print("=====================")