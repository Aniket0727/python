s1=set()
s2=set()
print("how many Roll no")
n=int(input())
print("Enter Roll no")
for i in range(n):
	e=int(input())
	s1.add(e)
print("how many Roll no")
n=int(input())
print("Enter Roll no")
for i in range(n):
	e=int(input())
	s2.add(e)
print(s1)
print(s2)
l=s1&s2
print(len(l))
#s1-s2 #1
#s1^s2 #2