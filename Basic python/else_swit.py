list=["Abhi","Aniket","Annu"]

ip=input("Enter Name: ")
for i in list:
    if ip==i:
        print(ip,"Present in list")
        break
    else:
        print("a")
    
    
else:
    print("Not Present")