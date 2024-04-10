 # Lesson.no 8 (Functions & Recursions) 
from os import makedirs
from unittest import makeSuite


def percentage(marks):
    p = ((marks[0] + marks[1] + marks[2] + marks[3] )/400)*100  
    return p

marks1 = [51, 80, 81, 78]
percentage1 = percentage(marks1)

marks2 = [79, 82, 81, 75]
percentage2 = percentage(marks2)

print('The percentage1 & percentage2 = ',percentage1,',', percentage2)

def greetings(name):
    print('Good Day, ' + name)
greetings('Harry')
greetings('Shashank')

# Function with arguments
def mysum(sum1, sum2):
    return(sum1 + sum2)

a = mysum(2, 12)
print(a)

# Defaut paremeter value
def greet(name = 'Stranger'):
    print('Goodday, ' + name)
greet('Harry')
greet()

# Recursions
 # n! = 1 * 2 * 3 * 4 * ... * n
'''n = 8
product = 1
for i in range (n):
    product = product * (i+1)
print(product)'''

'Wraping the Recursion in function (Making the Recursion into def)'
def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product
print(factorial_iter(4))

def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_recursive(n-1)
a = factorial_recursive(5)
print(a)

 # Practice set - 8 
#(i)
def maxium(num1, num2, num3):
    if (num1 > num2):
        if (num1 > num3):
             return num1
        else:
            return num3
    else:
        if (num2 > num3):
            return num2
        else:
            return num3
m = maxium(23, 314, 56)
print('The value of maxium is', m)

#(ii)
def farh(cel):
    return (cel * (9/5)) + 32
a = 34
f = farh(a)
print('Farnheat temprerature is ' + str(f))

#(iii)
'''print('Hello,', end=' ')
print('how', end=' ')
print('are', end=' ')
print('you?', end=' ')'''

#(iv)
"""def recur_sum(n):
    if(n<=0):
        return n
    else:
        return n+recur_sum(n-1)
num = int(input('Enter a natural number: '))
if(num<0):
    print('Enter a natural number.')
else:
    print(recur_sum(num))"""

#(v)
n = 3
for i in range(n):
    print('*' * (n-i))

#(vii)
def inch(cms):
    return(cms * 2.54)
b = 12
i = inch(b)
print("The convertion of inches to cms is: " + str(i))

#(viii)
def remove_and_split(string, word):
    newstr = string.replace(word, "")
    return newstr.strip()
    
this = "    Shashank is on the way to success    "
n = remove_and_split(this, 'is')
print(n)

#(ix)
def multi_table(num):
    a = int(input('Enter a natral number: '))
    if(a <= 0):
        return('\'!pls enter a natural number.\'')
    else:
        for i in range(1, 11):
            print(f"{a} x {i} = {a*i}")
print(multi_table(a))
