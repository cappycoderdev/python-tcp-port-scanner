Python TCP Port Scanner

A simple Python tool that scans a target domain or IP address to identify open TCP ports.

This project was built to better understand how **network services, TCP connections, and sockets** work in real-world networking.

Features

1. Scans a **customizable port range**
2. Resolves **domain names to IP addresses (DNS lookup)**
3. Attempts **TCP connections** to determine if ports are open
4. Displays **open and closed ports**

 How It Works??

1. User enters a **domain or IP address**
2. The program resolves the domain using **DNS**
3. The scanner attempts to establish a **TCP connection** to each port in the specified range
4. If the server responds to the **TCP handshake**, the port is considered **open*
