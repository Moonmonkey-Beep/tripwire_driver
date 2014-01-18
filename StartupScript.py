import RPi.GPIO as GPIO, time, os
from random import randint

def playsound( str ):
    bashCommand = str
    import subprocess
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
   
#####################################MAIN####################################### 
print "running StartupScript"

from random import randint
randnumber = randint(1,2) #Inclusive

if (randnumber == 1):
		playsound("sudo aplay /opt/ninja/drivers/tripwire_driver/sounds/hello1.wav");

elif (randnumber == 2):
		playsound("sudo aplay /opt/ninja/drivers/tripwire_driver/sounds/hello2.wav");


#bashCommand = "sudo python /opt/ninja/drivers/tripwire_driver/robot.py"
#os.system(bashCommand) 

