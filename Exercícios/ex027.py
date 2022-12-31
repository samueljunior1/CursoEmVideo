''' FIZ INCOMPLETO.
Exercício Python 27:
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o
último nome, separadamente.

Ex.: Ana Maria de Souza.
Primeiro: Ano.
último: Souza.

'''

nomec = str(input('Insira seu nome completo: ')).strip()
dividido = nomec.split()
prenome = dividido[0]
sobrenome = dividido[-1]
print(f'O prenome será {prenome}, o sobrenome é {sobrenome}.')