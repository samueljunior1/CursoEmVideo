''' FIZ! 19min.05s.

Exercício Python 25:
Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome:

'''

nome = str(input('Digite seu nome: ')).upper().strip()
print('Seu nome tem Silva?')
print('SILVA' in nome)