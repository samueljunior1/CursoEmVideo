''' FIZ MAIS OU MENOS.
Exercício Python 078:
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''
listanum = list()
maior = 0
menor = 0
for cont in range(0, 5):
    listanum.append(int(input(f'Informe o valor de número {cont}:')))
    if cont == 0:
        maior = listanum[cont]
        menor = listanum[cont]
    else:
        if listanum[cont] > maior:
            maior = listanum[cont]
        if listanum[cont] < menor:
            menor = listanum[cont]
print('=--' * 30)
print(f'Os valores digitados foram: {listanum}')
print(f'O maior valor é o {maior}, nas posições: ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'\nO menor valor é o {menor}, nas posições: ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}... ', end='')