# (Optional) Define pattern of file who should be deleted and standard direcory
# (Optional) Ask user if another directory should be used
# (Optional) Input fom user / could be explorer
# (Optional) Validate that input is a directory
# (Optional) Ask user for confirmation
# (Optional) Create backup folder if not already exists
# (Optional) Delete files with pattern from operating system

# https://pypi.org/project/schedule/
import schedule, time, glob, os, send2trash
from pathlib import Path

HOME_DIR = str(Path.home())
DEL_EXTENSIONS = ['.txt', '.log']

def clean_directory():    
    os.chdir(HOME_DIR)
    print(f"Check for new files in directory {os.getcwd()}")

    files = os.listdir()
    for file in files:
        if os.path.splitext(file)[1] in DEL_EXTENSIONS:
            send2trash.send2trash(file)
            print(F'Deleted file {file}')

if __name__ == "__main__":
    schedule.every(30).seconds.do(clean_directory)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        