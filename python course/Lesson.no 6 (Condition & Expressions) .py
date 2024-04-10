 # Lesson.no 6 (Condition & Expressions)

from cgitb import text
from xml.etree.ElementTree import Comment


a = 38
# This is known as if-elif-else ladder with or without the space in between them and you can create an multiple if and elif in the ladder Eg:(if-if-if-elif-elif-elif-else)
if(a>35):
    print("The value of a is greater than 35")

elif(a>15):
    print("The value of a is greater than 15")

else:
    print("The value of a is not greater than 35 and 15")
print(a)

# Multiple if statements 
a = 45
if(a>11): 
    print("The value of a is greater than 11")

if(a>43):
    print("The value of a is greater than 43")

if(a>32):
    print("The value of a is greater than 32")
else: 
    print("The value of a is not greater than 11 & 43")
print(a)
 
# Quick quize
'''a = int(input("Enter your age(Only in digits):\n"))
if(a>18):
    print("Your age is greater than 18")

elif(a==18):
    print("Your age is equal to 18")

else:
    print("Your age is lesser than 18")

print(a)'''

# Relational operators 
'==, <=, >=, >, <,  etc. Eg: if(18==18) if(12<=18)'

# Logical operators 
"and - For 'and' both the conditions - (a>18 and a<60) must be statisfy in the if statement"
#a = int(input('Enter your age number:\n'))
# if(a>18 and a<60):
#     print("You can get an job")
# else:
#     print("You cannot get a job")
# print(a)

"or - For 'or' just a single condition is needed to satisfy for it"
#a = int(input('Enter your age number:\n'))
# if(a>18 or a<60):
#     print("You can get an job")
# else:
#     print("You cannot get a job")
# print(a)

"not - For 'not' nothing is needed to satisfy it will just reverse the output like if its 'true then false' if its 'false then true' "
# a = int(input("Enter your age number:\n"))
# if(not a>18):
#     print("You can get a job")
# else:
#     print("You cannot get a job")

#in and is
"is"
a = None
if(a is None):
    print("Yes")
else:
    print("No")
print(a)

"in"
a = [12, 34, 56]
print(12 in a)

'else and elif is an optional statement if you want you can use it or not needed'

 # Practice set - 6
#(i)
'''num1 = int(input("Enter the first numbers: "))
num2 = int(input("Enter the second numbers: "))
num3 = int(input("Enter the third numbers: "))
num4 = int(input("Enter the fourth numbers: "))
if(num1>num2):
    print("num1 is greater than num2")
else:
    print("num1 is lesser than num2")

if(num1>num3):
    print("num1 is greater than num3")
else:
    print("num1 is lesser than num3")

if(num1>num4):
    print("num1 is greater than num4")
else:
    print("num1 is lesser than num4") 

if(num2>num3):
    print("num2 is greater than num3")
else:
    print("num2 is lesser than num3")  

if(num2>num4):
    print("num2 is greater than num4")
else:
    print("num2 is lesser than num4")  

if(num3>num4):
    print("num3 is greater than num4")
else:
    print("num3 is lesser than num4") '''

#(ii)
'''a = int(input('Enter your Mathematics marks to get your percentage: '))
b = int(input('Enter your Physic marks to get your percentage: '))
c = int(input('Enter your Chemistry marks to get your percentage: '))
print("The total passing pecentage is 40 in each subject is 33%")
if(a<33 or b<33 or c<33):
    print("You have failed")
else:
    print(" 'Congrats!!' you have passed in each subject")

if(a + b + c)/3 <40 :
    print("Your total percentage is less than 40 so 'your have Failed'")
else:
    print(" 'Congrats!!' your total percentage is above 40 'You have Passed'")
e = (a + b + c)
print("The sum of all subjets you got: ", e)
f = (a + b + c)/3 
print("Your total percentage is: ", f)'''

#(iii)
'''text = input("Type a comment: ")
if("Make a lot of money" in text):
    spam = True
elif("Buy now" in text):
    spam = True 
elif("subscribe this" in text):
    spam = True
elif("Click this" in text):
    spam = True
else:
    spam = False

if(spam):
    print('This comment is a spam')
else:
    print('This comment is not a spam') '''

#(iv)
'''username = input("Enter the username: ")
if(len(username)>10):
    print("Your username contains more than 10 character")
elif(len(username)<10):
    print("your username contains less than 10 character")
else:
     print("Your username characters is equal to 10")
print(username)'''

#(v)
'''a = {'Shashank','Nishanth','Varshit','Balji','Vatsalya','Harshit'}
b = input("Enter a name: ")
if(b in a):
    print("The name which you have typed is there in our list")
else:
    print("The name which you have typed is not there in our list")
print(a)'''

#(vi)
'''marks = (int(input("Enter your marks to check your grade: ")))

if marks>=90:
    grade = "\'A\'"
elif marks>=80:
    grade = "\'B\'"
elif marks>=70:
    grade = "\'C\'"
elif marks>=60:
    grade = "\'D\'"
elif marks>=50:
    grade = "\'F\'"
else:
    grade = "\'F\'"
print('your grade is ' + grade)'''

#(vii)
'''post = input("Type a comment: ")
if("Harry" in post):
    spam = True
elif("harry" in post):
    spam = True 
elif("Harry's" in post):
    spam = True
elif("harry's" in post):
    spam = True
else:
    spam = False

if(spam):
    print('This post is talking about Harry')
else:
    print('This post is not talking about Harry')''' 