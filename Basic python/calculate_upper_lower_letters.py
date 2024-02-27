# Prcatical No. 10
# Q.1	Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

s=input("Enter String: ")
up=0
lo=0
for i in s:
    if (i.isupper()):
        up=up+1
    else:
        lo=lo+1
print("Total Upper casr letters in string: ",up)
print("Total lower casr letters in string: ",lo)
