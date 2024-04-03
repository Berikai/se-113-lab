# Write a Python script that prints the following output. You must use nested loops.

for i in range(7):
    for j in range(i):
        print('*', end='')
    print()

for i in range(7, 0, -1):
    for j in range(i):
        print('*', end='')
    print()