import os
import sys

#####################################
# Path to save files
path = os.path.expanduser("~") + "/Downloads/"
# filename beginning
fileNameStart = "planer"
# file extension
fileExtension = ".txt"
# file
file = f'{path}{fileNameStart}{fileExtension}'
#####################################

# ------------------------------------------------
# Characters

NEWLINE = '\n'

# ------------------------------------------------
# Helper classes

class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# ------------------------------------------------
# Helper functions

def ask_user_number_input():
    try:
        return int(input())
    except ValueError:
        print('Please use an integer value as input!')

def ask_user_string_input():
    try:
        return str(input())
    except ValueError:
        print('Please use a string value as input!')

def create_color_string(color_of_text, color_after_text, text):
    return f'{color_of_text}{text}{color_after_text}'
    
def create_text_file():
    # Create new file if not already existing
    if not os.path.exists(file):
        f = open(file, "a")
        f.close()

# ------------------------------------------------
# Options

def show_menu_options():
    print(f'{create_color_string(Bcolors.OKBLUE, Bcolors.ENDC, "Option Menu...")}')
    print('1: Show options')
    print('2: Clear console')
    print('3: View all planned tasks')
    print('4: Create new planned task')
    print(f'5: Mark a planned tasks as {create_color_string(Bcolors.OKGREEN, Bcolors.ENDC, "DONE")}')
    print(f'6: Mark a planned tasks as {create_color_string(Bcolors.FAIL, Bcolors.ENDC, "TODO")}')
    print('7: Delete old planned task')
    print('8: Exit application.')
    print('--------------------------------------')

def read_from_file():
    print(f'{create_color_string(Bcolors.OKBLUE, Bcolors.ENDC, "View tasks...")}')
    f = open(file, "r")
    lines = f.readlines()
    f.close()
    if len(lines) == 0:
        print('No planned tasks found')
    else:
        for i, line in enumerate(lines) :
            if 'TODO' in line:
                print(f'{i}: {create_color_string(Bcolors.FAIL, Bcolors.ENDC, line)}', end='')
            elif 'DONE' in line:
                print(f'{i}: {create_color_string(Bcolors.OKGREEN, Bcolors.ENDC, line)}', end='')
    print('--------------------------------------')

def append_to_file():
    print(f'{create_color_string(Bcolors.OKBLUE, Bcolors.ENDC, "Add a new task...")}')
    value = ask_user_string_input()
    f = open(file, "a")
    if value != '':
        f.write(f'TODO | {value}{NEWLINE}')
    f.close()
    print('--------------------------------------')

def mark_as_done():
    print(f'Which task to mark as {create_color_string(Bcolors.OKGREEN, Bcolors.ENDC, "DONE")}?')
    value = ask_user_number_input()

    f = open(file, "r")
    lines = f.readlines()
    f.close()

    for index, line in enumerate(lines):
        if index == value:
            lines[index] = line.replace('TODO', 'DONE')

    f = open(file, "w")
    for line in lines:
        f.write(line)
    f.close()

    print('--------------------------------------')

def mark_as_todo():
    print(f'Which task to mark as {create_color_string(Bcolors.OKGREEN, Bcolors.ENDC, "DONE")}?')
    value = ask_user_number_input()

    f = open(file, "r")
    lines = f.readlines()
    f.close()

    for index, line in enumerate(lines):
        if index == value:
            lines[index] = line.replace('DONE', 'TODO')

    f = open(file, "w")
    for line in lines:
        f.write(line)
    f.close()

    print('--------------------------------------')

def delete_from_file():
    print(f'{create_color_string(Bcolors.OKBLUE, Bcolors.ENDC, "Delete a task...")}')

    value = ask_user_number_input()

    f = open(file, "r")
    lines = f.readlines()
    f.close()

    lines.remove(lines[value])

    f = open(file, "w")
    for line in lines:
        f.write(line)
    f.close()

    print('--------------------------------------')
    
# ------------------------------------------------
# App    

if __name__ == "__main__":
    # create a file for saving tasks
    create_text_file()

    # app iteration
    show_menu_options()
    while True:
        print(f'{create_color_string(Bcolors.BOLD, Bcolors.ENDC, "Enter your option")}', end=': ')
        number = ask_user_number_input()

        if number == 1: # MENU
            show_menu_options()
        elif number == 2: # CONSOLE CLEAR
            os.system('clear')
            show_menu_options()
        elif number == 3: # VIEW PLANNED TAKS
            read_from_file()
        elif number == 4: # ADD TASK
            append_to_file()
        elif number == 5: # MARK AS DONE
            mark_as_done()
        elif number == 6: # MARK AS TODO
            mark_as_todo()
        elif number == 7: # DELETE TASK
            delete_from_file()    
        elif number == 8:
            exit()

    