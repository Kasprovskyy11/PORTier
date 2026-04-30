from scanner.scanner import scan_ports

def print_results(host, port):
    state = "Open" if scan_ports(host, port) else "Closed"
    print(f"{port:<6}|{state}")