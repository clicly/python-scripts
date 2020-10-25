# https://pypi.org/project/schedule/
import schedule, time, glob, os, send2trash
from pathlib import Path

HOME_DIR = str(Path.home())
DELETE_EXTENSIONS = ['.txt', '.log']
NEW_LINE = '\n'

class ANSWER:
    CHANGE = 1
    STAY = 2
    EXIT = 3

def ask_user_confirmation():
    user_input = str(input())
    if user_input.lower() == 'y' or user_input.lower() == 'yes':
        return ANSWER.CHANGE
    elif user_input.lower() == 'n' or user_input.lower() == 'no':
        return ANSWER.STAY
    raise ValueError('Wrong user input')
    
def get_directory():
    print(f'Your directory is currently {HOME_DIR}. {NEW_LINE} Do you want to change it? (y/N)')
    user_dir_confirmation = ask_user_confirmation()

    if user_dir_confirmation is ANSWER.CHANGE:
        print('Insert your directory here: ')
        # could also use graphical app for choosing dir
        user_input_dir = str(input())
        if os.path.isdir(user_input_dir):
            print(f'Return path {user_input_dir}')
            return user_input_dir
        else:
            raise NotADirectoryError()
    elif user_dir_confirmation is ANSWER.STAY:
        print(f'Return path {HOME_DIR}')
        return HOME_DIR

def clean_directory(): 
    print(f"Check for new files in directory {os.getcwd()}")

    files = os.listdir()
    for file in files:
        # could also define regex pattern to choose files
        if os.path.splitext(file)[1] in DELETE_EXTENSIONS:
            # could also create directory for backups and copy content
            send2trash.send2trash(file)
            print(F'Deleted file {file}')

if __name__ == "__main__":
    directory = get_directory()
    os.chdir(directory)

    schedule.every().second.do(clean_directory)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        