import random

user_choice = int(input("Enter your choice: Typr 0 fer rock, Type 1 for paper , Type 2 for scissor=="))
if user_choice >= 3 or user_choice < 0:
    print(" you enter Invalid input, you lose" )
else:
     computer_choice = random.randint(0,2)
     print('computer chose:')
     print(computer_choice)
     if user_choice == computer_choice:
         print(" it's a drop")
     elif user_choice == 2 and computer_choice == 0:
         print("you lose")
     elif user_choice == 0 and computer_choice == 2:
         print("you win")
     elif user_choice  < computer_choice:
         print(" you lose")
     elif user_choice > computer_choice:
         print(" you win")
