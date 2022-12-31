'''
Exercício Python 8:
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''

medida = float(input('Informe um valor em metros (m): '))
vc = medida * 100
vm = medida * 1000
dm = medida * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000
print(f'A conversão do valor {medida}m para centímetros foi de {vc:.0f}cm, em mílitros, foi {vm:.0f}mm.')
print(f'A conversão do valor {medida}m para kilômetros foi de {km}. Para hectômetro foi de {hm}, decâmetro foi de {dam}, e decímetro foi de {dm}.')