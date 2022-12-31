'''
Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos import e from/import
no Python. Veja como carregar bibliotecas de funções e utilizar vários recursos adicionais nos seus
programas utilizando módulos built-in e módulos externos, oferecidos no Pypi.

#import math
from math import sqrt, ceil
num = int(input('Informe um número: '))
raiz = math.sqrt(num)
#raiz = num ** (1 / 2)
print(f'A raíz quadrada de {num:.2f} será {math.ceil(raiz)}.')

***---***

import random
#num = random.random()
num = random.randint(1, 10)
print(num)
'''
import emoji
print(emoji.emojize('ola, mundo!:globe_showing_Americas:', language='alias'))
