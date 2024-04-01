# Write a Python script to decide and print out whether an integer “n” given by the user is prime or
# not.

n = int(input("Please enter a number: "))

is_prime = True

for i in range(2, n):
    if n % i == 0:
        is_prime = False 
        break

if n < 2:
    is_prime = False

if is_prime:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")