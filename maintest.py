#####################################SETUP####################################### 

# Standard setup starts


import cPickle as pickle




def armtripwire():

	playchirps = 1
	Alertlevel = 10000 ## set the base level very high for the first run to prevent false alarms
	Alarmcount = 400 ## how many times to play the alarm when triggered (makes sure Ninja Cloud detects it)
	import cPickle as pickle
	#pickle.dump( "0", open( "save.p", "wb" ) )## create a file with zero in it
	while True:
	
	
	    Lightlevel = 10
	
	    if (Alarmcount > 0):
	    	pickle.dump( Alarmcount, open( "save.p", "wb" ) )
	    	print Alarmcount
	    	Alarmcount = Alarmcount - 1
	     
	    	
	       
	    Alertlevel = 2000 ## this is the ammount of darkness which triggers the alarm
	
	
armtripwire()    
