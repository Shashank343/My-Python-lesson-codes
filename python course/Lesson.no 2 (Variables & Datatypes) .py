 # Lesson.no 2 (Variables & Datatypes)
# Variables Eg:- 
a = "Ch.sai shashank"
b = 41
c = 41.356
d = True
#d = None
# Printing the types of variables:- 
print(type(a))
print(type(b))
print(type(c))
print(type(d))
# printing the Operations in python:-
 # Arthrimatic operators
a = 3
b = 5
print("The value of 3+5 is ", 3+5)
print("The value of 3-5 is ", 3-5)
print("The value of 3*5 is ", 3*5)
print("The value of 3/5 is ", 3/5)

# Assignment operators 
a = 4
a +=2
a -=2
a *=2
a /=2
print("The value of a is ", a)

# Comparition operators 
a = (14>7)
a = (14<7)
a = (14>=7)
a = (14>=7)
a = (14==7)
a = (14!=7)
print(a) 

# Logical operators = and,or,not and logical opertors is related to bool
a = True 
b = False
print('The value of a and b is', a and b)
print('The value of a or b is', a or b)
print('The value of not b is',not  b)

# Type function and typecasting
a = 38
print(type(a))
b = '93'
b = int(b)
print(b + 3)

# Input function
'''a = "Good Evening Mr."
b = input("Enter your name: ")
c = a + b
print (c)
print (type(c))'''

 # Practice set - 2
# (i) 
a = 39
b = 23       
c = a + b 
print(c)

# (ii)
a = 38
b = 83
print('The remainder of a and b is' , a%b) # Note(/ - Gives you quotient and % - Gives you the remainder)

#(iii)
'''a = input("Enter a name: ")
b = ('Welcome comander ')
c = b + a 
print(c)
print(type(c))'''
'''b = input('Enter a number : ')
b = int(b)
print(b)
print(type(b))'''

#(iv)
a = 34
b = 80
print(a > b)

#(v)
'''a = input('Enter the first number: ')
b = input('Enter the second number: ')
a = int(a)
b = int(b)
c = ("The average of two numbers a and b are : " , (a + b)/ 2)
print(c)'''

#(vi)
'''a = input('Enter a number: ')
a = int(a)
c = (a*a)
print(c)'''