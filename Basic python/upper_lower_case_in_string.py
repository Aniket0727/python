# Prcatical No. 11
# Exerise Question 
# Q.3 Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

import string
def cal(s):
    count1=0
    count2=0
    for i in s:
        if i.isupper():
            count1=count1+1
        else:
            count2=count2+1
    print("Total upeer case letters in string is: ",count1)
    print("Total lower case letters in string is: ",count2)

s=input("Enter String: ")
cal(s)