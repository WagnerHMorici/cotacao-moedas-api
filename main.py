"""
API - https://economia.awesomeapi.com.br/last/:moedas
"""
import requests


class Cotacao:
    def __init__(self):
        conversao = self.get_conversao()
        moeda = self.escolher_moeda(conversao)
        r = self.acessar_url(moeda)
        self.resultado = self.consulta(moeda, r)


    def get_conversao(self):
        print("Digite um número referente a moeda desejada.")
        print("1 = USD-BRL\n2 = EUR-BRL\n3 = BTC-BRL")
        return int(input("Digite o número da moeda: "))

    def __str__(self):
        return 'R$ ' + self.resultado

    def escolher_moeda(self, conversao):
        if conversao == 1:
            return 'USD-BRL'
        elif conversao == 2:
            return 'EUR-BRL'
        elif conversao == 3:
            return 'BTC-BRL'
        else:
            raise ValueError('Moeda Inválida')

    def acessar_url(self, moeda):
        url = 'https://economia.awesomeapi.com.br/last/{}'.format(str(moeda))
        return requests.get(url)

    def consulta(self, moeda, r):
        cotacao = moeda.replace('-', '')
        if r.status_code == 200:
            dados = r.json()
            return dados[cotacao]['bid']
        else:
            raise ValueError('Não foi possivel acessar a URL')
