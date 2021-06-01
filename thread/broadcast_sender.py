from properties import *


def broadcast_sender(nickname):
    # Send broadcast message
    message = nickname
    # Send message on broadcast address
    udp_socket.sendto(message.encode(UNICODE), (ip, BROADCAST_PORT))
    udp_socket.close()