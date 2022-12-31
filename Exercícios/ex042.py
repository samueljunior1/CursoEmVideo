''' NÃO CONSEGUI FAZER!

Recomendou assistir a correção do exercício, pois é uma forma diversa de aninhamento.

Exercício Python 42:
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes

'''

print('--=' * 20)
print('Analisador de triângulos')
print('--=' * 20)
r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2): #Não aprendi isso.
    print(f'As retas {r1}, {r2} e {r3} formam um triângulo.')
    if r1 == r2 and r1 == r3 and r2 == r3:
        print('Considerando que todos os lados são iguais, temos um triângulo equilátero.')
    elif r1 == r2 and r1 == r3 or r2 == r1 and r2 == r3 or r3 == r1 and r3 == r2: #Não soube fazer!
        print('Considerando que há dois lados iguais, temos um triângulo Isóceles.')
    elif r1 != r2 and r1 != r3 and r2 != r1 and r2 != r3 and r3 != r1 and r3 != r2:
        print('Considerando que todos os lados são diferentes, temos um triângulo escaleno.')
else:
    print(f'As retas {r1}, {r2} e {r3} não formam um triângulo!')
print('Término da análise.')