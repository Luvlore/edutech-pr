from datetime import date, datetime

class Cadastro:

    def __init__(self, nome, email, cpf, nacionalidade, dia, mes, ano):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.nacionalidade = nacionalidade
        self.data = datetime.strptime(f'{dia}/{mes}/{ano}', '%d/%m/%Y').date()
        self.data_formatada = self.data.strftime('%d/%m/%Y')
    
    def __str__(self):
        return f'  NOME: {self.nome}\n  EMAIL: {self.email}\n  CPF: {(self.cpf).strip()[0:3]}.{(self.cpf).strip()[3:6]}.{(self.cpf).strip()[6:9]}-{(self.cpf).strip()[9:11]}\n  NACIONALIDADE: {self.nacionalidade}\n  ANIVERSÁRIO: {self.data_formatada}'

def risquinhos(p):
    print('{:—^46}'.format(p))

def pula_linha():
    print('')

risquinhos('')
risquinhos(' BEM-VINDO ')
risquinhos('')

contas = [conta_amanda :=  Cadastro('Amanda',  'amanda@amanda.com',   '01547564589', 'Brasileira', 5,  8,  2001),
          conta_brenda :=  Cadastro('Brenda',  'brenda@brenda.com',   '32154684894', 'Brasileira', 14, 4,  2003),
          conta_bruna :=   Cadastro('Bruna',   'bruna@bruna.com',     '12345678900', 'Brasileira', 22, 7,  2003),
          conta_gabriel := Cadastro('Gabriel', 'gabriel@gabriel.com', '78948453123', 'Brasileiro', 7,  9,  2000),
          conta_margo :=   Cadastro('Margô',   'margo@margo.com',     '78975453189', 'Brasileira', 17, 2,  2018),
          conta_natalia := Cadastro('Natália', 'natalia@natalia.com', '99521534862', 'Brasileira', 25, 10, 1995),
          conta_nicole :=  Cadastro('Nicole',  'nicole@nicole.com',   '48653354644', 'Brasileira', 30, 4,  2000),
          conta_teka :=    Cadastro('Teka',    'teka@teka.com',       '45641531546', 'Brasileira', 11, 11, 2019),
          conta_vanette := Cadastro('Vanette', 'vanette@vanette.com', '54511561565', 'Brasileira', 15, 5,  1967),
          conta_yasmyn :=  Cadastro('Yasmyn',  'yasmyn@yasmyn.com',   '64548793123', 'Brasileira', 14, 1,  2003)]

while True:
    for indice, conta in enumerate(contas):
        print(f'  {1+indice:02}.', f'{conta.nome}')

    while not (numero_solicidade := input('\n Digite o número que deseje ver os detalhes: ')).isdigit() or (numero_solicidade := int(numero_solicidade)) > 10 or (numero_solicidade := int(numero_solicidade)) <= 0:
        print('\n  Por favor, digite um número válido.')

    for pos in range(0, len(contas)):
        if numero_solicidade == pos+1:
            print(f'\n{contas[pos]}\n')

    resp = ' '
    while resp not in 'SN':
        resp = str(input(' Deseja verificar mais algum usuário? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

risquinhos('')
risquinhos(' FIM DO PROGRAMA ')
risquinhos('')
