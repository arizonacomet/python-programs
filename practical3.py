#fibonacci series
m1=0
m2=1
noofvar=int(input("Enter the number of variables in series:"))
print("0 1",end=" ")
while(noofvar>2):
    m3=m1+m2
    print(m3,end=" ")
    m1=m2
    m2=m3
    noofvar=1
    