'''
Nessa aula, vamos aprender como utilizar estruturas condicionais simples e compostas (e simplificadas) nos seus programas em Python.

Condição:
if carro.esquerda():
    bloco True
else:
    bloco False

    ***

tempo = int(input('Quantos anos tem o seu carro? '))
if tempo <= 3:
    print(f'Seu carro tem {tempo} anos, logo, é novinho!')
else:
    print(f'Seu carro tem {tempo} anos, logo, é bem velhinho.')
print('=== Término da análise ===')
#Versão simplificada. print('Carro novo!' if tempo <= 3 else 'Carro velho!')

    ***
    nome = str(input('Qual é o seu nome? ')).
if nome == "Samuel":
    print('Olá, Samuel')
else:
    print('Seu nome é tão normal!')
print(f'Bom dia, {nome}.')

'''
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1 + n2) / 2
print(f'A sua média foi {m:.1f}.')
if m >= 6.0:
    print("Média razoável! Parabéns!")
else:
    print('Nota horrenda! Estude mais!')
# versão simplificada print('PARABÉNS!' if m >= 6.0 else 'ESTUDE MAIS!'.)
