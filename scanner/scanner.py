import socket

def scan_ports(host, port):
    try:
        socket.create_connection((host,port), timeout=1)
        return True
    except:
        return False