a=10
b=10
print("id(a)==id(b) :",a is b)#T
print("a is not b :",a is not b)#F

b=20

print("a is b :",a is b)#F
print("a is not b :",a is not b)#T

l=[1,2.3,3+2j,'hello']
l1=l
l1[1]=100
print(l)#[1,100

print("l is l1 :",l is l1)#T
print("l is not l1 :",l is not l1)#F

l1=l[:]
l1[1]=200

print(l)
print(l1)

print("l is l1 :",l is l1)#F
print("l is not l1 :",l is not l1)#T
