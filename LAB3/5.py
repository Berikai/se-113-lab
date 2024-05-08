# Write a script that reads a radius value and a height from the user and computes the lateral
# surface area of a cylinder with the radius and height values given. (Consider that pi is 22/7)
# Hint: https://en.wikipedia.org/wiki/Lateral_surface

pi = 22/7

radius = float(input("Enter radius value: "))
height = float(input("Enter height value: "))

lateral_surface_area = 2*pi*radius*height

print(f"Lateral surface area of the cylinder is {lateral_surface_area}")