''' Não consegui.
Exercício Python 074:
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''
from random import randint
números = (randint(1, 11), randint(1, 11), randint(1, 11),
     randint(1, 11), randint(1, 11))

#print(f'Os valores sorteados foram: {números}')
print(f'Os valores sorteados foram:')

for n in números:
    print(f'{n} ', end='')

print(f'\nO maior valor é {max(números)} e o menor é {min(números)}.') # O professor não usou laço.
