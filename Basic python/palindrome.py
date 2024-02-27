# Prcatical no.5
# Q.8 Write a python program that takes a number and checks whether it is a palindrome or not

num=int(input("Enter number: "))
a=num
rev=0
rem=0
while(num>0):           
    rem=num %10         
    rev=(rev*10) + rem  
    num=num//10         
  
if(a==rev):
    print(a,"is palindrome number")
else:
    print(a,"is not palindrome number")