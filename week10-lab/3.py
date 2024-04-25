# Define  an  iterative  function  that  takes  an  integer  n  as  a  parameter  and  returns  the 
# corresponding Fibonacci number 𝐹𝑛using a while loop structure. In your Python script, test 
# your function by passing an argument value.  
 
# Hint: https://en.wikipedia.org/wiki/Fibonacci_number 

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n >= 2:
        num1, num2, next = 0, 1, 2
        i = 1
        while i < n:
            next = num1 + num2
            num1, num2 = num2, next
            i += 1
        return next
    else:
        raise ValueError('Negative values are not allowed in def fibonacci(n):')

print(fibonacci(8)) # 21