"""1st practical:
Write the program for the following:
a.	Input user name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old."""
print("^^^^program to calculate when you will turn 100 year^^^^\n")
age = int(input("enter your birth year: "))
while age < 0:
    print("you have entered negative value")
    age = int(input("enter your age again: "))
else:
    year = age + 100
    print(f"you will turn hundred in {year} years!")


"""b.	Enter the number from the user and depending on whether the number is even or odd, print out an appropriate message to the user."""
print("^^^^Program to check if entered number is even or odd^^^^\n")
num = int(input("enter a number"))
if (num % 2 == 0):
    print("even number has been entered by you")
else:
    print("odd number has been entered by you")

 



"""c.	Write a program to generate the Fibonacci series."""
print("^^^^Program for fibonacci series^^^^")
t1 = 0
t2 = 1
terms = int(input("enter number of terms you want in fibonacci series"))
while terms < 0:
    print("entered terms are negative")
    terms = int(input("enter number of terms you want in fibonacci series"))

else:
    print(t1, " ", t2, end="  ")
    while (terms >= 2):
        t3 = t2 + t1
        print(t3, end="  ")
        t1 = t2
        t2 = t3
        terms -= 1

 

"""d. Write a function that reverses the user defined value."""
print("^^^^Program to reverse a string^^^^")
str1 = input("enter a string:  ")
rev = str1[::-1]
print("reverse = ", rev)

 


"""e. Write a function to check the input value is Armstrong and also write the function for Palindrome."""
print("^^^^Program to check whether armstrong and palindrome or not^^^^")
num = int(input("Enter a number to check whether is armstrong or not: "))
a = num
sum1 = 0
while (num != 0):
    rem = num % 10
    sum1 = sum1 + (rem * rem * rem)
    num = num // 10
if (sum1 == a):
    print("Number is armstrong")
else:
    print("Number is not armstromg")


def palind(str1):
    rev = str1[::-1]
    if (str1 == rev):
        print("It is palindrome")
    else:
        print("Not palindrome")


num = input("Enter a number to check its palindrome")
palind(num)

 
 


"""f. Write a recursive function to print the factorial for a given number."""
def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = int(input('enter a number'))

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))
 



"""a.	Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise."""
#2a
print("^^^^program to check whether entered character is vowel or not^^^^")

def vowel(char):
    if(char == 'a' or char=='e' or char== 'i' or char == 'o' or char=='u' or char== 'A'  or char=='E' or char== 'I' or char == 'O' or char =='U' ):
        return True
    else:
        return False


char = '0'
while not char.isalpha():
    char = input("enter a character: ")
if vowel(char):
     print(f"{char} is a vowel")
else:
     print(f"{char} is a consonant")



 
 



"""b.	Define a function that computes the length of a given list or string."""
# 2b
print("^^^^program to see the length of list^^^^")
def len_list(list1):
    print("list is", list1)
    return len(list1)


def len_str(str1):
    print("string is", str1)
    print("length of string", str1, "is:", len(str1))


list1 = [1, 4, 8, 'abc', 'xyz']
print("Length of list \'", list1, "\' is: ", len_list(list1))

print("\n^^^^program to see the length of string^^^^")
str1 = input("Enter a string: ")
len_str(str1)

 


"""c. Define a procedurehistogram() that takes a list of integers and prints a histogram to the screen."""
from matplotlib import pyplot as plt

import numpy as np
# Creating dataset
a = np.array([22, 87, 5, 43, 56,73, 55, 54, 11,20, 51, 5, 79, 31,27])

# Creating histogram
fig, ax = plt.subplots(figsize = (7, 10))
ax.hist(a, bins = [0, 25, 50, 75, 108])
#Show plot
plt.show()
 

"""A pangram is a sentence that contains all the letters of the English alphabet atleast once."""
print("^^^^Program to check whether entered string is panagram^^^^")
def panagram(str1):
    str = "abcdefghijklmnopqrstuvwxyz"
    for x in str:
        if x not in str1:
            return False
    else:
        return True

str1 = input("enter a sentence: ")

if panagram(str1.lower()):
    print(f"\'{str1}\' is panagram")
else:
    print(f"\'{str1}\' is not panagram")


 

 


"""Take a list, and write a program that prints out all the elements of the list that are less than 5"""
print("^^^^Program to check numbers lesser than 5^^^^")
def less_than5(list1):
    for x in list1:
        if x <= 5:
            print(x, end="\t")


list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
less_than5(list1)

 
""" Write a program that takes two lists and returns True if they have at least one common member."""
print("^^^^Program to remove specific index elements from list: ^^^^")
l = []
print("Enter 10 elements in list ")
for i in range(10):
    print("Enter Elements", i+1,": ",end="")
    element = input()
    l.append(element)
print("The List before removing elements", l)
l.pop(5)
l.pop(4)
l.pop(2)
l.pop(0)
print("The list after removing elements", l)

 

"""Write a Python program to print a specified list after removing the 0th , 2nd, 4th and 5th elements."""
print("^^^^Program to remove specific index elements from list: ^^^^")

def chkCommon(l1, l2):
    l3 = []
    if (len(l1) < len(l2)):
        arg1 = l1
        arg2 = l2
    else:
        arg1 = l2
        arg2 = l1

    for x in arg1:
        if x in arg2:
            l3.append(x)
    return l3


l1 = []
l2, l3 = [], []

num1 = int(input("How many elements you wish to enter for List 1: "))
print("Enter",num1,"elements for List 1")
for i in range(num1):
    print("Enter Elements", i+1,": ",end="")
    element = input()
    l1.append(element)

num2 = int(input("How many elements you wish to enter for List 2: "))
print("Enter",num2,"elements for List 2")
for j in range(num2):
    print("Enter Values", j+1,": ",end="")
    values = input()
    l2.append(values)

print("First List Elements are:",l1)
print("Second List Elements are:",l2)


l3 = chkCommon(l1, l2)
if l3!=[]:
    print("We have Common Values in List those are: ", l3)
else:
    print("We dont have Common values")


 


 



"""Write a Python program to clone or copy a list"""
print("^^^^Program to copy a list: ^^^^")
l1 = []
m = []
range1 = int(input("How many elements you wish to enter for List 1: "))
print("Enter", range1, "elements for List 1")
for i in range(range1):
    print("Enter Elements", i+1,": ",end="")
    element = input()
    l1.append(element)

print("First List Elements are: ", l1)
l2 = l1.copy()
print("Copying List using copy() elements are: ", l2)
l2.append(80)
print("after editing l2: ", l2, "and ", l1)

l3 = list(l1)
print("Copying List using list() elements are: ", l2)
l3.append(8)
print("after editing l3 ", l3, "and l1 are", l1)



 


"""Write a Python script to sort (ascending and descending) a dictionary by value."""
#5a
# #sort dictionary by value
print("^^^^Program to sort a dictionary: ^^^^")

dict1 = dict()
num = int(input("Enter number of keys you want in dictionary: "))
for x in range(num):
    pair = input(f"Enter name and marks for {x+1} seperated by \"_\" ")
    tempInput = pair.split('_')
    dict1[tempInput[0]] = int(tempInput[1])
# for  x in range(num):
#     key1 = input("Enter key for ",(x+1), ": ")
#     value1 = int(input("Enter value for ",(x+1)), ": ")
#     dict1[key1] = value1
print("Original dictionary:", dict1)
print("Ascending  order for value:", sorted(dict1.values()))
print("Descending order for value:", sorted(dict1.values(), reverse=True))
print("Ascending  order for keys:", sorted(dict1.keys()))
print("Descending order for keys:", sorted(dict1.keys(), reverse=True))


 


"""Write a Python script to concatenate following dictionaries to create a new one."""
#5b
#conat
print("^^^^Program to concat two dictionary: ^^^^")

dict3 = dict()
def concatenation(dict1, dict2):
    ans=input("enter d1 if you want to have values of 1st dictionary first or enter d2 if you want to have values of 1st dictionary first: ")
    if(ans.lower()=="d1"):
        dict3 = dict1.copy()
        dict3.update(dict2)
    elif ans.lower()=="d2":
        dict3 = dict2.copy()
        dict3.update(dict1)
    return dict3


dict1 = dict()
dict2 = dict()

num = int(input("Enter number of keys you want in dictionary1: "))
for x in range(num):
    pair = input(f"Enter name and marks for student{x+1} seperated by \"_\" : ")
    tempInput = pair.split('_')
    dict1[tempInput[0]] = int(tempInput[1])
num = int(input("Enter number of keys you want in dictionary2 : "))
for x in range(num):
    pair = input(f"Enter name and marks for student{x+1} seperated by \"_\" : ")
    tempInput = pair.split('_')
    dict2[tempInput[0]] = int(tempInput[1])
print("Dictionary1 = ", dict1)
print("Dictionary2 = ", dict2)
print("Concat of dict1 and dict2 : ", concatenation(dict1, dict2))


 
"""Write a Python program to sum all the items in a dictionary."""
#5c
# sum of values
print("^^^^Program to get the sum of values in dictionary: ^^^^")

dict1 = dict()
num = int(input("Enter number of keys you want in dictionary: "))
# for x in range(num):
#     pair = input(f"Enter name and marks for {x+1} seperated by \"_\" ")
#     tempInput = pair.split('_')
#     dict1[tempInput[0]] = int(tempInput[1])
for x in range(num):
    key1 = input("Enter key for student {x+1} : ")
    value1 = int(input(f"Enter value for student {x+1} : "))
    dict1[key1] = value1
print("Original dictionary:", dict1)
sum = 0
for x in dict1.values():
    sum = sum+x
print("Sum of the values in the dictionary are: ", sum)



 





"""Write a Python program to read an entire text file. Write a Python program to read last n lines of a file."""

try:
    print("^^^^This is file handling program^^^^")
    print("Enter filename to be created")
    fname = input()
    f=open(fname, 'w')
    print("Enter the text to the file")
    content = input()
    f.write(content) 
    f.close()
    print("Do you wish to continue Y/N?")
    answer=input()
    while answer=='y' or answer=='Y':
        f=open(fname, 'a')
        print("Write text to append")
        content=input()
        f.write(content)
        f.close()
        f=open(fname, 'r')
        print(fname,"currently contains the following text in the file:")
        print(f.read())
        print("Do you wish to continue Y/N?")
        answer= input()
    else:
        print("The final content of ", fname,"is:")
        f= open(fname,'r')
        print(f.read())

except:
    print("Error in file")

finally:
    print("File handling program ended")


 

"""Design a class that store the information of employee and display the same"""
class Employee:
    TotalSal = 0

    def __init__(self, emp_id, dept, designation, basicSalary, incentives):
        self.emp_id = emp_id
        self.dept = dept
        self.designation = designation
        self.basicSalary = basicSalary
        self.incentives = incentives

    def calcTotSal(self):
        self.TotalSal = self.basicSalary+self.incentives

    def displayDetails(self):
        print("Employee ID:",self.emp_id)
        print("Employee Department:",self.dept)
        print("Employee Designation:",self.designation)
        print("Basic Salary:",self.basicSalary)
        print("Incentives:",self.incentives)
        print("Total Salary",self.TotalSal)


print("Enter no. of Employees:")
num = int(input())
counter = 0
emp = []

for i in range(0, num):
 #   print("\n")
    print(f"Enter the Details for {i+1} :")
    emp_id = int(input("Enter Employee ID: "))
    dept = input("Department Name: ")
    designation = input("Designation: ")
    basicSalary = float(input("Enter the Salary: "))
    incentives = float(input("Enter Incentives: "))
    print("\n")
    emp.append(Employee(emp_id,dept, designation, basicSalary, incentives))
#    Employee(emp_id, dept, designation, basicSalary, incentives)

counter = 0
for i in range(0, num):
    emp[counter].calcTotSal()
    emp[counter].displayDetails()
    counter += 1

 


"""Inheritance in Python"""
class Employee
    TotalSal = 0

    def __init__(self, emp_id, dept, designation, basicSalary, incentives):
        self.emp_id = emp_id
        self.dept = dept
        self.designation = designation
        self.basicSalary = basicSalary
        self.incentives = incentives

    def calcTotSal(self):
        self.TotalSal = self.basicSalary+self.incentives

    def displayDetails(self):
        print("Employee ID:",self.emp_id)
        print("Employee Department:",self.dept)
        print("Employee Designation:",self.designation)
        print("Basic Salary:",self.basicSalary)
        print("Incentives:",self.incentives)
        print("Total Salary",self.TotalSal)


print("Enter no. of Employees:")
num = int(input())
counter = 0
emp = []

for i in range(0, num):
 #   print("\n")
    print(f"Enter the Details for {i+1} :")
    emp_id = int(input("Enter Employee ID: "))
    dept = input("Department Name: ")
    designation = input("Designation: ")
    basicSalary = float(input("Enter the Salary: "))
    incentives = float(input("Enter Incentives: "))
    print("\n")
    emp.append(Employee(emp_id,dept, designation, basicSalary, incentives))
#    Employee(emp_id, dept, designation, basicSalary, incentives)

counter = 0
for i in range(0, num):
    emp[counter].calcTotSal()
    emp[counter].displayDetails()
    counter += 1

 



"""Create classes , methods"""
class Employee:
    TotalSal = 0

    def __init__(self, emp_id, dept, designation, basicSalary, incentives):
        self.emp_id = emp_id
        self.dept = dept
        self.designation = designation
        self.basicSalary = basicSalary
        self.incentives = incentives

    def calcTotSal(self):
        self.TotalSal = self.basicSalary+self.incentives

    def displayDetails(self):
        print("Employee ID:",self.emp_id)
        print("Employee Department:",self.dept)
        print("Employee Designation:",self.designation)
        print("Basic Salary:",self.basicSalary)
        print("Incentives:",self.incentives)
        print("Total Salary",self.TotalSal)


print("Enter no. of Employees:")
num = int(input())
counter = 0
emp = []

for i in range(0, num):
 #   print("\n")
    print(f"Enter the Details for {i+1} :")
    emp_id = int(input("Enter Employee ID: "))
    dept = input("Department Name: ")
    designation = input("Designation: ")
    basicSalary = float(input("Enter the Salary: "))
    incentives = float(input("Enter Incentives: "))
    print("\n")
    emp.append(Employee(emp_id,dept, designation, basicSalary, incentives))
#    Employee(emp_id, dept, designation, basicSalary, incentives)

counter = 0
for i in range(0, num):
    emp[counter].calcTotSal()
    emp[counter].displayDetails()
    counter += 1

 

"""Implement Exception Handling"""


class Error(Exception): # Exception is a predefined class in Python
 pass
class ValueTooSmallError(Error):    # Raised when input value is small
 def __init__(self, arg):
    self.strerror = arg

class ValueTooLargeError(Error): # Raised when input value is too large
 def __init__(self, arg):
    self.strerror = arg

# user guesses this number
number = 15
# Looping till the number is equal
while True:
 try:
    input_num = int(input("Guess the number by entering the value: "))
    if input_num < number:
        raise ValueTooSmallError("Value entered is smaller than the answer")
    elif input_num > number:
        raise ValueTooLargeError("Value entered is larger than the answer")
    else:
        break
 except ValueTooSmallError as e:
    print("Error message:",e.strerror,"\n")
 except ValueTooLargeError as e:
    print("Error message:",e.strerror,"\n")

print("Congratulations you guessed the answer!\U0001f604")

 

"""Configuring widgets"""
Code:
from tkinter import *
from tkinter import messagebox
myWindow =Tk()
myWindow.title('FORM WINDOW')
myWindow.geometry('250x300')
myWindow.configure(bg='#dddddd')
def selection():
 choice = var.get()
 if choice == 1:
    m = 'Ms.'
 elif choice == 2:
    m = 'Mr.'
 elif choice == 3:
    pass
 return m
def submit():
 try:
     name = name_Tf.get()
     m = selection()
     return messagebox.showinfo('FORM WINDOW', f'{m} {name}, submitted form.')
 except Exception as ep:
    return messagebox.showwarning('FORM WINDOW', 'Please provide valid input')
def termsCheck():
 if cb.get() == 1:
    submit_btn['state'] = NORMAL
 else:
    submit_btn['state'] = DISABLED
 messagebox.showerror('FORM WINDOW', 'Accept the terms & conditions')
frame1 = Label(myWindow, bg='#dddddd')
frame1.pack()
frame2 = LabelFrame(frame1, text='Gender', padx=30, pady=10)
var =IntVar()
cb = IntVar()
Label(frame1, text='Full Name').grid(row=0, column=0, padx=5, pady=5)
Label(frame1, text='Email').grid(row=1, column=0, padx=5, pady=5)
Label(frame1, text='Password').grid(row=2, column=0, padx=5, pady=5)
Radiobutton(frame2, text='Female', variable=var,
value=1,command=selection).pack()
Radiobutton(frame2, text='Male', variable=var,
value=2,command=selection).pack(anchor=W)
Radiobutton(frame2, text='Others', variable=var,
value=3,command=selection).pack()
name_Tf = Entry(frame1)
name_Tf.grid(row=0, column=2)
Entry(frame1).grid(row=1, column=2)
Entry(frame1, show="*").grid(row=2, column=2)
frame2.grid(row=3, columnspan=3,padx=30)
Checkbutton(frame1, text='Accept the terms & conditions', variable=cb, onvalue=1, offvalue=0,command=termsCheck).grid(row=4, columnspan=4, pady=5)
submit_btn = Button(frame1, text="Submit", command=submit, padx=50, pady=5, state=DISABLED)
submit_btn.grid(row=5, columnspan=4, pady=2)
myWindow.mainloop()
 
 

 

"""Widget Type and their configuration"""
from tkinter import *
app = Tk()
app.geometry("400x400")


def get_x_and_y(event):
 global lasx, lasy # so that it is accessible to the other functions as well
 lasx, lasy = event.x, event.y

 
def draw_smth(event):
 global lasx, lasy
 canvas.create_line((lasx, lasy, event.x, event.y), fill='red', width=2)
 lasx, lasy = event.x, event.y


canvas = Canvas(app, bg='black')
canvas.pack(anchor='nw', fill='both', expand=1)
canvas.bind("<Button-1>", get_x_and_y)
canvas.bind("<B1-Motion>", draw_smth)
app.mainloop()

 
 

import tkinter as tk
fields = 'Last Name', 'First Name', 'Job', 'Country'
def fetch(entries):
 for entry in entries:
    field = entry[0]
    text = entry[1].get()
    print('%s: "%s"' % (field, text))
def makeform(root, fields):
 entries = []
 for field in fields:
    row = tk.Frame(root)
    lab = tk.Label(row, width=15, text=field, anchor='w')
    ent = tk.Entry(row)
    row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
    lab.pack(side=tk.LEFT)
    ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
    entries.append((field, ent))
 return entries


if __name__ == '__main__':
 root = tk.Tk()
 ents = makeform(root, fields)
 root.bind('<Return>', (lambda event, e=ents: fetch(e)))
 b1 = tk.Button(root, text='Show',
 command=(lambda e=ents: fetch(e)))
 b1.pack(side=tk.LEFT, padx=5, pady=5)
 b2 = tk.Button(root, text='Quit', command=root.quit)
 b2.pack(side=tk.LEFT, padx=5, pady=5)
 root.mainloop()





import tkinter as tk
def fahrenheit_to_celsius():
 fahrenheit = ent_temperature.get()
 celsius = (5/9) * (float(fahrenheit) - 32)
 lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
# Set-up the window
window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)
# Create the Fahrenheit entry frame with an Entry
# widget and label in it
frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")
# Layout the temperature Entry and Label in frm_entry
# using the .grid() geometry manager
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")
# Create the conversion Button and result display Label
btn_convert = tk.Button(  master=window,  text="\N{RIGHTWARDS BLACK ARROW}", command=fahrenheit_to_celsius)
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")
# Set-up the layout using the .grid() geometry manager
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)
# Run the application
window.mainloop()
 
 

"""Design a simple database application that stores the records and retrieve the same."""
import mysql.connector
from tkinter import *
from tkinter import messagebox

global mylist,mydb, mycursor,entName,entAddress
mydb = mysql.connector.connect(host="localhost", user="sybca", password="password@123")
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE PractDB")
mycursor.execute("SHOW DATABASES")
print("The Databases listed are :")
for x in mycursor:
  print(x)

mydb = mysql.connector.connect(host="localhost", user="sybca", password="password@123", database="PractDB")
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)
mydb.commit()

def displayRecords():
    global mycursor
    global mylist
    mycursor.execute("SELECT name, address FROM customers")
    myresult = mycursor.fetchall()
    print("Displaying Customer Records")
    for line in myresult:
        str = ' stays at '.join(line)
        mylist.insert(END, str)
        print(str)

def insertRecord():
    global mydb,mycursor, entName, entAddress
    query = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = (entName.get(), entAddress.get())
    mycursor.execute(query,val)
    mydb.commit
    messagebox.showinfo('Insert Record','Record inserted successfully')
    entName.delete(0,'end')
    entAddress.delete(0,'end')

myWindow = Tk()
myWindow.title("Add Record for New Customers")
myWindow.geometry('300x350')
myWindow.configure(background = "#856ff8");
Label(myWindow ,text ="Name").grid(row =0,column =0,pady=5,padx=5,ipadx=5,ipady=5)
Label(myWindow ,text ="Address").grid(row =1,column =0, pady=5,padx=5,ipadx=5,ipady=5)
entName = Entry(myWindow, width=30)
entName.grid(row =0,column = 1,pady=5,padx=5,ipadx=5,ipady=5)
entAddress = Entry(myWindow,width=30)
entAddress.grid(row = 1,column = 1,pady=5,padx=5,ipadx=5,ipady=5)
Button(myWindow ,text="Submit new record",command=insertRecord).grid(row=2,columnspan=2,pady=5,padx=5,ipadx=5,ipady=5)
Button(myWindow ,text="Show Records",command=displayRecords).grid(row=3,columnspan=2,pady=5,padx=5,ipadx=5,ipady=5)

scrollbar = Scrollbar(myWindow,orient=VERTICAL)
mylist = Listbox(myWindow, yscrollcommand=scrollbar.set)
mylist.grid(row=4,columnspan=2,sticky='nsew')
scrollbar.grid(row=4,column=2,sticky='NS')
scrollbar.config(command=mylist.yview)
myWindow.mainloop()

  

 


"""14 Design a database application to search the specified record from the database."""
import mysql.connector
from tkinter import *

global mylist,mydb, mycursor,entName,entAddress

mydb = mysql.connector.connect(host="localhost", user="sybca", password="password@123", database="PractDB")
mycursor = mydb.cursor()

def displayByName():
    global mycursor,mylist,entName
    query = "SELECT name,address FROM customers WHERE name = %s"
    val = (entName.get(),)
    mycursor.execute(query, val)
    mylist.delete(0, END)
    myresult = mycursor.fetchall()
    for line in myresult:
        str = ' stays at '.join(line)
        mylist.insert(END, str)


def displayByAddress():
    global mycursor, mylist, entAddress
    query = "SELECT name, address FROM customers WHERE address = %s"
    val = (entAddress.get(),)
    mycursor.execute(query, val)
    myresult = mycursor.fetchall()
    mylist.delete(0,END)
    for line in myresult:
        str = ' stays at '.join(line)
        mylist.insert(END, str)

def displayRecords():
    global mycursor
    global mylist
    mycursor.execute("SELECT name, address FROM customers")
    mylist.delete(0, END)
    myresult = mycursor.fetchall()
    for line in myresult:
        str = ' stays at '.join(line)
        mylist.insert(END, str)


myWindow = Tk()
myWindow.title("Search Customers")
myWindow.geometry('350x350')
myWindow.configure(background = "#856ff8");
Label(myWindow ,text ="Name").grid(row =0,column =0,pady=5,padx=5,ipadx=5,ipady=5)
Label(myWindow ,text ="Address").grid(row =1,column =0, pady=5,padx=5,ipadx=5,ipady=5)
entName = Entry(myWindow, width=30)
entName.grid(row =0,column = 1,pady=5,padx=5,ipadx=5,ipady=5)
entAddress = Entry(myWindow,width=30)
entAddress.grid(row = 1,column = 1,pady=5,padx=5,ipadx=5,ipady=5)
Button(myWindow ,text="Search by Name",command=displayByName).grid(row=2,column=0,pady=5,padx=5,ipadx=5,ipady=5)
Button(myWindow ,text="Search by Address",command=displayByAddress).grid(row=2,column=1,pady=5,padx=5,ipadx=5,ipady=5)
Button(myWindow ,text="Show ALL Records",command=displayRecords).grid(row=3,columnspan=2,pady=5,padx=5,ipadx=5,ipady=5)

scrollbar = Scrollbar(myWindow,orient=VERTICAL)
mylist = Listbox(myWindow, yscrollcommand=scrollbar.set)
mylist.grid(row=4,columnspan=2,sticky='nsew')
scrollbar.grid(row=4,column=2,sticky='NS')
scrollbar.config(command=mylist.yview)
myWindow.mainloop()
 
     

 



"""15 Design a database application to that allows the user to add, delete and modify the records"""
import mysql.connector
from tkinter import *
from tkinter import messagebox

global mylist,mydb, mycursor,entName,entAddress

mydb = mysql.connector.connect(host="localhost", user="sybca", password="password@123", database="PractDB")
mycursor = mydb.cursor()

def updateAddress():
    global mycursor,mylist,entAddress,entName
    query = "UPDATE customers SET address = %s WHERE name = %s"
    val = (entAddress.get(),entName.get())
    mycursor.execute(query, val)
    mylist.delete(0, END)
    mydb.commit
    messagebox.showinfo('Update Record', 'Record updated successfully')

def deleteCustomer():
    global mycursor,mylist,entName
    query = "DELETE FROM customers WHERE name = %s"
    val = (entName.get(),)
    mycursor.execute(query, val)
    mylist.delete(0, END)
    mydb.commit
    messagebox.showinfo('Delete Record', 'Record deleted successfully')

def displayRecords():
    global mycursor
    global mylist
    mycursor.execute("SELECT name, address FROM customers")
    mylist.delete(0, END)
    myresult = mycursor.fetchall()
    for line in myresult:
        str = ' stays at '.join(line)
        mylist.insert(END, str)


myWindow = Tk()
myWindow.title("Update and Delete Customer records")
myWindow.geometry('350x350')
myWindow.configure(background = "#856ff8");
Label(myWindow ,text ="Name").grid(row =0,column =0,pady=5,padx=5,ipadx=5,ipady=5)
Label(myWindow ,text ="New Address for Update").grid(row =1,column =0, pady=5,padx=5,ipadx=5,ipady=5)
entName = Entry(myWindow, width=30)
entName.grid(row =0,column = 1,pady=5,padx=5,ipadx=5,ipady=5)
entAddress = Entry(myWindow,width=30)
entAddress.grid(row = 1,column = 1,pady=5,padx=5,ipadx=5,ipady=5)
Button(myWindow ,text="Delete Customer",command=deleteCustomer).grid(row=2,column=0,pady=5,padx=5,ipadx=5,ipady=5)
Button(myWindow ,text="Update Address",command=updateAddress).grid(row=2,column=1,pady=5,padx=5,ipadx=5,ipady=5)
Button(myWindow ,text="Show ALL Records",command=displayRecords).grid(row=3,columnspan=2,pady=5,padx=5,ipadx=5,ipady=5)

scrollbar = Scrollbar(myWindow,orient=VERTICAL)
mylist = Listbox(myWindow, yscrollcommand=scrollbar.set)
mylist.grid(row=4,columnspan=2,sticky='nsew')
scrollbar.grid(row=4,column=2,sticky='NS')
scrollbar.config(command=mylist.yview)
myWindow.mainloop()

  
    
 







