import socket
import sys

class nmap:
    def __init__(self, IP):
        self.HOST_IP = IP

    def is_online(self):
        test_ports = [20, 22, 25, 53, 80, 123, 443]

        for port in test_ports:
            if self.is_open(port):
                return True

        return False

    def is_open(self, port_num):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            s.connect((self.HOST_IP, port_num))
        except socket.error:
            return False

        return True

    def get_servicename(self, port_num):
        try:
            service_name = socket.getservbyport(port_num, 'tcp')
            return service_name
        except OSError as e:
            print(f"Error: {e}")

    def check_ports(self, fport, eport):
        for port in range(fport, eport):
            if nm.is_open(port):
                service_name = nm.get_servicename(port)
                print(f"open port detected: {host_ip}\t-- port: {port}\t-- Service: {service_name}")

    def http_req(self, msg):
        self.s.send(msg)

        print(self.s.recv(1024).decode())


check = sys.argv[1]
if "POST" in check:
    user_name = sys.argv[2]
    user_age = sys.argv[3]

    msg = f'POST {user_name} {user_age}'

    nm = nmap(IP=socket.gethostname())
    if nm.is_open(1234):
        nm.http_req(msg.encode())
    else:
        print("Port is not open!")
elif "GET" in check:
    user_id = sys.argv[2]

    msg = f'GET {user_id}'

    nm = nmap(IP=socket.gethostname())
    if nm.is_open(1234):
        nm.http_req(msg.encode())
    else:
        print("Port is not open!")

else:
    host_ip = sys.argv[1]

    nm = nmap(IP=host_ip)

    if nm.is_online():
        print(f"{host_ip} is online.")
    else:
        print(f"{host_ip} is offline.")

    check = sys.argv[2]

    if len(sys.argv) == 4:
        fport = int(sys.argv[2])
        eport = int(sys.argv[3])
        nm.check_ports(fport=fport, eport=eport)