''' Consegui fazerrr.

Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça
para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

from random import randint
from time import sleep
pensou = randint(0, 5)
#print(pensou)
palpite = int(input("Qual foi o número que o PC pensou? "))
print('--=--' * 20)
print('Vou pensar um número entre 0 e 5, tente advinhar.')
print('--=--' * 20)
print('Processando...')
sleep(3)
if palpite == pensou:
    print('Você acertou! Parabéns.')
else:
    print(f'Você errou! O número que pensei foi {pensou}.')
print('Teste concluído.')
