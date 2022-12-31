''' Consegui.
Exercício Python 090:
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
'''
aluno = {}
aluno["nome"] = str(input(f'Nome do aluno: '))
aluno["media"] = float(input(f'Nota do aluno {aluno["nome"]}: '))
if aluno["media"] >= 7:
    aluno["situacao"] = "Aprovado"
elif aluno["media"] >= 5 and aluno["media"] < 7:
    aluno["situacao"] = "Em recuperação"
else:
    aluno["situacao"] = "Reprovado"
print("-=" * 30)
for k, v in aluno.items(): # Conjunto chave e valor.
    print(f' - {k} é igual a {v}')
print()