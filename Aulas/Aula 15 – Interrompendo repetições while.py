'''
Nessa aula, vamos aprender como utilizar a instrução break e os loopings infinitos a favor das nossas
estratégias de código. É muito importante saber usar o break no Python, já que em alguns casos precisamos
interromper um laço no meio do caminho.

Além disso, vamos aprender como trabalhar com as novas fstrings do Python.

cont  = 1
while cont <= 10:
    print(f'{cont}, ', end='')
    cont = cont + 1
print(f'Acabou.')

c = 0
n = 0
while c < 3:
    n = int(input(f'Informe-nos um número: '))
    c = c + 1
print(f'FIM.')

s = 0
n = 0
while n != 999:
    n = int(input(f'Informe-nos um número: '))
    s = s + n
# s = s - 999 gambiarra
print(f'A soma é {s}.')
print(f'FIM.')
'''
s = 0
n = 0
while True:
    n = int(input(f'Informe-nos um número: '))
    if n == 999:
        break
    s = s + n
#print('A some é {}'.format(s)(s))
print(f'A soma é {s}.')
print(f'FIM.')