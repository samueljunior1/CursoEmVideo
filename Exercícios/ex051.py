''' ERRADO
Exercício Python 51:
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
'''
termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
decimo = termo + (10 - 1) * razao
print(f'Considerando o termo inicial como sendo o número {termo}, e a razão {razao}, os 10 primeiros números serão:')
for c in range(termo, decimo + razao, razao):
    print(f'{c}', end='-> ')
print('FIM!')
