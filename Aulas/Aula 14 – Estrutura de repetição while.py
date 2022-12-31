'''
Nessa aula, vamos continuar a estudar os laços e vamos aprender a usar a estrutura de repetição while no Python.
Por exemplo:


for c in range(1, 10):
    print(c)
print('FIM!')

c = 1
while c < 10:
    print(c)
    c = c + 1
print('FIM!')

for c in range(1, 5):
    n = int(input('Digite um número: '))
print('FIM!')

r = S
n = 1
while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N]')).upper()
print('FIM!')

***

c = 1
while c != 10:

print(c)

c = c + 1

print(‘Acabou’)

'''

n = 1
totpar = 0
totimpar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            totpar = totpar + 1
        if n % 2 != 0:
            totimpar = totimpar +1
print(f'Foram {totpar} números pares.')
print(f'Foram {totimpar} números ímpares.')
print('FIM!')