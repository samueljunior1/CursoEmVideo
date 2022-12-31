''' FIZ!!! Recomendou começar por ele!
Exercício Python 040:
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO
'''

n1 = float(input('Informe-nos sua primeira nota: '))
n2 = float(input('Informe-nos sua segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua média é {m:.2f}.')
if m < 5.0:
    print('Você ficou abaixo de 5.0, portanto, está \033[1:31mREPROVADO\033[m!')
elif m >= 5.0 and m < 7.0:
    print('Você ficou com média entre 5.0 e 6.9, portanto, está de \033[1:33mRECUPERAÇÃO\033[m!')
else:
    print('Você ficou com nota igual ou superior a 7.0. Parabéns!, está \033[1:32mAPROVADO\033[m!')
print('Término da análise.')