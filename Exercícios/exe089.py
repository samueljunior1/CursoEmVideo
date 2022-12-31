''' Não consegui.
Exercício Python 089:
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário
possa mostrar as notas de cada aluno individualmente.
'''
ficha = list
while True:
    nome = str(input("Nome: "))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta in 'N':
        break
print('-=' * 30)
print(f'{"N.º":<4}{"Nome":<10}{"Média":>8}')
print('-=' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-=' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}.')
print('<<< VOLTE SEMPRE! >>>')

