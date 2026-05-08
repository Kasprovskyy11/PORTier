import socket
from service_describe.json_describe import json_describe
from service_describe.banner_grabbing import banner_grabbing


def scan_ports(host, port, timeout, version_detection):
    info = []
    try:
        connection = socket.create_connection((host,port), timeout=timeout)
        info.append("open")
        if version_detection:
                info.append(banner_grabbing(connection, port, timeout))
        else:
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