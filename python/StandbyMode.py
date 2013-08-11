 #####################################SETUP####################################### 

# Standard setup starts
import RPi.GPIO as GPIO, time, os
from time import sleep
from sys import exit
GPIO.setmode(GPIO.BCM)

# Standard setup ends

def RCtime (RCpin): ## Setup LDR detection
        reading = 0
        GPIO.setup(RCpin, GPIO.OUT)
        GPIO.output(RCpin, GPIO.LOW)
        time.sleep(0.1)
 
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
GPIO.setup(22, GPIO.OUT) ##Setup LED - this may not be needed
GPIO.output(22, False) # Turn LED off - this may not be needed
GPIO.setup(23, GPIO.IN) # this turns the button to input on 23
laseroff()
playsound("sudo aplay -q /opt/ninja/drivers/tripwire_driver/sounds/ready.wav");

while True:

    #flashled(1.5); ## This is when waiting button press to arm system
    if ( GPIO.input(23) == False ):
        #print "button pressed"
        playsound("sudo aplay -q /opt/ninja/drivers/tripwire_driver/sounds/button.wav");
        #time.sleep(1)## wait 1 second so sound can play
        #GPIO.output(22, False) # Turn LED off
        #exit(0) # quit app - can't use as later commands are not passed
            
        bashCommand = "sudo python /opt/ninja/drivers/tripwire_driver/python/ArmTRIPWIRE.py" ## launch align helper
        os.system(bashCommand) 

            
    #sleep(0.1);
    #should detect button press and then launch arm Tripwire
