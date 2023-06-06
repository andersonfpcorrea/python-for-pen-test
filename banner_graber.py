import socket


def banner(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    s.settimeout(5)
    print(s.recv(1024).decode("ascii"))


def main():
    ip = input("Enter the IP address: ")
    port = int(input("Enter the port number: "))
    try:
        banner(ip, port)
    except (ConnectionRefusedError, TimeoutError) as e:
        print("Error: ", e)


if __name__ == "__main__":
    main()
