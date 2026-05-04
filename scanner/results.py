from scanner.scanner import scan_ports

results = []

def collect_results(host, port, results, lock, filter, timeout):
    state = scan_ports(host, port, timeout)
    if filter == "open":
        if state[0] == "open":
            with lock:
                results.append((port, state[0], state[1]))
    elif filter == "closed":
        if state[0] == "closed":
            with lock:
                results.append((port, state[0], state[1]))
    elif filter == "filtered":
        if state[0] == "filtered":
            with lock:
                results.append((port, state[0], state[1]))
    else:
        with lock:
                results.append((port, state[0], state[1]))
    return results