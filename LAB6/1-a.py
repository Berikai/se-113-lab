# Ask the user to enter your birth year, and then print out years, starting from your birth year
# to current year.

birth_year = int(input('Please enter your birth year: '))
current_year = 2024

for i in range(birth_year, current_year+1):
    if i == current_year:
        print(i)
    else:
        print(i, end=', ')
