import pandas as pd
s1=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
s1=pd.Series([1,2,3,4,5])
print(type(s1))
print(s1)

s2=pd.Series([1,2,3,4,5],index=['a','b','c','d'])
print(s2)

s3=pd.Series({'one':1,'two':2,'three':3})
print(s3[:2])

s4=pd.Series([1,2,3,4,5])
s5=pd.Series([6,7,8,9,1])
print(s4 + s5)

d1=pd.DataFrame({'Name ':['Aniket','Omkar','Yash'],'Roll No':[1,2,3]})
print(d1)
d1=d1.drop(1)
print()
print(d1)
