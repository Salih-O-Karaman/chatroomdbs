import threading
from properties import *


def broadcast_listener():
    # Set the socket to broadcast and enable reusing addresses
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind socket to address and port
    udp_socket.bind((ip, BROADCAST_PORT))

    print("Listening to broadcast messages")

    while True:
        data = udp_socket.recv(BUFFER_SIZE)
        if data:
            print("Received a broadcast message from", data.decode(UNICODE))
        else:
            print("Receiving udp broadcast failed!")
