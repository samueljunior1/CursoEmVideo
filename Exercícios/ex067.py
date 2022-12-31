''' FIZ!
Exercício Python 67:
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
'''
while True:
    numero = int(input('Informe um número: '))
    if numero < 0:
        break
    print(f'*' * 30)
    print(f'A tabudada do número {numero} é:')
    for c in range(1, 11):
        produto = numero * c
        print(f'{numero} X {c} = {produto}')
    print(f'*' * 30)
print(f'=' * 30)
print(f'TÉRMINO.')
print(f'=' * 30)