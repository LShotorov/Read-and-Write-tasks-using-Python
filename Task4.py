#   Task 4.
#       Using the Books.csv file, ask the user to enter a start and end year.
#       Show all books published between these two years.


# Function to check if the input is two numbers (start_year and end_year)
def is_input_int(start, end):
    if not start.isdigit() or not end.isdigit():
        return is_input_int(input('Please add correct start and end year in this format- start-end: ').split('-'))
    return int(start), int(end)

# Asking the user to enter a start year and end year.
user_year_range = input('Please enter start and end year using this format- start-end: ').split('-')
# Verifying that the input is two numbers
start_year, end_year = is_input_int(user_year_range[0], user_year_range[1])

# dict to hold the results with key = Year Released / value = Book Name
year_search_results = {}
with open('Books.csv', 'r') as reader:
    for line in reader.readlines():
        line = line.split(',')
        year_released = line[2]
        book_name = line[0]
        # Creating tuple holding all numbers between start_year and end_year included.
        years_range = (year for year in range(start_year, end_year + 1))
        for year in years_range:
            # Checking if the current year in the tuple is the Year Released
            if str(year) == year_released:
                # If the year exist in the year_search_results, appending the value with the Book Name
                if year_released in year_search_results:
                    year_search_results[year_released] += f",{book_name}"
                # If the year doesn't exist in the year_search_results, creating new key = Year Released / value = Book Name
                else:
                    year_search_results[year_released] = book_name

# Checking if year_search_results is empty and printing appropriate message
if not year_search_results:
    print(f"Sorry, but I can't find any books from this period: {start_year}-{end_year}")
# Printing all found results
else:
    print(f'All the books we have from the period: {start_year}-{end_year} are:')
    for key, value in sorted(year_search_results.items()):
        print(f'Year: {key}', end = '\t')
        print('Books:', *value.split(','), sep = ' // ')