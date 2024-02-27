# Practical no.5
# nested loop
i=5
j=1
while(i<=10):
    while(j<=10):
        if(j<=10):
            print(i,"*",j,"=",i*j)
            j=j+1

print()
sub=['Java','PHP','Android','Python','JavaScript'];
for a in sub:
    for j in a:
        print(j,end="")
    print()