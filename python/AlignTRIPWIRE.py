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
    output = process.communicate()
       
# define function
def laseron():
    GPIO.setup(17, GPIO.OUT) ##Setup Laser
    GPIO.output(17, True) ## Laser on
   
   # define function
def laseroff():
    GPIO.setup(17, GPIO.OUT) ##Setup Laser
    GPIO.output(17, False) ## Laser on


#####################################MAIN####################################### 
laseroff()
playchirps = 1
playsound("sudo aplay -q /home/pi/laser/sounds/setup.wav");
playsound("sudo aplay -q /home/pi/laser/sounds/warmup.wav");

rightcount = 100 # this is how long it takes laser to align
while True:
    laseron(); # turn laser on pin #17
    if (playchirps > 0): ## makes sure sound is only played once
        playsound("sudo aplay -q /home/pi/laser/sounds/align_instruction.wav");
        playchirps = playchirps - 1

    
    # delare variable
 
    if (rightcount > 1):
            
            if (RCtime(18) < 200): ## a good signal
                playsound("sudo aplay -q /home/pi/laser/sounds/beephigh.wav");
                #flashled(.15);
                rightcount = rightcount - 30
                print rightcount
       
            elif (RCtime(18) < 300):## a medium signal
                playsound("sudo aplay -q /home/pi/laser/sounds/beepmed.wav");
                #flashled(.20);
                rightcount = rightcount - 20
                print rightcount
                
   
            elif (RCtime(18) < 500):## a poor signal
                playsound("sudo aplay -q /home/pi/laser/sounds/beeplow.wav");
                rightcount = rightcount - 5
                print rightcount
                
            #elif (RCtime(18) > 1000):## no signal
                #flashled(.25);
                
    else:
        laseroff()
        playsound("sudo aplay -q /home/pi/laser/sounds/laser_aligned.wav");
        #time.sleep(1)## wait 1 second so sound can play
        
        bashCommand = "sudo python /home/pi/laser/StandbyMode.py" ## launch align helper
        os.system(bashCommand) 

    
    