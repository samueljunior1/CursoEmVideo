
'''
Exercício Python 18:
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''

import math
angulo = float(input('Informe um ângulo: '))
angulo1 = math.radians(angulo)
seno = math.asin(angulo1)
coseno = math.cos(angulo1)
tangente = math.atan(angulo1)
print(f"Em um ângulo de {angulo:.2f}º, temos: \nSeno: {seno:.2f}. \nCoseno: {coseno:.2f}. \nTangente: {tangente:.2f}.")