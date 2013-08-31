#####################################SETUP####################################### 

# Standard setup starts
import RPi.GPIO as GPIO, time, os
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

import cPickle as pickle
from random import randint
import time


# Standard setup ends

def RCtime (RCpin): ## Setup LDR detection
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(0.05)     # adjust speed of reading
    GPIO.setup(RCpin, GPIO.IN)
    while (GPIO.input(RCpin) == GPIO.LOW):
        reading += 1
        return reading

Count = 100 ## how many times to play the alarm when triggered (makes sure Ninja Cloud detects it)




#flashled(1.5); ## This is when waiting button press to arm system

while True:
		

	if ( GPIO.input(23) == False ):

	
			if (Count > 0):
				print Count
				Count = Count - 1   
				time.sleep(.5)
	 
 	


if (Count > 50):
	print "short"
	print Count

else:
	print "long"  
	print Count

