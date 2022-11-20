# import requirements
import Rpi.GPIO as GPIO
import time
import sleep

#setup
GPIO.SETUP(8,GPIO.OUT,initial=GPIO.LOW)
GPIO.SETUP(9,GPIO.OUT,initial=GPIO.LOW)
GPIO.SETUP(10,GPIO.OUT,initial=GPIO.LOW)

#infinite loop
while true:
    onOff(8)
    onOff(9)
    onOff(10)

#finction
def onOff(a):
    GPIO.output(a,GPIO.HIGH)
    sleep(5)
    GPIO.output(a,GPIO.LOW)
    sleep(1)