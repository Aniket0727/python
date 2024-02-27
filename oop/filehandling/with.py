with open('abc.txt','w+') as f:
    f.write("Javascript\n")
    f.write("VB.Net\n")
    print(f.read())
    print("Is file closed: ",f.closed)
   
 print("Is file close: ",f.closed)
