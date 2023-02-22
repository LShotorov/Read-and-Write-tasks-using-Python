#   Task 5.
#       Using the Books.csv file, display all the data as well as the row number.


# Printing all rows from the file adding row numbers to it
with open("Books.csv", "r") as reader:
    for index, line in enumerate(reader.readlines()):
        print(index, line)