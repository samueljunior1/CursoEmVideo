''' CONSEGUI FAZER!
Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km
e R$ 0,45 para viagens mais longas.
'''

distancia = float(input('Informe a distância? '))
curtas = distancia * 0.50
longas = distancia * 0.45
# preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
if distancia <= 200.00:
    #preço = distancia * 0.50
    print(f'A distância percorrida foi de {distancia} KM, portanto, cada KM será precificado em R$ O,50. \nO valor total será de R$ {curtas}.')
else:
    #preço = distancia * 0.45
    print(f'A distância percorrida foi de {distancia} KM, portanto, cada KM será precificado em R$ 0,45. \nO valor total será de R$ {longas}.')
print('Término do cálculo.')