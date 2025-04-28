import RPi.GPIO as GPIO
import time

from picamera2 import Picamera2, Preview

swPin = 14

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(swPin,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)

picam2 = Picamera2()
picam2.preview_configuration.main.size = (800,600)
picam2.configure('preview')
picam2.start(show_preview = True)

oldSw = 0
newSw = 0

cnt = 1

try:
    while True:
        newSw = GPIO.input(swPin)
        if newSw != oldSw:
            oldSw = newSw

            if newSw == 1:
                file_name = 'click ' + str(cnt)
                print(file_name)
                picam2.capture_file(f'/home/pi30405/1_camera/click_num/{file_name}.jpg')
                cnt += 1
            time.sleep(0.2)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
