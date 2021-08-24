    #funções para deixar a excução do código show
def risquinhos():
    print('—'*51)

def centralizado(texto):
    print(f'{texto:^51}')

def pula_linha():
    print('')

def formatacao(texto):
    risquinhos()
    pula_linha()
    centralizado(texto)
    pula_linha()
    risquinhos()

    #variáveis
listagem =  ['Misto-Quente', 'Cachorro-Quente', 'Coxinha', 'Hamburgão', 'X-Burguer','X-Salada', 'X-Tudo', 'Refrigerante', 'Suco', 'Água', 'Água c/Gás', 'Café', 'Café c/Leite']
precos = [3, 4.5, 3, 3.5, 6, 7.5, 14, 4.5, 3.5, 2, 2, 3, 3]

    #valores
valor_total = 0
valor_item = 0

    #execução do código
while True:
        #título
    risquinhos()
    centralizado('CARDÁPIO DA LANCHONETE')
    risquinhos()

    #cardápio
    print(f'  LISTA\t\t     CÓDIGOS\t\t   PREÇOS\n')
    for codigo, pos in enumerate(range(len(listagem))):
        print(f'  {listagem[pos]:.<20}', f'{codigo + 1:03}','.'*13, f'R${precos[pos]:6.2f}')
    pula_linha()

    risquinhos()
    while not (codigo := input(' Digite o código do que deseja comprar\n Ou digite 0 a qualquer momento para cancelar: ')).strip().isdigit() or (codigo := int(codigo)) not in list(range(len(listagem) + 1)):
        formatacao('Por favor, digite um valor válido.')

    if codigo == 0:
        risquinhos()
        break

    formatacao(f'Você escolheu {listagem[codigo-1]}')
    
    while not (quantidade := input(' Digite a quantidade que deseja comprar: ')).strip().isdigit() or (quantidade := int(quantidade)) < 0:
        formatacao('Por favor, digite um valor válido.')

    if quantidade == 0:
        risquinhos()
        break
    
    for pos in range(0, len(listagem)):
        if (codigo == pos+1):
            valor_item = precos[pos] * quantidade
    formatacao(f' Valor do Item: R${valor_item:.2f}')
    valor_total += valor_item
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input(' Deseja comprar mais alguma coisa? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

    #final
if valor_item > 0:
    formatacao(f'Valor Total: R${valor_total:.2f}')

centralizado('FIM DO PROGRAMA')
risquinhos()
