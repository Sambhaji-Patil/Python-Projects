import random
import os

def clear_screen():
  """Clears the screen."""
  if os.name == 'nt':
    _ = os.system('cls')
  else:
    _ = os.system('clear')
logo="""
   _____                      _______ _             _   _                 _               
  / ____|                    |__   __| |           | \ | |               | |              
 | |  __ _   _  ___ ___ ___     | |  | |__   ___   |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ / __/ __|    | |  | '_ \ / _ \  | . ` | | | | '_ ` _ \| '_ \ / _ | '__|
 | |__| | |_| |  __\__ \__ \    | |  | | | |  __/  | |\  | |_| | | | | | | |_) |  __| |   
  \_____|\__,_|\___|___|___/    |_|  |_| |_|\___|  |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                                                                                                         
""" 
game_again=True
win=False
while game_again!=False:
    print(logo)
    print("Welcome To The Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    level=input("Choose a level Type easy or hard: ").lower()
    if level=='hard':
        attempts=5
    else:
        attempts=10

    #generates a random number
    def random_number():
        number=random.randint(1,100)
        return number

    answer=random_number()
    # print(f"answer is {answer}") #include this if you want to see the answer
    while win==False and attempts>0:
        print(f"You have {attempts} attempts left.")
        guess=int(input("Make a guess: "))
        if guess<answer:
            print("Too low\nGuess Again.")
            attempts=attempts-1
        elif guess>answer:
            print("Too High\nGuess Again.")
            attempts=attempts-1
        else:
            print(f"You got it! The answer was {answer}")
            win=True
    
    if attempts==0:
            print(f"You've run out of guesses, you lose.\nAnswer was {answer}!!")

    choice=input("\nDo you want to play again? Type Yes or No\n").lower()
    if choice=='yes':
        game_again=True
        clear_screen()
    else:
        print("GoodBye")
        game_again=False