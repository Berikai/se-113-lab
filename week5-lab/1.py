# Define a variable called rank. This variable holds information related to a worker’s position.
# This variable can only take the values 1, 2, 3 or 4. A worker’s rank determines the annual
# increase in that worker’s salary. The information related to rank is given in the following
# 
# Value Name of position Annual increase
# 1 Software Engineer %10
# 2 Senior Engineer %15
# 3 Principal Engineer %20
# 4 Distinguished Engineer %30
# 
# Prompt the user for the rank information of a worker, store it in the variable rank. Then, prompt
# the user once again for his/her current salary, and store it in another variable called salary.
# When both values (rank and salary) are provided, on the console, print the worker’s position,
# and print what his/her salary is going to be next year.

rank = int(input("What is the worker's rank? "))
salary = float(input("What is the worker's current salary? "))

def printInfo(job, next_year_salary):
    print(f"The worker is a {job}.")
    print(f"The worker's salary is going to increase to {next_year_salary} next year.")

if rank == 1:
    printInfo("Software Engineer", salary * (110/100))
elif rank == 2:
    printInfo("Senior Engineer", salary * (115/100))
elif rank == 3:
    printInfo("Principle Engineer", salary * (120/100))
elif rank == 4:
    printInfo("Distinguished Engineer", salary * (130/100))
else:
    print("Rank did not match any of the positions.")