def playsound( str ):

	print (str)


from random import randint


sound = "standby"
randnumber = randint(1,4) #Inclusive, the second figure is the largest file for this sound
randname =  "sudo aplay /opt/ninja/drivers/tripwire_driver/sounds/" + sound + str(randnumber) + ".wav"
playsound(randname);
