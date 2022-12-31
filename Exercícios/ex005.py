'''
Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Informa um número: '))
su = n + 1
an = n - 1
print(f'Analisando o valor {n}, seu antecessor é {an}, e o seu sucessor será {su}.')
'''

n = int(input('Informa um número: '))
su = n + 1
an = n - 1
print(f'Analisando o valor {n}, seu antecessor é {n - 1}, e o seu sucessor será {n + 1}.')