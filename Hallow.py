import time
import array
from PIL import Image
from gpiozero import Button
from picamera import PiCamera
from ola.ClientWrapper import ClientWrapper

# set gpio stuff
button = Button(21) # pin 40 on a pi 3b.

# set cam stuff
cam = PiCamera()

def DmxSent(state):
  wrapper.Stop()

overlayimg = Image.open ("overlay.png")

universe = 1
lred = array.array('B', [100, 100])
lgreen = array.array('B', [100, 0, 100])
lblue = array.array('B', [100, 0, 0, 100])
lall = array.array('B', [250, 240, 200, 250])
loff = array.array('B', [0, 0, 0, 0, 0])

cam.start_preview()

wrapper = ClientWrapper()
client = wrapper.Client()
client.SendDmx(universe, lall, DmxSent)
cam.iso = 200
time.sleep(2)
cam.shutter_speed=cam.exposure_speed
#cam.exposure_mode = 'off'
#cam.awb_mode = 'off'
print (cam.shutter_speed, cam.awb_gains)
client.SendDmx(universe, loff, DmxSent)
cam.sensor_mode = 2
cam.resolution = (2592, 1944)

    
# RUN FOREVER!
while True:
    if button.is_pressed:
        ct = str(time.time())
        fn = ct + ".jpg"
        wrapper = ClientWrapper()
        client = wrapper.Client()
        client.SendDmx(universe, lall, DmxSent)
        time.sleep(.1)
        cam.capture(fn)
        print (cam.shutter_speed, cam.awb_gains)
        client.SendDmx(universe, loff, DmxSent)
        bgimage = Image.open(fn)
        oimg = Image.new('RGBA', (2592,1944), (0, 0, 0, 0)) 
        oimg.paste(bgimage, (0,0))
        oimg.paste(overlayimg, (0,0), mask=overlayimg)
        nfn = "/home/pi/snaps/" + ct + ".png"
        oimg.save(nfn, format="png")
        time.sleep(1)
    else:
        time.sleep(.1)

