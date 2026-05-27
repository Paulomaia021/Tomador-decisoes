print('--- SEJA BEM VINDO AO SIMULADOR DE CARREIRA  ---')
print('Você tem exatamete 10 dias pra construir o seu jogador com objetivo de ir pra copa do mundo')

input("\nAperte ENTER para continuar...")
#Essa função e usada para pegar o nome que o usuário inserir
def Iniciar():
    nome = input('Defina o nome do seu jogador: ')
    
    print(f'Seja muito bem-vindo {nome}. Você está começando sua carreira agora e vai precisar tomar decisões para ter sucesso.')
    input("Aperte ENTER para continuar...\n")
    print(f'Olá {nome}. Você é um jogador da base de Engenheiro coelho e esta prestes a começar a sua carreira\n mas antes voce precisa saber dos seus atributos como jopgador.\n 1- Habilidade =50\n 2- Energia = 100\n 3- Fama = 0 ')
    return 

#Aqui aonde começa a primeira decisão feita pelo usuário 
def decisao1():
    input("Aperte ENTER para continuar...\n")

    
    print('Hoje é mais um dia normal de jogo contra Arthur nogueira, porém o tecnico te deu a opção de não jogar pra ficar treinando hoje se quiser')
    print('bem vindo baitola')
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
            
Iniciar()
decisao1()