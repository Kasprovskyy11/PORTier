from args.args import parse_args
from args.ports import parse_ports
from scanner.results import collect_results

import threading

args = parse_args()
host = args.host
ports = parse_ports(args.ports)
filter = args.filter
timeout = args.timeout

threads = []
results = []
lock = threading.Lock()
for i in ports:
    t = threading.Thread(target=collect_results, args=(host, i, results, lock, filter, timeout))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

results.sort(key=lambda x: x[0])

for port, state, banner in results:
    banner_str = f"{banner.strip()}" if banner else ""
    print(f"{port:<6} | {state:<10} | {banner_str}")

print(f"with timeout {timeout}s")