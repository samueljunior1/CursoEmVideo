'''
Exercício Python 7:
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
'''

n1 = float(input('Nota da primeira avaliação: '))
n2 = float(input('Nota da segunda avaliação: '))
m = (n1 + n2) / 2
print(f'A nota da Primeira Avaliação foi {n1:.1f}. Na Segunda Avaliação foi {n2:.1f}. \nPortanto, a média será {m:.1f}', end='')