# jogo de impar ou par.
# insiro um numero entre 0 - 10.
# a máquina joga um numero entre 0 - 10 aleatório.
# quem tiver 2 pontos ganha.
# 1 X 1 tem a terceira rodada.
# quem ganha o jogo:
# se o jogador esclhou impar e o resultado da soma for impar. o jogador ganha 1 ponto.
# se o jogador esclhou impar e o resultado da soma for par. a maquina ganha 1 ponto.
# o primeiro a juntar 2 pontos, vence o jogo.

######## JOOGADOR X COMPUTADOR ##########

# WALLAN MOTA

import random

pontosJogador = 0
pontosComputador = 0

while True:
    jogador = int(input('Digite um número: '))
    computador = random.randint(1, 10)
    soma = jogador + computador
    escolha = ' '
    while escolha not in 'parimpar':
        escolha = input('par ou impar? ')
    print(f'Você digitou {jogador} e o computador {computador}. A soma deu {soma}')
    print('Resultado: Par' if soma % 2 == 0 else 'Resultado: impar')
    if escolha == 'par':
        if soma % 2 == 0:
            print('vc ganhou!')
            pontosJogador += 1
            if pontosJogador == 2:
                print(f'Fim, vc ganhou {pontosJogador} vezes')
                break
        else:
            print('vc perdeu')
            pontosComputador += 1
            if pontosComputador == 2:
                print(f'Fim, computador ganhou {pontosComputador} vezes')
                break
    elif escolha == 'impar':
        if soma % 2 == 1:
            print('vc venceu')
            pontosJogador += 1
            if pontosJogador == 2:
                print(f'Fim, vc ganhou {pontosJogador} vezes')
                break
        else:
            print('vc perdeu')
            pontosComputador += 1
            if pontosComputador == 2:
                print(f'Fim, Computador ganhou {pontosComputador} vezes')
                break
    print('jogar de novo')




