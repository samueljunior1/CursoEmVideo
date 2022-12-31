
'''
Exercício Python 16:
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

#import math
from math import trunc
n = float(input('Digite um número: '))
inteiro = trunc(n)
print(f'O número {n} tem a parte inteira {inteiro}.')

'''

num = float(input('Digite um valor: '))
print(f'O número {num} tem a parte inteira {int(num)}.')