'''
Exercício Python 15:
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''
percorrido = float(input('Qual é a quantidade de km percorrido? '))
dias_alugados = int(input('Quantos dias ficou alugado? '))
preço_km = percorrido * 0.15
preço_dia = dias_alugados * 60
print(f'Um automóvel que rodou {percorrido}km, pagará R${preço_km} pelos kilômetros rodados.')
print(f'Tendo sido alugado por {dias_alugados} dias, o custo total das diárias será de R${preço_dia}.')
print(f'O valor total da locação será de R${preço_km + preço_dia:.2f}.')
