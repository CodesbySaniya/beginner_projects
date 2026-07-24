# slot machine program


import random

balance = 100

symbols = ["🍒","🍋","🔔","⭐","7️⃣"]


def get_bet(balance):
  while True:
    bet = int(input("enter your bet"))
    if bet <= 0 or bet > balance: 
     print("Invalid bet")
     continue
    else:
     return bet


def spin(symbols):
   result = []
   for res in range(3): 
    ans = random.choice(symbols)
    result.append(ans)
   return result

print(spin(symbols))


def check_result(result,bet,balance):
    if result[0] == result[1] and result[1] == result[2] :
      print("you won!")
      if result[0] == "🍒":
        reward = bet+20
      elif result[0] == "🔔":
        reward = bet+30
      elif result[0] == "🍋":
              reward = bet+40
      elif result[0] == "⭐":
              reward = bet+50
      elif result[0] == "7️⃣":
              reward = bet+70
      balance -= bet
      balance = reward
    else:
       reward= bet-30
       balance -= bet
       balance=reward

    return reward

