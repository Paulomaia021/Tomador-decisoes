# Responsável: Paulo
# Funções de ?
def escolha_de_time(historico):
    """Função que oferece a proposta para ir ao Palmeiras"""
    print('Você recebeu uma proposta de ir para o Palmeiras, você aceita? \n 1 - Aceito\n 2- Não aceito' )
    while True:
        proposta = int(input('Informe o numero: '))

        if proposta == 1:
            print('Meus parabéns, seja muito bem vindo ao Palmeiras ')
            historico.adicionar("Aceitou proposta do Palmeiras")
            break
        elif proposta == 2:
            print('Você tem certeza? Você sabe que no Palmeiras é um time grande.. estamos em época de copa, vc n qr ir?')
            print('Vou perguntar mais uma vez. Você aceita vir pro Palmeiras?')

            print('1 - aceito\n 2 - Não aceito')
            decisao2 = input('Informe o número: ')
            if decisao2 == '1':
                print('Meus parabéns, Você tomou a decisão certa ')
                historico.adicionar("Aceitou Palmeiras após reconsideração")
            elif decisao2 == '2':
                print('Tudo bem, ficamos triste mas entendemos o seu lado...')
                print('--- MENSAGEM DO SISTEMA---')
                print('Você perdeu')
                historico.adicionar("Recusou proposta do Palmeiras - Perdeu o jogo")
                exit()
        else:
            print('[ERRO] insira somente os números 1 ou 2')
            input('Aperte ENTER para tentar novamente...')


def chegada(atributos, historico):
    """Função que define a decisão de jogar ou descansar na chegada ao Palmeiras"""
    input('Aperte ENTER para continuar...') 
    while True:
        print('Você chegou no palmeiras e vai haver um jogo, mas\ncomo vc chegou a agora tem a opção de descansar, oq vc quer fazer?')
        print('1 - Jogar\n'\
              '2 - Descansar')
        jogar_ou_nao = input('Informe o numero:')
        print('')
        if jogar_ou_nao == '1':        
            print('Você ganhou mais 15+ habilidade, 30+ fama, 20- energia')
            atributos["habilidade"] += 15
            atributos["fama"] += 30
            atributos["energia"] -= 20
            historico.adicionar("Jogou na chegada ao Palmeiras - Ganhou +15 habilidade, +30 fama, -20 energia")
            input("\nAperte ENTER para continuar...") 
            break
        elif jogar_ou_nao == '2':
            print('Você ganhou + 10 de energia')
            atributos["energia"] += 10
            historico.adicionar("Descansou na chegada ao Palmeiras - Ganhou +10 energia")
            input("\nAperte ENTER para continuar...")
            break
        else:
            print('Informe somente o número 1 ou 2')
            input('Aperte ENTER para tentar novamente...')

