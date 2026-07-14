import json

employee = {
    "name": "Spongebob",
    "age": 30,
    "job": "cook"
}

file_path = "json_file_writing.json"

with open(file_path, "w") as file:
    json.dump(employee, file, indent=4)
    print(f"{file_path} was created succesfully.")