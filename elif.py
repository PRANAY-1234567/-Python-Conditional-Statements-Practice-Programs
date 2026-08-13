""""
1) num = eval(input("Enter the number: "))
if num%3==0 or num%4==0:
    print("Divisible")
elif num%3==0 and num%4==0:
    print("Divisible by booth")
else :
    print ("not divisible by any one")


3) num = "12365"
if len(num)==1:
    print("Single")
elif len(num) == 2:
    print("Double")
elif len(num)==3:
    print('Triple')
else:
    print("Above 3")
"""
"""
4) a = eval(input("Enter the character: "))
if isinstance(a,str):
    print(len(a))
elif isinstance(a,tuple):
    print(a[::-1])
else:
    print("Invalid")
"""
"""
5) age = eval(input("Enter the age: "))
if age>=0 and age<=17:
    print("Child")
elif age>=18 and age<=30:
    print("adult")
elif age>=31 and age<=60:
    print("men")
elif age>=61 and age<=100:
    print("Senior Citizen")
else:
    print("Invalid")"""

"""
6) a=eval(input("Enter the number: "))
b=eval(input("Enter the number: "))
c=eval(input("Enter the number: "))

if a<b and a<c:
    print("a is Samaller")
elif b<a and b<c:
    print("b is Samaller")
else:
    print("c is Samaller")"""

"""
7)m=eval(input("Enter the marks: "))
e=eval(input("Enter the marks: "))
h=eval(input("Enter the marks: "))
ma=eval(input("Enter the marks: "))
s=eval(input("Enter the marks: "))
total = m+e+h+ma+s
avg = total/5

if avg>=90 and avg <=100:
    print("Distintion",avg)
elif avg>=75 and avg <=89:
    print("First Class",avg)
elif avg>=60 and avg <=74:
    print("Second Class",avg)
if avg>=50 and avg <=59:
    print("Third Class",avg)
else:
    print("Fail")
"""
"""
8)username1=input("Enter Username: ")
username = "Pranay"
password1=eval(input("Enter the Password: "))
password="12345"

if username1==username and password1==password:
    print("Login Succesful")
elif username1==username and password1!=password:
    print("Incorrect Password")
elif username1!=username and password1!=password:
    print("User not found")
else:
    print("Invalid Both")
"""
"""
9)x=eval(input("Enter the number: "))
if x>=0 and x%2==0:
    print("Positive Even")
elif x>0 and x%2!=0:
    print("Positive Odd")
elif x<0 and x%2==0:
    print("Negative Even")
elif x<0 and x%2!=0:
    print("Negative odd")
else:
    print("Zero")"""
"""
10)Battery=eval(input("Enter the battery percentage: "))
Money = eval(input("Enter the money: "))
if Money >=1000 and Battery >= 80:
    print("Go on a Trip")
elif Money>=500 and Battery>= 50:
    print("Watch a Movie")
elif Money >= 200 and Battery >= 20:
    print(" Go to a Café")
else:          
    print("Stay Home and Study Python 🐍")"""