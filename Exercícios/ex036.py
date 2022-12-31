''' FIZ!!! Dúvidas se está certo.
Exercício Python 36:
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''

print('--=' * 20)
print('Sistema de Aprovação de Crédito')
print('--=' * 20)
valor_casa = float(input('Informe-nos o valor da casa que pretende financiar: '))
salario_comprador = float(input('Informe-nos o seu salário: '))
anos_amortizacao = int(input('Informe-nos em quantos anos pretende amortizar o financiamento: '))
anos = anos_amortizacao * 12
mensalidade = valor_casa / anos
limite = salario_comprador * 30 / 100
print(f'Uma casa no valor de R$ {valor_casa:.2f}, em {anos_amortizacao} anos para pagamento, ou {anos:.1f} meses,\nterá a mensalidade no valor de R$ {mensalidade:.3f}.')
if mensalidade <= limite:
    print(f'Considerando que não houve ultrapassagem ao teto de 30%, seu empréstimo foi DEFERIDO.')
else:
    print('Seu empréstimo foi INDEFERIDO.')
print('Término da análise.')