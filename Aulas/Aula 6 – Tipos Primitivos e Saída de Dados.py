'''
Nessa aula, vamos aprender como funcionam os tipos primitivos no Python e as peculiaridades do int() float() bool() e str().
Além disso, veremos como fazer as primeiras operações com a função print() do Python.

n1 = int(input('número 1: '))
n2 = int(input('número 2: '))
s = n1 + n2
# Python antigo. print('A soma entre', n1, 'e', n2, 'é igual a {}'.format(s))
print('A soma entre {} e {} é igual a {}'.format(n1, n2, s))

#Outro exemplo.
n = float(input('Digite um valor: '))
print(type(n))


n = input('Digite algo: ')
print(n.isnumeric())

'''


