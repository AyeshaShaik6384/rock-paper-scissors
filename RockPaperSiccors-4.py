import random
rock = '''
    _______
---'   ____)
      (_)
      (_)
      ()
---.(_)
'''

paper = '''
    _______
---'   ___)___
          ______)
          _______)
         _______)
---.)
'''

scissors = '''
    _______
---'   ___)___
          ______)
       __________)
      ()
---.(_)
'''
game=[rock,paper,scissors]
print("Lets play Rock, Paper, Scissors")
user_choice=int(input(print("Type 0 for Rock, 1 for Paper, and 2 for scissors")))
print(game[user_choice])
computer_choice=random.randint(0, 2)
print(game[computer_choice])
if user_choice>=3 or user_choice<0:
    print("You typed an invalid number.You lose")
elif user_choice==0 and computer_choice==2:
    print("You win")
elif computer_choice==0 and user_choice==2:
    print("You lose")
elif computer_choice > user_choice:
    print("You lose")
elif user_choice>computer_choice:
    print("You win")
elif computer_choice==user_choice:
    print("Its a draw")