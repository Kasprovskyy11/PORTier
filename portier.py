from args.args import parse_args
from args.ports import parse_ports
from scanner.results import print_results

import threading

args = parse_args()
host = args.host
ports = parse_ports(args.ports)

threads = []
for i in ports:
    t = threading.Thread(target=print_results, args=(host, i))
    t.start()
    threads.append(t)

for t in threads:
    t.join()