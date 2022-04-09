import socket
import threading

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_address_port = ('172.20.15.244', 5052)
# client.connect(server_address_port)
#

class comunication_module:
    def __init__(self , ip = ('172.20.48.1', 5052)):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address_port = ip
        self.client.connect(server_address_port)

        self.recv_data = None
        self.prev_data = None
        self.send_data = "1,2,3,4,5"

        self.test_par = 0

    def send(self , string_to_send):
        self.client.send(str.encode(string_to_send))
    def recv(self , buff = 1024):
        return self.client.recv(buff)

    def lopp_fun(self):

        dd = self.recv()
        if dd != None:
            self.recv_data = dd

        self.send(self.send_data)

    def start_deamon(self):
        self.thr = threading.Thread(target=self.lopp_fun, daemon=True)
        self.thr.start()

if __name__ == '__main__':
    c = comunication_module()
    c.start_deamon()
    while True:
        if c.recv_data:
            pass
            #print(c.recv_data)
