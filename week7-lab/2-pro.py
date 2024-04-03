# Write a Python script that prints the following output. You must use nested loops.

for i in range(13):
    for j in range(7, abs(i-6), -1):
        print('*', end='')
    print()