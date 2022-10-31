from pickle import FALSE, TRUE


def checkpanagram(String1):
    str="abcdefghijklmnopqrstuvwxyz"
    for x in str:
        if x not in String1.lower():
            return False
    return True
String1=input("Enter a statement : ")
if checkpanagram(String1):
    print("Yes it is a Panagram")
else:
    print("No its not a panagram")
