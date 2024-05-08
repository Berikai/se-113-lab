# Define a function logarithm_function that takes two positive real values (i.e., b 
# and n) and returns the result of logb(n).   
# Hint:  Within  the  definition  of  your  function  you  can  use  the  built-in  function 
# math.log  (By  the  way,  check  the  following  reference  page  for  all  built-in 
# Mathematical functions available to use in the module math of Python3: 
# https://docs.python.org/3/library/math.html).

import math

def logarithm_function(b, n):
    return math.log(n, b)

print(logarithm_function(2, 8)) # 3