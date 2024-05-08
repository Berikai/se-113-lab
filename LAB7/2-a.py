# Define a function sine_function that takes a real number d as a parameter (that is 
# an angle value in degrees) and returns sine of d.   
# Hint:  Within  the  definition  of  your  function,  you  can  call  the  built-in  function 
# math.sin,  however  this  function  takes  the  angle  in  radians,  not  degrees.  So, 
# you may consider converting d from degrees to radians. (pi =3.14)

import math

pi = math.pi # 3.14

def sine_function(d):
    return math.sin(d * (pi/180))

print(sine_function(0))
print(sine_function(30))
print(sine_function(90))