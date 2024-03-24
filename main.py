from art import logo,vs
from data import data
import random
import os

def clear_screen():
  """Clears the screen."""
  if os.name == 'nt':
    _ = os.system('cls')
  else:
    _ = os.system('clear')

game_end=False

while game_end!=True:
    clear_screen()
    print(logo)
    score=0


    def get_random_account():
        return random.choice(data)

    def game(account1,account2):
        print(f"\n\nCompare A: {account1['name']}, a {account1['description']}, from {account1['country']}.")
        print(vs)
        print(f"\Against B: {account2['name']}, a {account2['description']}, from {account2['country']}")
        compare(account1,account2)
    
    def compare(account1,account2):
        global score
        if account1['follower_count']>account2['follower_count']:
            winner=account1['name']
        elif account1['follower_count']<account2['follower_count']:
            winner=account2['name']
        ans=input("\nWho has more followers? Type 'A' or 'B': ").lower()
        if ans=='a':
            if account1['name']==winner:
                score=score+1
                print(f"\nYou are right. Current score: {score}")
                account2=get_random_account()
                game(account1,account2)
            else: 
                print(f"\nYou are wrong. Final Score: {score}")
                score=0
                game_end=True
        else:
            if account2['name']==winner:
                score=score+1
                print(f"\nYou are right. Current score: {score}")
                account1=account2
                account2=get_random_account()
                game(account1,account2)
            else:
                print(f"\nYou are wrong. Final Score: {score}")
                score=0
                game_end=True

    account1=get_random_account()
    account2=get_random_account()
    game(account1,account2)

    print("Game Over")
    op = input("\nDo you want to play again? Type 'y' or 'n': ")
    if op.lower() != 'y':
        print("Thank you for playing")
        game_end=True