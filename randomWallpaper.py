import os
import glob
import subprocess
import time
from secrets import randbelow

#####################################
# Wallpaper folder
path = os.path.expanduser("~") + "/Desktop/Workspace/Wallpaper"
# Should the commands run repeatedly
runRepeatedly = True
# Seconds between command execution
secondsBetweenRuns = 10.0
#####################################

def showRandomPicture(pictureArray):
    # Create random number
    random = randbelow(pictureArray.__len__())

    # Receive random picture name path
    picturePath = os.getcwd() + "/" + pictureArray[random]

    # Create bash command
    bashCommand = "feh --bg-fill " + picturePath

    # Execute bash command
    # Thanks to https://stackoverflow.com/questions/4256107/running-bash-commands-in-python
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()


if __name__ == "__main__":
     # Go to folder which should contain all wallpaper files
    os.chdir(path)

    # Get all files from specified directory as array
    pictureArray = glob.glob("*")

    starttime = time.time()
    while runRepeatedly:
        showRandomPicture(pictureArray)
        print(time.time())
        time.sleep(secondsBetweenRuns - ((time.time() - starttime) % secondsBetweenRuns))

