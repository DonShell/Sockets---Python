#!/usr/bin/env python3

#!/usr/bin/env python3

import socket
#para limpar a tela
import click

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


sem_cor = "\033[1;37;40m"
vermelho = "\033[1;31;40m"
verde = "\033[1;32;40m"
amarelo = "\033[1;33;40m"
azul = "\033[1;34;40m"
magenta = "\033[1;35;40m"
ciano = "\033[1;36;40m"

#limpar tela
click.clear()


#uma conexção
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print(magenta + "SERIDOR "+ verde +"RODANDO" + sem_cor)
    while True:
        print("\n" + magenta + "Buscando conexões" + sem_cor)
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(verde + 'Conectado por', addr, sem_cor)
            while True:
                entrada = str(conn.recv(1024))
                entrada = entrada[2:- 1]
                print(amarelo + '< ' + ciano + entrada + sem_cor + "\n")
                if not entrada or entrada == "fim":
                    break
                saida = str(input(amarelo + "> " + azul))
                print(sem_cor)
                conn.send(saida.encode('utf-8'))
        print(vermelho + "fim da conexão" + sem_cor)
    #fim da conexão
