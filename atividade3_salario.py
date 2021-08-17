def reajuste(salario):
    if salario <= 280:
        percentual = 0.2
        aumento = salario * percentual
        novo_salario = salario + aumento
    elif salario > 280 and salario <= 700:
        percentual = 0.15
        aumento = salario * percentual
        novo_salario = salario + aumento
    elif salario > 700 and salario <= 1500:
        percentual = 0.1
        aumento = salario * percentual
        novo_salario = salario + aumento
    else:
        percentual = 0.05
        aumento = salario * percentual
        novo_salario = salario + aumento


    linhas('')
    print(f'  Antes do reajuste:           R${salario :0.2f}')
    print(f'  O percentual aumentado:      {percentual * 100 :0.0f}%')
    print(f'  O valor do aumento:          R${aumento :0.2f}')
    print(f'  O novo salário:              R${novo_salario :0.2f}')
    linhas('')

def linhas(texto):
    print('{:—^45}'.format(texto))

def pula_linha():
    print('{: ^45}'.format(''))

def erro():
    pula_linha()
    linhas('')
    linhas('    Por favor, informe um valor válido!  ')
    linhas('')
    pula_linha()

def eh_numero(valor):
    try:
         float(valor)
    except ValueError:
         return False
    return True

linhas(' BEM-VINDO ')

while True:
    pula_linha()
    salario = input('  Informe o salário:           R$')
    while not eh_numero(salario) or (salario := float(salario)) < 0:
        erro()
        salario = input('  Informe o salário:           R$')

    pula_linha()
    reajuste(salario)

    resp = ' '  
    while resp not in 'SN':
        pula_linha()
        resp = str(input('  Deseja verificar mais algum? [S/N] ')).strip().upper()[0]
        pula_linha()
        linhas('')
    if resp == 'N':
        break
linhas(' FIM DO PROGRAMA ')
