f=open('abc.txt','w')
list=['Python\n','PHP\n','Java\n','C++\n']
f.writelines(list)
print('all lines from list written to file')
f.close()
