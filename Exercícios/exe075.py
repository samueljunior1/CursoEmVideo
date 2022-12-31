''' Não consegui.
Exercício Python 075:
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.
'''
número = (int(input('Informe um número: ')), int(input('Informe mais um número: ')),
          int(input('Informe outro número: ')), int(input('Informe o último número: ')))
print(f'A tupla informada é: {número}')
print(f'O número 9 apareceu {número.count(9)} vezes.')
if 3 in número:
    print(f'O valor 3 foi digitado pela primeira vez na {número.index(3) + 1}ª posição.')
else:
    print(f'O valor 3 não foi digitado.')
print(f'Os valores pares digitados foram: ', end=' ')
for n in número:
    if n % 2 == 0:
        print(f'{n}', end=' ')