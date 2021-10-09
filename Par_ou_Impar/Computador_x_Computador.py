# jogo par ou impar entre duas máquinas
# usuário escolhe a quantidade de rodadas
# o vencedor final
# quantas partidas cada um venceu?
# se o usuário escolher numero par mostrar  a msg (numero par, poderá ocorrer um empate)

######## COMPUTADOR X COMPUTADOR ###########

# WALLAN MOTA

import random

print('Jogo de Par ou impar entre duas maquinas!')
print('Cada rodada pode ter três jogadas, onde o primeiro computador que fizer 2 pontos leva a rodada!')
jogadas = int(input('Quantas rodadas as maquinas vão jogar? '))
if jogadas % 2 == 0:
    print('O número de rodadas é par!!! jogo pode terminar em empate!')

vitoria_maquina_1 = 0
vitoria_maquina_2 = 0
for rodada in range(jogadas):
    pt_maquina_1 = 0
    pt_maquina_2 = 0
    while True:
        num_maquina_1 = random.randrange(11)
        num_maquina_2 = random.randrange(11)
        par_impar = random.randrange(2)
        escolha_maquina_1 = par_impar
        if escolha_maquina_1 == 0:
            escolha_maquina_1 = 'impar'
        else:
            escolha_maquina_1 = 'par'
        escolha_maquina_2 = ' '
        resul_calc = (num_maquina_1 + num_maquina_2) % 2

        if "impar" == escolha_maquina_1 and resul_calc == 1:
            escolha_maquina_2 = "par"
            pt_maquina_1 += 1
        elif "par" == escolha_maquina_1 and resul_calc == 0:
            escolha_maquina_2 = "impar"
            pt_maquina_1 += 1
        else:
            pt_maquina_2 += 1

        if pt_maquina_1 == 2:
            vitoria_maquina_1 += 1
            break
        if pt_maquina_2 == 2:
            vitoria_maquina_2 += 1
            break

if vitoria_maquina_1 > vitoria_maquina_2:
    print(f"Final de jogo, Maquina 1 venceu!!!\nPlacar:\n"
          f"Rodadas: Maquina1: {vitoria_maquina_1} x Maquina2: {vitoria_maquina_2}")
elif vitoria_maquina_1 <= vitoria_maquina_2:
    print(f"Final de jogo, Maquina 2 venceu!!!\nPlacar:\n"
          f"Rodadas: Maquina2: {vitoria_maquina_2} x Maquina1: {vitoria_maquina_1}")
else:
    print(f"Final de jogo, EMPATE!!!\nPlacar:\n"
          f"Rodadas: Maquina1: {vitoria_maquina_1} x Maquina2: {vitoria_maquina_2}")