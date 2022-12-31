''' Nem ideia.
Exercício Python 083:
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
e fechados na ordem correta.
'''

expressao = str(input('Informe uma expressão que use parênteses: '))
pilha = list()
for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
print('-=' * 30)
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão é inválida!')

