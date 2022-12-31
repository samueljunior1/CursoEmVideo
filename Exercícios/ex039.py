''' FIZ!!!
Exercício Python 39:
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

from datetime import date
atual = date.today().year
nascimento = int(input('Quando você nasceu? '))
idade = atual - nascimento
print(f'Você nasceu em {nascimento} e tem {idade} anos.')
print('No Brasil, o alistamento militar é obrigatório para jovens com idade igual ou superior a 18 anos!')
if idade < 18:
    alistamento = 18 - idade
    momento = atual + alistamento
    print(f'Seu alistamento militar não é obrigatório! Você deverá se apresentar ao alistamento militar em {alistamento} anos.')
    print(f'Seu alistamento será no ano de {momento}.')
elif idade == 18:
    print('Seu alistamento militar é obrigatório. Apresente-se imediatamente ao \033[1:33mExército\033[m \033[1:32mBrasileiro\033[m.')
    print(f'Você está no ano exato para a feitura do alistamento!')
elif idade > 18:
    alistamento = idade - 18
    momento = atual - alistamento
    print(f'Você está em atraso com o alistamento militar há \033[1:31m{alistamento} anos\033[m.')
    print(f'O ano em que deveria ter se alistado era {momento}.')
print('Término da verificação.')