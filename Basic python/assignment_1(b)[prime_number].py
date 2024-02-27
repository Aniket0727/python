# Assignment No:- 2
# B. Write a Python program to check if a given number is prime or not.

num=int(input("Enter Number"))
flag=False
if num >1:
    for i in range(2,num):
        if (num % i)==0:
            flag =True
            break

if flag:
    print(num," = is not prime number")
else:
    print(num," = is Prime number")