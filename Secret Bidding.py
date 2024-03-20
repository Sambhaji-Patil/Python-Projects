import os

def clear_screen():
  """Clears the screen."""
  if os.name == 'nt':
    _ = os.system('cls')
  else:
    _ = os.system('clear')

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

bids={}

def highest_bid(bidding_record):
  highest=0
  for bidder in bidding_record:
    bid_amount=bidding_record[bidder]
    if bid_amount>highest:
      highest=bid_amount
      winner=bidder
  print(f"\nThe winner is {winner} with a bid of ₹{highest}")
  print("\nList of Bidders")
  for bidder in bids:
    print(f"Name:{bidder} Bid:{bids[bidder]}")
  
status=True
while status:
  name=input("What is your name?\n")
  price=int(input("What is your bid? ₹"))
  bids[name]=price
  decision=input("Are there any other bidders? Type 'yes' or 'no': ")
  if decision=="no":
    status=False
    highest_bid(bids)
  elif decision=="yes":
    clear_screen()