# Assignment no:-1
# a. Write a Python program to find largest number among three using short hand if...else.

a=int(input("Enter First Number"))
b=int(input("Enter Second Number"))
c=int(input("Enter Third Number"))

print(a," is grater") if a > b and a > c else print(b," is grater") if b > c else print(c,"is grater")
