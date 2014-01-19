#####################################SETUP####################################### 

# Standard setup starts
import RPi.GPIO as GPIO, time, os
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)


import cPickle as pickle
from random import randint

# Standard setup ends





    
    # define function playing sound - file defined in call
def playsound( str ):
    bashCommand = str
    import subprocess
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
   
# define function
def laseron():
	print "laser on" 
	GPIO.setup(17, GPIO.OUT) ##Setup Laser
	GPIO.output(17, False) ## Laser on
   
   # define function
def laseroff():
	print "laser off" 
	GPIO.setup(17, GPIO.OUT) ##Setup Laser
	GPIO.output(17, False) ## Laser on

	   # define function
def FaceSpotted():
	print "face Identified" 
	sound = "spotted" # The Sound to play
	randnumber = randint(1,4) #Inclusive, the second figure is the largest file number for this sound
	randname =  "sudo aplay /opt/ninja/drivers/tripwire_driver/sounds/" + sound + str(randnumber) + ".wav"
	playsound(randname);
	WeaponWarm()
	time.sleep(2)
	WeaponSingleFire()


# define function
def WeaponWarm():
	print "weapon warm on" 
	GPIO.setup(4, GPIO.OUT) ##Setup Laser
	GPIO.output(4, False) ## Laser on
   
   # define function

	
def WeaponSingleFire():
	print "weapon fire" 

	GPIO.setup(22, GPIO.OUT) ##Trigger
	GPIO.output(22, False) ## Trigger
	playsound("sudo aplay /opt/ninja/drivers/tripwire_driver/sounds/fire.wav");
	time.sleep(.5) 
	GPIO.output(22, True) ## trigger off
	GPIO.output(4, True) ## warmup off		
	


def shutdown():
	randnumber = randint(1,2) #Inclusive


	pickle.dump( "Offline", open( "/opt/ninja/drivers/save.p", "wb" ) )

	playsound("sudo aplay /opt/ninja/drivers/tripwire_driver/sounds/deactivated1.wav");

	laseroff()
	time.sleep(3) 
	bashCommand = "sudo halt"
	os.system(bashCommand)


def standbymode():
    laseroff()
    pickle.dump( "Disarmed", open( "/opt/ninja/drivers/save.p", "wb" ) )
    print "Standby Mode"

    sound = "standby" # The Sound to play
    randnumber = randint(1,2) #Inclusive, the second figure is the largest file number for this sound
	
    randname =  "sudo aplay /opt/ninja/drivers/tripwire_driver/sounds/" + sound + str(randnumber) + ".wav"
    playsound(randname);


    while True:


			if ( GPIO.input(23) == False ):
				playsound("sudo aplay -q /opt/ninja/drivers/tripwire_driver/sounds/buttonup.wav");      
				print "button pressed" 
	 			FaceSpotted()

#####################################MAIN####################################### 

print "running StartSYSTEM"

standbymode()
   