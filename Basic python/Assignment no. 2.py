print("Enter How many commands you have entere: ")
n=int(input())
list = []
new_list = []
for i in range(n):
    l=input().split()
    if l[0] =='print':
        new_list.append(list[:])
    elif l[0]=='remove':
        l[1]=int(l[1])	
        list.remove(l[1])
    elif l[0] =='append':
        l[1]=int(l[1])
        list.append(l[1])
    elif l[0] == 'sort':
        list.sort();
    elif l[0]=='reverse':
        list.reverse()
    elif l[0]=='pop':
        list.pop()
    elif l[0]=='insert':
        l[1]=int(l[1])
        l[2]=int(l[2])
        list.insert(l[1],l[2])

for i in range(0,len(new_list)):
	print(new_list[i])