'''
Exercício Python 14:
Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
'''

tg = float(input('Qual é a temperatura em graus celsius? '))
tf = (tg * 9 / 5) + 32
print(f'A temperatura de {tg:.2f}°C corresponde a {tf:.2f}ºF.')