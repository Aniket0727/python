# Practical no.3
# Q. Write simple python program using operators arithmatic operators, logical operaotrs, bitwise operaotrs. 

print("Operators in python");
print("***************************")
print("Arithmatic Operators");
x = 5
y = 3

print('x + y =',x+y)#addition

print('x - y =',x-y)#Subtraction

print('x * y =',x*y)#Multiplication

print('x / y =',x/y)#Float Division

print("x % y =",x%y )#Modulus

print('x // y =',x//y)#Floor Division

print('x ** y =',x**y)#Exponent

print("***************************")

print("Assignment Operators")
a = 10
b = 15
a += 2
b -= 2
a /= 3
a %= 3
a **= 3
print(a)
print(b)

print("***********************")

print("Comparison Operators")

print('a > b is',x>y)

print('a < b is',x<y)

print('a == b is',x==y)

print('a != b is',x!=y)

print('a >= b is',x>=y)

print('a <= b is',x<=y)

print("***********************")

print("Logical operators")
x = True
y = False
n =5
print('x and y is',x and y)

print('x or y is',x or y)

print(not(n > 3 and n < 10))

a=0
b=20
print(a and b)
print(a or b)
print(not a)

print("***********************")

print("Identity Operators")
x = 10
y = 20
z = x

print(x is z)#True
print(id(x))
print(id(z))
print(id(y))


print(x is y)#False

print(x == y)#False
print("***********************")

print("Bitwise Operators")

a = True      
b = False           

c = a & b    
print (c)

c = a | b;        
print (c)

c = a ^ b;       
print (c)

x=10
c = ~x;      
print (c)

c = x << 2;       
print (c)

c = x >> 2;    
print (c)

x=10           # 0 0 0 0 1 0 1 0
y=20           # 0 0 0 1 0 1 0 0
print(x & y)   # 0 0 0 0 0 0 0 0 (and operation)

x=8            # 0 0 0 0 1 0 0 0
y=5            # 0 0 0 0 0 1 0 1
print(x | y)   # 0 0 0 0 1 1 0 1

xx=30
yy=50

print(xx+yy)



print("***********************")

print("Membership Operator")
x = 'Hello world'
y = {1:'a',2:'b'}

print('H' in x)

print('hello' in x)

print(1 in y)

print('a' in y)

print("***********************")

print("Ternary Operator")
a = 10
b = 20
  
print("a is grater than b") if a > b else print("b is grater than a")

print("***********************************************")

print("Aniket",end=" ")
print("Shubhangi")

a=1
if(a):
    print("a")

  