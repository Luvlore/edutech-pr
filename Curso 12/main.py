from acesso_cep import BuscaEndereco
from cpf_cnpj import Documento
from datas_br import DatasBr
from telefones_br import TelefonesBr
from os import system

system('cls')

cep = '97576706'
cep_formatado = BuscaEndereco(cep)
print(cep_formatado)
bairro, rua, uf = cep_formatado.acessa_via_cep()
print(f'{bairro}, {rua}, {uf}')

cpf = Documento.criar_documento('06245238021')
print(cpf)

cnpj = Documento.criar_documento('38838027000120')
print(cnpj)

data = DatasBr()
print(data)
print(data.tempo_cadastro())

telefone = '5543985732573'
telefone_formatado = TelefonesBr(telefone)
print(telefone_formatado)
