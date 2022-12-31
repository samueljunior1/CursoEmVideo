''' CONSEGUI FAZER!
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
'''

#Identificamos se um número é par ou ímpar quando o dividimos por dois.
#Se o resto da divisão for zero, o número é par; caso contrário, é ímpar.

numero = int(input('Digite um número: '))
resto = numero % 2
if resto == 0:
    print(f'''Identificamos se um número é par ou ímpar quando o dividimos por dois.
    Se o resto da divisão for zero, o número é par; caso contrário, é ímpar. \nNo caso,
o número informado foi {numero}, sendo PAR.''')
else:
    print(f'''Identificamos se um número é par ou ímpar quando o dividimos por dois.
        Se o resto da divisão for zero, o número é par; caso contrário, é ímpar. \nNo caso,
    o número informado foi {numero}, sendo ÍMPAR.''')
print('Término da análise.')