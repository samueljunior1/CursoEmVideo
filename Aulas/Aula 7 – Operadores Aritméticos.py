'''
Nessa aula, vamos aprender quais são os operadores aritméticos do Python e também sua ordem de precedência dentro de expressões matemáticas.
Veja como funcionam os operadores de adição, subtração, multiplicação, divisão, exponenciação e quociente na linguagem Python.

Ordem de precedência
1. ()
2. **
3. * / // %
4. + -
'''

n1 = int(input('Valor 1: '))
n2 = int(input('Valor 2: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n o produto é {} \n e a divisão é {:.3f}'.format(s, m, d), end='. ')
print(f'A divisão inteira é {di}, o fatorial é {e}.')