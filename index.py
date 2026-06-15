tasks = []

while True:
    print("\n=====TO-DO-LIST=====")
    print("1. Add Tasks")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # choice for Enter Task
    if choice == "1":  
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    # to show tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\n Your Tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
    
    # for exit 
    elif choice == "3":
        print("Thank You")
        break
    
    # if entering wrong choice
    else:
        print("Invalid choice! Please try again.")

    