import socket
import sys

class nmap:
    HOST_IP = socket.gethostname()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HEADERSIZE = 10

    def __init__(self, IP, headersize):
        self.HOST_IP = IP
        self.HEADERSIZE = headersize


host_ip = sys.argv[1]

nm = nmap(IP=host_ip, headersize=10)