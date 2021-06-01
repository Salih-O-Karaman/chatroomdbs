import socket
import threading

import constants_old
import threadUdpBroadcast_old

serverIP = input('IP address of the server >>> ')
alias = input('Choose an alias >>> ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 8080
client.connect((constants_old.SERVER_IP, constants_old.TCP_PORT))


def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'alias?':
                client.send(alias.encode('utf-8'))
            else:
                print(message)
        except:
            print('Error!')
            client.close()
            break


def client_send():
    while True:
        message = f'{alias}: {input("")}'
        client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()
send_thread = threading.Thread(target=client_send)
send_thread.start()
threadUdpBroadcast_old.sender_broadcast()
