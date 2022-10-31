#4C
#cloning a list 
list=[ ]#empty list
elements=int(input("Enter the number of elements you want in your list:"))
print("enter",elements,"elements for l1")

for i in range(elements):
   print("enter element",i+1,":",end="")
   element=input()
   list.append(element)
   print("original list :",list)
   
l2=list.copy()

print ("clone list:",l2)
print("CLONE CREATED SUCCESSFULLY! ")