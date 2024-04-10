 # Lesson.no 7 (Loops)
i = 0
while i<10:
    print('yes ' + str(i))
    i = i + 1
print('Done')
'Note: If the codition never becomes false the loop just keeps the program executed until it gets true'

# Quick Quize
#(i)
i = 0 
while i<=50:
    print(i)
    i = i + 1
print('Done')

#(ii)
# While Loop
fruits = ['Mango', 'Watermelon', 'Dragonfruit', 'lichy', 'grapes', 'Oranges']
i = 0
while i<len(fruits):
    print(fruits[i])
    i = i + 1
print('The list of all the fruits are here:', fruits)

# For Loop
subjects = ['Mathematics', 'Physic', 'Chemistry', 'Computers', 'Art and Craft']
for item in subjects:
    print(item)

'For loop range'
for i in range(10): # for i in range(range, range, Stepsize/skipping values) Eg:-(1, 8, 2) / for i in range(range, Sepsize/Skipping values)
    print(i)

'For loop with else'
for i in range(8):
    print(i)
else:
    print('This is else used in for loop')

numbers = [3, 4, 5]
for item in numbers:
    print(item)
else:
    print("Done These are the numbers in the given list")

'The Break statement - when i = 13 it will stop it till there'
for i in range(20):
    print(i)
    if(i == 13):
      break
    
'The continous statement - when i = 11 it will just skip 11 and returns all the values'
for i in range(15):
    if i == 11:
        continue 
    print(i)

''''The pass statement - It is a null statement, It instructs you to do nothing'
i = 5
if i>0:
    pass
print('Shashank is making progress in building his own empire')

i = 12
if i>6:
    pass
while i>6:
    pass
print('This is the last statement or last thing in the loops this lesson is over')'''

 # Pracitce set - 7
#(i)
'''a = int(input('Enter a number: '))
for i in range(1, 11):
    # print(str(a) + ' X ' + str(i) + ' = ' + str(i*a)) 
    print(f"{a} x {i} = {a*i}")'''

#(ii)
l1 = ['Harry', 'Sachin', 'Sohan', 'Rahul']
for name in l1:
    if name.startswith('S'):
        print('Welcome to my brothers birthday party ' + name + '\nThanks for coming to the party!!!')
        
#(iii)
'''i = 0
while i<20000:
    print(str(i) + 'fall ')
i = i + 1 
print('completed')'''

#(iv)
'''a = int(input("Enter a number: "))
prime = True
for i in range(2, a):
    if(a%i == 0):
        prime = False
        break
if prime:
    print('This number is a prime number')
else:
    print('This number is not a prime number')'''

#(v)
'''num = int(input('Enter a number: '))
hold = num
sum = 0
if num <= 0: 
    print('Enter a whole number positive!')
else:
    while num>0:
        sum = sum + num
        num = num - 1
print('Sum of first',hold, 'Sum of n natural numbers is:', sum)'''

#(vi)
'''num = int(input("Enter the number: "))
factorial = 1 
for i in range(1, num+1):                      This code has a problem 
    facotrial = factorial * i
print(f"The factorial of {num} is {factorial}")'''

#(vii)
n = 3 
for i in range(3):
    print(" " * (n-i-1), end=" ")
    print("*" * (2*i+1), end=" ")
    print(" " * (n-i-1))

#(viii)
n = 4
for i in range(4):
    print('*' * i)

#(ix)
'''n = 3
for i in range(3):                             This code is not done and has a problem
    print("*" * (i*1))'''

#(x)
a = int(input('Enter a number: '))
for i in range (1, 11):
    i.reverse(1, 11)
    # print(str(a) + ' X ' + str(i) + ' = ' + str(i*a)) 
    print(f"{a} x {i} = {a*i}")
