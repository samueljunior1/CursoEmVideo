''' FIZ!!!
Exercício Python 059:
Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''
from time import sleep
valor1 = int(input(f'Informe-nos o primeiro valor: '))
valor2 = int(input(f'Informe-nos o segundo valor: '))
escolha = ''
while escolha != 5:
    escolha = int(input('[1] somar \n[2] multiplicar \n[3] maior \n[4] novos números \n[5] sair do programa'))
    if escolha == 1:
        soma = valor1 + valor2
        print(f'Segundo sua opção, a soma de {valor1} e {valor2} é {soma}.')
    elif escolha == 2:
        multiplicacao = valor1 * valor2
        print(f'Segundo a sua escolha, {valor1} x {valor2} é {multiplicacao}')
    elif escolha == 3:
        if valor1 > valor2:
            print(f'O maior valor é {valor1}.')
        else:
            print(f'O maior valor é {valor2}.')
    elif escolha == 4:
        print(f'Informe os números novamente: ')
        valor1 = int(input(f'Informe-nos o primeiro valor: '))
        valor2 = int(input(f'Informe-nos o segundo valor: '))
    elif escolha == 5:
        print(f'Você escolheu sair do programa, obrigado!')
    else:
        print(f'Opção inválida!')
    sleep(2)
print(f'Programa encerrado.')