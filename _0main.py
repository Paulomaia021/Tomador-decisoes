# Simulador: [Simulador de carreira]
# Grupo: Paulo Cézar, Kaue Souza, Guilherme Fonseca
from _1Guilherme import Iniciar, decisao1,chegada

print('--- SEJA BEM VINDO AO SIMULADOR DE CARREIRA  ---')
print('Você tem exatamete 10 dias pra construir o seu jogador com objetivo de ir pra copa do mundo')
input("\nAperte ENTER para continuar...")

atributos = {
    'habilidade': 50,
    'energia': 100,
    'fama': 0,
    'dia': 1,
    'reputacao': 50
}



def ciclo():
    while True:
        print('\nO que você quer fazer?:\n'
              '1 - Jogar\n'
              '2 - Não jogar, para ir treinar')
        
        jogou = input('Escolha um número: ')
        
        if jogou == '1':
            print('\nMeus parabéns, o seu time ganhou o jogo e a equipe técnica disse que um olheiro de time grande gostou de você!')
            print('Você ganhou +50 fama e perdeu -25 de energia.')
            atributos['energia'] -= 25
            atributos['fama'] += 50
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
    chegada(atributos)
    print(f'\nAtributos atuais: {atributos}')