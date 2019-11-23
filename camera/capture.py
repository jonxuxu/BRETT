from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (2592, 1944)  # Resolution of pi camera 1.3
camera.start_preview()
# Camera warm-up time
sleep(2)
for filename in camera.capture_continuous('img{counter:03d}.jpg'):
    print('Captured %s' % filename)
    sleep(5)  # wait 5 seconds
