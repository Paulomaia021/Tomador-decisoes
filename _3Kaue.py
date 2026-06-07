# Responsável: Kauê
# Funções de exibição (interface)

import os 

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_status(atributos):
    print(f"\n===== STATUS DO JOGADOR =====")
    print(f"Habilidade: {atributos['habilidade']}")
    print(f"Energia: {atributos['energia']}")
    print(f"Fama: {atributos['fama']}")
    print(f"Mês Atual: {atributos['mes']}")
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
        limpar_tela() 
        print("\n===== PRÓXIMA AÇÃO =====")
        print("1 - Voltar ao jogo")
        print("2 - Ver histórico de decisões")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            limpar_tela()
            return
        elif opcao == "2":
            limpar_tela()  
            mostrar_historico(historico)
            input("\nAperte ENTER para voltar ao menu de pausa...")
        else:
            print("Opção inválida!")
            input("Aperte ENTER para tentar novamente...")


def mostrar_tela_convocacao(nome, atributos):
    limpar_tela()  
    print("\n" + "="*50)
    print(f"PARABÉNS, {nome.upper()}!!!")
    print("="*50)
    print("O técnico da Seleção Brasileira acabou de anunciar a lista")
    print("oficial para a Copa do Mundo e o seu nome ESTÁ NELA!")
    print("-"*50)
    print(f"Habilidade Final: {atributos['habilidade']} (Requisito: >= 80)")
    print(f"Energia Final: {atributos['energia']} (Requisito: >= 30)")
    print(f"Fama Final: {atributos['fama']} (Requisito: >= 80)")
    print(f"Reputação com a Torcida: {atributos['reputacao']}")
    print("="*50)
    print("Você realizou o sonho de infância e vai em busca do Hexa!")
    print("="*50 + "\n")


def mostrar_tela_eliminacao(nome, atributos):
    limpar_tela()  
    print("\n" + "="*50)
    print(f"FALTOU POUCO, {nome.upper()}...")
    print("="*50)
    print("A lista da Copa do Mundo foi divulgada, mas você não foi chamado.")
    print("Você não conseguiu atingir as metas de convocação da comissão técnica:")
    print("-"*50)
    print(f"• Habilidade: {atributos['habilidade']}/80")
    print(f"• Energia: {atributos['energia']}/30")
    print(f"• Fama: {atributos['fama']}/80")
    print("-"*50)
    print("Continue treinando firme no Palmeiras para o próximo ciclo!")
    print("="*50 + "\n")

