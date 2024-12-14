def to_do_list():
    tasks = []
    
    while True:
        print("\n1. Add Task  2. View Tasks  3. Remove Task  4. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            task = input("Enter the task: ")
            tasks.append(task)
        elif choice == '2':
            print("\nTasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        elif choice == '3':
            index = int(input("Enter task number to remove: ")) - 1
            if 0 <= index < len(tasks):
                tasks.pop(index)
            else:
                print("Invalid task number.")
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

to_do_list()
