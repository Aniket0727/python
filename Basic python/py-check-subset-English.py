t=int(input())
list=[]
#print(type(list))
for i in range(t):
	A=set()
	B=set()
	n=int(input())
	v=input().split()
	for i in range(len(v)):
		A.add(v[i])
	n=int(input())
	v=input().split()
	for i in range(len(v)):
		B.add(v[i])
	tf=A.issubset(B)
	#print(A.issubset(B))
	#print(tf)
	list.append(tf)

for i in range(len(list)):
	print(list[i])
