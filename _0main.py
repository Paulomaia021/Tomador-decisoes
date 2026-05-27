# Simulador: [Simulador de carreira]
# Grupo: Paulo Cézar, Kaue Souza, Guilherme Fonseca
from _1Guilherme import  Iniciar 

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
            