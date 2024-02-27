class student:
    pass
s1=student()
s2=student()
s3=student()
s1.rollno=101
s2.rollno=105
s3.rollno=102
s1.age=23
s2.age=33
s3.age=45
print(s1.rollno)
print(s1.age)
s1.rollno=110
s1.age=10
print(s1.rollno)#110
print(s1.age)#10
print(s3.age)#45
