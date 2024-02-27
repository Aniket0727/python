# Practical No.5
# pattern - b

#     *
#    ***
#   *****
#    ***
#     *

# rows=int(input("Enter rows"))
rows=3
n=1
for i in range(rows):
    for j in range(rows-i-1,0,-1):
        print(' ',end='')
    for k in range(n):
        print('*',end='')
    print()
    n=n+2
m=1
l=n-4
for i in range(rows-1):
    for j in range(m):
        print(' ',end='')
    m+=1
    for k in range(l):
        print('*',end='')
    l-=2
    print() 
