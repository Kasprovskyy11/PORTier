def check_probe(probe, connection):
    if probe is None:
        return None
    try:
        connection.send(probe)
        bytes = connection.recv(1024)
        return bytes
    except:
        pass