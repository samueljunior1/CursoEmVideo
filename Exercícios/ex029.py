''' CONSEGUI FAZER.
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h., mostre uma mensagem dizendo que ele foi multado.
Amulta vai custar R$ 7.00 por cada km. acima do limite.
'''

velocidade = float(input('Informe-nos a velocidade: '))
ultrapassado = velocidade - 80
multa = 7 * ultrapassado
if velocidade > 80:
    print(f'Você ultrapassou a velocidade permitida, portanto, foi multado!')
    print(f'''Considerando que a cada km excedido, há a cobrança de R$ 7.00,
    considerando que você ultrapassou em {ultrapassado:.2f}KM/H o autorizado,
    a multa estipulada foi de R$ {multa:.2f}.''')
else:
    print(f'Sua velocidade foi de {velocidade}KM/H, estando dentro do limite legal.')
print('Término da análise!!!')