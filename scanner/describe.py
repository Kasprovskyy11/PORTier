def describe_service(connection):
    try:
        connection.send(b"GET / HTTP/1.0\r\n\r\n")
        bytes = connection.recv(1024)
        decoded = bytes.decode("utf-8", errors="ignore")
        for line in decoded.split("\n"):
            if line.startswith("Server:"):
                return line.strip()
            
        printable = ''.join(c for c in decoded if c.isprintable()).strip()
        return printable[:50]

    except Exception as e:
        return f"ERROR: {e}"
    