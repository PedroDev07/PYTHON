import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket criado')
print('Servidor online para servir...')

host = 'localhost'
port = 5432

s.bind((host, port))
mensagem_1 = '''
SERVIDOR: Ola cliente, tudo bem e contigo? Como posso te ajudar?'''


while 1:
    dados, end = s.recvfrom(4096)
    if dados: 
        print('------------------------------')
        print('Servidor enviando mensagem...')
        s.sendto(dados + (mensagem_1.encode()), end)