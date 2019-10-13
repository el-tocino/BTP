from gpiozero import Button
from picamera import PiCamera
from DmxPy import DmxPy
import time

# set gpio stuff
button = Button(21) # pin 40 on a pi 3b.

# set cam stuff
cam = PiCamera()
cam.exposure_mode = 'off'
cam.awb_mode = 'off'
cam.iso = 200
cam.sensor_mode = 2
### determine shutter speed for pics and set here
### cam.shutter_speed = int(ss)

# set dmx stuff
try:
    dmx = DmxPy('/dev/USBTTY0')
except:
    dmx = DmxPy('/dev/USBTTY1')

# RUN FOREVER!
while True:
    if button.is_pressed:
        fn = str(time.time()) + ".png"
        dmx.setChannel(0,200)
        dmx.setChannel(1,200)
        dmx.setChannel(2,200)
        dmx.setChannel(3,200)
        dmx.render()
        cam.capture(fn)
        dmx.blackout()
        dmx.render()
        time.sleep(3)
    else:
        time.sleep(.1)

    




