#WEIGHT CONVERTER PROGRAM

weight = float(input("Enter your weight"))
unit=input("weight in (K)g or (L)bs ?").upper()


if unit == "K":
  converted = weight * 2.205
  print(f"your weight is : {round(converted,2)}lbs")

elif unit == "L":
  converted = weight / 2.205
  print(f"your weight is{round(converted,2)} kg")

else:
  print("Enter correct unit(K or L)")
