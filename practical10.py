#WRITE A PROGRAM THAT TAKES TWO LIST AND RETURNS IF THEY HAVE ATLEAST ONE COMMON MEMBER
list=[ ]#empty list
elements=int(input("Enter the number of elements you want in your list:"))
print("enter",elements,"elements for l1")

for i in range(elements):
   print("enter element",i+1,":",end="")
   element=input()
   list.append(element)
   
list2=[ ]#empty list
no=int(input("how many elements you wish to enter for l2:"))
print("enter",no,"elements for l2")


for i in range(no):
   print("enter element",i+1,":",end="")
   element=input()
   list2.append(element) 
   
def common_el(list1,list2):
    
    if (len(list1) < len(list2)):
         arg1=list1
         arg2=list2
    else:
         arg1=list2
    arg2=list1
      
    for x in list1 :
        if x in list2 :
            return True
    return False
    
if common_el(list,list2):
    print(" common elements identified ")
else:
    print(" no common elements identified ")