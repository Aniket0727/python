f=open('output.txt','r')
lines=f.readlines()
print(lines)
for line in lines:
    print(line,end='')
#print(f.tell())
f.close()
