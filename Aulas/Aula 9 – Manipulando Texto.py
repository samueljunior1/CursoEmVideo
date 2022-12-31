'''
Nessa aula, vamos aprender operações com String no Python.
As principais operações que vamos aprender são o:
Fatiamento de String,
Análise com len(), count(), find(),
transformações com replace(), upper(), lower(), capitalize(), title(), strip(),
junção com join().
'''
frase = str('   Curso em vídeo')
print(frase[:12:2])
print(frase.upper().count('o'))
print(len(frase.strip()))
print(frase.replace('Curso', 'Aula'))
print('Curso' in frase) #não mostra a posição, como o find
print(frase.find('Curso'))
divido = frase.split()
print(divido)
print(divido[0][2])