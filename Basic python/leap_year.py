# Practical no.4
# Q.4 Write a program to check if the input year is a leap year or not

year = int(input("Enter a year"))

if (year % 4 == 0 or year % 400 == 0):
    print(year,"is a leap year")
else:
   print(year,"is not a leap year")
