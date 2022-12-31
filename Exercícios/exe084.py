''' Não fiz.
Exercício Python 084:
Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''
pessoas = []
dados = list()
contador = 0
maior = menor = 0
while True:
    dados.append(str(input('Informe o nome: ')))
    dados.append(float(input('Informe o peso: ')))
    if len(pessoas) == 0: # O prof. usou if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:]) # Cria uma cópia - fatiamento.
    contador = contador + 1 # O prof. usou o len(pessoas)
    dados.clear()
    resposta = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if resposta in 'Nn':
        break
print('-=' * 30)
print(f'Foram cadastradas {contador} pessoas.')
print(f'A pessoa mais pesada tem {maior}kg. É o peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'A pessoa mais leve tem {menor}kg. É o peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]')
print()
print('-=' * 30)