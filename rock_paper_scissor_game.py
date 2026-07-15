
  #rock_paer_scissor_game

import random

options = ["rock","paper","scissor"]



# computer = random.choice(options)

# print(computer)

while True:
 player=input("Enter yours ('Rock',,Paper'','Scissor'')").lower()
 computer = random.choice(options)
 print("Computer chose:", computer)
 if player == computer:
  print("game tie")
 elif player == "rock" and computer == "scissor":
  print("player win")
 elif player == "scissor" and computer == "paper":
  print("player win")
 elif player == "paper" and computer == "rock":
     print("player win")
 else:
   print("computer win")
   break
# print("Computer chose:", computer)
