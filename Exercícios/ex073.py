''' FIZ!
Exercício Python 73:
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.
'''
posição = ('Flamengo', 'Palmeiras', 'Atlético Mineiro', 'Grêmio','Athletico Paranaense','Santos',
           'São Paulo', 'Internacional', 'Fluminense', 'Corinthians', 'Fortaleza', 'Bahia','Ceará',
           'Cruzeiro', 'América Mineiro', 'Atlético Goianiense', 'Chapecoense','Botafogo',
           'Vasco da Gama', 'Red Bull Bragantino')

print(f'Os 5 primeiros colocados são: {posição[0:5]}')
print('=-' * 15)
print(f'Os 4 últimos colocados foram: {posição[-4:]}')
print('=-' * 15)
print(f'Os 20 primeiros times organizados alfabeticamente são {sorted(posição)}')
print('=-' * 15)
for pos, time in enumerate(posição): # o professor usou o método "index".
    if time == "Chapecoense":
        print(f'O time Chapecoense está na {pos + 1} posição.')
    # print(f'O time {time} está na posição {pos}') lista todos os times em suas devidas posições.
print(f'O time Chapecoense está na {posição.index("Chapecoense") + 1} posição.') # Método do professor.
#print(f'O time Chapecoense está em {} lugar.')