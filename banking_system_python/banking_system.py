#Banking System Project

accounts = []

while True:
 print("===== Banking System =====")
 menu = ["1. Create Account",
"2. Deposit Money",
"3. Withdraw Money",
"4. Check Balance",
"5. View All Accounts",
"6. Exit"]
 for mn in menu:
  print(mn)
 ask = int(input("select any option: "))
 if ask == 1:
   name = input("enter your name:")
   acc_no = int(input("enter your account number: "))
   balance = float(input("enter your starting balance:"))
   ls = {"name" : name,
        "acc_no" : acc_no,
        "balance" : balance}
   accounts.append(ls)
   for acc in accounts:
     print(acc)
   print("Account Created Successfully!")
   ask2 = input("you want to add more account (y/n)? ").lower()
   if ask2 =="yes" or ask2 == "y":
    continue
   else:
    print(accounts) 

 if ask == 2:
  found = False
  ask3 = int(input("enter your account number: "))
  deposit = float(input("enter amount you want to deposit: "))
  if deposit <0:
        print("amount cant be negative")
  else:
   for account in accounts:
    if account["acc_no"] == ask3:
     found = True
     account["balance"] += deposit
     print(account["balance"])
     print("money deposited in your account")
  if found == False:
   print("account not found")
  ask4 = input("you want to do more deposit (y/n)? ").lower()
  if ask4 =="yes" or ask4 == "y":
    continue
  else:
      # 
      print(account["balance"])
 if ask == 3:
   found= False
   ask5 = int(input("enter your account number: "))
   withdraw = float(input("enter amount you want to withdraw: "))
   if withdraw <0:
           print("amount cant be negative")
   else:
    for account in accounts:
     if account["acc_no"] == ask5:
       found = True
       if account["balance"] >= withdraw:
         new_amt = account["balance"] - withdraw
         account["balance"] = new_amt
        #  print(new_amt)
         print(account["balance"])
         print("amount withdraw successfully")
       else:
         print("unsufficient balance")
   if not found:
    print("account not found")

 if ask == 4:
   found = False
   ask6 = int(input("enter your account number:"))
   for acc in accounts:
     if acc["acc_no"] == ask6:
       found = True
       print(acc["balance"])

   if not found:
     print("account not found")

 if ask == 5:
   for account in accounts:
     print(f"Account_name: {account["name"]}")
     print(f"Account_number: {account["acc_no"]}")
     print(f"Account_balance: {account["balance"]}")
     print("-------------------------------------")
 if ask == 6:
   break
