from art import logo
print(logo)

bids = {}
finished = False
import os
def find_highest_bidder(bid_rec):
  highest = 0
  winner = ""
  for bidder in bid_rec:
    bid_amount = bid_rec[bidder]
    if bid_amount > highest: 
      highest = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest}")

while not finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    os.system('cls')
  