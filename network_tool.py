import os
import socket

def ping_host():
    host = input("Enter host to ping: ")
    os.system(f"ping {host}")

def dns_lookup():
    host = input("Enter domain: ")
    try:
        ip = socket.gethostbyname(host)
        print(f"IP Address: {ip}")
    except:
        print("DNS lookup failed")

def traceroute():
    host = input("Enter host: ")
    os.system(f"tracert {host}")

def menu():
    while True:
        print("\nNetwork Diagnostic Toolkit")
        print("1. Ping Host")
        print("2. DNS Lookup")
        print("3. Traceroute")
        print("4. Exit")

        choice = input("Select option: ")

        if choice == "1":
            ping_host()
        elif choice == "2":
            dns_lookup()
        elif choice == "3":
            traceroute()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

menu()