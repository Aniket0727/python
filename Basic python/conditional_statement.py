# Practical no.4
# Conditional Statenment

num1=int(input("Enter first number: "))
num2 =int(input("Enter second number: "))

# if statement
if(num1 > num2):
    print(num1,"is grater")


# if else statement
if(num1 > num2):
    print(num1,"is grater")
else:
    print(num2,"is grater")    


# nested if else
if(num1 > num2):
        if(num1 > 0):
            print(num1,"is positive number and grater than",num2)
else:
    print(num2,"is grater") 