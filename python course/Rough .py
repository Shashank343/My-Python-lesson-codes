'''a = "Good Evening Mr."
b = input("Enter your name: ")
c = a + b
print (c)
print (type(c))'''

'''import keyword
print(keyword.kwlist)'''

'''print(int(True))
print(int(False))'''

'''a = 'My favourite is mango'
b = 32
c = 12.35

print(a[0:6])
print(b) '''

'''a = True
b = False

print(a or b)
print(a and b)
print(not a)'''

from ctypes import Union


a = (14<7)
b = (98>78)

print(a and b)
print(a or b)
print(not a)

a = 25
b = 15
c = a/b
d = a%b
print(c)
print(d)

a = 'Shashank'
print(a[-1])

A = []
print(A)

a = [3, 5, 6, 4, 8, 1]
a[0] = 1
print(a)

a = (3, 4, 2, 8, 6, 9)
print(a.index(9))

# a = "Good Morning, "
# b = input("Enter your name: ")
# c = a + b
# print(c)

a = {
    "aim" : "Work hard for what you want nothing comes near you with lazyness",
  "Rolex" : "He is one of the character in a movie called vikaram. He plays a big and main role in that movie"
 }
print(a)

updatedict = {
    "Ram" : "Ram is know as Read only Memory"
}
a.update(updatedict)
print(a)
print(list(a.keys()))
print(type(a.keys()))
print(type(a.values()))
print(a.items())

a = set()
print(type(a))

a = {1, 2, 3, 4, 5, 6, 6.5}
a2 = {1, 2, 3, 4, 5, 6, 7}
a.union({4,8})
print(a)
a.intersection({5,2})
print(a)

'''age = 18
age = int(input("Enter your age :"))
if (age==18): 
    print("Your age is greater than 18")
else: 
    print("Your age is not greater than 18")
print(age)'''

# a = "Harry"
# print(a[0:-2])

'''a = int(input("Enter you age: "))
if(a>18):
    print("You age is greater than 18")
elif(a==18):
    print("Your age is Equal to 18")
else:
    print("your age is lesser than 18")
print(a)'''

a = ("Why i am not getting this code")
print(len(a))

# post = input("Type your post:\n")
# if("Harry" or "harry" or "harry's" or "Harry's" in post):
#     comment = True
# else:
#     comment = False

# if(comment):
#     print("This post is talking about Harry")
# else:
#     print("This post is not talking about Harry")

'''a = int(input('Enter a number: '))
for i in range(1, 11):
    print(str(a) + ' X ' + str(i) + ' = ' + str(i*a)) 
a = input('Enter your name: ')    
'''
done =  True 
print(isinstance(done,bool))

'''num = int(input("Please enter any number: "))
factorial = 1 
for i in range(1, num+1):
    facotrial = factorial * i
print(f"The factorial of %d - %d" %(num, factorial))'''

'''def account(balance):
    a = ('your bank balance is: 18,000')
    return a 
b = input('Enter your pin to check your bank balance:\n')
print(b + account)'''

a = 23
a = str(a)
print(a)

i = 0 
while 1000 > i :
    i = i + 1
    print('yes ' + str(i))

'while loop'
"""fruits = [' Apple', ' Banana', ' Grapes', ' Mango', ' Custedapple']
i = 0
while i<len(fruits):
    print(fruits[i])
    i = i + 1"""

for i in range(2, 12, 2):
    print(i)

'for loop'
fruits = [' Apple', ' Banana', ' Grapes', ' Mango', ' Custedapple']
for item in fruits:
    print(item)
else:                
    print('Yo man the above loop printed all the numbers and now it is exhausted(over)')

'Break statement'
for i in range(10):
   print(i)
   if i == 4:
    break

'Continue statement'
for i in range(10):
    if i == 4:
        continue
    print(i)

'Pass statement'
i = 2
if i < 4:
    pass
else:
    print("Hello moto")

while i > 3:
    pass

'''num = int(input('Enter a number: '))
for i in range(1, 11):
    print(str(num) + ' X ' + str(i) + ' = ' + str(i*num))'''

l1 = ['Harry', 'Sohan', 'Sachin', 'Rahul']
for item in l1:
    print('Good evening,', item)

'''num = int(input('Enter a number: '))
prime = True
for i in range (2, num):
    if(i%num ==0):
      prime = False  
    break
if prime:
      print('This number is a prime')
else:
    print('This number is not a prime')'''

# Function & Recurresion
def Greetings(names):
    return 'Welcome come in thanks for comming to the party'

names = ['\'Rohan\'', '\'Ankit\'', '\'Robert\'', '\'Zamer\'']
for items in names:
    print(Greetings(names), items)

def percentage(marks):
    p = ((marks[0] + marks[1] + marks[2] + marks[3])/400)*100
    return p  
marks1 = [70, 90, 79, 79]
percentage1 = percentage(marks1)

marks2 = [12, 69, 35, 65]
percentage2 = percentage(marks2)
print(percentage1, percentage2)

def greet(name):
    print('Good morning, ' + name)
greet('Shashank')

# Function with arruguments
def mysum(sum1, sum2):
    return sum1 + sum2
s = mysum(23 , 45)
print(s)

# Default parameter value
def greet(name = 'Stranger'):
    print('Goodday, ' + name)
greet('Harry')
greet()

## Recurssion
# n! = 1 * 2 * 3 * 4
n = 4
product = 1
for i in range (n):
    product = product * (i+1)
    print(product)

# practice set(Function's and reccursions)
'(i)'
def numbers(num1, num2, num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            print(num3)
    else:
        if (num2>num3):
           return num2
        else:
            return num3
    
a = numbers(12, 34, 53)
print(a)

i = 0
while i<5:
    print('\'yes\'', str(i))
    i = i + 1

L1 = [3, 53, 35, 12, 45]
L1.insert(3, 2)
print(L1)

s = {1, 3, 5, 2}
print(len(s))

i = 0
while i<3:
    print('Sai.Shashank')
    i = i+2

a = 'what is with you'
a = a.find('what')

# a = int(input("Enter the number for the table: "))
# i = 0 
# while i in range(1, 11):
#     print(i)
#     i = i + 1
# print([a], "X", [i], "=", [a*i])

'''a = int(input("Enter the number for tables: "))
for i in range(0 , 11):'''

# f = ("poem.txt", "r")
# t = f.read()
# if "twinkle" in t:
#     print("Twinlke is present in t")
# else:
#     print("Twinkle is not present in t")

# Printing and seeing the difference between Atributes like they are of two types one is class atributes and other is instance atribute
class Employe:
    company = "Honda"
    salary = "1000"
Harry = Employe()
Harry.salary = 2334
print("Harry's salary is:",Harry.salary)

'''Noun - class - name,object etc.. 
Adjective - employ - name, age, number, address etc...
Verb - method - getsalary, getfame etc... '''

class Zombie:
    Game = "Killing the Zombies"
    Cloths = "Shirt & Pant"
    def Wepon(self):
        print(f"The zombie is wering {self.Cloths} and has a kinfe in his hands")

Galvo = Zombie()
Galvo.Wepon()
Kalvo = Zombie()

class defination:
    comapny = "Yonx"
    def getsalary(self):
        print("The salary is 293847")
    @staticmethod
    def greet():
        print("Good Morning, Sir")

harry = defination()
harry.getsalary()

pooja = defination()
pooja.getsalary()

with open("another.txt") as f:
    a = f.read()
print(a)

f = open("sample.txt", "w")
f.write("Shashank is going to achive success in his life and bring glory to his family")
f.close()

vegetables = ['carrot', 'cabage', 'tomato', 'capsicum', 'bottleguard']
i = 0
while i<len(vegetables):
    print(vegetables[i])
    i = i + 1
print = "Here are some examples of", vegetables

a = len("Feeling like to live alone away from all others only me and my hobbies")
