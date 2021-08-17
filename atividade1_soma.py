# Faça um Programa que peça dois números e imprima a soma
def operacoes():
    nome = int(input('Digite 1 para Adição;\nDigite 2 para Subtração;\nDigite 3 para Multiplicação;\nDigite 4 para Divisão.\n'))
    if nome == 1:
        print('\nVocê escolheu Adição.')
        num1 = int(input("\nDigite seu primeiro número: "))
        num2 = int(input("Digite seu segundo número: "))
        return f'A soma de {num1} e {num2} é {num1+num2}.'
    elif nome == 2:
        print('\nVocê escolheu Subtração.')
        num1 = int(input("\nDigite seu primeiro número: "))
        num2 = int(input("Digite seu segundo número: "))
        return f'A subtração de {num1} e {num2} é {num1-num2}.'
    elif nome == 3:
        print('\nVocê escolheu Multiplicação.')
        num1 = int(input("\nDigite seu primeiro número: "))
        num2 = int(input("Digite seu segundo número: "))
        return f'A multiplicação de {num1} e {num2} é {num1*num2}.'
    elif nome == 4:
        print('\nVocê escolheu Divisão.')
        num1 = int(input("\nDigite seu primeiro número: "))
        num2 = int(input("Digite seu segundo número: "))
        return f'A divisão de {num1} e {num2} é {num1/num2}.'
    else:
        return '\nValor Inválido'


while True:
    print(operacoes())

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja realizar outra operação? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
