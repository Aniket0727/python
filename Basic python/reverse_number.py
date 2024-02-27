# Prcatical no.5
# Q.6 Write a python program to Reverse given number

num=int(input("Enter number: "))
rev=0
rem=0
while(num>0):           
    rem=num %10         
    rev=(rev*10) + rem  
    num=num//10         
  
print("Reverse number:",rev)