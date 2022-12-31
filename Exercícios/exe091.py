''' Fiz a maior parte. Não consegui colocar em ordem.
Exercício Python 091:
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''
from random import randint
from time import sleep
from operator import itemgetter
jogo = {"jogador 1": randint(1,6),
        "jogador 2": randint(1, 6),
        "jogador 3": randint(1, 6),
        "jogador 4": randint(1, 6)}
ranking = () # ou dict()
print('Valores sorteados')
for k, v in jogo.items():
    print(f'{k} tirou o valor {v} no dado.')
    sleep(1)
print('-=' * 30)
print('Ranking final')
print('-=' * 30)
ranking =  sorted(jogo.items(), key=itemgetter(1), reverse=True) # Esse resultado será tratado como lista.
for i, v in enumerate(ranking): # Não uso .items, visto ser uma lista.
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}.') # É uma Tupla dentro de uma Lista.
    sleep(1)
print()



