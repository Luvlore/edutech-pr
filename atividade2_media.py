# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
def linhas(texto):
    print('{:—^45}'.format(texto))

def centralizado(texto):
    print('{: ^45}'.format(texto))

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
        nota1 = float(input('    Primeiro bimestre: '))
        nota2 = float(input('    Segundo bimestre: '))
        nota3 = float(input('    Terceiro bimestre: '))
        nota4 = float(input('    Quarto bimeste: '))
        linhas('')
        print('')
        return (nota1 + nota2 + nota3 + nota4)/4
    elif periodo == 2:
        print('')
        linhas('')
        nota1 = float(input('  Primeiro trimestre: '))
        nota2 = float(input('  Segundo trimestre: '))
        nota3 = float(input('  Terceiro trimestre: '))
        linhas('')
        print('')
        return (nota1 + nota2 + nota3)/3
    elif periodo == 3:
        print('')
        linhas('')
        nota1 = float(input('  Primeiro semestre: '))
        nota2 = float(input('  Segundo semestre: '))
        linhas('')
        print('')
        return (nota1 + nota2)/2

linhas(' BEM-VINDO ')
linhas('')

while True:
    estudante = input('\n  Qual é o nome do(a) estudante? ').title()
    print(f'  A média das notas de {estudante} é {media():0.1f}')

    resp = ' '  
    while resp not in 'SN':
        linhas('')
        resp = str(input('  Deseja verificar mais alguma? [S/N] ')).strip().upper()[0]
        linhas('')
    if resp == 'N':
        break
linhas(' FIM DO PROGRAMA')
