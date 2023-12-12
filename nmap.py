import socket
import sys

class nmap:
    HOST_IP = socket.gethostname()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HEADERSIZE = 10

    def __init__(self, IP, headersize):
        self.HOST_IP = IP
        self.HEADERSIZE = headersize

    def is_online(self):
        try:
            socket.gethostbyaddr(self.HOST_IP)
        except socket.error:
            return False
        return True

    def is_open(self, port_num):
        try:
            self.s.connect((self.HOST_IP, port_num))
        except socket.error:
            return False
        
        return True


host_ip = sys.argv[1]

nm = nmap(IP=host_ip, headersize=10)

if nm.is_online():
    print(f"{host_ip} is online.")
else:
    print(f"{host_ip} is offline.")

check = sys.argv[2]

fport = int(sys.argv[2])
eport = int(sys.argv[3])