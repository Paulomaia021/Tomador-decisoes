import sys
import _1Guilherme as guilherme
import _2Paulo as paulo
import _3Kaue as kaue
import os 

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")
    
def executar_jogo():
    # Inicializando as variáveis do sistema com todas as chaves necessárias
    atributos = {
        "habilidade": 30, 
        "energia": 100, 
        "fama": 0, 
        "mes": 1, 
        "reputacao": 0
    }
    historico = []

    # 1. Guilherme valida o nome do jogador
    nome = guilherme.Iniciar()
    
    # 2. Guilherme roda os meses 1 e 2 (Engenheiro Coelho)
    escolha_f1 = guilherme.decisao_mes1_2(nome, atributos, historico)
    
    if escolha_f1 == '2':
        kaue.mostrar_resultado("Você perdeu uma grande oportunidade...\nVocê perdeu a chance de ir para a copa. O jogo acabou.")
        sys.exit()
        
    # Aplica os pontos da escolha 1 (Jogar)
    atributos["fama"] += 50
    atributos["energia"] -= 25
    atributos["reputacao"] += 10
    historico.append("Mês 1: Decidiu jogar contra Arthur Nogueira e atraiu olheiro.")

    # Menu de pausa do Kauê para o jogador decidir quando avançar
    kaue.pausar(historico)

    # 3. Transferência para a linha do tempo do Paulo (Palmeiras)
    paulo.escolha_de_time()
    jogar_ou_nao = paulo.chegada(atributos)
    
    kaue.pausar(historico)
    
    paulo.mes_2(jogar_ou_nao, atributos)
    
    kaue.pausar(historico)
    
    paulo.mes_3(atributos, historico)
    
    kaue.pausar(historico)
    
    paulo.mes_4_e_5(atributos, historico)
    
    kaue.pausar(historico)
    
    paulo.mes_6_e_7(atributos, historico)
    
    kaue.pausar(historico)
    
    paulo.mes_8_e_9(atributos, historico)
    
    kaue.pausar(historico)
    
    # 4. Decisão final do Mês 10 e verificação dos atributos pelo Paulo
    foi_convocado = paulo.mes_10(atributos, historico)

    # 5. Kauê assume a tela final baseada no resultado da convocação
    if foi_convocado:
        kaue.mostrar_tela_convocacao(nome, atributos)
    else:
        kaue.mostrar_tela_eliminacao(nome, atributos)

if __name__ == '__main__':
    executar_jogo()