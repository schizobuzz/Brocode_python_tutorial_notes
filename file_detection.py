import os

file_path = "fileWriting.txt" 

if os.path.exists(file_path): # Detection if it exists
    print(f"{file_path} exists!")

    if os.path.isfile(file_path): # Detection if it is a file.
        print(f"{file_path} is a file.")
    elif os.path.isdir(file_path): # Detection if it is a directory.
        print(f"{file_path} is a directory.")
else:
    print(f"{file_path} does not exist.")