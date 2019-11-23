from time import sleep
from picamera import PiCamera
import calendar
import os

# Camera setup
camera = PiCamera()
camera.resolution = (2592, 1944)  # Resolution of pi camera 1.3
camera.start_preview()

# Create new log file
count = 1
while(not path.exists(str(count))){
    count += 1
}
os.mkdir(str(count))
f = open(str(count) + "/log.txt", "w+")
f.write("Timestamp:\n")

# Camera warm-up time
sleep(2)
for filename in camera.capture_continuous(str(count) + '/{counter:03d}.jpg'):
    f.write(calendar.timegm(dt.utctimetuple() + "\n")
    print('Captured %s' % filename)
    sleep(5)  # wait 5 seconds

f.close()
