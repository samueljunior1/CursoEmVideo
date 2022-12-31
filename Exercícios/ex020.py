#NÃO SOUBE FAZER. OLHEI A RESOLUÇÃO!

'''
Exercício Python 20:
O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.


import random
nome1 = str(input('Nome do aluno 1: '))
nome2 = str(input('Nome do aluno 2: '))
nome3 = str(input('Nome do aluno 3: '))
nome4 = str(input('Nome do aluno 4: '))
lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)
print(f'O ordem de apresentação dos trabalhos será: {lista}')
'''

from random import shuffle
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'A ordem da apresentação será: \n{lista}.')

