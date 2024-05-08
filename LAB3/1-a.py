# Write a Python script that inputs a student’s name, ID and two exam scores. The script
# will print out the name, ID, and average of scores.

name = input("Enter your name: ")
id = input("Enter your ID: ")

exam1 = float(input("Enter first exam: "))
exam2 = float(input("Enter second exam: "))

exam_average = (exam1 + exam2) / 2

print(f"Hello {name}, your ID is {id}. Your exam average is {exam_average}")