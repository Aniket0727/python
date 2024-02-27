# Practical No. 16 
# Title Program: User define Exception

class Error(Exception):
    pass
class valid(Error):
    pass
class invalid(Error):
    pass

while True:
    try:
        i = int(input("Enter Number between 1 to 3 :"))
        if  i==1:
            raise valid
        elif i==2:
            raise valid
        elif i==3:
            raise valid
        else:
            raise invalid
    except valid:
        print("Number is correct between 1 to 3")
        print()
    except invalid:
        print("Enter Valid Number between 1 to 3")
        print()