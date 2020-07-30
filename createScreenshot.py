import os
import datetime
import subprocess

#####################################
# Path to save files
path = os.path.expanduser("~") + "/Downloads/"
# file extension
extension = ".png"
# filename beginning
fileNameStart = "screenshot"
#####################################

def createNewFileName():
    # Create new Date
    date = datetime.datetime.now()

    second = date.second
    minute = date.minute
    hour = date.hour
    day = date.day
    month = date.month
    year = date.year

    # format if <10
    if (second < 10):
        second = '0' + str(second)

    if (minute < 10):
        minute = '0' + str(minute)

    if (day < 10):
        day = '0' + str(day)

    if (month < 10):
        month = '0' + str(month)

    # Return file name
    return fileNameStart + "_" + str(year) + "_" + str(month) + "_" + str(day) + "_" + str(hour) + "_" + str(minute) + "_" + str(second) + extension

if __name__ == "__main__":
    
    txt = input("Want to select the area by yourself? (Y/y/yes): ")

    # Go to folder which should be the parent of the to creating files
    os.chdir(path)

    # Print directory to confirm folder path
    # print(os.getcwd())

    # Create file name
    fileName = createNewFileName()

    # Create bash command
    if (txt == "Y" or txt == "y" or txt == "yes"):
        # Print Advice
        print("Select area from screen...")

        bashCommand = "import " + fileName
    else:
        bashCommand = "import -window root " + fileName

    # Execute bash command
    # Thanks to https://stackoverflow.com/questions/4256107/running-bash-commands-in-python
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    # Print output
    print("Created screenshot: " + path + fileName)


