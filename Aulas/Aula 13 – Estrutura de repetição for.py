'''
Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o “for”,
que é uma estrutura versátil e simples de entender. Por exemplo:

for c in range(0, 4):
    print(c)
print(‘Acabou’)


for c in range(0,10):
    print('Oi')
print('FIM!')


i = int(input('Digite um número: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f + 1, p):
    print(c)
print('FIM!')

'''
s = 0
for c in range(0, 3):
    n = int(input('Digite um número: '))
    s = s + n
print(f'O somatório de todos os valores foi {s}.')



