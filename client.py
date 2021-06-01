from thread.broadcast_sender import *
from thread.write import *
from thread.receive import *
from properties import *
import threading

nickname = input("STATUS\nChoose a nickname: ")


def main():
    tcp_socket.connect((ip, TCP_PORT))


    # threads
    # broadcast_sender_thread = threading.Thread(target=broadcast_sender, args=(nickname,))
    # broadcast_sender_thread.start()

    receive_thread = threading.Thread(target=receive, args=(nickname,))
    receive_thread.start()

    write_thread = threading.Thread(target=write, args=(nickname, tcp_socket))
    write_thread.start()


# running client
broadcast_sender(nickname)
main()
