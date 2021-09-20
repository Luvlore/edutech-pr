from exceptions import SaldoInsuficienteError, OperacaoFinanceiraError
from leitor import LeitorDeArquivo

class Cliente:
    def __init__(self, nome, cpf, profissao):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao

class ContaCorrente:
    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente, agencia, numero):
        self.__saldo = 100
        self.__agencia = 0
        self.__numero = 0
        self.saques_nao_permitidos = 0
        self.tranferencias_nao_permitidas = 0
        self.cliente = cliente
        self.__set_agencia(agencia)
        self.__set_numero(numero)
        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = 30 / ContaCorrente.total_contas_criadas

    @property
    def agencia(self):
        return self.__agencia

    def __set_agencia(self, value):
        if not isinstance(value, int):
            raise ValueError('O atributo agencia deve ser um inteiro.', value)
        if value <= 0:
            raise ValueError('O atributo agência deve ser maior que zero.')
        
        self.__agencia = value

    @property
    def numero(self):
        return self.__numero

    def __set_numero(self, value):
        if not isinstance(value, int):
            raise ValueError('O atributo numero deve ser um inteiro.')
        if value <= 0:
            raise ValueError('O atributo numero deve ser maior que zero.')
        
        self.__numero = value

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, value):
        if not isinstance(value, int):
            raise ValueError('O atributo saldo deve ser um inteiro.')

    def transferir(self, valor, favorecido):
        if valor < 0:
            raise ValueError('O valor a ser tranferido é menor do que zero.')
        try:
            self.sacar(valor)
        except SaldoInsuficienteError as E:
            self.tranferencias_nao_permitidas += 1
            E.args = ()
            raise OperacaoFinanceiraError('Operação não finalizada.') from E
        favorecido.depositar(valor)

    def sacar(self, valor):
        if valor < 0:
            raise ValueError('O valor a ser sacado é menor do que zero.')
        if self.saldo < valor:
            self.saques_nao_permitidos += 1
            raise SaldoInsuficienteError(saldo=self.saldo, valor=valor)
        self.__saldo -= valor

    def depositar(self, valor):
        self.__saldo += valor


def main():
    import sys

    contas = []
    while True:
        try:
            nome = input('Nome do cliente:\n')
            agencia = input('Número de agência:\n')
            breakpoint()
            numero = input('Número da conta corrente:\n')
            cliente = Cliente(nome, None, None)
            conta_corrente = ContaCorrente(cliente, agencia, numero)
            contas.append(conta_corrente)
        except KeyboardInterrupt:
            print(f'\n\n{len(contas)}(s) contas criadas.')
            sys.exit()

# if __name__ == '__main__':
#     main()

# conta_corrente = ContaCorrente(None, 400, 1234567)
# conta_teste = ContaCorrente(None, 300, 9876)

# try:
#     conta_corrente.transferir(10000, conta_teste)
#     print(f'Conta corrente 1: {conta_corrente}')
#     print(f'Conta corrente 2: {conta_teste}')
# except OperacaoFinanceiraError as E:
#     breakpoint()
#     pass
with LeitorDeArquivo('arquivo.txt') as leitor:
    leitor.ler_proxima_linha()
