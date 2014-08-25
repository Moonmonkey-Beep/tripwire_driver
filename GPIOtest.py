#####################################SETUP####################################### 

# Standard setup starts
import RPi.GPIO as GPIO, time, os
import cPickle as pickle
from random import randint
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT) ##Setup Weapon Warm
GPIO.setup(15, GPIO.OUT) ##setup right wheel backward
GPIO.setup(17, GPIO.OUT) ##Setup Laser
GPIO.setup(21, GPIO.OUT) ##Setup Laser
GPIO.setup(18, GPIO.OUT) ##setup right wheel forward
GPIO.setup(22, GPIO.OUT) ##Setup Trigger
GPIO.setup(23, GPIO.IN) ##Setup Button 1
GPIO.setup(24, GPIO.OUT) ##setup left wheel forward
GPIO.setup(25, GPIO.OUT) ##setup left wheel backward
# Standard setup ends
   
    

GPIO.output(4, True) ## pin on
GPIO.output(4, False) ## pin off


GPIO.output(15, True) ## pin on
GPIO.output(15, False) ## pin off

GPIO.output(15, True) ## pin on
GPIO.output(15, False) ## pin off
standbymode()
   