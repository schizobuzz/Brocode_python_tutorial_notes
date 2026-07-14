import json
import csv

file_path = "file_writing.txt"

try:
    with open(file_path, "r") as file: # r is for reading
        content = file.read() # for .txt
        # content = json.load(file) # for .json # You can also use index searching []
        # content = csv.reader(file) # \n for line in content: print(line[row])
        print(content)
except FileNotFoundError:
    print(f"{file_path} was not found.")