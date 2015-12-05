def main():
    import socket
    import time
    import datetime

    cdef str temps
    cdef list msgList

    ss = socket.socket
    sockUDP = ss(socket.AF_INET, socket.SOCK_DGRAM)
    sockUDP.bind(('', 514))
    sockTCP = ss(socket.AF_INET, socket.SOCK_STREAM)
    sockTCP.connect(('51.255.62.22', 12345))

    while 1:
        data, addr = sockUDP.recvfrom(1024)
        temps = datetime.datetime.fromtimestamp(time.time()).strftime('%b %e %R:%S')
        msgList = [ (c if ord(c) >= 32 else "#" + str( oct( ord(c) ) )) for c in data[:-1] ]
        sockTCP.send( "%s %s\n" % ( temps, "".join(msgList) ) )

main()
