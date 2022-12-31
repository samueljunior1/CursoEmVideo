''' NÃO CONSEGUI!
Exercício Python 060:
Faça um programa que leia um número qualquer e mostre o seu fatorial.

Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120
'''

# from math import factorial
# n =int(input(f'Digite um número para calcular o seu fatorial: '))
# f = factorial(n)
# print(f'O fatorial de {n} é {f}.')


n = int(input(f'Digite um número para calcular o seu faturial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(f' X ' if c > 1 else ' = ', end='')
    f = f * c
    c = c - 1
print(f'{f}')


