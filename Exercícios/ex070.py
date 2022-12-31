''' FIZ! OLHANDO O 65.
Exercício Python 70:
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não.
No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
'''
total = 0
maior1000 = 0
barato_preco = 0
barato_nome = ' '
controle = 0
while True:
    nome = str(input(f'Nome: ')).strip().upper()
    preco = float(input(f'Peço R$: '))

    # CALCULA O TOTAL GASTO NA COMPRA.
    total = total + preco

    # QUANTITATIVO DE PRODUTOS QUE CUSTAM MAIS QUE 100.
    if preco > 1000:
        maior1000 = maior1000 + 1

    # NOME DO PRODUTO MAIS BARATO.
    controle = controle + 1

    if controle == 1: # SIMPLIFICOU ASSIM: if controle == 1 or preco < barato_preco:
        barato_preco = preco
        barato_nome = nome
    else:             # VER A SIMPLIFICAÇÃO
        if preco < barato_preco:
            barato_preco = preco
            barato_nome = nome

    # QUESTIONAMENTO SE QUER CONTINUAR.
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input(f'Quer continuar? [S/N] ')).strip().upper()[0]
    if pergunta == 'N':
        break

print(f' (TÉRMINO) ')
print(f'O total gasto nas compras foi de R${total:5.2f}.')
print(f'Há, na lista de compras {maior1000} produtos que custam mais que 1.000 Reais.')
print(f'O produto mais barato é o {barato_nome} e custa {barato_preco:.2f}.')