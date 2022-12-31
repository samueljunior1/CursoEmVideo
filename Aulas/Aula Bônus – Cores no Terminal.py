'''
Nessa aula, vamos aprender como utilizar os códigos de escape sequence ANSI para configurar cores para os seus programas em Python.
Veja como utilizar o código \033[m com todas as suas principais possibilidades.

style:
0 = none
1 = bold negritado
4 = sublinhado - underline
7 = inverter - negative

color:

30 = branco
31 = vermelho
32 = verde
33 = amarelo
34 = azul escuro
35 = magenta
36 = azul ciano
37 = cinza

back:

40 = branco
41 = vermelho
42 = verde
43 = amarelo
44 = azul escuro
45 = magenta
46 = azul ciano
47 = cinza

Desafio da aula: Selecionar dez exercícios anteriores e adicionar cores a eles.
Desafio master: fazer um dicionário de cores em todos os trinta e cinco exercícios.

'''

''''\033[0;30;41m
\033[4;33;44m
\033[1;35;43m
\033[30;42m
\033[m
\033[7;30m'''

print('\033[1;30;45mOlá, mundo!\033[m')
a = 1
b = 2
print(f'Os valores são \033[32m{a}\033[m e \033[33m{b}\033[m.')

nome = 'Samuel'
cores = {'limpa': '\033[m',
         'zul': '\033[34m',
         'amarelo': '\033[33m',
         'preto e branco': '\033[7;30m'}
#print('Muito prazer em conhecê-lo, {}{}{}.'.format('\033[4;33m', nome, '\033[m'))
print('Muito prazer em conhecê-lo, {}{}{}.'.format(cores['azul'], nome, cores['limpa']))