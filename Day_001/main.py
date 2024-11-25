print("\nWelcome to TODOLISTER!")

tasklist = []
running = True

# Define displaying task function
def display_tasks():
  if len(tasklist) != 0:
    print("Here is all your list of tasks\n")
    for task in tasklist:
      print(str(tasklist.index(task)+1)+".",task)
  else:
      print("**There is no task left! Congrat!!!\n")


while running:
  display_tasks()
  print("\nA = Add task\nD = Delete task\nQ = Quit\n")
  action = input("Please enter your action : ")

  if action.lower() == "a":
    t = input("Please enter the task you would like to add :\n")
    print("task was added!\n")
    tasklist.append(t)
  elif action.lower() == "q":
    running = False
  elif action.lower() == "d":
    if len(tasklist) != 0:
      display_tasks()
      d = int(input("Please select the number of task that you want to delete : "))
      dt = tasklist.pop(d-1)
      print("\nTask -",dt, "was remove from the list!")
    else:
      "There is no task to remove! Please add more task instead."
  else:
    print("There is no command for that input. Please try again.\n")
   