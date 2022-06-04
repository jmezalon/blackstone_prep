###################### File detection - check if a file exist 

import os

path = "/Users/jmezalon/Downloads"

if os.path.exists(path):   # check if the location exist 
    print('That location exists!')
    if os.path.isfile(path): # check if it is file 
        print('that is a file')
    elif os.path.isdir(path): # check if it is a folder/directory
        print("that is a directory!")
else:
    print('that location does not exist')