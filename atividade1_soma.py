def eh_numero(valor):
    try:
         float(valor)
    except ValueError:
         return False
    return True 

def operacoes():
    print('Digite 1 para Adição;\nDigite 2 para Subtração;\nDigite 3 para Multiplicação;\nDigite 4 para Divisão.\n')
    while not (nome := input('Selecione sua Operação:')).isdigit() or (nome := int(nome)) < 0 or (nome := int(nome)) > 4:
        print('\nPor favor, selecione uma opção válida!')
    if nome == 1:
        print('\nVocê escolheu Adição.')
        num1 = input("\nDigite seu primeiro número: ")
        while not eh_numero(num1) or not (num1 := float(num1)):
            print('Por favor, digite um valor válido!')
        num2 = input("Digite seu segundo número: ")
        while not eh_numero(num2) or not (num2 := float(num2)):
            print('Por favor, digite um valor válido!')
        return f'\nA soma de {num1} e {num2} é {num1 + num2}.'
    elif nome == 2:
        print('\nVocê escolheu Subtração.')
        num1 = input("\nDigite seu primeiro número: ")
        while not eh_numero(num1) or not (num1 := float(num1)):
            print('\nPor favor, digite um valor válido!')
        num2 = input("Digite seu segundo número: ")
        while not eh_numero(num2) or not (num2 := float(num2)):
            print('Por favor, digite um valor válido!')
        return f'A subtração de {num1} e {num2} é {num1 - num2}.'
    elif nome == 3:
        print('\nVocê escolheu Multiplicação.')
        num1 = input("\nDigite seu primeiro número: ")
        while not eh_numero(num1) or not (num1 := float(num1)):
            print('Por favor, digite um valor válido!')
        num2 = input("Digite seu segundo número: ")
        while not eh_numero(num2) or not (num2 := float(num2)):
            print('Por favor, digite um valor válido!')
        return f'\nA multiplicação de {num1} e {num2} é {num1*num2}.'
    elif nome == 4:
        print('\nVocê escolheu Divisão.')
        num1 = input("\nDigite seu primeiro número: ")
        while not eh_numero(num1) or not (num1 := float(num1)):
            print('Por favor, digite um valor válido!')
        num2 = input("Digite seu segundo número: ")
        while not eh_numero(num2) or not (num2 := float(num2)):
            print('Por favor, digite um valor válido!')
        return f'\nA divisão de {num1} e {num2} é {num1/num2}.'
    else:
        return '\nValor Inválido'

while True:
    print(operacoes())

    resp = ' '
    while resp not in 'SN':
        resp = str(input('\nDeseja realizar outra operação? [S/N] ')).strip().upper()[0]
        print('')
    if resp == 'N':
        break
