#   Task 2.
#       Use the created Books.csv file and have the user add a new entry after all the other lines in the file.
#       Print all lines from the file on a separate line.

import csv

# User input of the new entry. Splitting the entry by "," and making a list ['Book Name', 'Author', 'Year Released']
user_entry = input('Please add a new entry using this format:\nBook Name,Author,Year Released\n>').split(',')

# Appending the new entry to the file.
with open('Books.csv', mode = 'a', newline = '') as f:
    writer = csv.writer(f, delimiter = ',')
    writer.writerow(user_entry)

# Printing new line
print()
# Reading from the file and printing every row on a new line.
with open('Books.csv', 'r') as reader:
    for line in reader:
        print(line)