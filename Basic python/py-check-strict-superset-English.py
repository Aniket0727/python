A=set()
B=set()
e=input().split()
for i in range(len(e)):
	A.add(int(e[i]))
n=int(input())
for i in range(n):
	e=input().split()
	for i in range(len(e)):
		B.add(int(e[i]))
	#B.add(e)
	
#print(A)
print(A.issuperset(B))
#print(B)
