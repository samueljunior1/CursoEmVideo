'''
Exercício Python 4:
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.


algo = input('Insira algo: ')
print(algo, 'é do tipo primitivo', type(algo))
print(algo, 'Só tem espaços?', algo.isspace())
print(algo, 'É um número?', algo.isnumeric())
print(algo, 'É alfabético?', algo.isalpha())
print(algo, 'É alfanumérico?', algo.isalnum())
print(algo, 'Está em maiúscuo?', algo.isupper())
print(algo, 'Está em minúsculo?', algo.islower())
print(algo, 'Está capitalizada?', algo.istitle())

Desafio extra.

a = input('Insira algo: ')
print(f'é do tipo primitivo, {type(a)}')
print(f'Só tem espaços?, {a.isspace()}')
print(f'Só tem espaços? {a.isspace()}')
print(f'É um número? {a.isnumeric()}')
print(f'É alfabético? {a.isalpha()}')
print(f'É alfanumérico? {a.isalnum()}')
print(f'Está em maiúsculas? {a.isupper()}')
print(f'Está em minúsculas? {a.islower()}')
print(f'Está capitalizado? {a.istitle()}')

'''