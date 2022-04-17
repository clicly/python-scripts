import os
import shutil
from enum import Enum
from datetime import datetime

# Path where the folder structure should be saved
STRUCTURE_LOCATION_PATH = ''
# Path where the files are currently stored
FILES_PATH = ''
# Prevent moving files without knowing how the script works
CHECK_CHANGES = True

class SupportedExtensions(Enum):
    JPEG = '.jpeg'
    JPG = '.jpg'
    PNG = '.png'
    MV4 = '.mv4'
    MP4 = '.mp4'

class Colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[0m'

def has_supported_file_extension(absolute_file_path):
    """
    Return boolean if the given file is supported or not

    Checks if the given file has the same extension as one of
    the supported extensions.
    """
    extension = os.path.splitext(absolute_file_path)[1]
    
    for supported_extension in SupportedExtensions:
        if (extension == supported_extension.value):
            return True
    return False

def retrieve_supported_files(files_path):
    """
    Return array with absolute paths of files

    The files that should be moved into folder structure.
    """
    supported_files = []
    
    files = os.listdir(os.fsencode(files_path))
    for file in files:
        absolute_file_path = files_path + os.fsdecode(file)
        if (os.path.isfile(absolute_file_path) and has_supported_file_extension(absolute_file_path)):
            supported_files.append(absolute_file_path)
    
    return supported_files

def create_file_moves(supported_files):
    """
    Returns an array of move tuples

    Each tuple contains the absolute file path and the target directory.
    """
    file_moves = []

    modified_years = retrieve_modified_years(supported_files)
    for year in modified_years:
        year_path = STRUCTURE_LOCATION_PATH + str(year)
        create_folder_if_necessary(year_path)
        files_for_year = have_modified_year(supported_files, year)

        modified_months = retrieve_modified_months(files_for_year)
        for month in modified_months:
            year_month_path = year_path + '/' + str(month)
            create_folder_if_necessary(year_month_path)
            files_for_year_and_month = have_modified_month(files_for_year, month)
            
            for file in files_for_year_and_month:
               file_moves.append((file, year_month_path))

    return file_moves

def retrieve_modified_years(files):
    """
    Return array of years

    The distinct list of modified years of the files.
    """
    years = []
        
    for file in files:
        year = retrieve_modified_year(file)
        if (year not in years):
            years.append(year)

    return years

def retrieve_modified_months(files):
    """
    Return array of months

    The distinct list of modified months of the files.
    """
    months = []
        
    for file in files:
        month = retrieve_modified_month(file)
        if (month not in months):
            months.append(month)

    return months

def have_modified_year(files, year):
    """
    Return array with absolute paths of files

    The files that do have same same modified year as the given one.
    """
    files_for_year = []
    
    for file in files:
        if (retrieve_modified_year(file) == year):
            files_for_year.append(file)

    return files_for_year

def have_modified_month(files, month):
    """
    Return array with absolute paths of files

    The files that do have same same modified month as the given one.
    """
    files_for_month = []
    
    for file in files:
        if (retrieve_modified_month(file) == month):
            files_for_month.append(file)

    return files_for_month

def retrieve_modified_year(file):
    """
    Get the modified year of the file.
    """
    return datetime.fromtimestamp(os.path.getmtime(file)).year

def retrieve_modified_month(file):
    """
    Get the modified month of the file.
    """
    return datetime.fromtimestamp(os.path.getmtime(file)).month

def create_folder_if_necessary(path):
    """
    Creates a new folder with the given path if it not already exists.
    """
    if (not os.path.isdir(path)):
        os.mkdir(path)

def count_files(directory):
    """
    Returns the number of files within the given directory.
    """
    count = 0

    for folder_name, _ , file_name in os.walk(directory):
        for name in file_name:
            if (os.path.isfile(folder_name + '/' + name)):
                count +=1

    return count

def move(file, directory):
    """
    Moves the given file to the given directory.
    """
    try:
        if (not CHECK_CHANGES):
            shutil.move(file, directory)
        print_colorful(Colors.GREEN, f'Success | {file} ➔ {directory}')
    except Exception:
        print_colorful(Colors.RED, f'Error | {file} ➔ {directory}') 

def print_move_statistics(file_count_before_moves, file_count_after_moves, move_size):
    print_colorful(Colors.YELLOW, f'Previous file count: {file_count_before_moves}')
    print_colorful(Colors.YELLOW, f'Moves: {move_size}')
    print_colorful(Colors.YELLOW, f'New file count: {file_count_after_moves}')
    print_colorful(Colors.YELLOW, f'Files remaining: {count_files(FILES_PATH)}')

def print_colorful(color, text):
    """
    Prints out the given text in the given color on the console.
    """
    print(f'{color}{text}')

if __name__ == "__main__":
    supported_files = retrieve_supported_files(FILES_PATH)
    file_moves = create_file_moves(supported_files)

    file_count_before_moves = count_files(STRUCTURE_LOCATION_PATH)

    for file_move in file_moves:
        absolute_file_path = file_move[0]
        target_directory = file_move[1]
        move(absolute_file_path, target_directory)

    file_count_after_moves = count_files(STRUCTURE_LOCATION_PATH)
    print_move_statistics(file_count_before_moves, file_count_after_moves, len(file_moves))
   