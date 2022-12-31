'''
Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python.
As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura,
acessíveis por chaves individuais.

*** PRIMEIROS EXEMPLOS ***

num = (1, 2, 3, 4) # Tuplas são imutáveis.
#num[3] = 6
print(num)

número = [1, 2, 3, 4]
número[2] = 8 # Listas são mutáveis.
# número[4] = 5 ! Erro. Não é possível adicionar valores dessa forma.
número.append(5) # Append adiciona ao final da Lista.
número.insert(1, 0) # insere um valor em posição especificada (diversamente de append)
número.sort() # Ordena em sequência.
número.sort(reverse=True) # Ordena em sequência inversa.
número.pop() # Se não há parâmetro, remove o últivo valor.
número.pop(2) # Remove o elemento que está na posição dois.
número.remove(2) # Remove um elemento específico. Se houver mais de um elemento, removerá o PRIMEIRO. Ou seja, o remove procura apenas a primeira ocorrência da lista.
if 4 in número:
    número.remove(4) # Se o número a ser removido não existir, posso evitar o erro usando uma condicional IF.
else:
    print('Não encontrei o número 4.')
print(número)
print(f'Essa lista tem {len(número)} elementos.')


# Recebendo valores pelo teclado.

for cont in range(0, 5):
    valores = valores.append(int(input(f'Informe um valor:')))

'''

valores = [] # Também é possível começar uma Lista vazia assim: list()
valores.append(5)
valores.append(9)
valores.insert(0, 4)
print(valores)
for v in valores: # Para cada valor em valores. c = chave (índice).
    print(f'{v}...')

for c, v in enumerate(valores): # Para cada valor em valores. c = chave (índice). O enumerate pega tanto a chave quanto o valor.
    print(f'Na posição {c} tem o valor {v}')
print('Cheguei ao final da lista!')

# Peculiaridade do Python para Listas.

a = [1, 2, 3, 4]
b = a # A partir do momento em que eu igualo uma Lista em outra, o Python cria uma ligação entre elas.
b = a[:] # CÓPIA. Posso contornar a "ligação" que o igual provoca utilizando-se do fatiamento. Fazer com que B receba todos os itens de A.
b[2] = 8 # Mudará tudooo.
print(f'A lista a é {a}')
print(f'A lista b é {b}')
