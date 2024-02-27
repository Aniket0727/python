# Practical No.5
# pattern - c

# 1010101
#  10101
#   101
#    1

# rows=int(input("Enter rows"))
rows=4
k=1
for i in range(rows):
    n=k
    k+=2
m=1
for i in range(0,rows):
    for j in range(i):
        print(' ',end=' ')
    for k in range(n):
        if m==1:
            print('1',end='')
            m=0
        else:
            print('0',end='')
            m=1
    print()
    m=1
    n-=2
    