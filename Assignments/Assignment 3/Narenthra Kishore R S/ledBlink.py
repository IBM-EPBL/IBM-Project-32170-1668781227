# import requirements
import Rpi.GPIO as GPIO
import time
import sleep

#setup
GPIO.SETUP(8,GPIO.OUT,initial=GPIO.LOW)
while true:
    GPIO.output(8,GPIO.HIGH)
    sleep(1)
    GPIO.output(8,GPIO.LOW)
    sleep(1)