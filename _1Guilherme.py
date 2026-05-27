print('--- SEJA BEM VINDO AO SIMULADOR DE CARREIRA ---')

input("Aperte ENTER para continuar...")

def Iniciar():
    nome = input('Defina o nome do seu jogador: ')
    
    print(f'Seja muito bem-vindo {nome}. Você está começando sua carreira agora e vai precisar tomar decisões para ter sucesso.')
    input("Aperte ENTER para continuar...\n")
    print('')
    return nome

def Comeco(nome):
    print(f'Olá {nome}. Você é um jogador da base de Engenheiro coelho e esta prestes a começar a sua carreira\n mas antes voce precisa saber dos seus atributos como jopgador.\n 1- Habilidade =50\n 2- Energia = 100\n 3- Fama = 0 ')

def decisao1():
    input("Aperte ENTER para continuar...\n")
    
    print('Hoje é mais um dia normal de jogo contra Arthur nogueira, porém o tecnico te deu a opção de não jogar pra ficar treinando hoje se quiser')
     
    while True:
        print('\nO que você quer fazer?:\n'
              '1 - Jogar\n'
              '2 - Não jogar, para ir treinar')
        
        jogou = input('Escolha um número: ')
        
        if jogou == '1':
            print('\nMeus parabéns, o seu time ganhou o jogo e a equipe técnica disse que um olheiro de time grande gostou de você!')
            print('Você ganhou +50 fama e perdeu -25 de energia.')
            break  
            
        elif jogou == '2':
            print('\nVocê perdeu uma grande oportunidade...') 
            input('Aperte ENTER para continuar...') 
            print('Você perdeu a chance de ir para a copa. O jogo acabou.')
            break
            
        else:
           
            print('\n[ERRO] Opção inválida! Digite apenas 1 ou 2.')
            input('Aperte ENTER para tentar novamente...') 
            print('Seja bem vindo')
jogador = Iniciar()
Comeco(jogador)
decisao1()