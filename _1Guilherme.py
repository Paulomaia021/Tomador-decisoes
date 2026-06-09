# Responsável: Guilherme
# Funções de exibição (decisões)

import os 

def limpar_tela():
    # Executa o comando de limpar a tela de acordo com o sistema operacional
    os.system("cls" if os.name == "nt" else "clear")

def Iniciar():
    limpar_tela()
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
            limpar_tela()
            print(f'Seja muito bem-vindo {nome}.\n')
            break
    return nome


def exibir_atributos_e_historico(atributos, historico):
    limpar_tela()
    print("\n===== SEUS ATRIBUTOS ATUAIS =====")
    for chave, valor in atributos.items():
        print(f"• {chave.capitalize()}: {valor}")
    print("==================================")
    print("REQUISITOS PARA A CONVOCAÇÃO (COPA 2026):")
    print("• Habilidade: mínimo 80 | • Energia: mínimo 30 | • Fama: mínimo 80")
    print("==================================")
    
    print("\n===== HISTÓRICO DE DECISÕES =====")
    if not historico:
        print('Nenhuma decisão foi registrada ainda.')
    else:
        for acao in historico:
            print("-", acao)
    print("==================================")
    input("\nAperte ENTER para retornar ao jogo...")
    limpar_tela()


def decisao_mes1_2(nome, atributos, historico):
    input("Aperte ENTER para continuar...\n")
    limpar_tela()
    print(f'{nome} você é um jogador do time de Engenheiro Coelho e tem os seus atributos que serão muito importantes\n para alcançar seu objetivo')
    
    input("Aperte ENTER para conhecer seus atributos...\n")
    limpar_tela()
    print("===== SEUS ATRIBUTOS =====")
    for chave, valor in atributos.items():
        print(f"• {chave.capitalize()}: {valor}")
    print("==========================")
    
    input("Aperte ENTER para continuar...\n")
    limpar_tela()
    print('Hoje você tem um jogo contra o time de Arthur Nogueira, porém, o tecnico te deu a opção de não jogar pra ficar\n treinando hoje')
     
    while True:
        print('\nO que você quer fazer?:')
        print('1 - Jogar')
        print('2 - Não jogar, para ir treinar')
        print('3 - Ver histórico de decisões')
        
        jogou = input('Escolha um número: ')
        
        if jogou in ['1', '2']:
            limpar_tela()
            return jogou
        elif jogou == '3':
            exibir_atributos_e_historico(atributos, historico)
        else:
            print('\n[ERRO] Opção inválida! Digite apenas 1 ou 2.')
            input('Aperte ENTER para tentar novamente...')
            limpar_tela()