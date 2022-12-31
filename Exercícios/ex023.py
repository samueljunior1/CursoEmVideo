''' NÃO FIZ
Exercício Python 23:
Faça um programa que leia um número de 0 a 9999 e mostra na tela cada um dos dígitos separados:

Exe.:
Digite um número: 1834
Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1

'''

numero = int(input('Digite um número entre 0 e 9.999: '))
print(f'Analisando o número {numero}.')
unidade = numero / 1 % 10
dezena = numero / 10 % 10
centena = numero / 100 % 10
milhar = numero / 1000 % 10
print(f'Para o número {numero:.0f}, temos:')
print(f'Unidade: {unidade:.0f}.')
print(f'Dezena: {dezena:.0f}.')
print(f'Centena: {centena:.0f}.')
print(f'Milhar: {milhar:.0f}.')