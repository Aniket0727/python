# Assignment no.3

n=int(input("Enter Total number of company share:"))
l=[]
l2=[]
for i in range(n):
    print()
    print("Enter Details",i+1,"Share")
    sn=input("Enter Share Name :")
    dp=input("Enter Data :")
    cp=float(input("Enter cost for each share :"))
    ns=int(input("Number od shares :"))
    sp=float(input("Selling price of shares:"))
    tc=cp*ns
    ts=sp*ns
    t=(sn,dp,cp,ns,sp)
    t2=(tc,ts)
    l.append(t)
    l2.append(t2)
atc,ats=zip(*l2)
cps=sum(atc)
sps=sum(ats)
per=((sps-cps)/cps)*100
print()
print("Total cost of portfolio",cps)
print("Total amount gained or lost :",sps-cps)
if(sps-cps>0):
    print("Percentage profit made :",per)
else:
    print("Percentage loss made :",per)