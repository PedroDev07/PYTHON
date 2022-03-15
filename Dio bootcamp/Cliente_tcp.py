#cliente tcp 

import socket
import sys


def main():#tenta conexao tcp/ip
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('A conexao falhou')
        print('Erro: {}'.format(e))
        sys.exit()
    print('Socket criado com sucesso')
    host_alvo = input('Digite o host ou ip a ser conectado: ')
    porta_alvo = int(input('Digite a porta a ser conectada: '))



    try:
        s.connect((host_alvo, porta_alvo))
        print('Conexao bem sucedida')
        s.shutdown(2)
    except socket.error as e:
        print('A conexao falhou')
        print('Erro: {}'.format(e))
        sys.exit()


if __name__ == "__main__":
    main()