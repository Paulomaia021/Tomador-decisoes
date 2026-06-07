# Responsável: Paulo
# Funções de ?
from _3Kaue import mostrar_historico


def escolha_de_time():
    print('Você recebeu uma proposta de ir para o Palmeiras, você aceita? \n 1 - Aceito\n 2- Não aceito' )
    while True:
        proposta = input('Informe o numero: ')

        if proposta == '1':
                  print('Meus parabéns, seja muito bem vindo ao Palmeiras ')
                  break
        elif proposta == '2':
                 print('Você tem certeza? Você sabe que no Palmeiras é um time grande.. estamos em época de copa, vc n qr ir?')
                 print('Vou perguntar mais uma vez. Você aceita vir pro Palmeiras?')
                 print('1 - aceito\n '' 2 - Não aceito')
                 decisao2 = input('Informe o número: ')
                 if decisao2 == '1':
                    print('Meus parabéns, Você tomou a decisão certa ') 
                    break
                 elif decisao2 == '2':
                    print('Tudo bem, ficamos triste mas entendemos o seu lado...')
                    print('--- MENSAGEM DO SISTEMA---')
                    print('Você perdeu')
                    exit()
                    break
                 else:
                    print('[ERRO] insira somente os números 1 ou 2')
                    input('Aperte ENTER para tentar novamente...')


def chegada(atributos):
    input('Aperte ENTER para continuar...') 
    while True:
        print('Você chegou no palmeiras e vai haver um jogo, mas\ncomo vc chegou agora tem a opção de descansar, oque você quer fazer?')
        print('1 - Jogar\n'\
              '2 - Descansar')
        jogar_ou_nao = input('Informe o numero:')
        print('')
        if jogar_ou_nao == '1':        
            print('Você ganhou mais 15+ habilidade, 30+ fama, 20- energia')
            atributos["habilidade"] += 15
            atributos["fama"] += 30
            atributos["energia"] -= 20
            input("\nAperte ENTER para continuar...") 
            break
        elif jogar_ou_nao == '2':
            print('Você ganhou + 10 de energia')
            atributos['energia'] += 10
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
         print('1 -Jogar\n'
               '2 - Não jogar')
         medroso = input('Vai jogar ou não? ')
         if medroso == '1':
            print('Você entra no jogo aos 80 minutos e faz o gol do titulo')
            atributos['habilidade'] += 5
            atributos['fama'] += 20
            atributos['energia'] -= 10
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


#def mes_3(atributos):
#    print('Mês 3')
#    atributos['mes'] +=1
#
#    print('É mais um mês normal, você esta treinando, focado em ser o melhor e se destacar')
#    print('Oque você quer fazer hoje?\n'
#          '1 - Treinar'
#          '2 - Descansar'
#          '3 - Mostrar histórico')
#    a = input('Informe o número: ')
#
#    while True:
#        if a == '1':
#            print('Você ganhou +5 Habilidade +0 de fama -5 Energia ')
#            atributos['habilidade'] += 5
#            atributos['energia'] -= 5
#            
#        elif a == '2':
#            print('Você ganhou + 20 de energia')
#            atributos['energia'] +=20
#
#        elif a == '3':
#            mostrar_historico(historico)
#        else:
#            print('Informe um número entre 1, 2 ou 3')
#            input('Aperte ENTER para continuar...')

def mes_3(atributos, historico):
    print('Mês 3')

    while True:
        print('\nÉ mais um mês normal, você está treinando e focado em se destacar.')
        print('O que você quer fazer hoje?')
        print('1 - Treinar')
        print('2 - Descansar')
        print('3 - Mostrar histórico')

        a = input('Informe o número: ')

        if a == '1':
            print('Você ganhou +5 Habilidade e perdeu -5 Energia')
            atributos['habilidade'] += 5
            atributos['energia'] -= 5
            historico.append('Mês 3: Treinou')
            break

        elif a == '2':
            print('Você ganhou +20 de energia')
            atributos['energia'] += 20
            historico.append('Mês 3: Descansou')
            break

        elif a == '3':
            mostrar_historico(historico)

        else:
            print('Informe apenas 1, 2 ou 3.')



def dia_4(atributos):
    print('Mês 4')


    