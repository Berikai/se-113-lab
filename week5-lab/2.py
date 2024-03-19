# Suppose that a worker is promoted every 5 years. Implement the following addition to your
# program:
# After prompting the user for rank, also request the number of years for which the worker
# has stayed in that position (this has to be less than 5). Then, print the number of years in
# which the worker will be promoted.

rank = int(input("What is the worker's rank? "))
years = int(input("For how many years has the worker been in that rank? "))
salary = float(input("What is the worker's current salary? "))

def printInfo(job, years, next_year_salary):
    print(f"The worker is a {job}.")
    print(f"The worker is going to be promoted in {5 - years} years’ time.")
    print(f"The worker's salary is going to increase to {next_year_salary} next year.")

if years < 5:
    if rank == 1:
        printInfo("Software Engineer", years, salary * (110/100))
    elif rank == 2:
        printInfo("Senior Engineer", years, salary * (115/100))
    elif rank == 3:
        printInfo("Principle Engineer", years, salary * (120/100))
    elif rank == 4:
        printInfo("Distinguished Engineer", years, salary * (130/100))
    else:
        print("Rank input did not match any of the positions.")
else:
    print("Year input has to be less than 5.")