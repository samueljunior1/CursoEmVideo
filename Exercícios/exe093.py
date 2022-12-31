''' Consegui. Só não fiz a última forma de exibição. Laço na lista. jogador["gols"].
Exercício Python 093:
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''
jogador = dict()
partidas = list()
jogador["nome"] = str(input('Nome do  jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(1, tot + 1):
    partidas.append(int(input(f'Quantos gols fez na {c} jogo? ')))
jogador["gols"] = partidas[:]
jogador["total"] = sum(partidas)
print("-=" * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}', end=' ')
    print()
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.') # O prof. não usou a variável tot.
for i, v in enumerate(jogador["gols"]): # Laço na lista.
    print(f'Na partida {i + 1}, fez {v} gols.', end=" ")
    print()
print(f'Foi um total de {jogador["total"]} gols.')
print('-=' * 30)