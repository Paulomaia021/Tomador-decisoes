# Responsável: Kauê
# Funções de exibição (interface)

import os 
from pygame import mixer

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_status(atributos):
    print(f"\n===== STATUS DO JOGADOR =====")
    print(f"Habilidade: {atributos['habilidade']}")
    print(f"Energia: {atributos['energia']}")
    print(f"Fama: {atributos['fama']}")
    print(f"Mês Atual: {atributos['mes']}")
    print(f"Reputação: {atributos['reputacao']}")
    print("=============================")


def mostrar_menu():
    print("\n===== O QUE VOCÊ QUER FAZER? =====")
    print("1 - Jogar partida")
    print("2 - Treinar")
    print("3 - Descansar")
    print("4 - Ver histórico")
    print("==================================")


def mostrar_resultado(texto):
    print("\n===== RESULTADO =====")
    print(texto)
    print("=====================")


def mostrar_historico(historico):
    print("\n====== HISTÓRICO DE DECISÕES ======")
    if not historico:
        print('Nenhuma ação registrada ainda.')
    else:
        for i, acao in enumerate(historico, 1):
            print(f"{i}. {acao}")
    print("===================================")


def pausar(historico):
    while True:
        limpar_tela() 
        print("\n===== PRÓXIMA AÇÃO =====")
        print("1 - Voltar ao jogo")
        print("2 - Ver histórico de decisões")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            limpar_tela()
            return
        elif opcao == "2":
            limpar_tela()  
            mostrar_historico(historico)
            input("\nAperte ENTER para voltar ao menu de pausa...")
        else:
            print("Opção inválida!")
            input("Aperte ENTER para tentar novamente...")


import os
import time
from pygame import mixer

def mostrar_tela_convocacao(nome, atributos):
    limpar_tela()  

    # 1. Configuração do tempo em segundos
    tempo_inicio = 444  # 7:24
    tempo_fim = 451     # 7:31
    duracao_trecho = tempo_fim - tempo_inicio # 7 segundos de áudio

    # 2. Inicializa o mixer de áudio e carrega o arquivo
    mixer.init()
    mixer.music.load('audio.mp3')

    # 3. Toca o áudio a primeira vez a partir de 7:24
    mixer.music.play(start=tempo_inicio)
    marcador_tempo = time.time() # Guarda o momento exato em que começou

    # 4. Exibe o texto da convocação na tela
    print("\n" + "="*50)
    print(f"PARABÉNS, {nome.upper()}!!!")
    print("="*50)
    print("O técnico da Seleção Brasileira acabou de anunciar a lista")
    print("oficial para a Copa do Mundo e o seu nome ESTÁ NELA!")
    print("-"*50)
    print(f"Habilidade Final: {atributos['habilidade']} (Requisito: >= 80)")
    print(f"Energia Final: {atributos['energia']} (Requisito: >= 30)")
    print(f"Fama Final: {atributos['fama']} (Requisito: >= 80)")
    print(f"Reputação com a Torcida: {atributos['reputacao']}")
    print("="*50)
    print("Você realizou o sonho de infância e vai em busca do Hexa!")
    print("="*50 + "\n")

    # 5. Sistema de Loop Controlado para o terminal não fechar imediatamente
    print("Aperte ENTER para finalizar o jogo e fechar o simulador...")
    
    # Este loop checa o tempo a cada milissegundo enquanto o jogador não aperta Enter
    import msvcrt  # Biblioteca nativa do Windows para capturar teclas sem travar o código
    
    while True:
        # Se passaram 7 segundos, reinicia o trecho musical
        if time.time() - marcador_tempo >= duracao_trecho:
            mixer.music.play(start=tempo_inicio)
            marcador_tempo = time.time() # Reinicia o cronômetro do loop
        
        # Verifica se o jogador apertou Enter para sair do jogo
        if msvcrt.kbhit():
            tecla = msvcrt.getch()
            if tecla in (b'\r', b'\n'): # Se for a tecla Enter
                mixer.music.stop()
                break
        
        time.sleep(0.1) # Evita consumo excessivo do processador



import os
import time
from pygame import mixer

def mostrar_tela_eliminacao(nome, atributos):
    limpar_tela()  

    # 1. Configuração do tempo do áudio de eliminação (em segundos)
    tempo_inicio = 0  
    duracao_trecho = 3.5 # O áudio vai tocar por exatamente 3 segundos e reiniciar

    # 2. Inicializa o mixer e carrega o áudio de derrota/eliminação
    mixer.init()
    mixer.music.load('audio2.mp3') 

    # 3. Toca o som da eliminação
    mixer.music.play(start=tempo_inicio)
    marcador_tempo = time.time()

    # 4. Exibe o texto da eliminação no terminal
    print("\n" + "="*50)
    print(f"FALTOU POUCO, {nome.upper()}...")
    print("="*50)
    print("A lista da Copa do Mundo foi divulgada, mas você não foi chamado.")
    print("Você não conseguiu atingir as metas de convocação da comissão técnica:")
    print("-"*50)
    print(f"• Habilidade: {atributos['habilidade']}/80")
    print(f"• Energia: {atributos['energia']}/30")
    print(f"• Fama: {atributos['fama']}/80")
    print("-"*50)
    print("Continue treinando firme no Palmeiras para o próximo ciclo!")
    print("="*50 + "\n")

    print("[Atalho] Pressione 'S' ou 'ESPAÇO' para MUTAR o áudio.")
    print("Pressione 'ENTER' para fechar o simulador...")

    import msvcrt  

    # 5. Sistema de Loop do Áudio e Monitoramento de Teclas
    while True:
        # Repete o trecho do áudio se passarem 3 segundos
        if time.time() - marcador_tempo >= duracao_trecho:
            mixer.music.play(start=tempo_inicio)
            marcador_tempo = time.time()
        
        # Monitora os atalhos do teclado
        if msvcrt.kbhit():
            tecla = msvcrt.getch().lower()
            
            # Atalho para mutar o som (S ou Espaço)
            if tecla == b's' or tecla == b' ':
                parar_audio()
                print("\n🔇 Áudio silenciado.")
            
            # Atalho para fechar o jogo (Enter)
            if tecla in (b'\r', b'\n'):
                parar_audio()
                break
        
        time.sleep(0.1)

def parar_audio():
    from pygame import mixer
    mixer.music.stop()
    mixer.music.unload()
