import pandas as pd
import openpyxl

try:
    from .database import *
except ImportError:
    from database import *


def get_api_data():
    api_data = cursor.execute("""
    SELECT * FROM api_data
    """)
    api_data = cursor.fetchall()
    return api_data


def ipca_ano():
    dados = get_api_data()

    ano_incial = 2000
    soma = 0
    ipca_ano = []

    for index, i in enumerate(dados):
        data = i[0]
        ano = int(data[6:])

        if ano == ano_incial:
            ipca = dados[index][1]
            soma += float(ipca)

        else:
            info = {
                "Ano": ano_incial,
                "IPCA": f'{soma:.2f}',
            }
            ipca_ano.append(info)
            soma = 0
            soma += dados[index][1]
            ano_incial += 1

    info = {
        "Ano": ano_incial,
        "IPCA": f'{soma:.2f}',
    }
    ipca_ano.append(info)

    print(f'{__name__}: IPCA Organizado por Ano OK')

    return ipca_ano


def make_relatorio():
    df = pd.DataFrame()
    dados = ipca_ano()
    df = df.append(dados, ignore_index=True)
    df = df.to_excel('RelatorioIPCA_ANO.xlsx')

    print(f'{__name__}: Relatório IPCA Gerado em "RelatorioIPCA_ANO.xlsx"')


if __name__ == "__main__":
    for i in ipca_ano():
        print(i)
    make_relatorio()
