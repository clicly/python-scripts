import os
import datetime
import subprocess

#####################################
# Path to save files
path = os.path.expanduser("~") + "/Downloads/"
# filename beginning
fileNameStart = "notes"
# file extension
fileExtension = ".md"
#####################################

def create_new_filename():
    date = datetime.datetime.now()
    day = format_number(date.day)
    month = format_number(date.month)
    year = date.year

    return f'{fileNameStart}_{year}_{month}_{day}{fileExtension}'

def get_file_format_template(file_name):
    return f"""# {file_name} \n 
        ## Whats your goal today? \n
        # * [ ] \n
        ## Write the main points here: \n
        # * [ ] \n"""

def format_number(number):
    if number < 10:
        return f'0{number}'
    return number

if __name__ == "__main__": 
    # Go to folder where you want to save the file
    os.chdir(path)

    # Print directory to confirm folder path
    print(os.getcwd())

    # Create file name
    fileName = create_new_filename()

    # Create new file
    if not os.path.exists(fileName):
        f = open(fileName, "w")
        f.write(get_file_format_template(fileName))
        f.close()

    # Open file in vscode/codium with 'code' command
    # subprocess.call(['open', fileName]) # on mac
    subprocess.call(['code-oss', fileName]) # on solus
