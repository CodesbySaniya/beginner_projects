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

# print(spin(symbols))


def check_result(result,bet,balance):
    if result[0] == result[1] and result[1] == result[2] :
      print("you won!")
      balance = balance-bet
      if result[0] == "🍒":
        balance += 20
      elif result[0] == "🔔":
        balance += 30
      elif result[0] == "🍋":
        balance += 40
      elif result[0] == "⭐":
        balance += 50
      elif result[0] == "7️⃣":
        balance += 70
    
    else:
       print("you lose!")
       balance = balance-bet
       

    return balance

print(balance)


while True:
  new_bet = get_bet(balance)
  new = spin(symbols)
  print(new)
  updated_balance = check_result(new,new_bet,balance)
  balance = updated_balance
  print(f"balance left : {balance}")
  if updated_balance <= 0:
    print("Game Over!")
    break
