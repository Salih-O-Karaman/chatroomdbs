# sources:
# - https://www.youtube.com/watch?v=3UOyky9sEQY
# - 04 Dynamic discovery.pdf

from thread.broadcast_listener import *
from thread.handle_client import *
import threading
import broadcast

# Starting Server
tcp_socket.bind((host, TCP_PORT))
tcp_socket.listen()

# Lists For Clients and Their Nicknames
clients = []
nicknames = []


# Receiving / Listening Function
def main():
    broadcast_listener_thread = threading.Thread(target=broadcast_listener)
    broadcast_listener_thread.start()

    while True:
        # Accept Connection
        client, address = tcp_socket.accept()

        # Request And Store Nickname
        client.send('NICK'.encode(UNICODE))
        nickname = client.recv(BUFFER_SIZE).decode(UNICODE)
        nicknames.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname
        print("Connected with {}".format(nickname))
        broadcast.broadcast("{} joined!".format(nickname).encode(UNICODE), clients)
        client.send('Connected to server!'.encode(UNICODE))

        # threads
        handle_client_thread = threading.Thread(target=handle_client, args=(client, nickname, clients, nicknames))
        handle_client_thread.start()


# running server
print("Server is running and listening...")
main()
