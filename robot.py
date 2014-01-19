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
	GPIO.output(17, True) ## Laser on


# define function
def WeaponArm():
	print "weapon warm on" 
	GPIO.setup(4, GPIO.OUT) ##Setup Laser
	GPIO.output(4, True) ## Laser on
   
   # define function
def WeaponDisarm():
	print "weapon warm off" 
	GPIO.setup(4, GPIO.OUT) ##Setup Laser
	GPIO.output(4, False) ## Laser on

def Attack():
	WeaponArm()
	laseron()
	playsound("sudo aplay /opt/ninja/drivers/tripwire_driver/sounds/detected.wav");

		

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
	 			laseron()

#####################################MAIN####################################### 

print "running StartSYSTEM"

standbymode()
   