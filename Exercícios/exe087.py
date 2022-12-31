''' Não consegui.
Exercício Python 087:
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
maior = 0
somacoluna = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Informe o valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:5}]', end='')
        if matriz[l][c] % 2 == 0:
            pares = pares + matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {pares}.')
# Como a coluna é fixa (2) [0, 2][1, 2][2, 2], fazer um for apenas para a linha.
for l in range(0, 3):
    somacoluna = somacoluna + matriz[l][2]
print(f'A soma da terceira coluna é {somacoluna}.')
# Agora é a linha que está sempre fixa (1) [1, 0][1, 1][1, 2], fazer um for apenas para a coluna.
for c in range(0, 3):
    if c == 0: # Primeira coluna.
        maior = matriz[1][c]
    elif matriz[1][c] > maior: # Poderia ter utilizado o ou.
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}.')