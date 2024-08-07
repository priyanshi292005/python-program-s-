import  random
EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5
def set_difficulty(level_chosen):
    if level_chosen=='easy':
        return EASY_LEVEL_ATTEMPTS
    elif level_chosen=='hard':
        return HARD_LEVEL_ATTEMPTS
    else:
        return

def check_answer(guessed_number,answer,attempts):
    if guessed_number<answer:
        print("you guess is too low")
        return attempts-1
    elif guessed_number>answer:
        print("your guess is too high")
        return attempts-1
    else:
        print(f"your guess is right...The answer was {answer}")

def game():
   print("Let me think of a number between 1 to 50.")
   answer=random.randint(1,50)

   level=input("choose level of difficulty...Type 'easy' or 'hard':")
   attempts=set_difficulty(level)
   if attempts!=EASY_LEVEL_ATTEMPTS and attempts!=HARD_LEVEL_ATTEMPTS:
       print("you have entered wrong difficulty level..play again!!")
       return
   guessed_number=0
   while guessed_number!=answer:
       print(f"you have {attempts} remaining to guess the number.")
       guessed_number=int(input("Guess a number:"))
       attempts=check_answer(guessed_number,answer,attempts)
       if attempts==0:
          print("you are out of guesses... you lose!")
       else:
          print("guess again")


game()
