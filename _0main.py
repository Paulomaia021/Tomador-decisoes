# Simulador: Simulador de carreira
# Grupo: Paulo Cézar, Kaue Souza, Guilherme Fonseca
from _1Guilherme import Iniciar, decisao1
from _2Paulo import escolha_de_time, chegada, mes_2, mes_3
from _3Kaue import mostrar_menu, mostrar_resultado, mostrar_status, mostrar_historico

# 1. Mensagem inicial
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

# LISTA DE HISTÓRICO
historico = []

# 3. Início do jogo
nome = Iniciar()

# 4. Primeira decisão (acontece antes do menu)
decisao1(nome, atributos, historico)
historico.append("Dia 1: Jogou partida contra Arthur Nogueira")
atributos['mes'] += 1

# 5. Escolha de time (acontece antes do menu)
escolha_de_time()
historico.append("Dia 2: Escolheu um time")
atributos['mes'] += 1

# 6. Chegada no time (acontece antes do menu)
jogar_ou_nao = chegada(atributos)
historico.append("Dia 3: Chegou ao novo clube")
atributos['mes'] += 1

# 7. LOOP PRINCIPAL DO MENU
while atributos['mes'] <= 10:
    mostrar_status(atributos)
    mostrar_menu()

    opcao = input("\nEscolha uma opção: ")

    if opcao == '1':
        mes_2(jogar_ou_nao, atributos)
        historico.append(f"Mês {atributos['mes']}: Jogou partida")
        atributos['mes'] += 1

    elif opcao == '2':
        print("\nVocê foi treinar!")
        atributos['habilidade'] += 5
        atributos['energia'] -= 10
        historico.append(f"Mês {atributos['mes']}: Treinou")
        atributos['mes'] += 1

    elif opcao == '3':
        print("\nVocê descansou!")
        atributos['energia'] += 20
        historico.append(f"Mês {atributos['mes']}: Descansou")
        atributos['mes'] += 1

    elif opcao == '4':
        mostrar_historico(historico)  

    else:
        print("\n[ERRO] Opção inválida! Digite 1, 2, 3 ou 4.")

# 8. Fim do jogo
print("\n===== FIM DE CARREIRA =====")
mostrar_status(atributos)
mostrar_historico(historico)
