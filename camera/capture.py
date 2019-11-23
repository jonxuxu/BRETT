import time
from picamera import PiCamera
import os

# Camera setup
camera = PiCamera()
camera.resolution = (2592, 1944)  # Resolution of pi camera 1.3
camera.start_preview()

# Create new log file
count = 1
while(os.path.exists(str(count))):
    count += 1

os.mkdir(str(count))
f = open(str(count) + "/log.txt", "w+")
f.write("Timestamp: " + str(time.time()) + "\n")

# Camera warm-up time
time.sleep(1)
for filename in camera.capture_continuous(str(count) + "/{counter:03d}.jpg"):
    f.write(str(time.time()) + "\n")
    print('Captured %s' % filename)
    time.sleep(5)  # wait 5 seconds

f.close()
