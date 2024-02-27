# Experiment No.6  Program to check if a substring is present in a given string.

str="python is very very simple language"
print("Given String: ",str)
words = str.split()

s=input("Enter substring: ")
for i in words:
     if (i==s):
          print("Substring is present in given string")