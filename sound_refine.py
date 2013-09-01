#####################################SETUP####################################### 



import cPickle as pickle
from random import randint


    # define function playing sound - file defined in call
def playsound( str ):
    bashCommand = str % ".wav"
    import subprocess
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
 
playsound("opt/ninja/drivers/tripwire_driver/sounds/detected.wav");
