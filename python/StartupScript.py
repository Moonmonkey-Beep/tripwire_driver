#####################################SETUP####################################### 

# Standard setup starts
import RPi.GPIO as GPIO, time, os
GPIO.setmode(GPIO.BCM)


#####################################MAIN####################################### 
print "running StartupScript"
bashCommand = "sudo python /home/pi/laser/StartSYSTEM.py"
os.system(bashCommand) 

