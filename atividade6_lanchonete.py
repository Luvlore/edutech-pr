    #funções para deixar a excução do código show
def risquinhos():
    print("—"*49)

def centralizado(texto):
    print(f'{texto:^49}')

def pula_linha():
    print('')
def formatacao(texto):
    risquinhos()
    pula_linha()
    centralizado(texto)
    pula_linha()
    risquinhos()

    #variáveis
listagem =  ["Misto-Quente", "Cachorro-Quente", "Coxinha", "Hamburgão", "X-Burguer","X-Salada", "X-Tudo", 'Refrigerante', 'Suco', 'Água', 'Água c/Gás', 'Café', 'Café c/Leite']
codigos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
precos = [3, 4.5, 3, 3.5, 6, 7.5, 14, 5.5, 4.5, 2, 2, 3, 3]
nada = ''

    #título
risquinhos()
centralizado("CARDÁPIO DA LANCHONETE")
risquinhos()

    #cardápio
print(f'  LISTA\t\t     CÓDIGOS\t\t PREÇOS\n')
for pos in range(0, len(listagem)):
    print(f'  {listagem[pos]:.<20}', end='')
    print(f' {1+codigos[pos]:03}',f'{nada:.<13}',end='')
    print(f' R${precos[pos]:0.2f}')
    #valores
valor_total = 0
valor_item = 0

    #execução do código
while True:
    risquinhos()
    while not (codigo := input(' Digite o código que deseja comprar: ')).isdigit() or (codigo := int(codigo)) < 1 or (codigo := int(codigo)) > 13:
        formatacao('Por favor, digite um valor válido.').upper()
    formatacao(f'Você escolheu {listagem[codigo-1]}')
    
    while not (quantidade := input(' Digite a quantidade que deseja comprar: ')).isdigit() or (quantidade := int(quantidade)) < 0:
        formatacao('Por favor, digite um valor válido.').upper()
    
    for pos in range(0, len(codigos)):
        if (codigo == pos+1):
            valor_item = precos[pos] * quantidade
    formatacao(f' Valor do Item: R${valor_item:.2f}')
    valor_total += valor_item
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input(' Deseja comprar mais alguma coisa? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

formatacao(f'Valor Total: R${valor_total:.2f}')
