''' FIZ!!!
Exercício Python 45:
Crie um programa que faça o computador jogar Jokenpô com você.
'''
from time import sleep
import random
print('--=' * 20)
print('Vamos jogar jokenpô?')
print('--=' * 20)
print('Eu começo... pensando!')
sleep(2)
escolha_pc = random.choice(['PEDRA', 'PAPEL', 'TESOURA'])
print('Estou pronto! Agora é com você.')
escolha_user = str(input('Faça uma escolha: pedra, papel ou tesoura?')).upper().strip()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)
if escolha_pc == 'pedra' and escolha_user == 'tesoura':
    print(f'Eu ganhei! Escolhi {escolha_pc}, pedra ganha da tesoura (amassando-a ou quebrando-a).')
elif escolha_pc == 'tesoura' and escolha_user == 'papel':
    print(f'Eu ganhei! Escolhi {escolha_pc}, tesoura ganha do papel (cortando-o).')
elif escolha_pc == 'papel' and escolha_user == 'pedra':
    print(f'Eu ganhei! Escolhi {escolha_pc}, papel ganha da pedra (embrulhando-a).')
elif escolha_pc == escolha_user:
    print(f'HAHA, nós empatamos! Também escolhi {escolha_user}. Vamos de novo?')
else:
    print(f'Você ganhou! Escolhi {escolha_pc}.')
print('--=' * 20)