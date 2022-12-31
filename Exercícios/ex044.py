''' FIZ!!!
Exercício Python 44:
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço normal

– 3x ou mais no cartão: 20% de juros
'''
print(f'{"Lojas Gunabara":=^40}')
pn = float(input('Informe o preço normal do produto: '))
print('''[1] para à vista dinheiro/cheque.
[2] à vista nocartão.
[3] 2x no cartão e
[4] 3x ou mais no cartão.''')
cp = int(input('Indique a forma de pagamento:'))
if cp == 1:
    valorfinal = pn - (pn * 10 / 100)
elif cp == 2:
    valorfinal = pn - (pn * 5 / 100)
elif cp == 3:
    valorfinal = pn
    parcela = valorfinal / 2
    print(f'Sua compra será parcelada em 2x de R$ {parcela:.2f}, SEM JUROS.')
elif cp == 4:
    valorfinal = pn + (pn * 20/100)
    total_parcela = int(input('Total de parcelas: '))
    parcela = valorfinal / total_parcela
    print(f'Sua compra será parcelada em {total_parcela}x de R$ {parcela:.f}, COM JUROS.')
else:
    print('Opção inválida.')
print(f'Considerando o valor originário do produto de {pn:.2f}, bem como sua opção de pagamento, o valor final a ser pago será de R$ \033[1:36m{valorfinal:.2f}\033[m. Agradecemos pela preferência!')
