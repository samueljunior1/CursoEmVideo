''' #Fiz quase tudo, mas com um erro na exibição da lista em ordem decrescente.
Exercício Python 081:
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:

A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

lista = list() # ou lista = []
c = 0
while True:

    c = c + 1 # desnecessário, sóusar o len(lista).
    lista.append(int(input('Informe um valor: ')))
    resposta = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if resposta in 'Nn':
        break

print('-=' * 30)
print(f'Foram digitados {c} números ou {len(lista)}')
lista.sort(reverse=True)
print(f'A lista de valores em ordem decrescente é: {lista}')
if 5 in lista:
    print('O número 5 faz parte da lista.')
else:
    print(f'O número 5 não faz parte da lista.')