  # Lesson.no 10 (Object Oriented Programming language (OPP;s)) 
# OPP's - It another way solving problems like by creating objects. 

'''Syntax
class anyname:
    variables & Methods'''

# Let's take one example of a normal easy class.
class Number:
    def sum(self):
        return self.a + self.b
    
num = Number()
num.a = 12
num.b = 34
s = num.sum()
print(s)

# Pascal case ex:- EmployName, FatherInLaw see the case sensitive like in 1st ex E&N are capital and in 2nd ex F,I&L are capital this is pascal case.
# camel case ex:- employName, fatherInLaw see the case sentsitve like in 1st ex e is small and N is capital and 2nd ex f is small I&L are capital means in camel case.
# There are two types of attrubutes one is class attribute means which belongs to the class and the other one is instance attribute which belong to a particular Object.
class Railwayform:
    formtype = 'Railwayform' # --> Class attribute
    def printData(self): # self is a parameter which passes automatically, The details of an object goes to self parameter like below example
        print(f"The name of the passager is {self.Fullname}") # --> Instance Attribute
        print(f"The age of the passanger is {self.age}") # --> Instance Attribute
        print(f"Passenger's PhoneNumber {self.PhoneNumber}") # --> Instance Attribute
        print(f"Date of Birth of the passanger {self.DateOfBirth}") # --> Instance Attribute
        print(f"From where to where the passanger is travelling {self.WheretoWhere}") # Instance Attribute

# When a class is filled by someone it becomes their personal application
Shashank = Railwayform()
Shashank.Fullname = "Ch.Sai Shashank"
Shashank.age = 18
Shashank.PhoneNumber = 7997599699
Shashank.DateOfBirth = 17/6/2006
Shashank.WheretoWhere = "Hyderbad to Goa"
Shashank.printData()

# We can use Opp's in real entitee like you can use Opp's to create games, websites, app's etc... ex like 

'''class Remote:
    pass
class Player:
    def MoveRight(self):
        pass
    def MoveLeft(self):
        pass
    def MoveTop(self):
        pass
Remote1 = Remote()
Player1 = Player()
if(Remote1.isLeftPressed()):
    Player1.MoveLeft() '''
# When the User/Player has pressed the left button the player in game move according the button pressed on the remote. 
# Abstraction - A function that u can use is known as abstraction, When u press a button something happens, So when u press that button some files are procced which are hidded from u is called abstraction.
# Encapuslation - The details which are wrapped under same function, from above example in remote each button details are wrapped in a remote and a large no.of detailes subdivided and given to each button.

# Moddeling in OPP's:
# Nothing but ClassName is Noun like Employee etc.., Attributes is Adjective like Employee's name, DOB his detalis etc.., Methods is Verb(def name) getsalary(), getInfo etc..

class Employee:
    Company = "Youtube"
    def getInfo(self, signature): # I can pass mutiple arguments instead of self.
        print(f"The Employee name is {self.name} and his position is {self.position}") # You can write mulitple self parameter in single print defination. 
        print(f"The Employee's weekOff {self.weekOff} \n {signature}")
# To write a function we need 'self' parameter but if you only want do things like greeting etc.., That's where static method comes in handy where you don't use self parameter ex:-   
    @staticmethod
    def greet():
        print("Good Morning, Sir")
# i can create mutiple staticmethod's 
    @staticmethod
    def Time():
        print("The time is 9:00AM and its Morning")

Shashank = Employee()
Shashank.name = "Sai Shashank"
Shashank.position = "Team Manager"
Shashank.weekOff = "Saturday & Sunday"
print(Shashank.name) # you can get a particullar employees info not only that any particullar object info.
Shashank.greet()
Shashank.getInfo('Thanks!')

# There is also a thing called constructure it is (__inti__) this need's self parameter and it runs first as soon as the object is created it can also further aruguments like normal funciton
# why it is called as consturcture because it initialize object, lets take an exmaple

class Employee:
    def __init__(self, name, qualification, phone_no):
        print("Saving the details of the employee in the Office server")
        self.name = name
        self.qualification = qualification
        self.phone_no = phone_no
    
    def EmpolyeeInfo(self):
        print(f"The employee's name is {self.name}")
        print(f"The emplyee's qualification is {self.qualification}")
        print(f"The employee's phone.no is {self.phone_no}")

Shashank = Employee('Shashank', 'B.Tech Passed', 7997599699)
Shashank.EmpolyeeInfo()

  # Practice set - 10
#(i)
