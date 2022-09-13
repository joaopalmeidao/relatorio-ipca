from binaries.module import apidata
from binaries.module import ipca


if __name__ == '__main__':
    apidata.delete_api_data()
    apidata.insert_on_api_data()
    ipca.ipca_ano()
    ipca.make_relatorio()
