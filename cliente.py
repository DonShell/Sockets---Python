#!/usr/bin/env python3

import socket

#para limpar a tela
import click

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server


sem_cor = "\033[1;37;40m"
vermelho = "\033[1;31;40m"
verde = "\033[1;32;40m"
amarelo = "\033[1;33;40m"
azul = "\033[1;34;40m"
magenta = "\033[1;35;40m"
ciano = "\033[1;36;40m"

#limpar tela
click.clear()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        saida = str(input(amarelo + "> " + azul))
        print(sem_cor)
        s.send(saida.encode('utf-8'))
        if saida == "fim":
            break
        entrada = str(s.recv(1024))
        entrada = entrada[2:- 1]
        print(amarelo + '< ' + ciano + entrada + sem_cor + "\n")
    print("fim da conexção")

