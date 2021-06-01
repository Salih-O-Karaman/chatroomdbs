import socket
import threading

import constants_old
from threadUdpBroadcast_old import DynamicDiscovery

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Backlog
clients = []  # Threads
aliases = []  # User/Client Names

class Server:

    def __init__(self):

        self.server.bind((constants_old.SERVER_IP, constants_old.TCP_PORT))
        self.server.listen()
        self.hosts = []

        self.broadcastListenerThread = DynamicDiscovery()
        self.broadcastListenerThread.daemon = True
        # queuemsg = self.multicastlistener.queue.get()
        # reihgenfolge = queuemsg[0]
        # sender = queuemsg[1]
        # nachricht = queuemsg[2]
        #

        # nachricht vorbereiten
        # senderthread
        # self.sendingqueue.put(nachriccht_formatiert)

        try:
            self.broadcastListenerThread.start()  # thread udpBroadcast
            # threads => multicast
            # threads => tcp
            # thread => replication
            # thread => election
            # thread => sender

            # self


        except Exception as e:
            print(e)

        finally:
            self.broadcastListenerThread.join()
            self.broadcastListenerThread.stop()

    def broadcast(message):
        for client in message.clients:
            client.send(message)

    # function to handle clients connection
    def handle_client(client):
        while True:
            try:
                message = client.recv(1024)
                client.broadcast(message)
            except:
                index = client.clients.index(client)
                client.clients.remove(client)
                alias = aliases[index]
                client.close()
                #client.broadcast(('has left the chat room!'.encode('utf-8'))
                aliases.remove(alias)
                break

    # Main function to receive the clients connection
    def receive(self):
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
            #broadcast(f'{alias} has connected to the chat room'.encode('utf-8'))

            # Der Client bekommt eine Benachrichtigung, dass er Verbunden ist
            client.send(' you are now connected!'.encode('utf-8'))

            # Client wird in den Thread eingefügt oder Thread wird mit der Lebenszeit der Client abhängig gemacht
            # Funktion handle_cliedt wird gestartet
            #thread = threading.Thread(target=handle_client, args=(client,))

            # Thread wird gestartet
            #thread.start()
            #udpBroadcast.listener_broadcast()

    if __name__ == "__main__":
        print('Server IP >>> ' + constants_old.SERVER_IP)
        print('Server is running and listening...')
        receive()

    # 1) Prozess erstellen mit mehrere Threads udp broadcast, multicast listener,tcp socket verbindung pro Client
    # 2)
