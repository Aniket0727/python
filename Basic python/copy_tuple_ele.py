# Practical No.7
# Q.2 Write syntax to copy specific elements existing tuple into new tuple 

t1=(1,3,5,6,8,10,13,18)
t2=()
for i in t1:
    if(i%2==0):
        t2=list(t2)
        t2.append(i);
t2=tuple(t2)
print("Even items in tuple",t2)