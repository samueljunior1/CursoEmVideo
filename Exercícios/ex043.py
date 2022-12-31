''' FIZ!!!
Exercício Python 43:
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida
'''

peso = float(input('Informe-nos o seu peso: '))
altura = float(input('Informe-nos sua altura: '))
imc = peso / (altura ** 2)
print(f'Seu IMC é de {imc:.2f}')
if imc < 18.5:
    print(f'O seu IMC é de {imc:.1f}, portanto, está abaixo do peso ideal.')
elif imc >= 18.5 and imc < 25:
    print(f'O seu IMC é de {imc:.1f}, portanto, seu peso está ideal.')
elif imc >= 25 and imc < 30:
    print(f'O seu IMC é de {imc:.1f}, portanto, está em sobrepeso.')
elif imc >= 30 and imc < 40:
    print(f'O seu IMC é de {imc:.1f}, portanto, encontra-se em obesidade.')
else:
    print(f'O seu IMC é de {imc:.1f}, acima de 40, estando, portanto, com obesidade mórbida.')
print('Término da análise.')