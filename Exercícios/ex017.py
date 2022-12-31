
'''
Exercício Python 17:
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
'''

import math
comprimento_cateto_oposto = float(input('Comprimento do cateto oposto: '))
comprimento_cateto_adjacente = float(input('Comprimento do cateto adjacente '))
quadrados_de_a_b = math.pow(comprimento_cateto_oposto, 2) + math.pow(comprimento_cateto_adjacente, 2)
hipotenusa = math.sqrt(quadrados_de_a_b)
# (método matemático) hipotenusa = (comprimento_cateto_oposto ** 2 + comprimento_cateto_adjacente ** 2) ** (1 / 2)
# hipotenusa = math.hypot(camprimento_cateto_oposto, comprimento_cateto_adjacente)
print(f'A hipotenusa será {hipotenusa:.2f}')
