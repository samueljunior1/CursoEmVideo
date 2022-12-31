''' FIZ!!!
Exercício Python 041:
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade:

– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
'''

from datetime import date
nascimento = int(input('Informe-nos o seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nascimento
if idade <= 9:
    categoria = 'MIRIM'
elif idade > 9 and idade <= 14:
    categoria = 'INFANTIL'
elif idade > 14 and idade <= 20:
    categoria = 'JÚNIOR'
elif idade > 19 and idade < 20:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'
print(f'A idade do(a) atleta é {idade} anos, portanto, sua categoria será a \033[1:33m{categoria}\033[m.')
print('Término da categorização')