
import database

conectar = database.conexao()

criar = database.criar_tabela('debito', 'id_debito', 'int')
criar.criando_tabela()
