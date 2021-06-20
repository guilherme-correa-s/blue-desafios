from random import randint
from time import sleep
# lista que irá conter as opções [pedra, papel e tesoura]
listaJokenPo = ['Pedra', 'Papel', 'Tesoura']
# lista para printar animação
listaJokenPoAnimacao = ['Pedraaaaa', 'Papeeelll', 'Teeesoura!!!!!!']
# iniciar os jogos
while True:
    # contator para verificar quantas vezes o computador e o usuario ganhou
    jogadorWin = 0
    maquinaWin = 0
    empates = 0    
    # variável para armazenar quantas vezes o jogador gostaria de jogar
    qtdJogos = int(input('Quantas rodadas você deseja jogar? '))    
    # for para rodar a quantidade de rodadas escolhidas
    for i in range(qtdJogos):
        # máquina escolhe sua jogada
        escolhaMaquina = listaJokenPo[randint(0, len(listaJokenPo)-1)]
        # jogador escolhe sua jogada
        escolhaIndexJogador = int(input('\nQual a sua escolha?\n[ 1 ] Pedra\n[ 2 ] Papel\n[ 3 ] Tesoura\n '))
        escolhajogador = listaJokenPo[escolhaIndexJogador-1]
        for i in listaJokenPoAnimacao:
            print(i,end=' ')
            sleep(1)
        print('')    
        # se máquina jogar pedra    
        if escolhaMaquina == 'Pedra': 
            if escolhajogador == 'Papel': # se o jogador jogar papel
                print(f'Você escolheu {escolhajogador}.\nMáquina escolheu {escolhaMaquina}.\nVocê venceu.')
                jogadorWin += 1 # jogador vence
            elif escolhajogador == 'Tesoura': # se o jogador jogar tesoura
                print(f'Você escolheu {escolhajogador}.\nMáquina escolheu {escolhaMaquina}.\nA máquina venceu.')                
                maquinaWin += 1 # máquina vence
            else: 
                print(f'Você escolheu {escolhajogador}.\nMáquina escolheu {escolhaMaquina}.\nEMPATE!!')                
                empates += 1 # se ambos jogarem pedra, empate
         # se máquina jogar papel
        elif escolhaMaquina == 'Papel':
            if escolhajogador == 'Tesoura': # se o jogador jogar tesoura
                print(f'Você escolheu {escolhajogador}.\nMáquina escolheu {escolhaMaquina}.\nVocê venceu.')                
                jogadorWin += 1 # jogador vence
            elif escolhajogador == 'Pedra': # se o jogador jogar pedra
                print(f'Você escolheu {escolhajogador}.\nMáquina escolheu {escolhaMaquina}.\nA máquina venceu.')                
                maquinaWin += 1 # máquina vence
            else:
                print(f'Você escolheu {escolhajogador}.\nMáquina escolheu {escolhaMaquina}.\nEMPATE!!')                 
                empates += 1 # se ambos jogarem papel, empate   
        # se máquina jogar tesoura             
        elif escolhaMaquina == 'Tesoura':
            if escolhajogador == 'Pedra': # se o jogador jogar pedra
                print(f'Você escolheu {escolhajogador}.\nMáquina escolheu {escolhaMaquina}.\nVocê venceu.')                
                jogadorWin += 1 # jogador vence
            elif escolhajogador == 'Papel': # se o jogador jogar papel
                print(f'Você escolheu {escolhajogador}.\nMáquina escolheu {escolhaMaquina}.\nA máquina venceu.')                
                maquinaWin += 1 # máquina vence
            else: 
                print(f'Você escolheu {escolhajogador}.\nMáquina escolheu {escolhaMaquina}.\nEMPATE!!')                
                empates += 1 # se ambos jogarem tesoura, empate
    else:
        # exibir resultados
        print(f'\nFim das {qtdJogos} rodadas.\nA máquina ganhou {maquinaWin}x.\nJogador ganhou {jogadorWin}x.')
        if empates > 0:
            print(f'E houve {empates} empate(s).\n')
        if maquinaWin == jogadorWin:
            print('\nEmpatou!!!. Jogue novamente para desempatar.')
        elif maquinaWin > jogadorWin:
            print('\nA máquina foi a grande vencedora. Tente novamente.')
        else:
            print('\nParabéns, você foi o grande vencedor!!!!\n.') 
    # verificar se deseja continuar jogando            
    jogarNovamente = int(input('Deseja jogar novamente?\n[ 1 ] Sim\n[ 2 ] Não\n'))
    if jogarNovamente != 1:
        break       