import os
import sys
import re

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

regexObject = re.compile(r'^\w+')
NEWLINE = '\n'

class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def ask_user_number_input():
    """
    Asks the user for a numerical input.
    """
    try:
        return int(input())
    except ValueError:
        print('Please use an integer value as input!')

def ask_user_string_input():
    """
    Asks the user for a string input.
    """
    try:
        return str(input())
    except ValueError:
        print('Please use a string value as input!')

def create_color_string(color_of_text, color_after_text, text):
    """
    Creates a colorful output string with color specification before and after the string.
    """
    return f'{color_of_text}{text}{color_after_text}'
    
def create_text_file():
    """
    Create new file if not already existing.
    """
    if not os.path.exists(file):
        f = open(file, "a")
        f.close()

def show_menu_options():
    """
    Shows the available options that could be executed in the console planer.
    """
    print(f'{create_color_string(Bcolors.OKBLUE, Bcolors.ENDC, "Option Menu...")}')
    print('1: Show options')
    print('2: Clear console')
    print('3: View all planned tasks')
    print('4: Create new planned task')
    print(f'5: Mark a planned tasks as {create_color_string(Bcolors.OKGREEN, Bcolors.ENDC, "DONE")}')
    print(f'6: Mark a planned tasks as {create_color_string(Bcolors.FAIL, Bcolors.ENDC, "TODO")}')
    print(f'7: Mark a planned tasks as {create_color_string(Bcolors.OKBLUE, Bcolors.ENDC, "WAIT")}')
    print('8: Delete old planned task')
    print('9: Exit application.')
    print_line()

def read_from_file():
    """
    Prints all created tasks to the console.
    """
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
            elif 'WAIT' in line:
                print(f'{i}: {create_color_string(Bcolors.OKBLUE, Bcolors.ENDC, line)}', end='')
    
    print_line()

def append_to_file():
    """
    Add a new task to the task file.
    """
    print(f'{create_color_string(Bcolors.OKBLUE, Bcolors.ENDC, "Add a new task...")}')
    value = ask_user_string_input()
    f = open(file, "a")
    if value != '':
        f.write(f'TODO | {value}{NEWLINE}')
    f.close()

    print_line()

def mark_as_done():
    """
    Option to mark a task that is successfully completed as done.
    """
    print(f'Which task to mark as {create_color_string(Bcolors.OKGREEN, Bcolors.ENDC, "DONE")}?')
    value = ask_user_number_input()

    f = open(file, "r")
    lines = f.readlines()
    f.close()

    for index, line in enumerate(lines):
        if index == value:
            lines[index] = line.replace(regexObject.search(line).group(), 'DONE')

    f = open(file, "w")
    for line in lines:
        f.write(line)
    f.close()

    print_line()

def mark_as_todo():
    """
    Option to mark a task that is not successfully completed as todo.
    """
    print(f'Which task to mark as {create_color_string(Bcolors.FAIL, Bcolors.ENDC, "TODO")}?')
    value = ask_user_number_input()

    f = open(file, "r")
    lines = f.readlines()
    f.close()

    for index, line in enumerate(lines):
        if index == value:
            lines[index] = line.replace(regexObject.search(line).group(), 'TODO')

    f = open(file, "w")
    for line in lines:
        f.write(line)
    f.close()

    print_line()

def mark_as_wait():    
    """
    Option to mark a task that is currently blocked as wait.
    """
    print(f'Which task to mark as {create_color_string(Bcolors.OKBLUE, Bcolors.ENDC, "WAIT")}?')
    value = ask_user_number_input()

    f = open(file, "r")
    lines = f.readlines()
    f.close()

    for index, line in enumerate(lines):
        if index == value:
            lines[index] = line.replace(regexObject.search(line).group(), 'WAIT')

    f = open(file, "w")
    for line in lines:
        f.write(line)
    f.close()

    print_line()

def delete_from_file():
    """
    Option to delete a created task.
    """
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

    print_line()

def print_line():
    print('--------------------------------------') 

if __name__ == "__main__":
    # create a file for saving tasks
    create_text_file()

    show_menu_options()
    while True:
        print(f'{create_color_string(Bcolors.BOLD, Bcolors.ENDC, "Enter your option")}', end=': ')
        number = ask_user_number_input()

        if number == 1: # MENU
            show_menu_options()
        elif number == 2: # CONSOLE CLEAR
            os.system('clear')
            show_menu_options()
        elif number == 3: # VIEW PLANNED TASKS
            read_from_file()
        elif number == 4: # ADD TASK
            append_to_file()
        elif number == 5: # MARK AS DONE
            mark_as_done()
        elif number == 6: # MARK AS TODO
            mark_as_todo()
        elif number == 7: # MARK AS WAIT
            mark_as_wait()
        elif number == 8: # DELETE TASK
            delete_from_file()    
        elif number == 9:
            exit()

    