#s={1,2,3,4,5,6,7,8,9}
#print(type(s))
#1 2 3 4 5 6 7 8 9
#10
'''s.pop()
s.remove(9)
s.discard(9)
s.discard(8)
s.remove(7)
s.pop()
s.discard(6)
s.remove(5)
s.pop()
s.discard(5)
print(s)'''
s=set()
n=int(input())
e=input().split()
for i in range(n):
	s.add(int(e[i]))
#print(s)
c=int(input())
for i in range(c):
	l=input().split()
	cs=l[0]
	if cs=="pop":
		s.pop()
	elif cs=="remove":
		s.remove(int(l[1]))
	else:
		s.discard(int(l[1]))

print(s)
	