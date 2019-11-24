import time
from picamera import PiCamera
import os
import RPi.GPIO as GPIO

# Camera setup
camera = PiCamera()
camera.resolution = (2592, 1944)  # Resolution of pi camera 1.3
camera.start_preview()

# Wait until pins 4(5V) and 8(GPIO14) are connected
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN)
print("Pin disconnected. Connect pin 4 to 8 to start capture. Disconnect pins to stop.")
while(not GPIO.input(0)):
    time.sleep(1)
print("Starting capture.")

# Create new log file
count = 1
while(os.path.exists(str(count))):
    count += 1

os.mkdir(str(count))
f = open(str(count) + "/log.txt", "w+")
f.write("Timestamp: " + str(time.time()) + "\n")

# Camera warm-up time
for filename in camera.capture_continuous(str(count) + "/{counter:03d}.jpg"):
    f.write(str(time.time()) + "\n")
    print('Captured %s' % filename)
    if(not GPIO.input(0)):
        print("Pin disconnected. Ending capture.")
    time.sleep(5)  # wait 5 seconds

f.close()
