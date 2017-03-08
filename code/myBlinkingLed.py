#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

def Blink(num):
     for i in range(0,num):
         print "blink #" + str(i+1)
         GPIO.output(17,True)
         time.sleep(.5)
         GPIO.output(17,False)
         time.sleep(.5)
     print "done!!"
     
while True:
    Blink(3)
    time.sleep(5)
    Blink(4)
    time.sleep(5)
GPIO.cleanup()
