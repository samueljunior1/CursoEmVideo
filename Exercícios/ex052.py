''' Nem ideia.
Exercício Python 52:
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''

n = int(input('Informe um número inteiro: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        tot = tot + 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')
print(f'\n\033[mO número {n} foi divisível {tot} vezes.')
if tot == 2:
    print('Este é um número primo. \nCumpre com os dois requisitos.')
    print('Um número primo é aquele que é dividido apenas por um e por ele mesmo.')
else:
    print('Não é primo.')
print('FIM.')