''' Não consegui.
Exercício Python 094:
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) A média de idade.
C) Uma lista com as mulheres.
D) Uma lista de pessoas com idade acima da média.
'''
galera = []
pessoa = {}
soma = media = 0 # Duas variáveis distintas.
while True:
    pessoa.clear()
    pessoa["nome"] = str(input('Nome: '))
    while True:
        pessoa["sexo"] = str(input('Sexo: ')).strip().upper()[0]
        if pessoa["sexo"] in 'MmFfOo':
            break
        print('ERRO! Informe uma opção válida.')
    pessoa["idade"] = int(input('Idade: '))
    soma = soma + pessoa["idade"] # A soma das idades será realizada a cada leitura.
    galera.append(pessoa.copy()) # Prof. havia errado!
    while True:
        pergunta = str(input('Quer continuar[S/N]? ')).strip().upper()[0]
        if pergunta in 'SsNn':
            break
        print('ERRO! Responda apenas sim ou não.')
    if pergunta in "Nn": # Dúvida! Prof. usou "== s", entendo que seria IGUAL a n para parar. == não foi aceito. Entendi o porquê, usei a variação maiúsculo/minúsculo.
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.') # Não usou o contador. Len mostra o quantitativo de dicionários internos à lista "galera".
media = soma / len(galera) # Soma das idades divida pelo quantitativo de pessoas.
print(f'B) A média das idades é {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end=" ")
for p in galera: # Galera é a lista, o conjunto de dicionários.
    if p["sexo"] == 'F': # Agora usei o == (visto inexistir variação).
        print(f'{p["nome"]} ', end=' ')
print()
print(f'D) lista das pessoas que estão acima da média: ', end=" ")
for p in galera: # Galera é a lista, o conjunto de dicionários. Só não entendo como esse "p" consegue ver as chaves dos dicionários.
    if p["idade"] >= media:
        print('     ', end=" ")
        for k, v in p.items():
            print(f'{k} = {v}; ', end=' ')
        print()
print('<<< ENCERRADO >>>')







