'''
Exercício Python 12:
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''

p = float(input('Preço original do produto: R$'))
d = p * 5 / 100
pd = p - d
print(f'O preço original do produto era de {p:.2f} reais, com 5% de desconto seu valor será de {pd:.2f} reais.')