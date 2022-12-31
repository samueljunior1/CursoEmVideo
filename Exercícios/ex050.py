''' FIZ!!!
Exercício Python 50:
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.
'''
s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Informe um número inteiro: '))
    par = (n % 2)
    if par == 0:
        s = s + n
        cont = cont + 1
    else:
        impar = n
print(f'A soma dos números pares informados é igual a {s}. Foram {cont} números pares informados.')
print('FIM.')
