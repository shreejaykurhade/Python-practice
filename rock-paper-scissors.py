import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice=[rock,paper,scissors]
play=0; score1=0; score2=0; 
playername=input("Enter you name player : ") 

while play==0:
    
    player=int(input("What do you choose ? Type 1 for Rock , 2 for Paper , 3 for Scissors.\n "))-1
    
    print(choice[player])
    computer=random.randint(0,2)
    print("Computer choose \n",choice[computer])
    
    if (player==0 and computer==0) or (player==1 and computer==1) or (player==2 and computer==2) :
        print("It's a Draw.")
    elif (player==1 and computer==0) or (player==2 and computer==1) or (player==0 and computer==2) :
        print("You Won.")
        score1+=1 
    else :
        print("You Lose.")
        score2+=1
    print(f"\n\n{playername}'s score is {score1}\nComputer's score is {score2}")
    play=int(input("To Play Again Press 0 or Press 9\n"))
    