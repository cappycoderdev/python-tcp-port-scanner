import socket

def port_scanner():
    target = input("Enter domain or IP to scan: ")
    try:
        ip = socket.gethostbyname(target)
        print(f"\nScanning {target} ({ip}) for open TCP ports...\n")
    except:
        print("DNS lookup failed. Check the domain/IP.")
        return

    # Get port range from user
    try:
        start_port = int(input("Enter starting port (e.g., 20): "))
        end_port = int(input("Enter ending port (e.g., 100): "))
    except ValueError:
        print("Invalid input. Please enter numbers for ports.")
        return

    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("Invalid port range. Ports must be between 1 and 65535, and start <= end.")
        return

    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is closed")
        s.close()

    print("\nScan completed.")

if __name__ == "__main__":
    port_scanner()