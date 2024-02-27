x=10
try:
    print(x)#exception
    print(10/0)#will not be exceuted
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
print("Hello")


