#   Task 6.
#       Import the data from the Books.csv file into a list. Show the list to the user.
#       Ask the user to select a row from the list to be deleted and remove it from the list.
#       Ask the user what data they want to change and change it.
#       Write the data back to the original .csv file, overwriting the existing data with the changed data.

import csv


# Function to check if the input is a number.
def is_input_int(the_input):
    if not the_input.isdigit():
        return is_input_int(input('Please enter the correct number: '))
    return int(the_input)

# Function to print all the data with the changes made
def show_to_user(dictionary):
    for key, value in dictionary.items():
        print(f'ID number: {key}')
        temp = value.copy()
        # Removing the "\n" at the end of the Year Released, so the print will be more readable
        temp[2] = temp[2][:-1]
        print(temp)
        print('\n')

# dict to hold the new data- key = Row Number / value = ['Book Name', 'Author Name', 'Year Released']
all_data = {}
# holding the header of the file to add it later with the new data
header = []
with open('Books.csv', 'r') as r:
    header = r.readlines()[0].split(',')

# Adding all existing data from the file to all_data dict
with open('Books.csv', 'r') as reader:
    for index, line in enumerate(reader.readlines()[1:]):
        all_data[index] = line.split(',')

# Printing the data to the user
show_to_user(all_data)

# Asking the user which row to be deleted using the row number as ID
user_delete_id = is_input_int(input('Please select which row from the list you want to delete? Enter the ID number: '))
# Checking if the user input is valid
while user_delete_id not in all_data.keys():
    user_delete_id = is_input_int(input('Please enter the correct ID number: '))
# deleting the entry from all_data dict
else:
    del all_data[user_delete_id]

# Printing the data with the changes made
show_to_user(all_data)

# Asking the user which row to be altered using the row number as ID
user_change_id = is_input_int(input('\nPlease select which data you want to change? Enter the ID number: '))
# Checking if the user input is valid
while user_change_id not in all_data.keys():
    user_change_id = is_input_int(input('Please enter the correct ID number: '))

# Asking the user which information to be altered
user_change_data = is_input_int(input("\nPlease select which data you want to change:\n1.Book Name\n2.Author\n3.Year Released\n4.All data\n0.I don't want to change anything\n> "))
# Creating temporary list, that holds the information from the chosen row
change_data = all_data[user_change_id]


if user_change_data == 1:
    # Asking the user to input the new Book Name for the chosen row and changing it in the temporary list.
    # Then saving the changes to all_data dict
    change_data[0] = input('\nPlease enter the new name of the Book: ')
    all_data[user_change_id] = change_data
elif user_change_data == 2:
    # Asking the user to input the new Author Name for the chosen row and changing it in the temporary list.
    # Then saving the changes to all_data dict
    change_data[1] = input('\nPlease enter the new name of the Author: ')
    all_data[user_change_id] = change_data
elif user_change_data == 3:
    # Asking the user to input the new Year Released for the chosen row and changing it in the temporary list.
    # Then saving the changes to all_data dict
    change_data[2] = input('\nPlease enter the new Year Released: ')
    all_data[user_change_id] = change_data
elif user_change_data == 4:
    # Asking the user to input a whole new entry for the chosen row and changing it in the temporary list.
    # Then saving the changes to all_data dict
    user_input = input('\nPlease add a new entry using this format:\nBook Name,Author,Year Released\n>').split(',')
    change_data = user_input
    all_data[user_change_id] = change_data


# Re-writing the information in the file with the changes made.
with open('Books.csv', mode = 'w', newline = '') as f:
    writer = csv.writer(f, delimiter = ',')
    writer.writerow(header)
    for value in all_data.values():
        writer.writerow(value)

# Printing the changed data that is in the file
print('\nDone!!!')
print()
books_csv = open('Books.csv', 'r')
print(books_csv.read())
books_csv.close()