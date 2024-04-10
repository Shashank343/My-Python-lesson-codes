  # Lesson.no 9 (File I/O)
" ### This lesson is an another file's like ex: 'sample.txt', 'another.txt', etc... "

f = open('sample.txt', 'r')
data = f.read(8) # This no. can also be empty just prints the no.of chartaters u want
print(data)
f.close()

# "Readline" an another method we can use instead of read & This read's only one line instead of the whole sentence
f = open('sample.txt', 'r')
 # Read's only first line 
data = f.readline()
print(data)
 # Read's the second line and so on...
data = f.readline()
print(data)
f.close()

# How to write & update a file
f = open('another.txt', 'w')
f.write("This another txt file which is created by u.")
f.close()

# How to append in a file
f = open('another.txt', 'a')
f.write(" This file is created by shashank") # This can be use mutilple times 
f.close()

# "with" method which help's to open a file easly this method can also work with other modes also
with open('another.txt', 'r') as f:
    a = f.read()
print(a)

  # Practice set - 9
#(i)
f = open('poem.txt')
t = f.read()
if 'twinkle' in t:
   print('twinkle word is present in the poem')
else:
   print('twinkle is not present in the poem')
f.close()