import socket
import time

#store entries?
#logfn = str(time.time() + ".log")
#logfile = open(logfn,"w")

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.bind(("", 37020))
curdata = {}

while True:
    data, addr = client.recvfrom(1024)
    data = data.decode()
    entry = data.split(',')
    #logfile.write(entry)
    phn = entry[0]
    newvals = (entry[1],entry[2])
    curdata.update({phn: newvals})
    print (entry[0], entry[1], entry[2])


