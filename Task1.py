# Task 1.
#       Create a .csv file to hold the information from the data. Name the file “Books.csv”

import csv

# The data to be written to the Books.csv
data = (["Book", "Author", "Year Released"],
        ["To Kill A Mockingbird", "Harper Lee", "1960"],
        ["A Brief History of Time", "Stephen Hawking", "1988"],
        ["The Great Gatsby", "F. Scott Fitzgerald", "1922"],
        ["The Man Who Mistook His Wife for a Hat", "Oliver Sacks", "1985"],
        ["Pride and Prejudice", "Jane Austen", "1813"],
)

# Creating new file and writing to it
with open('Books.csv', mode = 'w', newline = '') as f:
    writer = csv.writer(f, delimiter = ',')
    for entry in data:
        writer.writerow(entry)

# Printing the data from the file
books_csv = open('Books.csv', 'r')
print(books_csv.read())
books_csv.close()