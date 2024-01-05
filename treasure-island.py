print(''' _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|''')

print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')


print('''\nWelcome to Treasure Island ,''')
print('''You're goal is to find the Treasure.''')

choice1 = input('''While walking around , You come across a crossroad . Decide to turn "left" or "right" : ''').lower()

if choice1 == "right" :
    print("\nYou fell into a hole . \n G A M E  O V E R")
elif choice1 == "left":
    choice2=input('''You have come across a lake . You can "swim" or "wait" for the boat . ''').lower()
    if choice2 == "wait":
        choice3=input("You arrived at the island unharmed . There is a house with 3 doors with different colour .\n blue , yellow , green which door do you choose ").lower()
        if choice3 == "blue":
            print("You entered a room full of fire. \nG A M E  O V E R")
        elif choice3 == "yellow":
            print("You found the treasure. Congratulations ")
        elif choice3 == "green":
            print("You entered a room full of beasts. \nG A M E  O V E R")
        else:
            choice4 = input('''You entered a labyrinth. As you go down you see underground temple. You can go "back" or "forward" ''').lower()
            if choice4 == "back":
                print("You encounter a zombie.\nG A M E  O V E R")
            elif choice4 == "forward":
                choice5=input('''Entering the temple you see skeletons with armour, swords and shields. "wield" them or keep on "moving" ''').lower()
                if choice5 == "wield":
                    choice6 = input(''''You see 3 routes to treasure room . \nWhich do you choose "1" with deadly smoke , "2" with venemous snakes or "3" with hungry lions who havent eaten in a year ''')
                    if choice6 == "1":
                        print("The fire burned you to a crisp.\nG A M E  O V E R")
                    elif choice6 =="2":
                        print("The snakes even digested you bones.\nG A M E  O V E R")
                    elif choice6 =="3":
                        print("You easily crossed the route and entered the treasure room.\nThe room is filled with gems , diamonds , gold jewellery . Congratulations")
                else:
                    print("A snake  bit you . \nG A M E  O V E R")
                
                 
            
    else:
        print("You were eaten by a pirahnas. \nG A M E  O V E R")    
