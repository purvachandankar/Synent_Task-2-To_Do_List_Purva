def task():
    tasks = []

    while True:
        print("\n1.Add Task\n")
        print("2.Delete Task\n")
        print("3.View Task\n")
        print("4.Exit\n")

        choice = input("Enter your choice:")

        if choice == "1":
            task = input("\nEnter the task:")
            tasks.append(task)
            print("\n....Task added successfully.....\n")
        
        elif choice == "2":
            task_deleted = input("\nEnter the task you want to delete:")
            if task_deleted in tasks:
                tasks.remove(task_deleted)
                print(f"...{task_deleted} Task is deleted...")
            else:
                print("Task not found")

        elif choice == "3":
            if len(tasks) == 0:
                print("No task is mentioned")
            else:
                print("\nTask are\n")
                for i , t in enumerate (tasks,start = 1):
                    print(f"{i} {t}")
        
        elif choice == "4":
            print("........Exit........")
            break 
        else: 
            print("In-valid Choice")

task()
    
