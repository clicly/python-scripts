import os
import datetime
import subprocess

#####################################
# Path to save files
path = os.path.expanduser("~") + "/Downloads/"
# file extension
extension = ".md"
# filename beginning
fileNameStart = "notes"
#####################################

def createNewFileName():
    # Create new Date
    date = datetime.datetime.now()
    day = date.day
    month = date.month
    year = date.year

    # format day or month if <10
    if (day < 10):
        month = '0' + str(month)

    if (month < 10):
        month = '0' + str(month)

    # Return file name
    return fileNameStart + "_" + str(year) + "_" + str(month) + "_" + str(day) + extension

def getFileFormatTemplate(fileName):
    return "# " + fileName + "\n" + "## What's your goal today?" + " \n" + "* [ ]" + " \n" + "## Write the main points here:" + " \n"+ "* [ ]" + " \n"

if __name__ == "__main__":
    
    # Go to folder which should be the parent of the to creating files
    os.chdir(path)

    # Print directory to confirm folder path
    # print(os.getcwd())

    # create file name
    fileName = createNewFileName()

    # Create new file
    if not os.path.exists(fileName):
        f = open(fileName, "w")
        f.write(getFileFormatTemplate(fileName))
        f.close()

    # open file on mac
    subprocess.call(['open', fileName])
