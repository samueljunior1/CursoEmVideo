''' FIZ!
Exercício Python 66:
Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
'''
soma = 0
total = 0
while True:
    numero = int(input(f'Informe-nos um número: '))
    if numero == 999:
        break
    total = total + 1
    soma = soma + numero
print(f'Foram digitados {total} números cuja soma é {soma}.')