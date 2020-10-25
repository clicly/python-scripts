import os

#####################################
# path to file to modify
path = os.path.expanduser("~") + "/Desktop/Workspace/scripts_python/test.txt"
#####################################

def execute_action(lines):
    for element in lines:
        print ("Test" + element)

if __name__ == "__main__":
    # Open the file with read only permit
    f = open(path, "r")
    
    # get list containing all lines in the file
    lines = f.readlines()
    
    # do something with lines
    execute_action(lines)

    # close the file after reading the lines.
    f.close()
