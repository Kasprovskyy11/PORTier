from scanner.scanner import scan_ports

results = []

def collect_results(host, port, results, lock, filter):
    state = "open" if scan_ports(host, port) else "closed"
    if filter == "open":
        if state == "open":
            with lock:
                results.append((port, state))
    elif filter == "closed":
        if state == "closed":
            with lock:
                results.append((port, state))
    else:
        with lock:
            results.append((port, state))

    return results