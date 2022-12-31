''' NÃO SEI.
Exercício Python 63:
Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de
uma Sequência de Fibonacci.
Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8
'''
print(f'---' * 30)
print(f'Sequência de Fibonacci')
print(f'---' * 30)
n = int(input(f'Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print(f'~~~' * 30)
print(f'{t1} -> {t2} -> ', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    cont = cont + 1
    print(f'{t3}', end='')
print(f'FIM!')