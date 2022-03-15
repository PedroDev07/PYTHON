import socket 
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('****cliente socket criado com sucesso****\n')
    print('****Iniciando conversa****\n')
except socket.error as e:
    print('socket nao foi criado')
    print('Erro: {}'.format(e))
    sys.exit()
host = 'localhost'
porta = 5433
mensagem = 'Cliente: Ola server, tudo bem?'


try:

    s.sendto(mensagem.encode(), (host, 5432))
    dados, servidor = s.recvfrom(4096)
    dados= dados.decode()
    print(dados)
    
    
except socket.error as e:
    print('\nconexao falhou com o servidor falhou')
    print('Erro: {}'.format(e))
    sys.exit()
finally:
    print('Cliente: Tudo bem!')
    print('Cliente: Nao quero nada, somente saber se esta online')
    print('Cliente: Vou fechar a conexao')
    print('\n\n***Fechando a conexao***')
    s.close()




