''' CONSEGUI.
Exercício Python 082:
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''

lista = []
pares = []
impares = []
while True:
    n = int(input('Informe um valor: '))
    lista.append(n)
    if (n % 2) == 0:
        print(f'{n} é um valor par.')
        pares.append(n)
    else:
        print(f'{n} é um valor ímpar.')
        impares.append(n)
    resposta = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if resposta in 'Nn':
        break
print('-=' * 30)
print(f'A lista integral é {lista}')
print(f'A lista composta por números pares é {pares}.')
print(f'A lista composta por números ímpares é {impares}.')


########### O professor fez assim: ###########
# for i, v in enumerate(lista):
#   if v % 2 == 0:
#       pares.append(v)
#   else: # ou para ser explícito: v % 2 == 1:
#       impares.append(v)