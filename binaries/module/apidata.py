try:
    from .database import *
    from .request import request_bacen
except ImportError:
    from database import *
    from request import request_bacen


def delete_api_data():
    db.execute("""
    DELETE FROM api_data
    """)
    db.commit()
    print(f'{__name__}: Dados Deletados da Tabela "api_data"')


def insert_on_api_data():
    dados = request_bacen()
    print(f'{__name__}: Gravando Dados na Tabela "api_data"')
    for i in dados:
        data = i['data']
        valor = i['valor']
        cursor.execute(f"""

        INSERT INTO api_data VALUES (
            "{data}",
            "{valor}"
        )
        """)
        db.commit()
    print(f'{__name__}: Dados Gravados na Tabela "api_data"')


if __name__ == '__main__':
    delete_api_data()
    insert_on_api_data()
