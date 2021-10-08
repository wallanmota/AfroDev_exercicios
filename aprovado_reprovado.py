# Imagina que estamos fazendo um sistema para uma escola
# E esse vai definir se o aluno foi aprovado ou não
# condições aprovação media de 4 notas >= 7
# numero de faltas, tem que ser menor que 4
# o sistema vai receber o nome, as notas e as faltas e vai exibir o nome e o status 
# Aprovado ou reprovado.
# Se a nota for 6, exibir a mensagem:  Status recuperação.
######################################
# Novas condições para o exercício:
# não sei a quantidade de notas
# não sei a média
# não sei a quantidade de faltas permitidas
# Print as mensagem de acordo com a identidade escolhida.


print('SISTEMA DE APROVAÇÃO\n')

nome = input('Olá, digite o nome de alun@: ')
nome = nome.title()
identidade = input('Gostaria de ser identificado com pronome "masculino", "feminino" ou "neutro"? ')
identidade = identidade.lower()
alu = "alu"
if identidade == 'masculino':
    alu = 'o aluno'
elif identidade == 'feminino':
    alu = 'a aluna'
elif identidade == 'neutro':
    alu = 'ê alune'
else:
    alu = 'o/a alun@'

mediaAprovacao = float(input('Qual a média para aprocação? '))
mediaRecuperacao = float(input('Qual a méda para a recueração? '))
qtdFaltas = int(input('Quantidade de faltas permitidas: '))

listaQtdNotas = []
qtdNotas = int(input('Quantas notas você quer adicionar? '))
for i in range(1, qtdNotas + 1):
    listaQtdNotas.append(i)

listaNotas = []
for nota in listaQtdNotas:
    nota = float(input(f'Digite a {nota}ª nota: '))
    listaNotas.append(nota)
media = sum(listaNotas) / qtdNotas

faltas = int(input(f'Quantas faltas que {alu} teve: '))

msgAprovado = f'Parabéns, {alu} {nome} foi APROVADO\nA média foi {media}'
msgRecuperacao = f'Opa! {alu} {nome} está de RECUPERAÇÃO\nA média foi {media}'
msgReprovado = f'Infelizmente {alu} {nome} foi REPROVADO\nA média foi {media}'

if media >= mediaAprovacao and faltas <= qtdFaltas:
    print(msgAprovado)
elif media >= mediaRecuperacao  and faltas < qtdFaltas:
    print(msgRecuperacao)
else:
    print(msgReprovado)

print('\nFIM DO PROGRAMA')