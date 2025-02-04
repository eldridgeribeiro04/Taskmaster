from datetime import date, datetime

from tkinter import *
from tkinter import ttk

class TaskMaker:
    
    def __init__(self):
        self.tasks = []

    def set_date(self, year, month, day):
        return date(year, month, day)

    def add_task(self):
        # title = input("Please enter the title of the task: ")
        # description = input("Please enter a description of the task: ")
        # user_input = input("Please enter the date as YYYY, MM, DD: ")
        
        task_title = title.get()
        task_description = description.get()
        user_input = task_date.get()
        
        if user_input:
            year, month, day = map(int, user_input.split(", "))
            due_date = self.set_date(year, month, day)
            
            if due_date < date.today():
                print("Incorrect entry. Date cannot be in the past")
            elif any(task[2] == due_date for task in self.tasks):
                print("You already have a task to finish, choose another date")  
            else:
                self.tasks.append([title, description, due_date])
                print(title + " - " + description + " - " + str(day) + "/" + str(month) + "/" + str(year))
        else:
            pass


    def get_tasks(self):        
        if not self.tasks:
            print("No tasks available")
        else:
            for num, task in enumerate(self.tasks, start=1):
                title, description, due_date = task
                formatted_date = due_date.strftime('%d/%m/%Y')
                print("Task list:")
                print(f'{num}) {title} - {description} - {formatted_date}')


    def remove_task(self):
        task_number = int(input("Please enter a number: "))
        if 0 < task_number <= len(self.tasks):
            del self.tasks[task_number-1]
            print(self.tasks)
        else:
            print("Incorrect task number")


    def retrieve_task(self):
        task_number = int(input("Please enter a number: "))
        if 0 < task_number <= len(self.tasks):
            print(self.tasks[task_number-1])
        else:
            print("Incorrect task number")


    def run(self):
        
        while True:
            select = input("Please enter A if you want to add a task,"
                        "Please enter V to view all tasks,"
                        "Please enter T to get a specific task,"
                        "Please enter D to delete a task,"
                        "Please enter Q to quit: ").lower()
        
        
            if select == "a":
                self.add_task()     
            elif select == "v":
                self.get_tasks()    
            elif select == "t":
                self.retrieve_task()
            elif select == "d":
                self.remove_task()
            elif select == "q":
                print("Goodbye")
                break
            
task_manager = TaskMaker()
# task_manager.run()

root = Tk()
root.title("Task Master")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

title = StringVar()
title_entry = ttk.Entry(mainframe, width=7, textvariable=title)
ttk.Label(mainframe, text="Task title: ").grid(column=1, row=1, sticky=(W, E))
title_entry.grid(column=2, row=1, sticky=(W, E))

description = StringVar()
desc_entry = ttk.Entry(mainframe, width=7, textvariable=description)
ttk.Label(mainframe, text="Task description: ").grid(column=1, row=2, sticky=(W, E))
desc_entry.grid(column=2, row=2, sticky=(W, E))

task_date = StringVar()
date_entry = ttk.Entry(mainframe, width=7, textvariable=task_date)
ttk.Label(mainframe, text="Task finish date(yyyy, mm, dd): ").grid(column=1, row=3, sticky=(W, E))
date_entry.grid(column=2, row=3, sticky=(W, E))

ttk.Button(mainframe, text="Save", command=task_manager.add_task()).grid(column=2, row=4)
ttk.Button(mainframe, text="View all", command=task_manager.get_tasks()).grid(column=1, row=5)
ttk.Button(mainframe, text="Search Task").grid(column=2, row=5)
ttk.Button(mainframe, text="Delete Task").grid(column=3, row=5)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
    
title_entry.focus()


# ttk.Label(mainframe, text="Enter your plan", command=task_manager.add_task())

root.mainloop()

