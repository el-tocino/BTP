#!/usr/bin/python3
import sys
import socket
import subprocess
import time
import string 

interface = 'wlan0'

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
server.settimeout(0.2)
server.bind(("", 54321))
hname = socket.gethostname()

while True:
    cmd = subprocess.Popen('iwconfig %s' % interface, shell=True,
                           stdout=subprocess.PIPE)
    for line in cmd.stdout:
        if 'Link Quality' in line.decode("utf-8"):      
            rtime = time.time()
            signalstrength = line.decode("utf-8")
            signalstrength = signalstrength.split('=')[2]
            signalstrength = signalstrength.replace(' dBm','')
            pdata = hname + "," + str(rtime) + "," + signalstrength
            message = str.encode(pdata)
            server.sendto(message, ('<broadcast>', 37020))
            print(pdata)
    time.sleep(.05)
