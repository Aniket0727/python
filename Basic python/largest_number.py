# Practical no.4
# Q.3 Write a program to check the largest number among the three numbers

num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
num3=int(input("Enter Third number "))

print(num1," is grater") if num1 > num2 and num1 > num3 else print(num2,"is grater") if num2 > num3 else print(num3,"is grater")


