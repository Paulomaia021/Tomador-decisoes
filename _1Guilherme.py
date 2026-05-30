# Responsável: Guilherme
# Funções de exibição (decisões)

#Essa função e usada para pegar o nome que o usuário inserir
def Iniciar():
    while True:
        nome = input('Defina o nome do seu jogador: ').strip().title()

        if not nome:
            print('[ERRO] O nome não pode estar vazio!')

        elif not nome.replace(' ', '').isalpha():
            print('[ERRO] O nome deve conter apenas letras!')

        elif len(nome.replace(' ', '')) < 3:
            print('[ERRO] O nome deve ter pelo menos 3 letras!')

        elif len(set(nome.lower().replace(' ', ''))) <= 2:
            print('[ERRO] Digite um nome mais válido!')

        else:
            print(f'Seja muito bem-vindo {nome}.')
            break
    return nome
         


def decisao1(nome, atributos, historico):

    input("Aperte ENTER para continuar...\n")
    
    print(f'{nome} você é um jogador do time de engenheiro coelho e tem os seus atributos que serão muito importantes\n para conseguir ir para a copa ')
    
    input("Aperte ENTER para conhecer seus atributos...\n")
    print("===== SEUS ATRIBUTOS =====")
    for chave, valor in atributos.items():
        print(f"• {chave.capitalize()}: {valor}")
    print("==========================")
    
    input("Aperte ENTER para continuar...\n")

    print('Hoje é mais um dia normal de jogo contra Arthur nogueira, porém o tecnico te deu a opção de não jogar pra ficar\n treinando hoje se quiser')
     
    while True:
        print('\nO que você quer fazer?:\n'
              '1 - Jogar\n'
              '2 - Não jogar, para ir treinar\n'
              '3 - Ver histórico de decisões')
        
        jogou = input('Escolha um número: ')
        
        if jogou == '1':
            print('\nMeus parabéns, o seu time ganhou o jogo e a equipe técnica disse que um olheiro de time grande gostou de você!')
            print('Você ganhou +50 fama e perdeu -25 de energia.')
            atributos["fama"] += 50
            atributos["energia"] -= 25
            input("Aperte ENTER para continuar...\n")

            break  
            
        elif jogou == '2':
            print('\nVocê perdeu uma grande oportunidade...') 
            input('Aperte ENTER para continuar...') 
            print('Você perdeu a chance de ir para a copa. O jogo acabou.')
            exit()
            break

        elif jogou == '3':
          print("\n===== HISTÓRICO DE DECISÕES =====\n")
          if not historico:
              print('Nenhuma decisão foi registrada ainda.')
          else:
            for acao in historico:
             print("-", acao)
      
        else:
            print('\n[ERRO] Opção inválida! Digite apenas 1 ou 2.')
            input('Aperte ENTER para tentar novamente...') 

    return atributos, nome