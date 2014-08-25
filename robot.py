#####################################SETUP####################################### 

# Standard setup starts
import RPi.GPIO as GPIO, time, os
import cPickle as pickle
from random import randint
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT) ##Setup Weapon Warm
GPIO.setup(15, GPIO.OUT) ##setup right wheel backward
GPIO.setup(17, GPIO.OUT) ##Setup Laser
GPIO.setup(18, GPIO.OUT) ##setup right wheel forward
GPIO.setup(22, GPIO.OUT) ##Setup Trigger
GPIO.setup(23, GPIO.IN) ##Setup Button 1
GPIO.setup(24, GPIO.OUT) ##setup left wheel forward
GPIO.setup(25, GPIO.OUT) ##setup left wheel backward

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
	GPIO.output(17, False) ## pin on
   
   # defdine function
def laseroff():
	print "laser off" 
	GPIO.output(17, True) ## pin off


# define function
def WeaponWarm():
	print "weapon warm on" 
	GPIO.output(4, True) ## pin on
   
   # define function

	
def WeaponSingleFire():
	print "weapon fire (Single)" 
	GPIO.output(22, False) ## Trigger note this is invetered - true is off
	playsound("sudo aplay /opt/ninja/drivers/tripwire_driver/sounds/fire.wav");
	time.sleep(.25) 
	GPIO.output(22, True) ## trigger off note this is invetered - true is off
	GPIO.output(4, True) ## warmup off	 note this is invetered - true is off	

def WeaponFullAuto():
	print "weapon fire (Auto)" 
	GPIO.output(22, False) ## Trigger note this is invetered - true is off
	playsound("sudo aplay /opt/ninja/drivers/tripwire_driver/sounds/fire.wav");
	time.sleep(8) 
	GPIO.output(22, True) ## trigger off note this is invetered - true is off
	GPIO.output(4, True) ## warmup off	note this is invetered - true is off 
			


def Forward():
	GPIO.output(24, True) ## trigger off note this is invetered - true is off
	GPIO.output(18, True) ## trigger off note this is invetered - true is off
	print "leftF"
	time.sleep(2) 
	GPIO.output(24, False) ## trigger off note this is invetered - true is off
	GPIO.output(18, False) ## trigger off note this is invetered - true is off
		
def LeftForward():
	GPIO.output(24, True) ## trigger off note this is invetered - true is off
	print "leftF"
	time.sleep(2) 
	GPIO.output(24, False) ## trigger off note this is invetered - true is off
	
def leftBackward():
	GPIO.output(25, True) ## trigger off note this is invetered - true is off
	print "leftB"
	time.sleep(2) 
	GPIO.output(25, False) ## trigger off note this is invetered - true is off
		
def RightForward():
	GPIO.output(18, True) ## trigger off note this is invetered - true is off
	print "RightF"
	time.sleep(2) 
	GPIO.output(18, False) ## trigger off note this is invetered - true is off

def RightBackward():
	GPIO.output(15, True) ## trigger off
	print "RightB"
	time.sleep(2) 
	GPIO.output(15, False) ## trigger off

	   # define function
	#get the laser working!!
	
def FaceSpotted():
	print "face Identified" 
	sound = "spotted" # The Sound to play
	randnumber = randint(1,4) #Inclusive, the second figure is the largest file number for this sound
	randname =  "sudo aplay /opt/ninja/drivers/tripwire_driver/sounds/" + sound + str(randnumber) + ".wav"
	playsound(randname);
	laseron()
	WeaponWarm()
	time.sleep(2)
	WeaponSingleFire()
	LeftForward()
	time.sleep(1)
	leftBackward()
	time.sleep(1)
	RightForward()
	time.sleep(1)
	RightBackward()

			
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
   