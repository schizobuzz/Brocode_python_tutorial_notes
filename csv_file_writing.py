import csv

employees = [["Name", "Age", "Job"],
            ["Spongebob", 30, "Cook"],
            ["Patrick", 37, "Unemployed"],
            ["Sandy", 27, "Scientist"]]

file_path = "csv_file_writing.csv"

with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    for row in employees:
        writer.writerow(row)
    print(f"{file_path} was created succesfully.")