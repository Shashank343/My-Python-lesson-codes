 # Lesson.no 3 (Strings)
# Types of strings
'single qoute string' 
"double court string"
'''Triple court string'''

greetings = "Good morning, "
name = 'Shashank'
c = (greetings + name) # Concatinating two string using (+ Symbol)
print(c)

# String slicing 
a = 'Shashank'
print(a[0:3])
print(a[0:]) # This type of statement print from startitng till the of the string  
print(a[:8]) # This is also the same function as the above 
print(a[:-1]) # If we don't know the ending of the string we can use the this function

# Slicing and skipping 
a = 'Shashank is having hard times at home'
print(a[0::3]) # The last number help to skip the values in the string 

# String functions 
Statement = ("I am learning python language from a famous youtuber called CodingwithHarry. His vedios help a lot for the people who wanted to learn coding")
print(len(a))
print(Statement.endswith('coding'))
print(Statement.count('o'))
print(Statement.capitalize())
print(Statement.find('python'))
print(Statement.replace('python', 'C++'))


# Escape sequence character
a = 'Nothing comes for free.\\ \n \t \"You must work hard to get it\"'
print(a)

 # Practice set - 3
#(i)
a = input("Enter your name: ")
b = 'Good Morning '
c = b + a
print(c)

#(ii)
letter = '''Dear, <|Name|>
 Greeting From VS CODE Company that you got selected Congracts!

   <|Date|> '''
 
Name = input("Enter your Name: ")
Date = input("Enter today's Date: ")
letter = letter.replace("Name", Name)
letter = letter.replace("Date", Date)
print(letter)

#(iii)3 & 4
ShortStory = "Once upon a time there was a Master who does overthinking.  To save the world from the creatures who want to distroy this   earth in future and make this world a   better place"
print(ShortStory.count('  '))
print(ShortStory.replace('  ', ' '))

#(iv)
oldletter = '''Dear harry, This python course is really nice.Thanks!!'''
print(oldletter)
Formatedletter = '''Dear Harry,\n\tThis Python course is really nice.\n\t\tThanks!!'''
print(Formatedletter) 