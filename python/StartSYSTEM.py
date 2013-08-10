#####################################SETUP####################################### 

# Standard setup starts
import RPi.GPIO as GPIO, time, os
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


#####################################MAIN####################################### 
##print "running StartSYSTEM"
laseroff()

##playsound("sudo aplay /usr/share/adafruit/webide/repositories/my-pi-projects/LaserTripWire/warmup.wav");   dont think we need this sound

while True: ## this quickly pulses the laser and checks if a signal is recieved if not recieved triggers setup.

    laseron(); # turn laser on pin #17
    
    # delare variable
 
    if (RCtime(18) < 1001): ## signal detected
        laseroff(); # turn laser off pin #17
        bashCommand = "sudo python /home/pi/laser/StandbyMode.py" ## launch standby
        os.system(bashCommand) 
        
    elif (RCtime(18) >1000):## no signal
        laseroff(); # turn laser off pin #17
        bashCommand = "sudo python /home/pi/laser/AlignTRIPWIRE.py" ## launch align helper
        os.system(bashCommand) 

    
    