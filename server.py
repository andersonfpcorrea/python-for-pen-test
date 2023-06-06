import socket

server_socket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM
)  # AF_INT = IPv4, SOCK_STREAM = TCP
host = socket.gethostname()  # host is equal to the IP address of the machine
port = 3000

server_socket.bind((host, port))  # bind socket to host and port
server_socket.listen(3)  # 3 = number of connections

while True:
    client_socket, address = server_socket.accept()
    print("Received connection from %s " % str(address))
    message = "Hello! Thank you for connecting to the server" + "\r\n"
    client_socket.send(message.encode("ascii"))
    client_socket.close()
