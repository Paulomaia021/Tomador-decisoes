# Responsável: Paulo
# Funções de: Lógica do Jogo, Atualização de Atributos e Linha do Tempo
import os
import sys

def mostrar_historico_local(historico):
    #Função de contingência para exibir o histórico dentro do fluxo do Paulo.
    print("\n===== HISTÓRICO DE DECISÕES =====")
    if not historico:
        print('Nenhuma decisão foi registrada ainda.')
    else:
        for acao in historico:
            print(f"- {acao}")
    print("==================================")
    input("Aperte ENTER para continuar...")

def verificar_limites_energia(atributos):
    #Garante que a energia não passe de 100 e não fique negativa
    if atributos["energia"] > 100:
        atributos["energia"] = 100
    if atributos["energia"] < 0:
        atributos["energia"] = 0

def escolha_de_time():
    print('Você recebeu uma proposta de ir para o Palmeiras, você aceita? \n 1 - Aceito\n 2- Não aceito' )
    while True:
        proposta = input('Informe o numero: ').strip()

        if proposta == '1':
            print('Meus parabéns, seja muito bem vindo ao Palmeiras ')
            break
        elif proposta == '2':
            print('Você tem certeza? Você sabe que o Palmeiras é um time grande.. estamos em época de copa, você não quer ir?')
            print('Vou perguntar mais uma vez. Você aceita vir pro Palmeiras?')
            print('1 - aceito\n 2 - Não aceito')
            decisao2 = input('Informe o número: ').strip()
            if decisao2 == '1':
                print('Meus parabéns, Você tomou a decisão certa ') 
                break
            elif decisao2 == '2':
                print('Tudo bem, ficamos triste mas entendemos o seu lado...')
                print('--- MENSAGEM DO SISTEMA---')
                print('Você perdeu')
                sys.exit()
            else:
                print('[ERRO] insira somente os números 1 ou 2')
                input('Aperte ENTER para tentar novamente...')

def chegada(atributos):
    input('Aperte ENTER para continuar...') 
    while True:
        print('Você chegou no palmeiras e vai haver um jogo, mas\ncomo você chegou agora tem a opção de descansar, oque você quer fazer?')
        print('1 - Jogar\n2 - Descansar')
        jogar_ou_nao = input('Informe o numero:').strip()
        print('')
        if jogar_ou_nao == '1':        
            print('Você ganhou mais 15+ habilidade, 30+ fama, 20- energia')
            atributos["habilidade"] += 15
            atributos["fama"] += 30
            atributos["energia"] -= 20
            verificar_limites_energia(atributos)
            input("\nAperte ENTER para continuar...") 
            break
        elif jogar_ou_nao == '2':
            print('Você ganhou + 10 de energia')
            atributos['energia'] += 10
            verificar_limites_energia(atributos)
            break
        else:
            print('Informe somente o número 1 ou 2')
            input('Aperte ENTER para tentar novamente...')
    return jogar_ou_nao

def mes_2(jogar_ou_nao, atributos):
    print('==================================')
    print('Mês 2')
    input('Aperte ENTER pra continuar...')
    if jogar_ou_nao == '2':
        print('Vai haver uma final do Paulistão contra o Corinthians')
        print('Você não se sente corajoso para esse jogo e pensa em pedir para não jogar ')
        print('Oque você vai fazer?')
        while True:
            print('1 -Jogar\n2 - Não jogar')
            medroso = input('Vai jogar ou não? ').strip()
            if medroso == '1':
                print('Você entra no jogo aos 80 minutos e faz o gol do titulo!!!')
                atributos['habilidade'] += 5
                atributos['fama'] += 20
                atributos['energia'] -= 10
                verificar_limites_energia(atributos)
                break
            elif medroso == '2':
                print('O treinador recusou seu pedido, você vai jogar')  
                break
            else:
                print('Informe somente 1 ou 2')
                input('Aperte ENTER para continuar...')

    print('Você entra no jogo aos 80 minutos e faz o gol do titulo')
    atributos['habilidade'] += 5
    atributos['fama'] += 20
    atributos['energia'] -= 10
    verificar_limites_energia(atributos)

def mes_3(atributos, historico):
    print('==================================')
    print('Mês 3')
    while True:
        print('\nÉ mais um mês normal, você está treinando e focado em se destacar.')
        print('O que você quer fazer hoje?')
        print('1 - Treinar')
        print('2 - Descansar')
        print('3 - Mostrar histórico')

        a = input('Informe o número: ').strip()

        if a == '1':
            print('Você ganhou +5 Habilidade e perdeu -5 Energia')
            atributos['habilidade'] += 5
            atributos['energia'] -= 5
            verificar_limites_energia(atributos)
            historico.append('Mês 3: Treinou pesado no dia a dia.')
            break
        elif a == '2':
            print('Você ganhou +20 de energia')
            atributos['energia'] += 20
            verificar_limites_energia(atributos)
            historico.append('Mês 3: Optou por descansar.')
            break
        elif a == '3':
            mostrar_historico_local(historico)
        else:
            print('Informe apenas 1, 2 ou 3.')

def mes_4_e_5(atributos, historico):
    print('==================================')
    print('Mês 4 e Mês 5: Quartas de Final da Libertadores')
    input('Aperte ENTER para continuar...')
    print('O Palmeiras perdeu o jogo de ida contra a LDU na altitude por 1x0.')
    print('O jogo de volta no Allianz Parque exige sua melhor preparação. O que você fará?')
    
    while True:
        print('1 - Focar em treinos táticos intensos\n'
              '2 - Focar em fisioterapia e poupar o físico\n'
              '3 - Mostrar histórico')
        
        escolha = input('Informe o número: ').strip()
        if escolha == '1':
            print('\nVocê deu duas assistências e o Palmeiras venceu por 2x0!')
            atributos['habilidade'] += 15
            atributos['energia'] -= 15
            atributos['fama'] += 15
            verificar_limites_energia(atributos)
            historico.append('Mês 4-5: Treinou pesado e garantiu a vaga contra a LDU.')
            break
        elif escolha == '2':
            print('\nVocê entrou no segundo tempo e fez o gol da classificação!')
            atributos['energia'] += 25
            atributos['fama'] += 15
            verificar_limites_energia(atributos)
            historico.append('Mês 4-5: Descansou e foi decisivo vindo do banco contra a LDU.')
            break
        elif escolha == '3':
            mostrar_historico_local(historico)
        else:
            print('Informe apenas 1, 2 ou 3.')

def mes_6_e_7(atributos, historico):
    print('==================================')
    print('Mês 6 e Mês 7:')
    input('Aperte ENTER para continuar...')
    print('Você descobriu que olheiros da Seleção estarão na semifinal da Libertadores.')
    print('Porém, seu joelho esquerdo está estalando e apresentando dores.')
    
    while True:
        print('O que você decide fazer?:\n'
              '1 - Dobrar a carga de treinos para chocar os olheiros (Risco de Lesão Extrema)\n'
              '2 - Tratar a dor com o Departamento Médico\n'
              '3 - Mostrar histórico')
        
        escolha = input('Informe o número: ').strip()
        if escolha == '1':
            print('\nDurante um pique no treino, seu Ligamento Cruzado Anterior (LCA) se rompeu por completo!')
            print('Você terá que operar o joelho e perdeu totalmente a chance de ir para a Copa.')
            sys.exit()
        elif escolha == '2':
            print('\nO DM tratou sua dor, estabilizou seu joelho e você está pronto para jogar seguro.')
            atributos['energia'] += 15
            atributos['habilidade'] += 5
            verificar_limites_energia(atributos)
            historico.append('Mês 6-7: Decidiu tratar o joelho no DM e evitou uma lesão de LCA.')
            break
        elif escolha == '3':
            mostrar_historico_local(historico)
        else:
            print('Informe apenas 1, 2 ou 3.')

def mes_8_e_9(atributos, historico):
    print('==================================')
    print('Mês 8 e Mês 9: Semifinal contra o River Plate')
    input('Aperte ENTER para continuar...')
    print('Noite épica de Libertadores no Allianz Parque! Semifinal pegada contra o River Plate.')
    print('O jogo está empatado e a pressão da torcida é gigantesca. Qual será sua postura?')
    
    while True:
        print('1 - Chamar a responsabilidade nas jogadas individuais \n'
              '2 - Jogar coletivamente priorizando passes seguros \n'
              '3 - Mostrar histórico')
        
        escolha = input('Informe o número: ').strip()
        if escolha == '1':
            print('\nVocê da uma caneta no zagueiro e faz um golaço! Vaga na final garantida!')
            atributos['fama'] += 20
            atributos['habilidade'] += 10
            atributos['energia'] -= 20
            verificar_limites_energia(atributos)
            historico.append('Mês 8-9: Brilhou individualmente contra o River Plate.')
            break
        elif escolha == '2':
            print('\nMuito inteligente! Você controlou o meio de campo e deu o passe pro gol que carimbou a vaga na Final!')
            atributos['habilidade'] += 10
            atributos['energia'] -= 10
            verificar_limites_energia(atributos)
            historico.append('Mês 8-9: Atuação coletiva segura contra o River Plate.')
            break
        elif escolha == '3':
            mostrar_historico_local(historico)
        else:
            print('Informe apenas 1, 2 ou 3.')

def mes_10(atributos, historico):
    print('==================================')
    print('Mês 10: A Grande Final e o Veredicto da Seleção')
    input('Aperte ENTER para ver a decisão final...')
    print('Chegou o momento da grande Final da Libertadores contra o Flamengo no Maracanã!')
    print('Você joga a vida e corre até a exaustão. Placar Final: Palmeiras Campeão da América!')
    
    # Impacto físico do jogo do título
    atributos['habilidade'] += 10
    atributos['fama'] += 30
    atributos['energia'] -= 20
    verificar_limites_energia(atributos)
    
    print("\n==============================================")
    print("      VEREDICTO FINAL DA CONVOCAÇÃO")
    print("==============================================")
    print(f"SEUS ATRIBUTOS FINAIS:")
    print(f"• Habilidade: {atributos['habilidade']} (Mínimo exigido: 80)")
    print(f"• Energia: {atributos['energia']} (Mínimo exigido: 30)")
    print(f"• Fama: {atributos['fama']} (Mínimo exigido: 80)")
    print("==============================================")
    
    if atributos['habilidade'] >= 80 and atributos['energia'] >= 30 and atributos['fama'] >= 80:
        return True
    else:
        return False