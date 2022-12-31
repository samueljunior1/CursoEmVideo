''' FIZ!
Exercício Python 72:
Crie um programa que tenha uma Tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

Não consegui fazer o desafio final (perguntar ao usuário o desejo em continuar ou não).

'''
contagem = ('zero', 'um', 'dois', 'três', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove',
            'dez', 'onze', 'doze', 'treze', 'quatorse',
            'quinze', 'dezesseis', 'dezessete', 'dezoito',
            'dezenove', 'vinte')
numero = 0
resp = ' '
while True:
    while numero not in (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20): # O prof. usou While True: (looping infinito) If numero >= 0 and <= 0 break
       numero = int(input('Informe-nos um número entre 0 e 20: '))
#       print('Tente novamente.', end='')
    print(f'O número é {contagem[numero]}')
    resp = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'FIM')