# Experiment No.9 Program to create a dictionary with key as first character and value as words starting with that character.

dict1={}
n=int(input("Enter Number Of elements: "))
for i in range(n):
     key=input("Enter key: ")
     dict1[key]=input("Enter Value: ")
print(dict1)
