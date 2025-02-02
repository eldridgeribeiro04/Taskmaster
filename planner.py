from datetime import date, datetime

# class TaskMaker:
    
#     def __init__(self, title, description, due_date):
#         title = self.title
#         description = self.description
#         due_date = self.due_date

tasks = []

def set_date(year, month, day):
    spec_date = date(year, month, day)
    return spec_date

def add_task():
    title = input("Please enter the title of the task: ")
    description = input("Please enter a description of the task: ")
    user_input = input("Please enter the date as YYYY, MM, DD: ")
    
    if user_input:
        year, month, day = map(int, user_input.split(", "))
        due_date = set_date(year, month, day)
        
        if due_date < date.today():
            print("Incorrect entry. Date cannot be in the past")
        elif any(task[2] == due_date for task in tasks):
            print("You already have a task to finish, choose another date")  
        else:
            tasks.append([title, description, due_date])
            print(title + " - " + description + " - " + str(day) + "/" + str(month) + "/" + str(year))
    else:
        pass


def get_tasks():
    result = []
    
    if len(tasks) < 1:
        print("No tasks")
    else:
        for num, i in enumerate(tasks):
            result.append((f"{num+1}) {i}"))
            print(result)


def remove_task():
    task_number = int(input("Please enter a number: "))
    if 0 < task_number <= len(tasks):
        del tasks[task_number-1]
        print(tasks)
    else:
        print("Incorrect task number")


def retrieve_task():
    task_number = int(input("Please enter a number: "))
    if 0 < task_number <= len(tasks):
        print(tasks[task_number-1])
    else:
        print("Incorrect task number")


def run():
    
    while True:
        select = input("Please enter A if you want to add a task,"
                    "Please enter V to view all tasks,"
                    "Please enter T to get a specific task,"
                    "Please enter D to delete a task,"
                    "Please enter Q to quit: ").lower()
    
    
        if select == "a":
            add_task()     
        elif select == "v":
            get_tasks()    
        elif select == "t":
            retrieve_task()
        elif select == "d":
            remove_task()
        elif select == "q":
            print("Goodbye")
            break
            
run()
