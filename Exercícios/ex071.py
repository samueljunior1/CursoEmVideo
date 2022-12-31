''' FIZ APÓS OLHAR A LÓGICA NA INTERNET, estava diferente, refiz pela do professor.
Exercício Python 071:
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''
from time import sleep
print(f"#{'TERMINAL':^40}#")
print("#{:^40}#".format("CAIXA S.A"))
saque = int(input(f'Qual o valor do saque: R$ '))
total = saque
ced = 50
total_ced = 0
while True:
    if total >= ced:
        total = total - ced
        total_ced = total_ced + 1
    else:
        if total_ced > 0:
            print(f'Total de {total_ced} cédulas de {ced} reais.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_ced = 0
        if total == 0:
            break
print(f"#{'DADOS':^40}#")
print('--==-' * 2, "TRANSAÇÃO FINALIZADA" , '-==--' * 2)