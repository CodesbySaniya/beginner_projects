#project-TO_DO_LIST_PROJECT IN PYTHON
while True:
  print("1.add task")
  print("2.view task")
  print("3.exit task")
  choice=int(input("enter your choice:"))
  if choice==1:
    task=input("enter your task")
    with open('to_do_list.txt',"a") as f:
      f.write(task+"\n")
  elif choice==2:
    with open('to_do_list.txt',"r") as f:
       task=f.readlines()
       for i,task in enumerate(task,1):
        print(i,task) 
  elif choice == 3:
    break
print("thank you for your time")
