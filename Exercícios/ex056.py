''' NÃO FIZ.
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
A média de idade do grupo.
Qual é o nome do homem mais velho.
Quantas mulheres tem menos de 20 anos.
'''
soma_idade = 0
maior_idade_homem = 0
homem_velho = ''
totmulheres20 = 0
for c in range(1 , 6):
    print(f'------= {c}ª pessoa =------')
    nome = str(input('NOME: ')).upper().strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO: '))
    soma_idade = soma_idade + idade
    if c == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        homem_velho = nome
    if sexo in 'Mn' and idade > maior_idade_homem:
        maior_idade_homem = idade
        homem_velho = nome
    if sexo in 'Ff' and idade < 20:
        totmulheres20 = totmulheres20 + 1
media = soma_idade / c
print(f'A média da idade do grupo é de {media}.')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {homem_velho}.')
print(f'Há {totmulheres20} com menos de 20 anos.')
