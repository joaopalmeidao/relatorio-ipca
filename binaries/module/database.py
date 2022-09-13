import sqlite3


db = sqlite3.Connection("DataBase.bd")

cursor = db.cursor()

print(f'{__name__}: Banco de Dados "DataBase.bd" Conectado')
