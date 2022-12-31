'''
Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em Python.
Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura,
acessíveis por chaves literais.
'''
pessoa = {'nome': 'Samuel', 'sexo': 'O', 'idade': 26} # No momento de declarar os elementos uso chaves.
print(pessoa['nome'])
print(f'O {pessoa["nome"]} tem {pessoa["idade"]} anos.') # No momento de referenciar os elementos uso colchetes.
print(pessoa.keys()) # Chaves
print(pessoa.values()) # Valores
print(pessoa.items()) # Items - é a composição dos elementos, a própria "lista" [] composta por tuplas ().

# Acessando os items, chaves e valores através do laço.
for k in pessoa.keys():
    print(k)
for v in pessoa.values():
    print(v)
for i in pessoa.items():
    print(i)
for k, v in pessoa.items(): # No dicionário não temos o enumerate como nas Tuplas e nas Listas.
    print(k, end=' ')
    print(v)
    print(f'{k} = {v}')
del(pessoa['sexo']) # Apaga tanto a chave quando o valor.
print(pessoa)
pessoa['nome'] = 'Leandro' # Alteração de valores.
pessoa['peso'] = 67.4 # Não se adiciona através do append. Basta informar o inexistente.
print(pessoa)

# Colocando dicionários dentro de listas.

brasil = []
estado1 = {'UF': 'Minas Gerais', 'sigla': 'MG'}
estado2 = {'UF': 'Ceará', 'sigla': 'CE'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil) # Mostrará a lista [] com os dois dicionários {} declarados.
print(brasil[0]) # Primeiro dicionário.
print(brasil[0]['UF']) # Mostrará a chave UF do primeiro dicionário.
print(brasil[1]['sigla'])

# Outro momento.

estado = dict() # Ou {}
brasil = list() # Ou []
for c in range (0, 3):
    estado['UF'] = str(input('Informe a unidade federativa: '))
    estado['sigla'] = str(input('Informe a sigla: '))
  # brasil.append(estado[:]) # Assim como nas listas, é preciso fazer a cópia do elemento, entretanto, não é possíver usar o fatiamento [:].
    brasil.append(estado.copy()) # Método interno próprio.
print(brasil)

for e in brasil: # Cada Estado é um dicionário dentro da lista Brasil.
    print(e)
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
        # Ou:
    for v in e.values():
        print(v, end= ' ')
    print()