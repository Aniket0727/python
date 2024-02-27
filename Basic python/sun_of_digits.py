# Practical no.5
# Q.7 Write a python program takes in a number and finds the sum of digits in a number
num=int(input("Enter number: "))
add=0        
while(num>0):   
    a=num % 10   
    add=add+a    
    num=num//10  
print("Addition: ",add)