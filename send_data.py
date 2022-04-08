import socket


# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_address_port = ('172.20.15.244', 5052)
# client.connect(server_address_port)
#

class comunication_module:
    def __init__(self , ip = ('172.20.48.1', 5052)):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address_port = ip
        self.client.connect(server_address_port)
    def send(self , string_to_send):
        self.client.send(str.encode(string_to_send))
    def recv(self , buff = 1024):
        return self.client.recv(buff)

if __name__ == '__main__':
    c = comunication_module()
    while True:
        c.send("1,2,3,4,5")
        print(c.recv(1024))