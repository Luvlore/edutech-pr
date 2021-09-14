import re
class ExtratorURL:

    def __init__(self, url):
        self._url = self.sanitizar(url)
        self.validar()

    def sanitizar(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''
    
    def validar(self):
        if not self._url:
            raise ValueError('A URL está vázia.')
        
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self._url)

        if not match:
            raise ValueError('A URL não é válida.')

    def get_base(self):
        indice_interrogacao = self._url.find('?')
        url_base = self._url[:indice_interrogacao]
        return url_base

    def get_parametros(self):
        indice_interrogacao = self._url.find('?')
        url_parametros = self._url[indice_interrogacao+1:]
        return url_parametros
    
    def get_valor_parametro(self, parametro_busca):
        indice_parametros = self.get_parametros().find(parametro_busca)
        indice_valor = indice_parametros + len(parametro_busca) + 1
        indice_e_comercial = self.get_parametros().find('&', indice_valor)

        if indice_e_comercial == -1:
            valor = self.get_parametros()[indice_valor:]
        else:
            valor = self.get_parametros()[indice_valor:indice_e_comercial]
        return valor
    
    def __len__(self):
        return len(self._url)

    def __str__(self):
        return f'{self._url}\nParâmetros: {self.get_parametros()}\nURL Base: {self.get_base()}'

    def __eq__(self, outro):
        return self._url == outro._url

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)

valor_dolar = 5.50  # 1 dólar = 5.50 reais
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")

if moeda_origem == "real" and moeda_destino == "dolar":
    valor_conversao = int(quantidade) / valor_dolar
    print("O valor de R$" + quantidade + " reais é igual a $" + str(valor_conversao) + " dólares.")
elif moeda_origem == "dolar" and moeda_destino == "real":
    valor_conversao = int(quantidade) * valor_dolar
    print("O valor de $" + quantidade + " dólares é igual a R$" + str(valor_conversao) + " reais.")
else:
    print(f"Câmbio de {moeda_origem} para {moeda_destino} não está disponível.")
