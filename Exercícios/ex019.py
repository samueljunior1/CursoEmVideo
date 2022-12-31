
'''
Exercício Python 19:
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
'''

'''
import random
nome1 = str(input('Nome do aluno 1: '))
nome2 = str(input('Nome do aluno 2: '))
nome3 = str(input('Nome do aluno 3: '))
nome4 = str(input('Nome do aluno 4: '))
#sorteado = random.randint(1, 4)
print(f'Possibilidades: \nAluno 1: {nome1} \nAluno 2: {nome2} \nAluno 3: {nome3} \nAluno 4: {nome4}')
print(f'O aluno sorteado foi o de número {sorteado}')
'''

import random
nome1 = str(input('Nome do aluno 1: '))
nome2 = str(input('Nome do aluno 2: '))
nome3 = str(input('Nome do aluno 3: '))
nome4 = str(input('Nome do aluno 4: '))
lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)
print(f'O aluno sorteado foi: {random.choice(lista)}')

