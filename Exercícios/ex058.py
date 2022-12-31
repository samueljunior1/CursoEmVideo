''' FIZ!!!
Exercício Python 58:
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.
'''
from random import randint
from time import sleep
pensou = randint(0, 10) #O código acima importa as bibliotecas + faz o PC escolher um número aleatório no intervalo desejado.
print('--=--' * 20)
print('Vou pensar um número entre 0 e 10, tente advinhar.')
print('--=--' * 20)
palpite = ''
tentativas = 0
acertou = False
while not acertou:
    palpite = int(input("Qual foi o número que pensei?"))
    tentativas = tentativas + 1
    print('Processando...')
    sleep(3)
    if palpite == pensou:
        acertou = True
        print('Você acertou! Parabéns.')
        print(f'Foram {tentativas} tentativas.')
    else:
#       print(f'Você errou! O número que pensei foi {pensou}.')
        print(f'Errou! Vamos outra rodada!')
        if palpite < pensou:
            print(f'Mais.')
        elif palpite > pensou:
            print(f'Menos.')
print(f'FIM!')
print('Teste concluído.')