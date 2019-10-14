import time
import array
from gpiozero import Button
from picamera import PiCamera
from ola.ClientWrapper import ClientWrapper

# set gpio stuff
button = Button(21) # pin 40 on a pi 3b.

# set cam stuff
cam = PiCamera()
cam.exposure_mode = 'off'
cam.awb_mode = 'off'
cam.iso = 200
cam.sensor_mode = 2
cam.shutter_speed = int(67998)

def DmxSent(state):
  wrapper.Stop()

universe = 1
lred = array.array('B', [100, 100])
lgreen = array.array('B', [100, 0, 100])
lblue = array.array('B', [100, 0, 0, 100])
lall = array.array('B', [250, 220, 200, 220])
loff = array.array('B', [0, 0, 0, 0, 0])
    
# RUN FOREVER!
while True:
    if button.is_pressed:
        fn = str(time.time()) + ".png"
        wrapper = ClientWrapper()
        client = wrapper.Client()
        client.SendDmx(universe, lall, DmxSent)
        cam.capture(fn)
        client.SendDmx(universe, loff, DmxSent)
        time.sleep(3)
    else:
        time.sleep(.1)
