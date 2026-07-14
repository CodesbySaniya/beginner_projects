#python quiz program

Questions = ("who is our prime minister?",
              "who is our chief misnister?",
              "who is our president?",
              "who is our home minister?"
)
options =   ( ("A.neha","B.narendra","C.rishi","D.ajay"),
            ("A.nidhi","B.kritika","C.saniya","D.bhajan lal"),
            ("A.draupadi","B.riya","C.sita","D.ram"),
            ("A.mihit","B.krish","C.dhruv","D.amit shah"))

answers = ("B", "D", "A", "D")

guesses = []

count = 0

ques_num = 0


for ques in Questions: 
     print("--------")
     print(ques)
     for opt in options[ques_num]:
          print(opt)
     


     guess = input("Enter (A, B, C, D): ").upper()
     guesses.append(guess)
     if guess == answers[ques_num]:
       print("CORRECT!")
       count+=1
     else:
         print("WRONG!")
     ques_num+=1

     
print("--------")
print("Result")
print("--------")
print(f"Correct Answers : {answers}")
print(f"Your Guesses    : {guesses}")
print(f"Your Score      : {count}/{len(Questions)}")
print(f"Your Percentage : {count/len(Questions)*100:.0f}%")
