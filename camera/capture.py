import time
from picamera import PiCamera
import os
import RPi.GPIO as GPIO
from subprocess import call

# Camera setup
camera = PiCamera()
camera.resolution = (2592, 1944)  # Resolution of pi camera 1.3
camera.start_preview()

# Wait until pins GPIO16 and GPIO21 are connected
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(21, GPIO.OUT)
GPIO.output(21, 1)
while(not GPIO.input(16)):
    if(GPIO.input(20)):  # Connect BCM 20 to 21 to shutdown
        break
    while(not GPIO.input(16)):
        print("Pin disconnected. Connect BCM pins 16 and 21 to start capture. Disconnect pins to stop.")
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
        if(not GPIO.input(16)):
            print("Pin disconnected. Ending capture.")
            break
        time.sleep(5)  # wait 5 seconds
    f.close()

while(True):
    if(GPIO.input(20)):
        print("Shutting down")
        time.sleep(1)
        call("sudo shutdown -h now", shell=True)
    print("Connect BCM 20 to 21 to shutdown headless")
    time.sleep(3)
