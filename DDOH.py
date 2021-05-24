import socket

UDP_IP = "255.255.255.255"
UDP_PORT = 5005

MESSAGE = "Hello, World!"


def sender_broadcast():
    print("UDP target IP   :", UDP_IP)
    print("UDP target port :", UDP_PORT)
    print("Message         :", MESSAGE)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(MESSAGE.encode("utf-8"), (UDP_IP, UDP_PORT))
    sock.close()
    sock.close()


def listener_broadcast():
    print("UDP Receive IP   :", UDP_IP)
    print("UDP Receive port :", UDP_PORT)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        data, addr = sock.recvfrom(1024)
        print("Received Data    :", data)
