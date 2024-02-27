# Experiment No.8 Program to count the frequency of words appearing in a string using a dictionary.

s = input("Enter the string :")
list=[]
list=s.split()
word_freq=[list.count(p) for p in list]
print("The frequency of words is ...")
print(dict(zip(list,word_freq)))