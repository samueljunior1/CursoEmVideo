''' NÃO SOUBE O ÚLTIMO, NÃO TENTAREI ESTE.
Exercício Python 62:
Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
'''

primeiro = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
termo = primeiro
contador = 1
total = 0
mais = 10
print(f'Considerando o termo inicial como sendo o número {primeiro}, e a razão {razao}, os 10 primeiros números serão:')
while mais != 0:
    total = total + mais
    while contador <= total:
        print(f'{termo} -> ', end='')
        termo = termo + razao
        contador = contador + 1
    print('PAUSA!')
    mais = int(input(f'Quantos termos você quer mostrar a mais: '))
print(f'Progresso finalizada com {total} termos mostrados.')
print(f'FIM.')