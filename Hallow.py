from gpiozero import Button
from picamera import PiCamera
from DmxPy import DmxPy
import time

# set gpio stuff
button = Button(21)

# set cam stuff
cam = PiCamera()
cam.exposure_mode = 'off'
cam.awb_mode = 'off'
cam.iso = '200'
### determine shutter speed for pics and set here
### c.shutter_speed = int(ss)

# set dmx stuff
dmx = DmxPy('/dev/USBTTY0')


while True:
    if button.is_pressed:
        fn = str(time.time()) + ".jpg"
        dmx.setChannel(1,200)
        dmx.setChannel(2,200)
        dmx.setChannel(3,200)
        dmx.render()
        cam.capture(fn)
    else:
        time.sleep(.1)
    time.sleep(3)
    

    




