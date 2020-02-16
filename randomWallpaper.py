import os
import glob
import subprocess
from secrets import randbelow

#####################################
# Wallpaper folder
path = os.path.expanduser("~") + "/Desktop/Workspace/Wallpaper"
#####################################

if __name__ == "__main__":
    # Go to folder which should contain all wallpaper files
    os.chdir(path)

    # Get all files from specified directory as array
    pictureArray = glob.glob("*")

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

