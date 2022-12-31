''' Consegui. HEHEHE.
Exercício Python 079:
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
num  = list()
while True:
    numero = int(input(f'Informe um número: '))
    if numero not in num:
        num.append(numero)
        print(f'Valor adicionado com sucesso!')
    else:
        del(numero) # Desnecessário. Professor não usou.
        print(f'Valor duplicado. Desconsiderado pelo sistema.')
    resposta = str(input('Quer continuar [S/N]? ')).upper()[0].strip()
    if resposta in 'Nn':
        break
print(f'--=' * 30)
print(f'Os números digitados foram:', end='')
print(f'{sorted(num)}', end='')