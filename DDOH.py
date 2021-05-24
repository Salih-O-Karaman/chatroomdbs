import socket
import time
from socketserver import BaseRequestHandler, UDPServer


def sender_broadcast():
    #     # Create a UDP socket
    #     broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #     # Send message on broadcast address
    #     broadcast_socket.sendto(str.encode(broadcast_message), (ip, port))
    #     broadcast_socket.close()
    #
    #
    # if __name__ == '__main__':
    #     # Broadcast address and port
    #     BROADCAST_IP = "192.168.0.255"
    #     BROADCAST_PORT = 5973
    #     # Local host information
    #     MY_HOST = socket.gethostname()
    #     MY_IP = socket.gethostbyname(MY_HOST)
    #     # Send broadcast message
    #     message = MY_IP + ' sent a broadcast'
    #     sender_broadcast(BROADCAST_IP, BROADCAST_PORT, message)

    # client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  # UDP
    #
    # # Enable port rusage so we will be able to run multiple clients and servers on single (host, port).
    # client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    #
    # # Enable broadcasting mode
    # client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    #
    # client.bind(("", 37020))
    # while True:
    #     data, addr = client.recvfrom(1024)
    #     print("received message: %s" % data)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
    s.settimeout(5)

    s.sendto("hello".encode('utf-8'), ("255.255.255.255", 5555))
    try:
        print("Response: %s" % s.recv(1024))
    except socket.timeout:
        print("No server found")

    s.close()


def listener_broadcast():
    # Listening port
    # BROADCAST_PORT = 5972
    # # Local host information
    # MY_HOST = socket.gethostname()
    # MY_IP = socket.gethostbyname(MY_HOST)
    # # Create a UDP socket
    # listen_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # # Set the socket to broadcast and enable reusing addresses
    # listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    # listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # # Bind socket to address and port
    # listen_socket.bind((MY_IP, BROADCAST_PORT))
    # print("Listening to broadcast messages")
    #
    # while True:
    #     data, addr = listen_socket.recvfrom(1024)
    #     if data:
    #         print("Received broadcast message:", data.decode())

    # server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    # server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    #
    # # Enable broadcasting mode
    # server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    #
    # # Set a timeout so the socket does not block
    # # indefinitely when trying to receive data.
    # server.settimeout(0.2)
    # message = b"your very important message"
    # while True:
    #     server.sendto(message, ('255.255.255.255', 37020))
    #     print("message sent!")
    #     time.sleep(1)

    class Handler(BaseRequestHandler):
        def handle(self):
            print("message:", self.request[0])
            print("from:", self.client_address)
            socket = self.request[1]
            socket.sendto("hello", self.client_address)

    addr = ("", 5555)
    print("listening on %s:%s" % addr)
    server = UDPServer(addr, Handler)
    server.serve_forever()
