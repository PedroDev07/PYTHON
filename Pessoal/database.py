import pyodbc 



def conexao():
    dados_conexao = ("DRIVER={SQL Server};"
    "SERVER=DESKTOP-HR5T3Q5;"
    "DATABASE=financas")
    conexao = pyodbc.connect(dados_conexao)
    print("Sucesso!")


class criar_tabela:
    def __init__ (self, nome_tabela, nome_coluna, tipo):
        self.nome = nome_tabela
        self.coluna = nome_coluna
        self.tipo = tipo
                
    def criando_tabela(self):
        comando = f"""use financas 
        create table {self.nome} (
        )
        """
        cursor = conexao.cursor()
        cursor.execute(comando)
        cursor.commit()
        print("correto")