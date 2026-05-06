import socket
from service_describe.json_describe import json_describe


def scan_ports(host, port, timeout, version_detection):
    info = []
    try:
        connection = socket.create_connection((host,port), timeout=timeout)
        info.append("open")
        if not version_detection:
            try:
                info.append(json_describe(port))
            except:
                info.append("Service unknown")
        return info
    except ConnectionRefusedError:
        info.append("closed")
        info.append("")
        return info
    except:
        info.append("filtered")
        info.append("")
        return info