#####################################SETUP####################################### 

# Standard setup starts
import RPi.GPIO as GPIO, time, os
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
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
    
    
    
    
# define function  
def AlignLaser(): # align laser
	
	laseroff()
	playchirps = 1
	playsound("sudo aplay -q /opt/ninja/drivers/tripwire_driver/sounds/setup.wav");
	playsound("sudo aplay -q /opt/ninja/drivers/tripwire_driver/sounds/warmup.wav");
	
	rightcount = 150 # this is how long it takes laser to align
	while True:
	    laseron(); # turn laser on pin #17
	    if (playchirps > 0): ## makes sure sound is only played once
	        playsound("sudo aplay -q /opt/ninja/drivers/tripwire_driver/sounds/align_instruction.wav");
	        playchirps = playchirps - 1
	    # delare variable
	 
	    if (rightcount > 1):
	            
	            if (RCtime(18) < 200): ## a good signal
	                playsound("sudo aplay -q /opt/ninja/drivers/tripwire_driver/sounds/beephigh.wav");
	                #flashled(.15);
	                rightcount = rightcount - 30 ## this number denotes a strong signal
	                print rightcount
	       
	            elif (RCtime(18) < 300):## a medium signal
	                playsound("sudo aplay -q /opt/ninja/drivers/tripwire_driver/sounds/beepmed.wav");
	                #flashled(.20);
	                rightcount = rightcount - 20
	                print rightcount
	                
	   
	            elif (RCtime(18) < 500):## a poor signal
	                playsound("sudo aplay -q /opt/ninja/drivers/tripwire_driver/sounds/beeplow.wav");
	                rightcount = rightcount - 5
	                print rightcount
	                
	            #elif (RCtime(18) > 1000):## no signal
	                #flashled(.25);               
	    else:
	        laseroff()
	        playsound("sudo aplay -q /opt/ninja/drivers/tripwire_driver/sounds/laser_aligned.wav");
	        #time.sleep(1)## wait 1 second so sound can play
	        
	        bashCommand = "sudo python /opt/ninja/drivers/tripwire_driver/python/StandbyMode.py" ## launch align helper
	        os.system(bashCommand) 
	
	

#####################################MAIN####################################### 
##print "running StartSYSTEM"
laseroff()


while True: ## this quickly pulses the laser and checks if a signal is recieved if not recieved triggers setup.

    laseron(); # turn laser on pin #17
    
    # delare variable
 
    if (RCtime(18) < 1001): ## signal detected STANDBY MODE
        laseroff(); # turn laser off 

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
        
                
    elif (RCtime(18) >1000):## no signal ALIGHN LASER
    	AlignLaser() ## calls align laser function (at the top)
       
    
    