def main():
    import socket
    import time

    cdef str data
    cdef int timestamp
    cdef int timestampOld = 0

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 12345))
    sock.listen(1)
    conn, addr = sock.accept()

    while True:
        data, timestamp = conn.recv(1024), time.time()
        f = open("/opt/gclc/gclc.log", "w" if (timestamp-timestampOld > 300) else "a")
        timestampOld = timestamp
        f.write(data)
        f.close()

main()
