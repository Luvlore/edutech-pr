print ('URNA ELETRONICA')
candidatos = ['João', 'José', 'Jacó', 'Jobé', 'Nulo', 'Branco']
votos = [0, 0, 0, 0, 0, 0]
numeros = 1

for candidato in candidatos:
    print(numeros, '-', candidato)
    numeros += 1

while True:

    while not (voto := input('\nDigite o número que deseja votar\nOu digite 0 para sair do programa: ')).isdigit() or (voto := int(voto)) < 0 or (voto := int(voto)) > 6:
        print('Por favor, digite uma opção válida.')
    
    for pos in range(0, len(candidatos)):
        if voto == pos+1:
            votos[pos] += 1
    if voto == 0:
        break

print('')

for pos in range(0, len(candidatos)):
    print(f'{candidatos[pos]} recebeu {votos[pos]} votos.')
