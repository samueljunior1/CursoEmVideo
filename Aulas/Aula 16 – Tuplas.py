'''
Nessa aula, vamos aprender o que são TUPLAS e como utilizar tuplas em Python.
As tuplas são variáveis compostas e imutáveis que permitem armazenar vários valores em uma mesma
estrutura, acessíveis por chaves individuais.

() tupla
[] lista
{} dicionário

*** PRIMEIROS EXEMPLOS DA AULA ***

lanches = ('Hambúrguer', 'suco', 'pizza', 'pudim', 'Batata frita')
# Tuplas são imutáveis.
# lanches[1] = 'refrigerante'
print(len(lanches))

for cont in range(0, len(lanches)):
    print(f'Eu vou comer {lanches[cont]} na posição {cont}')

print(lanches[1:3]) # no fatiamento o último item é ignorado.

for comida in lanches:
    print(f'Eu vou comer {comida}') # Seu eu não precisar da posição.

for pos, comida in enumerate(lanches):
    print(f'Eu vou comer {comida} na posição {pos}')

print(sorted(lanches)) # sorted = organizado. Em ordem alfabética. Irá tranformar em LISTA.
print(lanches) # a Tupla permanece IMUTÁVEL.

print(f'Comi demais!!!')
'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b # A tupla C não é a mesma coisa que b + a. A ordem tem influência.
print(a)
print(b)
print(sorted(c))
print(len(c))
print(c.count(5))
print(c)
print(c.index(2, 4)) # pega a primeira ocorrência (caso haja repetições). Usar o DESLOCAMENTO.

pessoa = ('Samuel', 28, 'M', 56.45, 'Brasileiro') # Diversamente dos "vetores", em Java, as Tuplas de Python podem ter tipos DIFERENTES.
# del(pessoa) # Apaga a tupla.
del(pessoa[0]) # Partindo da regra de que as tuplas são imutáveis, só é possível apagá-las por completo.
print(pessoa)



