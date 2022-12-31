''' NEM IDEIA.
Exercício Python 61:
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''
primeiro = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
termo = primeiro
contador = 1
print(f'Considerando o termo inicial como sendo o número {primeiro}, e a razão {razao}, os 10 primeiros números serão:')
while contador <= 10:
    print(f'{termo} -> ', end='')
    termo = termo + razao
    contador = contador + 1
print('FIM!')