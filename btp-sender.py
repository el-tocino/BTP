import sys
import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
server.settimeout(0.2)
server.bind(("", 44444))
packetdata = str.encode(sys.argv[1])
message = packetdata
server.sendto(message, ('<broadcast>', 37020))
print("message sent!")
