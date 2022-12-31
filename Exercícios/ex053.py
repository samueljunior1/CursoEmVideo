''' NÃO FIZ.

Exercício Python 53:
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
'''

frase = str(input('Informe-nos uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, - 1, - 1):
    inverso = inverso + junto[letra]
print(f'O inverso de {frase} é {inverso}.')
if inverso == junto:
    print('Ele é um palíndrimo')
else:
    print('Ele não é um palíndromo.')

