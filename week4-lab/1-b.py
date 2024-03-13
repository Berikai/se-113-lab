# Write a Python script that reads the student’s name and scores in order to calculate the
# student’s grade of SE113 course. First, you need to define a variable name, and ask the user to
# enter his/her name. Then, ask the user for the scores of the following items: lab, homework,
# midterm and final. Finally, calculate and print the student’s course grade using the weights
# available in SE113 syllabus. (20% lab, 20% homework, 20% midterm and 40% final)

name = input("What is your name? ")

print(f"Hello {name}, enter your scores for SE113  items.")

lab = float(input("Lab score: "))
homework = float(input("Homework score: "))
midterm = float(input("Midterm score: "))
final = float(input("Final score: "))

total = (20*lab + 20*homework + 20*midterm + 40*final ) / 100

print(f"Your grade of SE113 course is {total}")