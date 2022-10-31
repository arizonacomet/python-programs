#printing a specified list after removing the 0th,2nd,4th and 5th elements
list=[ ]#empty list
elements=int(input("Enter the number of elements you want in your in your list:"))
print("enter",elements,"elements for list")


for i in range(elements):
   print("enter element",i+1,":",end="")
   element=input()
   list.append(element) 
   print("List before removing the elements")
   print(list)
list.pop(5)
list.pop(4)
list.pop(2)
list.pop(0)
print("List after removing the elements : ")
print(list)
   