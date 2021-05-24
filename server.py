import socket
import threading
import sys
import time

import DDOH

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
port = 8080
server.bind((ip, port))
server.listen()  # Backlog+
clients = []  # Threads
aliases = []  # User/Client Names


def broadcast(message):
    for client in clients:
        client.send(message)


# function to handle clients connection
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            alias = aliases[index]
            client.close()
            broadcast(f'{alias} has left the chat room!'.encode('utf-8'))
            aliases.remove(alias)
            break


# Main function to receive the clients connection
def receive():
    while True:
        #
        client, address = server.accept()  # Connection established
        # print(f'connection is established with {str(address)}')

        # Nachfrage nach Alias
        client.send('alias?'.encode('utf-8'))

        # Alias wird vom Client empfangen
        alias = client.recv(1024).decode('utf-8')

        # Die Variable Alias in Liste Aliases hinzugefügt
        aliases.append(alias)

        # Der Client selber wird in die Liste der CLients hinzugefügt
        clients.append(client)
        # print(f'The alias of this client is {alias}')

        # Server benachrichtigt ALLE Clients, dass der neue Client verbunden ist
        broadcast(f'{alias} has connected to the chat room'.encode('utf-8'))

        # Der Client bekommt eine Benachrichtigung, dass er Verbunden ist
        client.send(' you are now connected!'.encode('utf-8'))

        # Client wird in den Thread eingefügt oder Thread wird mit der Lebenszeit der Client abhängig gemacht
        # Funktion handle_cliedt wird gestartet
        thread = threading.Thread(target=handle_client, args=(client,))

        # Thread wird gestartet
        thread.start()


if __name__ == "__main__":
    print('Server IP >>> ' + ip)
    print('Server is running and listening...')
    receive()
    DDOH.listener_broadcast()
