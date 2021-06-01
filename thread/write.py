from properties import *


def write(nickname, client):
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode(UNICODE))
