import socket
import queue
import threading

from OldFiles import constants_old

UDP_IP = "255.255.255.255"
UDP_PORT = 8080
MESSAGE = "Hello, World!"


class DynamicDiscovery(threading.Thread):

    def __init__(self):
        super().__init__()
        self.incomingmsg_queue = queue
        self.outgoingqueue = queue

    def run(self):
        print("UDP Receive IP   :", constants_old.BROADCAST_IP)
        print("UDP Receive port :", constants_old.UDP_PORT_CLIENTS)

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.bind((UDP_IP, UDP_PORT))

        while True:
            if data:
                data, addr = sock.recvfrom(1024)
                print("Received Data    :", data)
                self.incomingmsg_queue.put([data, addr])
                self.sender_broadcast(data, addr)

    # DD | ACK | Chat-Query-Req (CQR) |

    def sender_broadcast(self, data, sender):
        print("UDP target IP   :", constants_old.BROADCAST_IP)
        print("UDP target port :", UDP_PORT)
        print("Message         :", MESSAGE)
        data = "DD"
        if data == "CQR":

            request = self.incomingmsg_queue.get()
            if request[0] == "12 UHrr":
                pass
            # datenbank => uhrzeit
            # replikation message rausschiekcne

            receiver = sender  # der suchender Server/client

            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(request, (receiver, UDP_PORT))
            sock.close()

        if data == "D":
            msg = "I am here"  # Server
            receiver = sender  # der suchender Server/client

            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(msg, (receiver, UDP_PORT))
            sock.close()
