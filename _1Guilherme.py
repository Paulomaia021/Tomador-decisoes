#Essa função e usada para pegar o nome que o usuário inserir
def Iniciar():
    while True:
        nome = input('Defina o nome do seu jogador: ').strip()
        
        if not nome:
            print('[ERRO] O nome não pode estar vazio! Tente novamente.')
        elif not nome.replace(' ', '').isalpha():
            print('[ERRO] O nome deve conter apenas letras! Tente novamente.')
        else:
            break
    
    print(f'Seja muito bem-vindo {nome}. Você está começando sua carreira agora e vai precisar tomar decisões para ter sucesso.')

#Aqui aonde começa a primeira decisão feita pelo usuário 
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

        print('Hoje é mais um dia normal de jogo contra Arthur nogueira, porém o tecnico te deu a opção de não jogar pra ficar treinando hoje se quiser')

def chegada(atributos):
    print('Você chegou no palmeiras e ja foi convocado para jogar um jogo')
    print('Você ganhou mais 15+ habilidade, 30+ fama, 20- energia')
    atributos["habilidade"] += 15
    atributos["fama"] += 30
    atributos["energia"] -= 20
input("\nAperte ENTER para continuar...")

Iniciar()
decisao1()
chegada()
