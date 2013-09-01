Section = '"sudo cd /opt/ninja/drivers/tripwire_driver/sounds/"'
sound = "deactivated1.wav" % Section



def playsound( str ):
    bashCommand = str
    import subprocess
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]


playsound("sound");
