#Armsrtong and Palidrome number
import numbers


num=int(input("Enter a number: "))
def armstrong():
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp//=10
    if num== sum:
        print("the number is armstrong")
    else:
        print("the number is not armstrong")

armstrong()

def palindrome():
    temp=num
    rev=0
    while temp>0:
        digit=temp%10
        rev=rev*10+digit
        temp//=10
        if num==rev:
            print("the number is palindrome")
palindrome()