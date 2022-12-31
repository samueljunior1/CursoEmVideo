''' ERRO!
Exercício Python 49:
Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.
'''
numero = int(input('Número a ser convertido em tabuada: '))
print('==-' * 20)
print(f'A tabuada do número {numero} é:')
for c in range(1 , 11):
    tabuada = numero * c
    print(f'{numero}X{c:2} = {tabuada}')
print('==-' * 20)