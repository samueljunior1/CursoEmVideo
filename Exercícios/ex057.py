''' FIZ com muito custo.
Exercício Python 57:
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
sexo = str(input(f'Informe o seu gênero corretamente [H/M/O]: ')).upper()[0].strip()
while sexo not in 'HhMmOo':
    sexo = str(input(f'Informe o seu gênero corretamente [H/M/O]: ')).upper()[0].strip()
print(f'O gênero {sexo} foi informado corretamente. FIM!')
print(f'--=' * 20)