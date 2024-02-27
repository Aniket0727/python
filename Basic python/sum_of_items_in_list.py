# Prcatical no.6
# Q.1 Write a python program to sum all the items in a list.

add=0
num = int(input('How many numbers: '))
for n in range(num):
    ele = int(input('Enter number: '))
    add=add+ele
print("addition is :",add)