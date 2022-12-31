''' Olhei na internet a forma de converter!!! A estrutura eu que fiz.
ASSUNTO NÃO ABORDADO NA AULA. Recomendou olhar as respostas.
Exercício Python 37:
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal.
'''

print('--=' * 20)
print('Vamos converter?')
print('--=' * 20)
n = int(input('Informe um número: '))
print('''Escolha sua base de conversão:
1 - Binário
2 - Octal
3 - Hexadecimal
''')
base_de_conversao = int(input('Selecione a base de conversão:\n1 para Binário. \n2 para Octal. \n3 para Hexadecimal.'))
if base_de_conversao == 1:
    #fazer cálculo para binário.
    base_nome = 'binário'
    convertido = (bin(n)[2:])
elif base_de_conversao == 2:
    #fazer cálculo para octal.
    base_nome = 'octal'
    convertido = (oct(n)[2:])
elif base_de_conversao == 3:
    #fazer cálculo para hexadecimal.
    base_nome = 'hexadecimal'
    convertido = (hex(n)[2:])
else:
    print('Número inválido.')
print(f'O número {n} convertido para \033[1:33m{base_nome}\033[m é \033[1:32m{convertido}\033[m.')
print('Término da análise.')