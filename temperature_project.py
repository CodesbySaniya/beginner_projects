#TEMPRATURE PROGRAM

temperature = float(input("what is the temprature rn ?"))
unit = input("write unit (C) or (F)").upper()

if unit == "C":
  converted =temperature * 9/5
  print(f"Temperature in farenheit is : {round(converted + 32 , 2)} F")

elif unit =="F":
  converted =temperature - 32
  print(f"Temperature in celcius is : {round(converted * 5/9 , 2)} C")

else:
  print("write correct unit")
