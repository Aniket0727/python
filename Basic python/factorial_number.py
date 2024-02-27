# Practical no.5
# Q.5 Write a python program to calculate factorial of a number

# Ex. number is 5
# 5* 4*3*2*1
# 120

num=int(input("Enter number: "))

factorial=1

while(num > 0):
    factorial= factorial * (num)
    num-=1           
print("The factorial of",num,"is",factorial)


# for i in range(1,num + 1):
#     factorial = factorial*i
# print("The factorial of",num,"is",factorial)
