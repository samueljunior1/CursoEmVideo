'''
Exercício Python 076:
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

produtos = ('Sabonete', 26,
            'Desodorante', 0.34,
            'Escova', 12,
            'Shampoo', 15,
            'Perfume', 180,
            'Cola', 2)
print('-' * 32)
print(f'{"PRODUTOS":^32}')
print('-' * 32)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R$ {produtos[pos]:>8.2f}')
print('-' * 32)