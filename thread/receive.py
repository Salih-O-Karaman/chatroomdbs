from properties import *


def receive(nickname):
    while True:
        try:
            message = tcp_socket.recv(BUFFER_SIZE).decode(UNICODE)
            if message == 'NICK':  # checking if the content of the message is a nickname
                tcp_socket.send(nickname.encode(UNICODE))
            else:
                print(message)
        except Exception as e:
            print("STATUS: ")
            print(e)
            tcp_socket.close()
            break
