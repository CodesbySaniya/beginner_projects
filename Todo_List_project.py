#project-updated_TO_DO_LIST_PROJECT IN PYTHON
while True:
  print("1.add task")
  print("2.view task")
  print("3.exit task")
  print("4.delete task")
  choice=int(input("enter your choice:"))
  if choice==1:
    task=input("enter your task")
    with open('to_do_list.txt',"a") as f:
      f.write(task+"\n")
  elif choice==2:
    with open('to_do_list.txt',"r") as f:
       tasks=f.readlines()
       for i,task in enumerate(tasks,1):
        print(i,task) 
  elif choice==4:
    delete_task=int(input("enter the task number you want to delete"))
    with open("to_do_list.txt","r") as f:
      tasks=f.readlines()
      for i,task in enumerate(tasks,1):
        print(i,task) 
        # delete_task=int(input("enter the task number you want to delete"))
        del tasks[delete_task-1]
        with open('to_do_list.txt',"w") as f:
         for t in tasks:
           f.write(t)

  elif choice == 3:
    break
print("thank you for your time")
