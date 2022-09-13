import requests


def request_bacen():
    url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json&dataInicial=01/01/2000&dataFinal=31/12/2100'

    dados = requests.get(url).json()
    print(f'{__name__}: Request Data OK')
    return dados


if __name__ == '__main__':
    dados = request_bacen()
    for i in dados:
        print(i)
