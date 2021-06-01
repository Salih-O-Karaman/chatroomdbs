import threading
import queue

class MulticastGroup(threading.Thread):

    def __init__(self):
        super().__init__()
        self.queue = queue

    # receiver:
    # put into quue
    # list = data.split(";")
    # self.queue.put(list])

    # "122;Stefano;Nachricht="Stefano left the room";Uhrzeit;"
    # "123;Hüseyin;Nachricht=Halllo wie geht es dir; Uhrzeit;"