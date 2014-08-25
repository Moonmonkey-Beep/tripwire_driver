#####################################SETUP####################################### 

# Standard setup starts
import RPi.GPIO as GPIO, time, os
GPIO.setmode(GPIO.BCM)


while True:

		def laseron():
			GPIO.setup(9, GPIO.OUT) ##Setup Laser
			GPIO.output(9, True) ## Laser on


