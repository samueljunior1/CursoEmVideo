''' NÃO FIZ!
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas
podem ou não formar um triângulo.
Ex.:
r1 ---
r2 --
r3 ----
'''

print('--=' * 20)
print('Analizador de triângulos')
print('--=' * 20)
r1 = float(input('Comprimento da primeira reta: '))
r2 = float(input('Comprimento da segunda reta: '))
r3 = float(input('Comprimento da terceira reta: '))
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print(f'As três retas informadas podem produzir um triângulo.')
else:
    print(f'A três retas informadas {r1, r2, r3} não formam um triângulo.')
print('Término da verificação.')