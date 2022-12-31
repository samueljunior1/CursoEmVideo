''' INCOMPLETO.
Exercício Python 64:
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''
# n = soma = c = 0 reduzido
n = 0
soma = 0
c = 0
n = int(input(f'Informe um número inteiro: '))
while n != 999:
    c = c + 1 # reduzido é c += 1
    soma = soma + n # reduzido é soma += n
    n = int(input(f'Informe um número inteiro: '))
print(f'Pare')
print(f'Foram digitados {c} números.')
print(f'A soma total foi de {soma}.')
print(f'TÉRMINO.')
