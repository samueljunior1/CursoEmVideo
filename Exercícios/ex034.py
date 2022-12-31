''' CONSEGUI FAZER!
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a r$ 1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais o aumento é de 15%.
'''

'''salario_base = float(input('Qual é o seu salário? '))
aumento_alto = float(salario_base * 10 / 100)
ajustado_alto = float(salario_base + aumento_alto)
aumento_baixo = float(salario_base * 15 / 100)
ajustado_baixo = float(salario_base + aumento_baixo)
if salario_base > 1250:
    print(f'O seu salário base é superior a R$ 1.250,00, razão pela qual receberá um aumento de 10%, sendo R$ {ajustado_alto}.')
else:
    print(f'O seu salário base é inferior ou igual a R$ 1.250,00, razão pela qual receberá um aumento de 15%, sendo R$ {ajustado_baixo}.')
print('Término do cálculo.')'''

# Versão do professor:

salario = float(input('Infome-nos o seu salário: '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print(f'Considerando um salário de {salario:.2f}, seu novo salário será de {novo:.2f}.')