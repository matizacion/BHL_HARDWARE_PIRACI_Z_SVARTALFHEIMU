import socket
from plik_mateusza import funkcja_mateusza

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address_port = ('172.20.15.244', 5052)
client.connect(server_address_port)


if __name__ == '__main__':
    data = funkcja_mateusza()
    client.send(str.encode(str(data)))