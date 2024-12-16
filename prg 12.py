n=int (input("Enter the Limit"))
s=0
for i in range (1,n+1):
    print("enter",i,end='')
    a=int (input("th number :"))
    s=s+a
avg=s/n
print ("The sum of entered numbers: ",s)
print ("The average of entered numbers: ",avg)
