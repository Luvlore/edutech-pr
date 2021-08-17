#Python Avançado Orientação a Objetos.
#Faça um sistema de cadastro de pessoas que realize o cadastro de 10 pessoas e quando solicitado mostre o valor da pessoa solicitada. 
# Utilize Classe e sistemas de repetição para te auxiliar.

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

def espaço_em_branco(p):
    print('{: ^45}'.format(p))

def risquinhos(p):
    print('{:—^45}'.format(p))

quantidade = 0
pessoa = 1

risquinhos('')
risquinhos(' BEM-VINDO ')
espaço_em_branco(' você poderá cadastrar até 10 pessoas ')

while quantidade <= 10:
    risquinhos('')
    espaço_em_branco('')

    nome = str(input('  Insira o seu nome: ')).title()
    email = input('  Insira seu email: ').lower()
    while not (cpf := input('  Insira seu CPF: ')).isdigit():
        espaço_em_branco('Por favor, insira um valor válido!')
    while (nacionalidade := (input('  Insira sua nacionaliade: ').title())).isdigit():
        espaço_em_branco('Insira uma nacionalidade válida!')
    while not (dia := input('  Insira o dia do seu aniversário: ')).isdigit() or (dia := int(dia)) <= 0 or (dia := int(dia)) > 31:
        espaço_em_branco('Insira um valor válido!')
    while not (mes := input('  Insira o mês do seu aniversário: ')).isdigit() or (mes := int(mes)) <= 0 or (mes := int(mes)) > 12:
        espaço_em_branco('Insira um valor válido!')
    while not (ano := input('  Insira o ano do seu aniversário: ')).isdigit() or (ano := int(ano)) < 1900 or (ano := int(ano)) > 2021:
        espaço_em_branco('Insira um valor válido!')
    espaço_em_branco('')

    risquinhos('')
    espaço_em_branco('')
    espaço_em_branco(f'——— PESSOA {pessoa} ———')
    espaço_em_branco('')
    conta = Cadastro(nome, email, cpf, nacionalidade, dia, mes, ano)
    print(conta)
    espaço_em_branco('')
    
    pessoa += 1
    quantidade += 1
    resp = ' '
    while resp not in 'SN':
        risquinhos('')
        resp = str(input('  Deseja continuar? [S/N] ')).strip().upper()[0]
    if quantidade == 10 or resp == 'N':
        break

risquinhos('')
risquinhos(' FIM DO PROGRAMA ')
risquinhos('')
