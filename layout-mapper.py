import sys
import socket
import time
import numpy as np



def Average(lst): 
    return sum(lst) / len(lst)


client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.bind(("", 37020))
sslist = []

t_end = time.time() + 10 
while time.time() < t_end:
    data, addr = client.recvfrom(1024)
    data = data.decode()
    entry = data.split(',')
    #logfile.write(entry)
    phn = entry[0]
    sstr = int(entry[2])
    addtolist = (phn, sstr)
    sslist.append(addtolist)

#strave = Average(sslist)
parse1 = [item[0] for item in sslist]
parse1 = sorted(set(parse1))
for hname in parse1:
    sum = 0
    count = 0
    for line in sslist:
        if (line[0] == hname):
            sum = (sum + line[1])
            count = (count + 1) 
    haver = (sum / count)
    csvout = hname + "," + str(haver)

