'''
Exercício Python 9:
Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
'''

n = int(input('Número a ser convertido em tabuada: '))
print('=' * 12)
print(f'A tabuada do número {n} é: \n{n}X{1:2} = {n * 1:2}. \n{n}X{2:2} = {n * 2}. \n{n}X{3:2} = {n * 3}. \n{n}X{4:2} = {n * 4}. \n{n}X{5:2} = {n * 5}. \n{n}X{6:2} = {n * 6}. \n{n}X{7:2} = {n * 7}. \n{n}X{8:2} = {n * 8}. \n{n}X{9:2} = {n * 9}. \n{n}X{10:2} = {n * 10}.', end='\n')
print('=' * 12)