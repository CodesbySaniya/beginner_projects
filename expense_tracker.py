#Expense Tracker project

expense = []

menu = [ "1. Add Expense",
"2. View Expenses",
"3. Total Expense",
"4. Exit"]


user_choice = input("would u like to see menu for what to do update ? (Y/N)" ).lower()
if user_choice == "y" or user_choice == "yes":
  for option in menu:
    print(option)
else:
  print("ok do updation ")



while True:

 update = int(input("enter what to do(1-4) ?"))


 if update == 1: 
   item = input("enter item or q to quit: ").lower()
   if item != "q":
    amount = int(input("enter amount"))
    expense.append({"item" :item ,
                    "amount": amount})
    if expense != []:
      print("expense added successfully!")
    else:
      print("expense not added")

    print(expense)
   else:
    break
  
 elif update == 2:
  if expense:
   for exp in expense:
    print(exp["item" ] , exp["amount" ])
  else:
    print("No expenses added")

 elif update == 3:
  total = 0
  print(expense)
  if expense != []:
   for amt in expense:
    total+= amt["amount"]
   print(total)
  
 elif update not in [1,2,3,4]:
  print("Invalid Choice")

 else:
   break



