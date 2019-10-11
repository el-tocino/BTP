import RPi.GPIO as GPIO
from picamera import PiCamera
from DmxPy import DmxPy
import time

# set gpio stuff
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# set cam stuff
cam = PiCamera()
cam.exposure_mode = 'off'
cam.awb_mode = 'off'
cam.iso = '200'
### determine shutter speed for pics and set here
### c.shutter_speed = int(ss)

# set dmx stuff
dmx = DmxPy('/dev/USBTTY0')




GPIO.input(channel)

dmx.setChannel(1,200)
dmx.setChannel(2,200)
dmx.setChannel(3,200)
dmx.render()




