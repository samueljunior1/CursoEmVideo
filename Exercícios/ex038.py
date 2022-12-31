''' FIZ!!!
Exercício Python 038:
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais
'''

print('--=' * 20)
print('Analisador de números')
print('--=' * 20)
n1 = int(input('Informe um número: '))
n2 = int(input('Informe outro número: '))
if n1 > n2:
    print(f'O primeiro valor é superior ao segundo, visto que {n1} é maior que {n2}.')
elif n1 < n2:
    print(f'O segundo valor é superior ao primeiro, visto que {n2} é maior que {n1}.')
else:
    print(f'Não há que se falar em número maior ou menor, pois são números iguais.')
print('Término da análise.')