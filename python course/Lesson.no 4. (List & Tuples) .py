 # Lesson.no 4 (List & Tuples)
# List - In list you can change the value of an index in that string
'''a = ['Shashank', 12, 38.0, True, False, None]
'print(a)'
print(a[5])
a[0] = 41
print(a)'''

# List Methods
from itertools import count
from tkinter import N


L1 = [1, 2, 3, 4, 56, 27, 13.8]
L1.sort()
L1.reverse()
L1.append('Shashank')
L1.insert(4, 5)
L1.pop(0)
L1.remove(13.8)
print(L1)

# Tuples - In list you can change the values of an index, but in Tuples you cannot change the value of an index
a = ('Shashank', 12, 38.0, True, False, None)
print(a)
t1 = (1,) # It is known as a tuple with an single element. A comma must to be there even if you give only one element in a tuple
print(t1)

# Tuple methods 
Truth = (2, 3, 5, 7, 7, 11, 13, 17, 19)
print(Truth.count(7))
print(Truth.index(11))

 # Practice set - 4 
#(i)
'''f1 = input('Enter the name of the fruit: 1.')
f2 = input('Enter the name of the fruit: 2.')
f3 = input('Enter the name of the fruit: 3.')
f4 = input('Enter the name of the fruit: 4.')
f5 = input('Enter the name of the fruit: 5.')
f6 = input('Enter the name of the fruit: 6.')
f7 = input('Enter the name of the fruit: 7.')
fruitlist = [f1, f2, f3, f4, f5, f6, f7]
print(fruitlist)'''

#(ii)
'''M1 = int(input('Enter the marks of student.no 1. '))
M2 = int(input('Enter the marks of student.no 2. '))
M3 = int(input('Enter the marks of student.no 3. '))
M4 = int(input('Enter the marks of student.no 4. '))
M5 = int(input('Enter the marks of student.no 5. '))
M6 = int(input('Enter the marks of student.no 6. '))
Marks = [M1, M2, M3, M4, M5, M6]
Marks.sort()
print(Marks)'''

#(iii)
'''a = (2, 3, 5, 3, 2)
a[3] = 4
print(a)'''

#(iv)
a = [23, 34, 56, 67]
# print(sum(a))
'or'
print(a[0] + a[1] + a[2] + a[3])

#(v)
a = (7, 0, 8, 0, 0, 9)
print(a.count(0)) 