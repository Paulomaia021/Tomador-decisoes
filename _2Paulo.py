# Responsável: Paulo
# Funções de ?
def escolha_de_time():
    print('Você recebeu uma proposta de ir para o Palmeiras, você aceita? \n 1 - Aceito\n 2- Não aceito' )
    while True:
        proposta = int(input('Informe o numero: '))

        if proposta == 1:
            print('Meus parabéns, seja muito bem vindo ao Palmeiras ')
            break
        elif proposta == 2:
            print('Você tem certeza? Você sabe que no Palmeiras é um time grande.. estamos em época de copa, vc n qr ir?')
            print('Vou perguntar mais uma vez. Você aceita vir pro Palmeiras?')

            print('1 - aceito\n '' 2 - Não aceito')
            decisao2 = input('Informe o número: ')
            if decisao2 == '1':
             print('Meus parabéns, Você tomou a decisão certa ')
            elif decisao2 == '2':
                print('Tudo bem, ficamos triste mas entendemos o seu lado...')
                print('--- MENSAGEM DO SISTEMA---')
                print('Você perdeu')
                exit()
        else:
            print('[ERRO] insira somente os números 1 ou 2')
            input('Aperte ENTER para tentar novamente...')


def chegada(atributos):
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
            input("\nAperte ENTER para continuar...") 
            break
        elif jogar_ou_nao == '2':
            print('Você ganhou + 10 de energia')
            break
        else:
            print('Informe somente o número 1 ou 2')
            input('Aperte ENTER para tentar novamente...')
    return jogar_ou_nao

def dia_2(jogar_ou_nao, atributos):
    print('Mês 2')
    atributos['mes'] +=1
    input('Aperte ENTER pra continuar...')
    if jogar_ou_nao == 2:
     print('Vai Haver uma final do Paulistão contra o Corinthians')
     print('Você não se sente corajoso p esse jogo e pensa em pedir p n jogar ')
     print('Oq vc vai fazer?')
     while True:
         print('1 -Jogar\n'
               '2 - Não jogar')
         medroso = input('Vai jogar ou não? ')
         if medroso == '1':
            break
         elif medroso == '2':
             print('O treinador recusou seu pedido, vc vai jogar')  
             break
         else:
            print('Informe somente 1 ou 2')
            input('Aperte ENTER para continuar...')

     print('Você entra no jogo aos 80 minutos e faz o gol do titulo')
     atributos['habilidade'] += 5
     atributos['fama'] =+ 2
     atributos['energia'] -= 10
     
         
