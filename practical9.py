#check list for less than 5
mylist=[1,2,3,4,5,6,7,8,9,10]
def lessthan5(mylist):
    for x in mylist:
        if x <= 5:
            print(x,end="")
lessthan5()