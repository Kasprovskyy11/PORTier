from args.args import parse_args
from args.ports import parse_ports
from scanner.results import collect_results

import threading

args = parse_args()
host = args.host
ports = parse_ports(args.ports)
filter = args.filter
timeout = args.timeout
version_detection = args.vC

threads = []
results = []
lock = threading.Lock()
for i in ports:
    t = threading.Thread(target=collect_results, args=(host, i, results, lock, filter, timeout, version_detection))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

results.sort(key=lambda x: x[0])

for port, state, service in results:
    print(f"{port:<6} | {state:<8} | {service}")

