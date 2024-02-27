# Practical no.5
# Q.4 Write a python program to print Fibonacci series 
# 0 1 1 2 3 5 8 13

n=int(input("Enter number how many Fibonacci series has to be generated: "))
num1=0
num2=1 
add=0
i=1
while(i<=n):
    print(add,end=" ")
    i=i + 1
    num1 = num2
    num2 = add
    add = num1 + num2
    
# for i in range(0,n):
#     print(add,end=" ")
#     num1=num2
#     num2=add
#     add=num1 + num2
#     i=i+1

