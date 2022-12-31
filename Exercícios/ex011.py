'''
Exercício Python 11:
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
'''
l = float(input('Largura da parede em metros: '))
a = float(input('Altura da parede em metros: '))
area = l * a
lata = area / 2
print(f'A parede tem {l}m de largura e {a}m de altura. Sua área, portanto, é {area}m². \n Se uma lata de tinta é capaz de pintar 2m², para {area}m² serão necessárias {lata} latas de tinta.')