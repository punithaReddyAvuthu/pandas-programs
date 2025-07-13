import csv
with open("C:\\Users\\punit\\OneDrive\\Documents\\sample-csv-files-sample-5.csv") as files:
    data = csv.reader(files)
    for row in data:
        print(row)