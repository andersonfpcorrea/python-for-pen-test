import socket

client_socket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM
)  # AF_INET = IPv4, SOCK_STREAM = TCP

host = socket.gethostname()  # host is equal to the IP address of the machine
port = 3000

client_socket.connect((host, port))

message = client_socket.recv(1024)

client_socket.close()

print(message.decode("ascii"))
