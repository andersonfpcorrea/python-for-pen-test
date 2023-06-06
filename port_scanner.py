import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(4)

host = input("Enter the IP you want to scan: ")  # 137.74.187.102 hackthissite.org
port = int(input("Enter the port you want to scan: "))  # 80, 443 are open


def port_scanner(port):
    if s.connect_ex((host, port)):
        print("The port is closed")
    else:
        print("The port is open")


port_scanner(port)
