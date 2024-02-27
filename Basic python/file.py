# fname = input("Enter file name:")

# with open(fname, 'r') as f:
     # for line in f:
          # l=line.title()
          # print(l)
          

# file = open("F:\py\ok.txt",'r')

# for each in file:
#      print(each)

import os
path = input("Enter the path:")
os.chdir(path)

user_input = input("Enter the file name:")
a= user_input +".txt"

if os.path.exists(a):
     f = open(a,"r")
     c = f.read()
     print(c)
     f.close
else:
     print("file not exist")