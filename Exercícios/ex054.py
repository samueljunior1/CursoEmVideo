'''
Exercício Python 54:
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''

from datetime import date
nascimento = {}
atual = date.today().year
totalmaior = 0
totalmenor = 0
for c in range(1, 8):
    nascimento = int(input(f'Informe o ano de nascimento da {c}ª pessoa: '))
    idade = atual - nascimento
    if idade >= 21:
        totalmaior = totalmaior + 1
    else:
        totalmenor = totalmenor + 1
print(f'Há {totalmaior} pessoas maiores e {totalmenor} menores.')