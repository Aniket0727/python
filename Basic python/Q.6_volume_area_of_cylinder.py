# Practical no.3
# Q.6 Write a program to calculate surface volume and area of a cylinder

pi=22/7
height = float(input("Enter Height of cylinder:"))
radius = float(input("Enter Radius of cylinder:"))
volume = pi * radius * radius * height
area = ((2*pi*radius) * height) + ((pi*radius**2)*2)
print("Volume is: ", volume)
print("Surface Area is: ",area)