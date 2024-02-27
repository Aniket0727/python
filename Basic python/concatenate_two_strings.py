#  Practical No. 13
#  Q.2	Write a Python program to concatenate two strings.
import string
s=input("Enter First String: ")
s2=input("Enter Second String: ")
print(s+s2)
print("% s % s" % (s, s2))
print("".join([s, s2]))
print("{} {}".format(s, s2))   