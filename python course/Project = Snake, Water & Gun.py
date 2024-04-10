import random

# Snake, water & gun or Rock, paper & sissors (Game)
def gamewin(computer, you):
    # If two values are equal the it is a tie 
    if computer == you:
        return None
    
    # Check for all the properties when computere choses 's'
    elif computer == 's':
        if you== 'w':
            return False
        elif you== 'g':
            return True
    
    # Check for all the properties when computer choses 'w'
    elif computer == 'w':
        if you== 'g':
            return False
        elif you== 's':
            return True
    
    # Check for all the properties when computer choses 'g'
    elif computer == 'g':
        if you== 's':
            return False
        elif you== 'w':
            return True

computer = ('computer Turn: Snake(s), Water(w) or Gun(g)?')
randno = random.randint(1, 3)
if randno == 1: 
    computer = 's'
elif randno == 2:
    computer = 'w'
elif randno == 3:
    computer = 'g'

you = input('Your turn: Snake(s), Water(w) & Gun(g)?: ')
a = gamewin(computer, you) 

print(f'Computer chose {computer}')
print(f'You chose {you}')

if a == None:
    print('The game is a tie')
elif(a):
    print("!!!YOU WON!!!")
else:
    print('YOU LOST (^__^)')   