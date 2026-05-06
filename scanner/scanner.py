import socket


def scan_ports(host, port, timeout):
    info = []
    try:
        connection = socket.create_connection((host,port), timeout=timeout)
        info.append("open")
        info.append("")
        return info
    except ConnectionRefusedError:
        info.append("closed")
        info.append("")
        return info
    except:
        info.append("filtered")
        info.append("")
        return info