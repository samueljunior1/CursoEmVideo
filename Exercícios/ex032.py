''' OLHEI NA INTERNET, ESTAVA ERRADO.
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
'''
from datetime import date
ano = int(input('Informe-nos o ano ou coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
resto = ano % 4
if resto == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é um ano bissexto.')
else:
    print(f'O ano de {ano} não é um ano bissexto.')
print('Término da análise!')