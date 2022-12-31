'''
Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python.
As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura,
acessíveis por chaves individuais.

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste) # há uma ligação.
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:]) # há uma cópia.
print(galera)

*** outra forma de declarar.

galera = [['João', 12], ['Lucas', 13], ['Lauro', 22], ['Paulo', 34]]
print(galera)
print(galera[0]) # Apenas os dados de João, 12.
print(galera[0][0]) # Apenas o nome João.

for pessoa in galera:
    print(pessoa) # Caso eu queira apenas os nomes - print(pessoa[0])
    print(f'pessoa[0] tem {pessoa[1]} anos.')

galera = list()
dado = []
totmaior = totmenor = 0
for c in range (0, 3):
    dado.append(str(input('Informe o nome: ')))
    dado.append(int(input('Informa a idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)

*** Mostrar só quem tem acima de tantos anos.

for pessoa in galera:
    if pessoa[1] >= 18:
        print(f'pessoa[0] é maior de idade.')
        totmaior = totmaior + 1
    else:
        print(f'pessoa[0] é menor de idade.')
        totmenor = totmenor + 1
print(f'Temos {totmaior} pessoas maiores de idade e {totmenor} menores de idade.')

'''