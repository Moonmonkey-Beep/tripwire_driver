import RPi.GPIO as GPIO, time, os


#####################################MAIN####################################### 
print "running StartupScript"
bashCommand = "sudo python /opt/ninja/drivers/tripwire_driver/main.py"
os.system(bashCommand) 

