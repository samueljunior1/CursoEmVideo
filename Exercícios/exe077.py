'''
Exercício Python 077:
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''
palavras = ('esperanca',
            'amor',
            'paz',
            'sabedoria',
            'aprendizado',
            'resiliencia')

for p in palavras: # No primeiro laço o que se analisa são os elementos presentes na Tupla.
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p: # No segundo laço a análise será das letras de cada palavra (cada palavra é uma lista).
        if letra.upper() in 'AEIOU': # Posso colocar as variações acentuadas.
            print(letra, end=' ')
print('FIM.')
