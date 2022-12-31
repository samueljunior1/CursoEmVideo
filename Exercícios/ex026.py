''' NÃO FIZ  - CITOU NA AULA (17min.58s.) MAS NÃO CONSEGUI.

Exercício Python 26:
Faça um programa que leia uma frase pelo teclado e mostre:

Quantas vezes aparece a letra 'A'
Em que posição ela aparece a primeira vez.
Em que posição ela aparece pela última vez.
'''

frase = str(input('Digite uma frase: ')).strip().upper()
letra_a = frase.count('A')
posicao_primeira = frase.find('A' + 1)
posicao_ultima = frase.rfind('A' + 1)
print(f'Na frase {frase}, há {letra_a} letras A.')
print(f'A primeira vez que ela aparece é na posição {posicao_primeira}.')
print(f'A última vez que ela aparece é na posição {posicao_ultima}.')