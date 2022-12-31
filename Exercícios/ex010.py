'''
Exercício Python 10:
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
'''

cofrinho = float(input('Quanto você tem na carteira? R$'))
dol = cofrinho / 3.27
print(f'R${cofrinho:.2f} reais é o mesmo que U${dol:.2f} dólares')
