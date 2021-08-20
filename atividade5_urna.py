def centralizado(texto):
    print(f'{texto:^38}')

def risquinhos():
    print('—'*38)

candidatos = ['João', 'José', 'Jacó', 'Jobé', 'Nulo', 'Branco']
votos = [0, 0, 0, 0, 0, 0]

risquinhos()
centralizado('URNA ELETRONICA')
risquinhos()

while True:
    for indice, candidato in enumerate(candidatos):
        print(f'  {indice+1} - {candidato}')

    risquinhos()

    while not (voto := input(' Digite o número  que deseja votar\n Ou digite 0 para sair do programa: ')).isdigit() or (voto := int(voto)) < 0 or (voto := int(voto)) > 6:
        print('\n Por favor, digite uma opção válida.')
        risquinhos()
    
    risquinhos()

    for pos in range(0, len(candidatos)):
        if voto == pos+1:
            votos[pos] += 1
    if voto == 0:
        break

for pos in range(0, len(candidatos)):
    print(f'  {candidatos[pos]} recebeu {votos[pos]} votos.')
risquinhos()
