import socket
import picamera
import time

camera = picamera.PiCamera()
camera.led = False
camera.resolution = (1920, 1080)
hn = socket.getfqdn()

def snap():
    curtime = time.time()
    shotname = hn + str(curtime) + ".jpg"
    camera.capture(shotname)
    return(shotname)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.bind(("", 37020))
#print ("Listening for trigger packet!")
while True:
    data, addr = client.recvfrom(1024)
    #print ("evaluating packet data: %s!" % data)
    if data == b"shoot":
        print(snap())
        
    if data == b"quit":
        break
        
camera.close()
