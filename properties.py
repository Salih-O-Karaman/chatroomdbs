import socket

# HOST name and IP of the device
host = socket.gethostname()
ip = socket.gethostbyname(host)
BROADCAST_IP = "192.168.0.255"

# global ports
TCP_PORT = 55555            # port for tcp connection
BROADCAST_PORT = 55556      # port for UDP broadcasting (dynamic discovery of hosts)
MULTICAST_PORT = 55557      # port for Multicasting

# sockets
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# # lists
# clients = []  # empty list of clients
# nicknames = []  # empty list of nicknames

# Other
UNICODE = 'utf-8'
BUFFER_SIZE = 1024
