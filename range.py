#####################################SETUP####################################### 

# Standard setup starts
import RPi.GPIO as GPIO, time, os
GPIO.setmode(GPIO.BCM)




def laseron():
    GPIO.setup(11, GPIO.OUT) ##Setup Laser
    GPIO.output(11, True) ## Laser on


