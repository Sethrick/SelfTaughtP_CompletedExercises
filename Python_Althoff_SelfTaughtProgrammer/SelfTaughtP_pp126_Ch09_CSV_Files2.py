
# A CSV file is a type of file that contains data values separated by commas.
# These "Comma Separated Value" files are essentially the spreadsheet version
# of text files.

# Each piece of data separated by a comma in a CSV file represents a cell in a
# spreadsheet, and every line represents a row.

# Python contains a built-in module for handling CSV files.

import csv

with open("Test_CSV.csv", "r") as f:
     r = csv.reader(f, delimiter=",")
     for row in r:
         print(",".join(row))
