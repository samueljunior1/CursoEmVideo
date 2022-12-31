''' Fiz de forma duvidosa.
Exercício Python 086:
Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.

Minha versão:

l1 = [[], [], []]
l2 = [[], [], []]
l3 = [[], [], []]
c = 0
for v in range(1, 10):
    valores = int(input(f'Informe o {v}º valor: '))
    c = c + 1
    if c == 1:
        l1[0].append(valores)
    else:
        if c == 2:
            l1[1].append(valores)
        if c == 3:
            l1[2].append(valores)
        if c == 4:
            l2[0].append(valores)
        if c == 5:
            l2[1].append(valores)
        if c == 6:
            l2[2].append(valores)
        if c == 7:
            l3[0].append(valores)
        if c == 8:
            l3[1].append(valores)
        if c == 9:
            l3[2].append(valores)
print(l1)
print(l2)
print(l3)

'''
# Versão do professor.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Informe o valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:5}]', end='')
    print()