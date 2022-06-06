###################### File detection - check if a file exist 

# import os

# path = "/Users/jmezalon/Downloads"

# if os.path.exists(path):   # check if the location exist 
#     print('That location exists!')
#     if os.path.isfile(path): # check if it is file 
#         print('that is a file')
#     elif os.path.isdir(path): # check if it is a folder/directory
#         print("that is a directory!")
# else:
#     print('that location does not exist')



###################### Read the content of the file

# try:
#     with open('/Users/jmezalon/Desktop/Development/blackstone_prep/READMEd.md') as file:
#         print(file.read())
# except FileNotFoundError:
#     print('That file was not found :(')



###################### Write files

# text = "\nto append to this file, you would just write a in the second argument in open"
# with open('test.md','a') as file:
#     file.write(text)


# read the created file
# with open('test.md') as file:
#     print(file.read())


###################### copying files

# copyfile() = copies content of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times

# import shutil  

# shutil.copyfile('test.md', 'copy.md') #src, dst  ### copy and copy2 has the exact same arguments

###################### move files using python 

# import os 

# source = "copy.md"
# destination = '/Users/jmezalon/Downloads/copy.md'

# try:
#     if os.path.exists(destination):
#         print('there is already a file there')
#     else:
#         os.replace(source, destination)
#         print(source+" was moved")
# except FileNotFoundError:
#     print(source+" was not found")

# this work exactly the same way if you want to move a folder

###################### delete files using python

# import os
# import shutil

# path = 'del.txt' 
# path = 'empty_folder' 
# path = 'folder'



# try:
#     # os.remove(path) # remove file, do not remove empty folder
#     # os.rmdir(path) # command for removing empty folders, will not delete folders that contains files
#     shutil.rmtree(path) # be careful with this fucntion, it will remove the directory and all containing files
# except FileNotFoundError:
#     print('this file was not found')
# except PermissionError:
#     print('you do not have permission to delete this folder')
# except OSError:
#     print('you cant delete that using that function')
# else:
#     print(path+' was deleted!')
