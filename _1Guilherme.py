print('--- SEJA BEM VINDO AO SIMULADOR DE DECISÕES ---')

input("Aperte ENTER para continuar...")

def Iniciar():
    nome = input('Defina o nome do seu jogador: ')
    
    print(f'Seja muito bem-vindo {nome}. Você está começando sua carreira agora e vai precisar tomar decisões para ter sucesso.')
    input("Aperte ENTER para continuar...")
    return nome

def Comeco(nome):
    print(f'Olá {nome}. Você é um jogador da base do flamengo e esta prestes a começar a sua carreira\n mas antes voce precisa saber dos seus atributos como jopgador.\n 1- Habilidade =50\n 2- Dinheiro = 1000\n 3- Energia = 100\n 4- Fama = 0\n 5- idade =  17 ')

def decisao1():

    print('Você recebeu 3 propostas diferentes pra jogar no futebol profissional\n' 
      'Porém é em 3 estados diferentes. ')
    print('Escolha aonde quer ir:\n'
          '1- Bahia\n'
          '2- Rio de Janeiro\n'
          '3- São Paulo\n')
    estado = input('Informe o número do estado: ')
    if estado == 1:
        print('Meus parabens por decidido ir para o Bahia,\n agora você tem mais uma supresa escolher entre 3 times pra atuar.')      

jogador = Iniciar()
Comeco(jogador)
decisao1()