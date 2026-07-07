num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

operator = input("Enter the operator you want to use : (+,-,/,*) ")

if operator == "+":
  print(f"Addition of numbers is:{round(num1+num2,3)}")
elif operator == "-":
  print(f"Subtraction of numbers is: {num1-num2}")
elif operator =="/":
  if num2==0:
    print("divide is not possible")
  else:
   print("Division of a numbers is",num1/num2)
elif operator == "*":
  print("Multiplication of numbers is",num1*num2)
else:
  print("Invalid operator! use(+,-,/,*)")