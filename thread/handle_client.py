import broadcast
from properties import *


def handle_client(client, nickname, clients, nicknames):
    while True:
        try:

            message = client.recv(BUFFER_SIZE)  # receiving a message from client
            print(message.decode(UNICODE))
            broadcast.broadcast(message, clients)
        except Exception as e:

            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            print(e)
            broadcast.broadcast(f'STATUS: {nickname} left the chat!'.encode(UNICODE), clients)
            nicknames.remove(nickname)
            break
