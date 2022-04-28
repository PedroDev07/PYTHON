from colorama import Cursor
import pyodbc 

dados_conexao = ("DRIVER={SQL Server};"
    "SERVER=DESKTOP-HR5T3Q5;"
    "DATABASE=financas")


conexao = pyodbc.connect(dados_conexao)
print("Sucesso!")


cursor = conexao.cursor()

comando = """use financas 
create table categoria(
id_categoria int,
categoria varchar(40),
)
"""
cursor.execute(comando)
cursor.commit()