'''
Nessa aula, vamos aprender como criar estruturas condicionais aninhadas, usando os comandos if.. elif.. else em programas Python.
'''
nome = str(input('Qual é o seu nome? '))
if nome == 'Samuel':
    print('Que nome belíssimo, Samuel!')
elif nome == 'Luan' or nome == 'Pablo' or nome == 'Laura':
    print('Nome diferente.')
elif nome in 'Lucia Ana Tereza':
    print('Nome bem feio.')
else:
    print('Seu nome é bem básico!')
print(f'Tenha um ótimo dia, {nome}!')