import pandas as pd
import numpy as np
dict={
    "name":["Annu","Omakar","Rahul"],
    "Roll_No":[10,20,30],
    "City":["Georai","Jalna","Jalna"]
}
a=pd.DataFrame(dict)
# a.to_csv('list.csv')
print(a.describe())
b=pd.read_csv('list.csv')
b['Roll_No'][0]=50
print(b)
print(b.head(1))
print(b.tail(1))

p=pd.DataFrame(np.random.rand(10,2),index=np.arange(10))
print(p)
p.loc[0,0]=999
p.drop(0)
p.columns=list("AB")
p.drop([0],inplace=True)
print(p.loc[(p['A']<0.5)])
print(p)
