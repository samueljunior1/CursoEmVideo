''' FIZ INCOMPLETO
Exercício Python 24:
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'.

'''

cidade = str(input('Nome da cidade: ')).strip()
#método do professor print(cidade[:5].upper() == 'SANTO')
dividido = cidade.split()
primeiro = dividido[0].upper()
santo = 'SANTO' in primeiro
print(f'{santo}.')