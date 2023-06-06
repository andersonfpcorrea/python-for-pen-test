import nmap
from textwrap import dedent

scanner = nmap.PortScanner()

print("Welcome, this is a simple nmap automation tool")
print("<-------------------------------------------------->")

ip_addr = input("Please enter the IP address you want to scan: ")
print(f"The IP you entered is: {ip_addr}")

initial_prompt = dedent(
    """
    Please enter the type of scan you want to run
    1) SYN ACK Scan
    2) UDP Scan
    3) Comprehensive Scan\n
    """
)

response = input(initial_prompt)
print(f"You selected the option '{response}'")

if response == "1":
    print(f"Nmap Version: {scanner.nmap_version()}")
    scanner.scan(
        ip_addr, "1-1024", "-v -sS", sudo=True  # -sS is SYN ACK scan
    )  # ip address, port range, type of scan (verbose, SYN ACK)
    print(scanner.scaninfo())  # displays the type of scan
    print(
        f"IP Status: {scanner[ip_addr].state()}"
    )  # displays the status of the IP (up or down)
    print(
        scanner[ip_addr].all_protocols()
    )  # displays the protocols that are running on the IP
    print(
        f"Open Port: {scanner[ip_addr]['tcp'].keys() if 'tcp' in scanner[ip_addr] else None}"
    )
elif response == "2":
    print(f"Nmap Version: {scanner.nmap_version()}")
    scanner.scan(
        ip_addr, "1-1024", "-v -sU", sudo=True  # sU is UDP scan
    )  # ip address, port range, type of scan (verbose, SYN ACK)
    print(scanner.scaninfo())  # displays the type of scan
    print(
        f"IP Status: {scanner[ip_addr].state()}"
    )  # displays the status of the IP (up or down)
    print(
        scanner[ip_addr].all_protocols()
    )  # displays the protocols that are running on the IP
    print(
        f"Open Port: {scanner[ip_addr]['udp'].keys() if 'udp' in scanner[ip_addr] else None}"
    )
elif response == "3":
    print(f"Nmap Version: {scanner.nmap_version()}")
    scanner.scan(
        ip_addr,
        "1-1024",
        "-v -sS -sV -sC -A -O",
        sudo=True,  # -sV is version scan, -sC is script scan, -A is aggressive scan, -O is OS detection
    )  # ip address, port range, type of scan (verbose, SYN ACK)
    print(scanner.scaninfo())  # displays the type of scan
    print(
        f"IP Status: {scanner[ip_addr].state()}"
    )  # displays the status of the IP (up or down)
    print(
        scanner[ip_addr].all_protocols()
    )  # displays the protocols that are running on the IP
    print(
        f"Open Port: {scanner[ip_addr]['udp'].keys() if 'udp' in scanner[ip_addr] else None}"
    )
else:
    print("Please enter a valid option")
