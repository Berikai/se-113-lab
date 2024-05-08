# Calculate your age and print it to the screen exactly as shown in sample output below. You
# are supposed to perform it using the following way: Define an integer and assign its value to
# 0. From the year after your birth year to the current year, increase this value by 1 for each
# year. (Make sure that the final value will be equal to your age.)

birth_year = 2003 + 1 # year after my birthday
current_year = 2024

age = 0

for i in range(birth_year, current_year+1):
    age += 1

print(f'I was born in {birth_year} and currently it is {current_year}.')
print(f'Therefore, my age is {age}.')