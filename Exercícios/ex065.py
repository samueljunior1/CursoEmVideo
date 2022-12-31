'''
Exercício Python 65:
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''
resposta = s
media = 0
soma = 0
quantidade = 0
maior = 0
menor = 0
while resposta in 'Sn':
    n = int(input(f'Informe um número: '))
    soma = soma + n
    quantidade = quantidade + 1
    if quantidade == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resposta = str(input(f'Quer continuar digitando [sim] ou [nao]: ')).upper().strip()[0]
media = soma / quantidade
print(f'A média dos {quantidade} valores digitados é {media}.')
print(f'O maior valor digitado foi {maior} e o menor foi {menor}.')
print(f'Encerrando.')