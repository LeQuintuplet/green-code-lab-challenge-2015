import socket

HOST = ''
PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

print "Listening on port 12345 (UDP)"

while True:
    data, addr = sock.recvfrom(1024)
    print "message recu => " + data
    
