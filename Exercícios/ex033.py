''' NÃO FIZ!
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''

'''n1 = int(input('Insira o número 1: '))
n2 = int(input('Insira o número 2: '))
n3 = int(input('Insira o número 3: '))
lista = [n1, n2, n3]
ordenado = sorted(lista)
print(f'O menor número será {ordenado[0]}, já o maior {ordenado[2]}.')'''

n1 = int(input('Insira um número: '))
n2 = int(input('Insira um número: '))
n3 = int(input('Insira um número: '))
# verificando qual é o menor:
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# verificando qual é o maior:
maior = n3
if n2 > n3 and n2 > n1:
    maior = n2
if n1 > n2 and n1 > n3:
    maior = n1
print(f'O maior número é {maior}, já o menor é {menor}.')