print("\nWelcome to TODOLISTER!")

running = True

# Define displaying task function.
def display_tasks():
  with open("tasklist.txt", "r") as file:  
    tasklist = file.readlines()

    if len(tasklist) != 0:
      print("Here is all your list of tasks\n")
      for task in tasklist:
        print(str(tasklist.index(task)+1)+".",task.strip("\n"))
    else:
      print("**There is no task left! Congrat!!!\n")
    return tasklist

# Continuously running program.
while running:
  tasklist = display_tasks()
  print("\nA = Add task\nD = Delete task\nQ = Quit\n")
  action = input("Please enter your action : ")

  if action.lower() == "a":
    t = input("Please enter the task you would like to add :\n") + "\n"
    print("task was added!\n")
    tasklist.append(t)

    with open("tasklist.txt", "w") as file:
      file.writelines(tasklist)
    
  elif action.lower() == "q":
    running = False
  elif action.lower() == "d":
    if len(tasklist) != 0:
      display_tasks()
      d = int(input("Please select the number of task that you want to delete : "))
      if d > 0 and d <= len(tasklist):        
        dt = tasklist.pop(d-1)
        print("\nTask -",dt, "was remove from the list!")
      else:
        print("Invalid number! Please try again.\n")
    else:
      print("There is no task to remove! Please add more task instead.")
  else:
    print("There is no command for that input. Please try again.\n")
   