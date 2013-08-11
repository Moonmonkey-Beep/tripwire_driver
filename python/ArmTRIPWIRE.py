#####################################SETUP####################################### 

# Standard setup starts
import RPi.GPIO as GPIO, time, os
from time import sleep
from sys import exit
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN) # this turns the button to input on 23

# Standard setup ends

def RCtime (RCpin): ## Setup LDR detection
        reading = 0
        GPIO.setup(RCpin, GPIO.OUT)
        GPIO.output(RCpin, GPIO.LOW)
        time.sleep(0.05)
 
        GPIO.setup(RCpin, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(RCpin) == GPIO.LOW):
                reading += 1
        return reading
        
# define function flashing LED - flash rate defined in the call
def flashled( str ):
    GPIO.setup(22, GPIO.OUT) ##Setup LED
    GPIO.output(22, True)
    time.sleep(str)
    GPIO.output(22, False)
    time.sleep(str)
    
    # define function playing sound - file defined in call
def playsound( str ):
    bashCommand = str
    import subprocess
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
   
# define function
def laseron():
    GPIO.setup(17, GPIO.OUT) ##Setup Laser
    GPIO.output(17, True) ## Laser on
   
   # define function
def laseroff():
    GPIO.setup(17, GPIO.OUT) ##Setup Laser
    GPIO.output(17, False) ## Laser on

##################################ACTIVE#####################################

## THE LOWER THE LIGHT CONDITIONS, THE HIGHER THE READING FROM THE PHOTOCELL
## PLAN TO MAKE THE ALERT LEVEL ADAPTIVE (TWICE AS MUCH DARKNESS AS LAST LIGHT LEVEL INSTEAD OF A FIXED NUMBER)
## ALSO SHOULD HAVE DIFFERENT TRIGGER WHEN LIGHT LEVEL INCREASES DRASTICLY - BUT NEED TO CALIBRATE TO AVOICE BEING TRIGGERED BY LIGHT SWITCHES
## NEED TO CHECK FOR DARKNESS ON FIRST RUN AND LAUNCH CALIBRATION MODE

playchirps = 1
playsound("sudo aplay -q /home/pi/laser/sounds/warmup.wav");
laseron(); # turn laser on pin #17
Alertlevel = 10000 ## set the base level very high for the first run to prevent false alarms

while True:


    Lightlevel = RCtime(18)

    print "0"
       
    Alertlevel = 2000


    if (playchirps > 0): ## makes sure sound is only played once
        playsound("sudo aplay -q /home/pi/laser/sounds/chirps.wav");
        playchirps = playchirps - 1
        
        
 
    if (Lightlevel > Alertlevel):
        
        # this is when intruder is detected
        #flashled(.1);  
        print "1"
  
        
        playsound("sudo aplay -q /home/pi/laser/sounds/detected.wav");
        #laseroff()

    else:
       if ( GPIO.input(23) == False ):
            #print "button pressed"
            playsound("sudo aplay -q /home/pi/laser/sounds/button.wav");
            laseroff()
            playsound("sudo aplay -q /home/pi/laser/sounds/deactivated.wav");
            bashCommand = "sudo python /home/pi/laser/StartSYSTEM.py" 
            ## launch start system
            os.system(bashCommand) 