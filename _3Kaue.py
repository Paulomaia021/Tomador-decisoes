# Responsável: Kauê
# Funções de exibição (interface)
# init[autoreset]=True
# from colorama import Fore, Style 
# print(Back.Yellow+ "Funções de exibição carregadas com sucesso!" + Style.RESET_ALL)

def mostrar_status(atributos):
    print("\n===== STATUS DO JOGADOR =====")
    print(f"Habilidade: {atributos['habilidade']}")
    print(f"Energia: {atributos['energia']}")
    print(f"Fama: {atributos['fama']}")
    print(f"Dia: {atributos['dia']}")
    print(f"Reputação: {atributos['reputacao']}")
    print("=============================")


def mostrar_menu():
    print("\n===== O QUE VOCÊ QUER FAZER? =====")
    print("1 - Jogar partida")
    print("2 - Treinar")
    print("3 - Descansar")
    print("==================================")


def mostrar_resultado(texto):
    print("\n===== RESULTADO =====")
    print(texto)
    print("=====================")