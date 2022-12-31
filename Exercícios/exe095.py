''' Não consegui.
Exercício Python 095:
Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''
jogador = dict()
partidas = list()
times = []

while True:
    jogador.clear()
    jogador["nome"] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(1, tot + 1):
        partidas.append(int(input(f'Quantos gols fez no {c} jogo? ')))
    jogador["gols"] = partidas[:]
    jogador["total"] = sum(partidas)
    times.append(jogador.copy()) # Não é possível fazer fatiamento dentro de dicionários [:]
    while True:
        resposta = str(input('Quer continuar[S/N]? ')).strip().upper()[0]
        if resposta in "SsNn":
            break
        print('ERRO! Responda S para sim e N para não.')
    if resposta in 'Nn':
        break

print('-=' * 30)
print('cod ', end=" ")
for i in jogador.keys():
    print(f'{i:<15}', end=" ")
print()
print('-=' * 30)

print('-' * 40)
for k, v in enumerate(times): # O time é uma lista, por isso o enumerate.
    print(f'{k:>3} ', end=" ")
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
print('-' * 40)
while True:
    busca = int(input(f'Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca > len(times): # Prof. usou maior igual. Entendo que igual está no parâmetro.
        print(f'ERRO! Não existe jogador com o código {busca}!')
    else:
        print(f"LEVANTAMENTO DO JOGADOR {times[busca]['nome']}:")
        for i, g in enumerate(times[busca]["gols"]):
            print(f'   No jogo {i + 1}, fez {g} gols.')
    print('-=' * 40)
print('<<< VOLTE SEMPRE >>>')