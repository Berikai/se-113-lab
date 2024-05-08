# Write a Python script which takes a real number x as input, and displays another real number y
# based on the following equation:

# You can find the equation in LAB4.pdf

# You can (approximately) confirm your results by examining the graph below:

x = float(input("x: "))

def y(x):
    if x <= -1:
        return x**3
    elif -1 < x < 0:
        return 1/x
    elif x == 0:
        return 0
    elif 0 < x < 1:
        return 1/x
    elif x >= 1:
        return x**3
    
print(f"y: {y(x)}")
    