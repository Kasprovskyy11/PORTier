def parse_ports(portsStr):
    ports = []
    if "-" in portsStr:
        scope = portsStr.split("-")
        for i in range(int(scope[0]), int(scope[1])+1):
            ports.append(i)
    else:
        ports.append(portsStr)
    return ports;