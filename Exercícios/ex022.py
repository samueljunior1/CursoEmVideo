''' Não FIZ! Maiúsculas e minúsculas: 20min.56s. Supressão dos espaços: 23min.56s.
Falou sobre espaços no meio, não disso como fazer. 26min.23s.

Exercício Python 22:
Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços). [NÃO SOUBE FAZER ISSO]

– Quantas letras tem o primeiro nome.
'''

nome = str(input('Informe seu nome completo: ')).strip()
print('Analisando o seu nome...')
print(f'O nome em maiúsculo é: {nome.upper()}.')
print(f'O nome em minúsculo é: {nome.lower()}.')
print(f'O comprimento total com espaços é: {len(nome)} caracteres.')
dividido = nome.split()
primeiro_nome = dividido[0]
reescreve = nome.replace(' ', '')
print(f'Desconsiderando os espaços, o nome completo tem {len(reescreve)} caracteres.')
#print(f'Desconsiderando os espaços, o nome completo tem {len(nome) - nome.count('')} caracteres.')
print(f'O primeiro nome é {primeiro_nome}, e tem {len(primeiro_nome)} caracteres.')
#print(f'Seu primeiro nome tem {nome.find(' ')} caracteres.')