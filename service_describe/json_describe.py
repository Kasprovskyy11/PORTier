import json
import os

def json_describe(port):
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "..", "services.json")

    file_path = os.path.abspath(file_path)

    with open(file_path) as f:
        services = json.load(f)
    return services.get(str(port), "Unknown service")