print('--- SEJA BEM VINDO AO SIMULADOR DE DECISÕES ---')

input("Aperte ENTER para continuar...")

def Iniciar():
    nome = input('Defina o nome do seu jogador: ')
    
    print(f'Seja muito bem-vindo {nome}. Você está começando sua carreira agora e vai precisar tomar decisões para ter sucesso.')
    return nome

def Comeco(nome):
    print(f'Olá {nome}. Você é um jogador da base do flamengo e esta prestes a começar a sua carreira\n mas antes voce precisa saber dos seus atributos como jopgador.\n 1- Habilidade =50\n 2- Dinheiro = 1000\n 3- Energia = 100\n 4- Fama = 0\n 5- idade =  17 ')


jogador = Iniciar()
Comeco(jogador)