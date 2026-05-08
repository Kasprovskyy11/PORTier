import os
import json

from service_describe.check_probe import check_probe
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "probe.json")
file_path = os.path.abspath(file_path)


with open(file_path, encoding="utf-8") as f:
    raw = json.load(f)
    probes = {int(k): v.encode('latin-1') for k, v in raw.items()}

def banner_grabbing(connection, port, timeout):
    try:
        connection.settimeout(timeout)
        try:
            bytes = connection.recv(1024)
        except Exception as e:
            print(f"DEBUG recv error: {e}")
            bytes = None
        if bytes:
            print(f"DEBUG bytes: {bytes[:50]}")  # pierwsze 50 bajtów
            return bytes.decode('utf-8', errors="ignore").partition('\n')[0]
        else:
            try:
                return check_probe(probes.get(port), connection).decode('utf-8', errors="ignore").partition('\n')[0]
            except:
                    for probe in probes.values():
                        received = check_probe(probe, connection)
                        if received:
                            return received.decode('utf-8', errors="ignore").partition('\n')[0]
    except Exception as e:
        print(f"DEBUG error: {e}")
        return ""
    return ""   