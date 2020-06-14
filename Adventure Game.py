
import time  # import time to sleep some times
import random  # import random to select random objects
# Confugre List Of Objects
Places = ['Forest', 'Desert', 'House']
Weapons = ['Sword', 'Knife', 'Gun', 'Rock']
Forest_Monsters = ['Bear', 'Rabbit', 'Lion', 'Wolf', 'Monkey']
Desert_Monsters = ['Alien', 'Giant Monster', 'Snake', 'Dog']
House = ['Eat', 'Drink', 'Sleep', 'Watch Movie']
Game_Result = ['Win', 'Lose']
# End Configuration
# Define Function To print Messages


def PrintSleep(msg, seconds):
    print(msg + '\n')
    time.sleep(seconds)
PrintSleep('Welcome to the game of adventures fun game ' , 2)
PrintSleep('takes you to another world of fun and thrill' , 2)
PrintSleep('We will help you during the game choices, but you have to think well before each selection so you can win' , 2)
name = input('Please Enter Your Name To Start Game \n')
time.sleep(1)
print('Please Choose Witch Place you want to play \n')
time.sleep(1)
for place in Places:
    print(place)
    time.sleep(1)
Choice = ''
while Choice not in Places:
    msg = 'Give me your choise for forest write f or forest or 1\n for desert write desert or d or 2 \nfor house write house or h or 3\n'
    Choice=input(msg)
    if Choice.lower() == 'Forest'.lower() or Choice.lower() == 'F'.lower() or  Choice == '1':
        Choice = 'Forest'
    elif Choice.lower() == 'Desert'.lower() or Choice.lower() == 'D'.lower() or  Choice == '2':
        Choice= 'Desert'
    elif Choice.lower() == 'House'.lower() or Choice.lower() == 'H'.lower() or  Choice == '3':
        Choice = 'House'
    else:
        Choice = ''
time.sleep(2)
print('you have a weapon ')
weaponchoosed = random.choice(Weapons)
print(weaponchoosed)
changerequest = input('would you like to change weapon\n')
if changerequest == 'yes':
    weaponchoosed=random.choice(Weapons)
    print(weaponchoosed)
print('\nyou now in ' + Choice + ' and you have a weapon ' + weaponchoosed)
time.sleep(1)
print('now you see fornt of you ')
if Choice == 'Forest':
    print(random.choice(Forest_Monsters))
if Choice == 'Desert':
    print(random.choice(Desert_Monsters))
if Choice == 'House':
    print(random.choice(House))
time.sleep(2)
PrintSleep('Use weapon to kill monster' , 2)

print('you ' + random.choice(Game_Result))
time.sleep(2)
print ('Game Over')
