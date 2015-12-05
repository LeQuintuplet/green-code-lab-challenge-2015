import socket
import time

IP = "51.255.62.22"
PORT = 12345
MESSAGE = "Hello, World!"
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

print "UDP target IP:", IP
print "UDP target port:", PORT

for i in range(3):
	sock.sendto(MESSAGE + " (" + str(i+1) + ")", (IP, PORT))
	print "message : " + MESSAGE + " (" + str(i+1) + ")"
	time.sleep(2)
