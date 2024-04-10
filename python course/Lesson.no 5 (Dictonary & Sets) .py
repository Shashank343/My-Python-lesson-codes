 # Lesson.no 5 (Dictonary & sets)
# Dictonary and printing methods 
from distutils import bcppcompiler


MyDict = {
    'Shashank' : 'He is a person who want to make more money & and make his parents feel proud of him',
      'skills' : 'skills is nothing but to learning something and making money by it',
     'goals' : 'Working on or learning about something which you always wanted to achive in your life',
     'Marks' : [15, 26, 50, 12],
     'AnotherDict' : {'anotherDict' : 'Means you can create an anotherDict in a created one',
      'life' : 'No one knows what happens in future so work hard and enjoy your life'
      }        
}
print(MyDict['skills'])
print(MyDict['goals'])
MyDict['Marks'] = [34, 67, 86, 56, 56] 
print(MyDict['Marks'])
print(MyDict['AnotherDict'])
print(MyDict['AnotherDict']['life'])

# Dictonary methods
mydict = {
  "Supercars" : "Those are the cars which shows the about your wealth and make them think that its his luck",
   "Mindset"  : "If you want to start a startup you can by beliving in yourself and working hard not by a job mindest",
     "Quotes" : "Middle class people don't need quotes or motivation they know by their standard of living and they already have a unique midset than others",
    "Success" : "Success meant for people who work hard, don't waste time, take risk and those people are also known as 1% member"
}
print(mydict)
print(mydict.keys()) # It prints the keys. You can use this '(list(mydict.keys()))' to print it in a list form and 'type' to print the type of it
print(mydict.values())
print(mydict.items())# It prints ("key" : "values") in the type of list like tuple
updatedict = {
  "True friends" : "True friend are the friends who help you everythime and atlest remember you after the division from school"
}
mydict.update(updatedict)
print(mydict)
# print(mydict["Success2"]) This throws an error because square brackets gives only the value which is there in the dictionary
print(mydict.get("Success2"))# But this'get' method will not through the error instead of that it gives a 'None'  

# Sets
a = {1, 3, 5, 6}
print(a)
print(type(a))

b = set() # This gives as an empty set and this a = {} gives empty dictonary
b.add(1)# It adds one in set and gives the output like {1}
b.add(2)
# b.add(2) It will not add 2 instead of that it will through an error because set do not contain duplicate keys 
b.add((3, 4, 5)) # It can add tuple but not a list [] & Dictonary {} too...
print(b)
print(type(b))

# Set's Method 
a = {1, 2, 3, 4, 4.5}
print(len(a))
a.remove(4.5)
print(a)
print(a.pop())
# a.clear()
# print(a)
print(a.union({4.9}))

 # Practice set - 5
#(i)
'''HindiDict = {
  "Kalemirchi" : "Red dried chilli",
  "Dabba"  : "Box",
  "pankka" : "seeling fan or the fan we use when the current is gone",
  "Chatha" : "Umberalla",
  "Vastue" : "Things or Iteams",
  "Mazak"  : "joke or did something for fun(prank)."
}
print('Hi, what meaning you want form the HindiDict, The option are: ',HindiDict.keys())
a = input("Enter the word what you want from options: ")
print("The meaning for your word is: \n", (HindiDict.get(a)))'''

#(ii)
'''num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
num3 = int(input("Enter your third number: "))
num4 = int(input("Enter your fourth number: "))
num5 = int(input("Enter your fifth number: "))
num6 = int(input("Enter your sixth number: "))
num7 = int(input("Enter your seveth number: "))
num8 = int(input("Enter your eigth number: "))
a = {num1, num2, num3, num4, num5, num6, num7, num8}
print(a)'''

#(iv)
a = {18, "18", 18,1}
print(a)

#(v)
s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(s)
print(len(s))

#(v)
s = {}
print(type(s))

#(vi)
favlang = {}
a = input("Enter you favourate language Varshit:\n")
b = input("Enter you favourate language Balaji:\n")
c = input("Enter you favourate language Vatsalya:\n")
d = input("Enter you favourate language Harshit:\n")
favlang['Varshit'] = a
favlang['Balaji'] = b
favlang['Vatsalya'] = c
favlang['Harshit'] = d
print(favlang)

#(vii)
'If the languages of the two friend are the same then it will give single friends meaning'

#(viii)
s = {8, 7, 12, 'Harry', [1,2]}
print(s)
'No you cannot change the value of the set like Dictonary because it is immutable means connot change & there is list which is unashable means i list connot be in a set if its a tuple also you cannot change tuple also right so it throws an error'
