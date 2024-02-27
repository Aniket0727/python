# Practical no.4
# Q.6 Write A program that takes the marks of 5 subject and display the grade 

Programing_in_c=int(input("Enter Programing in C marks "))
Java=int(input("Enter Java marks "))
python=int(input("Enter Python marks "))
php=int(input("Enter php marks "))
android=int(input("Enter android marks "))

total=Programing_in_c + Java + python + php + android
percent=total/5

if(percent<=100):
    if(percent >= 85 and percent <= 100):
        print("You have A grade")
    elif(percent >= 65 and percent <= 84 ):
        print("You have B grade")
    elif(percent >= 45 and percent <=64):
        print("You have C grade")
    elif(percent >= 28 and percent <=44):
        print("You have D grade")
    else:
        print("You Fail try next time")
else:
    print("Please enter valid marks")
