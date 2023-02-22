#   Task 3.
#       Using the Books.csv file, ask the user how many entries he wants to add,
#       and then allow him to add that many.
#       After all the data is added, ask the user to enter an author and print all the books for that author.
#       If there are no books by this author listed, display an appropriate message.

import csv



# Function to check if the input from the user is a number > 0
def is_input_int(the_input):
    if not the_input.isdigit() or int(the_input) <= 0:
        return is_input_int(input('Please add a number higher than 0: '))
    return int(the_input)


# Asking the user about the number of entries to be made
number_of_entries = is_input_int(input('How many entries do you want to make: '))

# loop getting new entries and appending them to the file
for _ in range(number_of_entries):
    user_input = input('Please add a new entry using this format:\nBook Name,Author,Year Released\n>').split(',')

    with open('Books.csv', mode = 'a', newline = '') as f:
        writer = csv.writer(f, delimiter = ',')
        writer.writerow(user_input)


# Asking the user about the Author to be looked for
user_author_search = input('Please enter the name of the author you are looking for: ').lower()

# dict to hold the results with key = Author Name / value = Book Name
author_search_results = {}
with open('Books.csv', 'r') as reader:
    for line in reader.readlines():
        line = line.split(',')
        author_name = line[1]
        book_name = line[0]
        # Checking if the user input is in the Author column.
        if user_author_search in author_name.lower():
            # If the Author Name already exist in the author_search_results, we add the Book Name to the values
            if author_name in author_search_results:
                author_search_results[author_name] += f",{book_name}"
            # If the Author Name doesn't exist in the author_search_results, we create new key=Author Name with Book Name as value
            else:
                author_search_results[author_name] = book_name

# Checking if author_search_results is empty and printing appropriate message
if not author_search_results:
    print(f"Sorry, but I can't find any books by this author: {user_author_search}")
# Printing all found results
else:
    print(f'All the books we have of {user_author_search} are:')
    for key, value in author_search_results.items():
        print(f'Author: {key}')
        print('Books: ', *value.split(','), sep = ' // ')