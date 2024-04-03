# Use a while loop to calculate and print the result of the following sum: 2 + 5 + 8 + … + 50

sum = 0
i = 2

while i <=50:
    sum += i
    i += 3

print(sum)