# Ask the user to enter numbers until a negative number is entered. Then, print the count of
# the prime numbers given by the user.

prime_counter = 0

def isPrime(number):
    is_prime = True

    if number < 2:
        return False
    
    for i in range(2, number):
        if number % i == 0:
            return False
        
    return is_prime

while True:
    number = int(input('Enter a number: '))

    if number < 0:
        break

    if isPrime(number):
        prime_counter += 1

print('\nCount of the prime numbers:', prime_counter)