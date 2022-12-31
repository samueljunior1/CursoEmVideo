''' Consegui.
Exercício Python 092:
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

# Minha resposta:

import datetime
from datetime import date

data = datetime.date.today() # Pega o dia, o mês e o ano.
ano = data.year # Pego apenas o ano.

cidadao = {}
cidadao["nome"] = str(input("Nome: "))
cidadao["nascimento"] = int(input("Ano de nascimento: "))
cidadao["idade"] = cidadao["nascimento"] - ano # ou - data.year
pergunta = str(input("Tem CPTS? [S/N]")).strip().upper()[0]
if pergunta in "Ss":
    cidadao["ctps"] = int(input("CPTS: "))
    cidadao["contratacao"] = int(input("Ano de contratação: "))
    cidadao["salario"] = float(input("Salário: "))
    cidadao["aposentadoria"] = 80 - (ano - cidadao["contratacao"]) + cidadao["idade"]
for k, v in cidadao.items():
    print(f"{k}: {v}.")
    print()

'''
from datetime import datetime
dados = dict()
dados["nome"] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: ')) # É uma variável norma, visto que não estará no Dicionário.
dados["idade"] = datetime.now().year - nasc
dados["ctps"] = int(input('Carteira de trabalho (0 = não tem): '))
if dados["ctps"] != 0:
    dados["contratacao"] = int(input('Ano de contratação: '))
    dados["salario"] = float(input('Salário: R$ '))
    dados["aposentadoria"] = dados["idade"] + ((dados["contratacao"] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k} tam o valor {v}.')
print()