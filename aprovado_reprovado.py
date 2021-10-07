# Imagina que estamos fazendo um sistema para uma escola
# E esse vai definir se o aluno foi aprovado ou não
# condições aprovação media de 4 notas >= 7
# numero de faltas, tem que ser menor que 4
# o sistema vai receber o nome, as notas e as faltas e vai exibir o nome e o status 
# Aprovado ou reprovado.
# Se a nota for 6, exibir a mensagem:  Status recuperação.

print('SISTEMA DE APROVAÇÃO\n')

def valor(n):
    if n.isnumeric() == False:
        return False
    else:
        return True

nome = input('Olá, digite o nome do aluno: ')
nome = nome.title()

n1 = input('Digite a primeira nota: ')
if valor(n1) == False:
    while valor(n1) == False:
        print('favor inserir apenas numeros')
        n1 = input('Digite a primeira nota: ')

n2 = input('Digite a segunda nota: ')
if valor(n2) == False:
    while valor(n2) == False:
        print('favor inserir apenas numeros')
        n2 = input('Digite a segunda nota: ')

n3 = input('Digite a terceira nota: ')
if valor(n3) == False:
    while valor(n3) == False:
        print('favor inserir apenas numeros')
        n3 = input('Digite a terceira nota: ')

n4 = input('Digite a quarta nota: ')
if valor(n4) == False:
    while valor(n4) == False:
        print('favor inserir apenas numeros')
        n4 = input('Digite a quarta nota: ')

faltas = input('Digite a quantidade de faltas: ')
if valor(faltas) == False:
    while valor(faltas) == False:
        print('favor inserir apenas numeros')
        faltas = input('Digite a quantidade de faltas: ')
faltas = int(faltas)

media = (float(n1) + float(n2) + float(n3) + float(n4)) / 4


if media >= 7 and faltas < 4:
    print(f'Parabéns {nome}, você foi APROVADO')
elif media >= 6 and faltas < 4:
    print(f'Opa! {nome}, você está de RECUPERAÇÃO')
else:
    print(f'{nome}, infelizmente você foi REPROVADO')

print('\nFIM DO PROGRAMA')