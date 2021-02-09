import sys
import datetime

HELP = 'Usage :-\n$ ./todo add "todo item"  # Add a new todo\n$ ./todo ls               # Show remaining todos\n$ ./todo del NUMBER       # Delete a todo\n$ ./todo done NUMBER      # Complete a todo\n$ ./todo help             # Show usage\n$ ./todo report           # Statistics'


def excute(command):
    if command == "add":
        try:
            task = sys.argv[2]
        except:
            print("Error: Missing todo string. Nothing added!")
            return
        file = open("todo.txt", "a")
        file.write(task + "\n")
        print(f'Added todo: "{task}"')

    elif command == "ls":
        tasks=[]
        try:
            file = open("todo.txt", "r")
            tasks = file.readlines()
        except:
            pass
        
        if len(tasks) == 0:
            print("There are no pending todos!")
        else:
            i = len(tasks)
            while i != 0:
                print(f"[{i}] {tasks[i-1]}", end="")
                i = i - 1

    elif command == "del":
        try:
            file = open("todo.txt", "r")
        except:
            return
        tasks = file.readlines()
        tasks = [task.strip() for task in tasks]
        task_id = -1
        # task_id=sys.argv[2]
        try:
            task_id = sys.argv[2]
        except:
            print(len(tasks))
            err='Error: Missing NUMBER for deleting todo.'
            print(str(err))
            return
        task_id = int(task_id) - 1
        if int(task_id) == -1 or int(task_id) >= len(tasks):
            print(f"Error: todo #{int(task_id+1)} does not exist. Nothing deleted.")
        else:
            del tasks[int(task_id)]
            print(f"Deleted todo #{task_id+1}")
            file.close()
            file = open("todo.txt", "w")
            tasks = [task + "\n" for task in tasks]
            file.writelines(tasks)

    elif command == "done":
        try:
            file = open("todo.txt", "r")
        except:
            pass
        tasks = file.readlines()
        tasks = [task.strip() for task in tasks]
        task_id = -1
        try:
            task_id = sys.argv[2]
        except:
            print("Error: Missing NUMBER for marking todo as done.")
            return
        task_id = int(task_id) - 1
        if int(task_id) == -1 or int(task_id) > len(tasks):
            print(f"Error: todo #{task_id+1} does not exist.")
        else:
            data = open("done.txt", "a")
            data.write(tasks[int(task_id)] + "\n")
            del tasks[int(task_id)]
            print(f"Marked todo #{task_id+1} as done.")
            file.close()
            data.close()
            file = open("todo.txt", "w")
            tasks = [task + "\n" for task in tasks]
            file.writelines(tasks)

    elif command == "help":
        print(HELP)

    elif command == "report":
        today = datetime.date.today()
        try:
            file = open("todo.txt", "r")
        except IOError as e:
            print(str(e))

        tasks = file.readlines()
        tasks = [task.strip() for task in tasks]
        file.close()
        try:
            data = open("done.txt", "r")
        except IOError as e:
            print(str(e))
        completed = data.readlines()
        completed = [comp.strip() for comp in completed]
        print(f"{today} Pending : {len(tasks)} Completed : {len(completed)}")


def main():
    cmd = ["add", "ls", "del", "done", "help", "report"]
    command = ""
    try:
        command = sys.argv[1]
    except:
        pass
    finally:
        if len(command) == 0:
            print(HELP)
        else:
            if command not in cmd:
                print("Wrong command")
                return
            else:
                excute(command)


if __name__ == "__main__":
    main()