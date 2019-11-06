import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
        if GPIO.input(12):
                print ("Door open!")
        else:
                print ("DOOR CLOSED!")
time.sleep(0.1)
