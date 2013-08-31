#####################################SETUP####################################### 

# Standard setup starts
import RPi.GPIO as GPIO, time, os
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

import cPickle as pickle
from random import randint


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


def standbymode():
    laseroff()
    pickle.dump( "Disarmed", open( "/opt/ninja/drivers/save.p", "wb" ) )
    print "Standby Mode"
    from random import randint
    randnumber2 = randint(1,4) #Inclusive

    if (randnumber2 == 1):
		playsound("sudo aplay /opt/ninja/drivers/tripwire_driver/sounds/standby1.wav");

    elif (randnumber2 == 2):
		playsound("sudo aplay /opt/ninja/drivers/tripwire_driver/sounds/standby2.wav");

    elif (randnumber2 == 3):
		playsound("sudo aplay /opt/ninja/drivers/tripwire_driver/sounds/standby3.wav");

    elif (randnumber2 == 4):
		playsound("sudo aplay /opt/ninja/drivers/tripwire_driver/sounds/standby4.wav");


    while True:

		#flashled(1.5); ## This is when waiting button press to arm system
			if ( GPIO.input(23) == False ):
				playsound("sudo aplay -q /opt/ninja/drivers/tripwire_driver/sounds/button.wav");       
				armtripwire()    
	    
def armtripwire():
	print "Arming Tripwire"
	pickle.dump( "Armed", open( "/opt/ninja/drivers/save.p", "wb" ) )
	playchirps = 1
	playsound("sudo aplay -q /opt/ninja/drivers/tripwire_driver/sounds/warmup.wav");
	laseron(); # turn laser on pin #17
	Alertlevel = 10000 ## set the base level very high for the first run to prevent false alarms
	Alarmcount = 0 ## how many times to play the alarm when triggered (makes sure Ninja Cloud detects it)
	while True:

	    Lightlevel = RCtime(18)
	
	    if (Alarmcount > 0):
	    	pickle.dump( "Alarm", open( "/opt/ninja/drivers/save.p", "wb" ) )
	    	print Alarmcount
	    	Alarmcount = Alarmcount - 1
	    else:
	    	pickle.dump( "Armed", open( "/opt/ninja/drivers/save.p", "wb" ) )	    
	    	
	       
	    Alertlevel = 2000 ## this is the ammount of darkness which triggers the alarm
	
	
	    if (playchirps > 0): ## makes sure sound is only played once
	       

			playchirps = playchirps - 1
			randnumber = randint(1,4) #Inclusive

	 
			if (randnumber == 1):
				playsound("sudo aplay /opt/ninja/drivers/tripwire_driver/sounds/activated1.wav");
				playchirps = playchirps - 1
			elif (randnumber == 2):
				playsound("sudo aplay /opt/ninja/drivers/tripwire_driver/sounds/activated2.wav");
				playchirps = playchirps - 1
			elif (randnumber == 3):
				playsound("sudo aplay /opt/ninja/drivers/tripwire_driver/sounds/activated3.wav");
				playchirps = playchirps - 1
			elif (randnumber == 4):
				playsound("sudo aplay /opt/ninja/drivers/tripwire_driver/sounds/activated4.wav");
				playchirps = playchirps - 1
	        
	        
	 
	    if (Lightlevel > Alertlevel):
	        
	        # this is when intruder is detected
	        #flashled(.1);  
	        Alarmcount = 20 ## how many times to play the alarm when triggered (makes sure Ninja Cloud detects it)
	        if (Alarmcount >= 0):
	        	print Alarmcount
	        	Alarmcount = Alarmcount - 1
	  
	        
	        playsound("sudo aplay -q /opt/ninja/drivers/tripwire_driver/sounds/detected.wav");


	        #laseroff()
	
	    else:
	       if ( GPIO.input(23) == False ):
	            print "button pressed"
	            playsound("sudo aplay /opt/ninja/drivers/tripwire_driver/sounds/button.wav");
	            laseroff()
	            playsound("sudo aplay /opt/ninja/drivers/tripwire_driver/sounds/deactivated.wav");
	            standbymode()
    
# define function  
def AlignLaser(): # align lasers
	print "Aligning Tripwire"
	laseroff()
	pickle.dump( "Align", open( "/opt/ninja/drivers/save.p", "wb" ) )## create a file with zero in it
	playchirps = 1
	playsound("sudo aplay /opt/ninja/drivers/tripwire_driver/sounds/setup.wav");
	playsound("sudo aplay /opt/ninja/drivers/tripwire_driver/sounds/warmup.wav");
	
	rightcount = 150 # this is how long it takes laser to align
	
	while True:
	    laseron() # turn laser on pin #17
	    if (playchirps > 0): ## makes sure sound is only played once
	        #playsound("sudo aplay -q /opt/ninja/drivers/tripwire_driver/sounds/align_instruction.wav");
	        playchirps = playchirps - 1

	 
	    if (rightcount > 1):
	            
	            if (RCtime(18) < 200): ## a good signal
	                playsound("sudo aplay /opt/ninja/drivers/tripwire_driver/sounds/beephigh.wav");
	                #flashled(.15);
	                rightcount = rightcount - 30 ## this number denotes a strong signal
	                print rightcount
	       
	            elif (RCtime(18) < 300):## a medium signal
	                playsound("sudo aplay /opt/ninja/drivers/tripwire_driver/sounds/beepmed.wav");
	                #flashled(.20);
	                rightcount = rightcount - 20
	                print rightcount
	                
	   
	            elif (RCtime(18) < 500):## a poor signal
	                playsound("sudo aplay /opt/ninja/drivers/tripwire_driver/sounds/beeplow.wav");
	                rightcount = rightcount - 5
	                print rightcount
	                
	            #elif (RCtime(18) > 1000):## no signal
	                #flashled(.25);               
	    else:
	        	standbymode()

def mirrorchecker():
	laseroff()

		 ## this quickly pulses the laser and checks if a signal is recieved if not recieved triggers setup.

	laseron(); # turn laser on pin #17
	    
	    # delare variable
	 
	if (RCtime(18) < 1001): ## signal detected STANDBY MODE
	        laseroff() # turn laser off
	        print "aligned"
	        standbymode()

	                    
	                
	elif (RCtime(18) >1000):## no signal ALIGN LASER
	        print "not aligned"
	    	AlignLaser() ## calls align laser function (at the top)


	       
	        	

#####################################MAIN####################################### 

print "running StartSYSTEM"

mirrorchecker()
   