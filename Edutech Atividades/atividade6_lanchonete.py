from atividade6_lista import listagem
from funcoes_de_formatacao import centralizado, formatacao, pula_linha, risquinhos, limpa_tela

# valores
valor_total = 0
valor_item = 0

# execução do código
while True:
    # título
    risquinhos()
    centralizado('CARDÁPIO DA LANCHONETE')
    risquinhos()
    # cardápio
    print(f'  LISTA\t\t     CÓDIGOS\t\t   PREÇOS\n')
    for codigo, (alim, preco) in enumerate(listagem.items()):
        print(f'  {alim:.<20}', f'{codigo + 1:03}','.'* 13, f'R${preco:6.2f}')
    pula_linha()
    risquinhos()

    while not (codigo := input(' Digite o código do que deseja comprar\n Ou digite 0 a qualquer momento para cancelar: ')).strip().isdigit() or (codigo := int(codigo)) not in list(range(len(listagem) + 1)):
        formatacao('Por favor, digite um valor válido.')

    if codigo == 0:
        risquinhos()
        break

    for pos, alim in enumerate(listagem.keys()):
        if codigo == pos + 1:
            formatacao(f'Você escolheu {alim}')
    
    while not (quantidade := input(' Digite a quantidade que deseja comprar: ')).strip().isdigit() or (quantidade := int(quantidade)) < 0:
        formatacao('Por favor, digite um valor válido.')

    if quantidade == 0:
        risquinhos()
        break
    
    for pos, preco in enumerate(listagem.values()):
        if codigo == pos+1:
            valor_item = preco * quantidade
    formatacao(f' Valor do Item: R${valor_item:.2f}')
    valor_total += valor_item
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input(' Deseja comprar mais alguma coisa? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

    limpa_tela()

# final
if valor_item > 0:
    formatacao(f'Valor Total: R${valor_total:.2f}')

centralizado('FIM DO PROGRAMA')
risquinhos()
