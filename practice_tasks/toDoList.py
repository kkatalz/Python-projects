from termcolor import colored

tasksList = []
VIEW_TASKS = "View Tasks"
ADD_TASK = "Add Task"
REMOVE_TASK = "Remove Task"
EXIT = "Exit"

def addTask():

    while True:
        task = input("Enter a new task: ").strip()
        
        if task == "":
            print(colored("Invalid task.", "red"))
            continue

        else:
            tasksList.append(task)
            print(colored(f"Task '{task}' added."),"lightgreen")
            break
            

def showTask():
    if tasksList == []:
        print(colored("No task in the list.", "cyan"))

    else:
        print("\n")
        print("Tasks:")
        for i in range(len(tasksList)):
            print(f"{colored(i+1, 'light_magenta')}. {tasksList[i]}")

def removeTask():
    while True:
        
        showTask()
        if tasksList == []:
            break

        remove_task = input("Enter the task number to remove: ").strip()
        task = int(remove_task)-1
        if 0 <= task < len (tasksList):
            tasksList.pop(task)
            print(f"Task '{task+1}' removed.") 
            break
        else:
            print(colored("Invalid task number.", "red"))
            continue
    
def main():

    action = None
    while action != "Exit":
        print("\n")
        print("Todo List Menu:")

        listMenu = [VIEW_TASKS, ADD_TASK, REMOVE_TASK, EXIT]

        for i in range(len(listMenu)):
            print(f"{i+1}. {listMenu[i]}")


        while True:
            choice = input("Enter your choice: ").strip()
     
            try:
                choice = int(choice)
                if 1 <= choice <= len(listMenu):
                   action = listMenu[choice-1]
                   break

            except ValueError:
                print("Invalid choice. Please enter a number.")
                continue
                
        if action == VIEW_TASKS:
            showTask()
        elif action == ADD_TASK:
            addTask()    
        elif action == REMOVE_TASK:
            removeTask()


if __name__ == "__main__":
    main()