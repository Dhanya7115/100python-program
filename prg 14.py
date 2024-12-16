a= [ ]
n=int (input ("Enter number of elements:"))
for i in range (1,n+1):
    b=int (input("enter element:"))
    a.append(b)
a.sort()
print ("second largest elements is:",a[n-2])
