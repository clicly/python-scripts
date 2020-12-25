import os
from datetime import datetime
import shutil

class SortingStructure:
    YEAR = 1
    YEARANDMONTH = 2

class Colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def print_with_color(color, text):
    print(f'{color}{text}')

def get_last_modified_date(filename):
    changed_time = os.path.getmtime(filename)
    formatted_date = datetime.fromtimestamp(changed_time)
    return formatted_date

def move_file_into_directory(filename, modified_year_dir):
    try:
        shutil.move(filename, modified_year_dir)
        print_with_color(Colors.GREEN, f'Moved {filename} to {modified_year_dir}!')
    except Exception:
        print_with_color(Colors.FAIL, f'Moving {filename} will not work!') 

def count_files(dir):
    count = 0
    for folder_name, _ , file_name in os.walk(dir):
        for name in file_name:
            if (os.path.isfile(folder_name + '/' + name)):
                count +=1
    return count

#####################################
# directory where each picture is saved
FILE_DIR = os.path.expanduser("~") + "/Downloads"
# sorting
SORT = SortingStructure.YEARANDMONTH
#####################################

if __name__ == "__main__":

    os.chdir(FILE_DIR)
    print_with_color(Colors.BLUE, 'Navigated to file directory: ' + os.getcwd())

    processed_files = 0
    for file in os.listdir(os.fsencode(FILE_DIR)):
        filename = os.fsdecode(file)

        if (os.path.isfile(filename)):
            processed_files+=1

            date = get_last_modified_date(filename)
            year_str = str(date.year)
            if (not os.path.isdir(year_str)):
                os.mkdir(year_str)
                print_with_color(Colors.WARNING, f'Created directory {year_str}!')
            
            if SORT == SortingStructure.YEAR:
                move_file_into_directory(filename, year_str)
            elif SORT == SortingStructure.YEARANDMONTH:
                os.chdir(FILE_DIR + '/' + year_str)
                
                date = get_last_modified_date(FILE_DIR + '/' + filename)
                month_str = str(date.month)
                if (not os.path.isdir(month_str)):
                    os.mkdir(month_str)
                    print_with_color(Colors.WARNING, f'Created directory {month_str}/{year_str}!')

                move_file_into_directory(FILE_DIR + '/' + filename, month_str)
                os.chdir(FILE_DIR)
            else:
                raise ValueError('Unknown sorting algorithm')
        
    print_with_color(Colors.BLUE, f'Finished sorting! Processed {processed_files} files')
    print_with_color(Colors.BLUE, f'Directory has {count_files(FILE_DIR)} files.')