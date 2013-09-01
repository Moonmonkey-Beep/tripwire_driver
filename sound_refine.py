def playsound( str ):
    earlyCommand = "mee"
    rudeCommand = "pooo"
    bashCommand = rudeCommand % earlyCommand
    import subprocess
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print bashCommand

#playsound("sudo aplay /opt/ninja/drivers/tripwire_driver/sounds/hello2.wav");
playsound("sudo aplay /opt/ninja/drivers/tripwire_driver/sounds/deactivated2.wav");

