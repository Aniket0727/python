# Prcatical no.6
# Q.2 Write a Python program to multiplies all the items in a list.

mul=1
num = int(input('How many numbers you have to enter: '))
for n in range(num):
    ele = int(input('Enter number: '))
    mul=mul*ele
print("Multiplication is :",mul)