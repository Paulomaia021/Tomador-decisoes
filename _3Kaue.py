# Responsável: Kauê
# Funções de exibição (interface)

def mostrar_status(atributos):
    print(f"\n===== STATUS DO JOGADOR =====")
    print(f"Habilidade: {atributos['habilidade']}")
    print(f"Energia: {atributos['energia']}")
    print(f"Fama: {atributos['fama']}")
    print(f"Dia: {atributos['mes']}")
    print(f"Reputação: {atributos['reputacao']}")
    print("=============================")


def mostrar_menu():
    print("\n===== O QUE VOCÊ QUER FAZER? =====")
    print("1 - Jogar partida")
    print("2 - Treinar")
    print("3 - Descansar")
    print("4 - Ver histórico")
    print("==================================")


def mostrar_resultado(texto):
    print("\n===== RESULTADO =====")
    print(texto)
    print("=====================")


def mostrar_historico(historico):
    print("\n====== HISTÓRICO DE DECISÕES ======")
    if not historico:
        print('Nenhuma ação registrada ainda.')
    else:
        for i, acao in enumerate(historico, 1):
            print(f"{i}. {acao}")
    print("===================================")


def pausar(historico):
    while True:
        print("\n===== PRÓXIMA AÇÃO =====")
        print("1 - Voltar ao jogo")
        print("2 - Ver histórico de decisões")

        opcao = input("Escolha: ")

        if opcao == "1":
            return

        elif opcao == "2":
            mostrar_historico(historico)

        else:
            print("Opção inválida!")