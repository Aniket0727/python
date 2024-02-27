# Prcatical No. 11
# Exerise Question 
# Q.1	Write a Python function that takes a number as a parameter and check the number is prime or not.
temp=0
def check(num):
    for i in range(2, num):
        if (num % i) == 0:
            temp=1
            return(temp)
            
num=input("Enter Number: ")
num=int(num)
temp=check(num)
if(temp==1):
    print(num," is not prime number")
else:
    print(num," is prime number")