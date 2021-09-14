import os

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

def limpa_tela():
    os.system('cls')
