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
            print('Lamentamos, mas desejamos sucesso...')
            break
        else:
            print('[ERRO] insira somente os números 1 ou 2')

def chegada(atributos):
    input('Aperte ENTER para tentar novamente...') 
    
    print('Você chegou no palmeiras e ja foi convocado para jogar um jogo')
    print('Você ganhou mais 15+ habilidade, 30+ fama, 20- energia')
    atributos["habilidade"] += 15
    atributos["fama"] += 30
    atributos["energia"] -= 20
    input("\nAperte ENTER para continuar...") 