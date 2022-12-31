'''
Exercício Python 13:
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''
sb = float(input('Salário base: '))
a = (sb * 15) / 100
sa = sb + a
print(f'O salário base é {sb} reais, com 15% de aumento será {sa} reais.')