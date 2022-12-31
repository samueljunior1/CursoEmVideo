''' FIZ ERRADO!
Exercício Python 68:
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
from random import choice, randint
print(f'--=' * 10, 'PAR OU ÍMPAR GAME', '--=' * 10)
while True:
    jogador = int(input(f'Digite um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    v = 0
    while tipo not in 'PI':
        tipo = str(input(f'Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}.', end= ' ')
    print(f'DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print(f'Você venceu!')
            v = v + 1
        else:
            print(f'Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print(f'Você venceu!')
            v = v + 1
        else:
            print(f'Você perdeu!')
            break
    print(f'Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes! Show.')