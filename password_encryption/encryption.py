#encryption project python

while True:
 menu = ("===== Encryption Tool =====",
"1. Encrypt",
"2. Decrypt",
"3. Exit",
)
 for m in menu:
  print(m)
 choose = int(input("enter your choice"))

 enc_msg = ""
 dec_msg = ""
 if choose == 1:
 
  msg = input("enter your message: ")
  key = int(input("enter the key: "))
  print(msg)
  print(key)
  for mn in msg:
   if mn == " ":
    enc_msg = enc_msg+mn
    
   else: 

    number = ord(mn)
    new_value =  number -97 
    new_key = key+new_value
    new_val = new_key % 26
    new_pos = new_val + 97
    new_letter = chr(new_pos)

    enc_msg = enc_msg+new_letter
  print(enc_msg)

 elif choose == 2:
       msg = input("enter your message: ")
       key = int(input("enter the key: "))
       print(msg)
       print(key)
       for mn in msg:
         if mn == " ":
          dec_msg = dec_msg+mn
         else:
          number = ord(mn)
          new_value =  number -97 
          new_key = new_value - key
          new_val = new_key % 26
          new_pos = new_val + 97
          new_letter = chr(new_pos)
          dec_msg = dec_msg+new_letter
       print(dec_msg)

 elif choose ==3:
  break

 else:
  print("Invalid Choice!")
