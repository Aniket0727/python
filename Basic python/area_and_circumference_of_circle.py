# Practical No. 12
# Exerice Question
# Q.2	Write a Python program that will calculate area and 
#     circumference of circle using inbuilt Math Module

import math
PI = 3.14
r = float(input('Enter the radius of a circle: '))
area = PI * r * r
circumference = 2 * PI * r
print(" Area Of a Circle = " ,area)
print(" Circumference Of a Circle = " ,circumference)