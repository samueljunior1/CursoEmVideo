''' FIZ!!!
Exercício Python 69:
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
'''
from time import sleep
homens = 0
mulheres_m20 = 0
total_m18 = 0
while True:
    idade = int(input('Informe sua idade: '))
    sexo = ' '
    while sexo not in 'HMO':
        sexo = str(input('Informe seu sexo [H/M/O]: ')).strip().upper()[0]

    ### DESCOBRIR SE É HOMEM...
    if sexo in 'Hh':
        homens = homens + 1

    ### DESCOBRIR SE É MULHER E SE TEM MENOS QUE 20 ANOS.
    if sexo in 'Mm' and idade < 20:
        mulheres_m20 = mulheres_m20 + 1

    ### DESCOBRIR O TOTAL COM MAIS DE 18 ANOS
    if idade >= 18:
        total_m18 = total_m18 + 1

    ### PERGUNTA DE CONTINUAR
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Você gostaria de continuar [S/N]? ')).strip().upper()[0]
    if pergunta not in 'S':
        break

    print(f'Registrando...')
    sleep(1)

print(f'PROCESSANDO DADOS...')
sleep(2)

print(f'=-=' * 15)
print(f'Foram cadastrados {homens} homens na plataforma.')
print(f'Das mulheres cadastradas, {mulheres_m20} tem menos que 18 anos.')
print(f'No total, {total_m18} pessoas têm 18 anos ou mais.')
print(f'=-=' * 15)
