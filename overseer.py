#import logging
import time
import socket
import os
import sys
import threading
from gpiozero import Servo

""" Using pre-mapped data, take updates from the reporters
    then adjust the servos in relation.  """

def selfconfigure(paramsfilef):
    with open(paramsfilef, "r") as f:
        paramline = f.read().splitlines()
        if paramline[0] = 'hostnames':
        if paramline[0] = 'UR':
        if paramline[0] = 'CP':
        if paramline[0] = 'LL':
        if paramline[0] = 'start_pos':

# hn_ll
# hn_cp
# hn_ur
# for hname in split(paramline[1],","):
#    x_min = LL.hname[1]
#    x_cp = CP.hname[2]
#    x_max = UR.hname[3]
#    for y in range(-10, 0, 1):
#        incrementer = ((x_cp - x_min) / 9)
#        y_val = (x_min + (incrementer * (y - 1)))
#        new_y = (hname,y_val)
#        y_range.append(new_y)
#        
#    y_cp = (hname, x_cp)
#    y_range.append(y_cp)
#    for y in range(1,11):
#        incrementer = ((x_max - x_cp) / 9)
#        y_val = (x_min + (incrementer * (y - 1)))
#        new_y = (hname,y_val)
#        y_range.append(new_y)
#     

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.bind(("", 37020))
curdata = {}
paramsfile = argv[1]
selfconfigure(paramsfile)
servo_x = Servo(17)
servo_y = Servo(27)
servo_x.value(cur_x)
servo_y.value(cur_y)
target_x = cur_x
target_y = cur_y

def listener():
    """ Listen for UDP packets from reporters and update curdata"""
    while True:
        data, addr = client.recvfrom(1024)
        data = data.decode()
        entry = data.split(',')
        #logfilename.write(entry)
        phn = entry[0]
        newvals = (entry[1],entry[2])
        curdata.update({phn: newvals})

def map_target(cur_data):
    for phn in (cur_data[0]:
        host_str = cur_data[2]
        #
        relative_pos = ((host_str - min) * 100) / (max - min)
        
        if target_x > 1:
            target_x = 1
        if target_x < -1:
            target_x = -1
        if target_y > 1:
            target_y = 1
        if target_y < -1:
            target_y = -1

    print("mapping out circle of interest")

def move_servo():
    """ calc two midpoints, then move servo to mids then target"""
    while True:
        if cur_x != target_x or cur_y != target_y:
            mid_x1 = (cur_x + ( .25 * (target_x - cur_x)))
            mid_y1 = (cur_y + ( .25 * (target_y - cur_y)))
            mid_x2 = (cur_x + ( .75 * (target_x - cur_x)))
            mid_y2 = (cur_y + ( .75 * (target_y - cur_y)))
            servo_x.value(mid_x1)
            servo_y.value(mid_y1)
            servo_x.value(mid_x2)
            servo_y.value(mid_y2)
            servo_x.value(target_x)
            servo_y.value(target_y)
            cur_x = targetx
            cur_y = targety
            #print("Current position:", cur_x, cur_y)
            time.sleep(.015)

def main():
    """ Do the stuff and the things."""
    listen_thread = threading.Thread(target=listener)
    listen_thread.start()
    move_thread = threading.Thread(target=move_servo)
    move_thread.start()
    while True:
        map_target(curdata)
        print(cur_x, cur_y)
        time.sleep(.2)

main()

exit()
