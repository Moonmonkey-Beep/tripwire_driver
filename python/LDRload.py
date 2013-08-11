  #!/usr/bin/env python

# Example for RC timing reading for Raspberry Pi
# Must be used with GPIO 0.3.1a or later - earlier verions
# are not fast enough!

import RPi.GPIO as GPIO, time, os      

DEBUG = 1
GPIO.setmode(GPIO.BCM)

def RCtime (RCpin):
        reading = 0
        GPIO.setup(RCpin, GPIO.OUT)
        GPIO.output(RCpin, GPIO.LOW)
        time.sleep(0.1)

        GPIO.setup(RCpin, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(RCpin) == GPIO.LOW):
                reading += 1
        return reading

if True:                                     
        # Load the dictionary back from the pickle file.
        import pickle
        
        favorite_color = pickle.load( open( "save.p", "rb" ) )
        print favorite_color
        # favorite_color is now { "lion": "yellow", "kitty": "red" }	print lightlevel
