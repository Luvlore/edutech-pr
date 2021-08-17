# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
def linhas(texto):
    print('{:—^45}'.format(texto))

def centralizar(texto):
    print('{: ^45}'.format(texto))

def eh_numero(valor):
    try:
         float(valor)
    except ValueError:
         return False
    return True

def media():
    print('\n    1: Para Bimestre\n    2: Para Trimestre\n    3: Para Semestre\n')
    
    while not (periodo := input('  Selecione o seu período: ')).isdigit or (periodo := int(periodo)) < 0 or (periodo := int(periodo)) > 3:
        print('')
        linhas(' Selecione uma opção válida! ')
        print('')
    print('')
    if periodo == 1:
        print('')
        linhas('')
        nota1 = input('    Primeiro bimestre: ')
        while not (eh_numero(nota1)) or (nota1 := float(nota1)) < 0 or (nota1 := float(nota1)) > 10:
            centralizar('Por favor, digite um valor válido!')
        nota2 = input('    Segundo bimestre: ')
        while not (eh_numero(nota2)) or (nota2 := float(nota2)) < 0 or (nota2 := float(nota2)) > 10:
            centralizar('Por favor, digite um valor válido!')
        nota3 = input('    Terceiro bimestre: ')
        while not (eh_numero(nota3)) or (nota3 := float(nota3)) < 0 or (nota3 := float(nota3)) > 10:
            centralizar('Por favor, digite um valor válido!')
        nota4 = input('    Quarto bimeste: ')
        while not (eh_numero(nota4)) or (nota4 := float(nota4)) < 0 or (nota4 := float(nota4)) > 10:
            centralizar('Por favor, digite um valor válido!')
        linhas('')
        print('')
        return (nota1 + nota2 + nota3 + nota4)/4
    elif periodo == 2:
        print('')
        linhas('')
        nota1 = input('    Primeiro trimestre: ')
        while not (eh_numero(nota1)) or (nota1 := float(nota1)) < 0 or (nota1 := float(nota1)) > 10:
            centralizar('Por favor, digite um valor válido!')
        nota2 = input('    Segundo trimestre: ')
        while not (eh_numero(nota2)) or (nota2 := float(nota2)) < 0 or (nota2 := float(nota2)) > 10:
            centralizar('Por favor, digite um valor válido!')
        nota3 = input('    Terceiro trimestre: ')
        while not (eh_numero(nota3)) or (nota3 := float(nota3)) < 0 or (nota3 := float(nota3)) > 10:
            centralizar('Por favor, digite um valor válido!')
        linhas('')
        print('')
        return (nota1 + nota2 + nota3)/3
    elif periodo == 3:
        print('')
        linhas('')
        nota1 = input('    Primeiro semestre: ')
        while not (eh_numero(nota1)) or (nota1 := float(nota1)) < 0 or (nota1 := float(nota1)) > 10:
            centralizar('Por favor, digite um valor válido!')
        nota2 = input('    Segundo semestre: ')
        while not (eh_numero(nota2)) or (nota2 := float(nota2)) < 0 or (nota2 := float(nota2)) > 10:
            centralizar('Por favor, digite um valor válido!')
        linhas('')
        print('')
        return (nota1 + nota2)/2

linhas(' BEM-VINDO ')
linhas('')

while True:
    estudante = input('\n  Qual é o nome do(a) estudante? ').title()
    print(f'  A média das notas de {estudante} é {media():0.1f}\n')

    resp = ' '  
    while resp not in 'SN':
        linhas('')
        resp = str(input('  Deseja verificar mais alguma? [S/N] ')).strip().upper()[0]
        linhas('')
    if resp == 'N':
        break
linhas(' FIM DO PROGRAMA')
