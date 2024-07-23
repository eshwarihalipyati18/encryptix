from tkinter import *
from tkinter import messagebox
my_tdl = Tk()
my_tdl.geometry('600x600')
my_tdl.title('To- Do  List Application')
my_tdl.config(bg='gray')
my_tdl.resizable(0,0)

tasks = []

def newTask():
    task = Entry.get()
    if task != "":
        tasks.append((task, False))  
        updateListBox()
        Entry.delete(0, "end")
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def updateTask():
    try:
        index = lb.curselection()[0]
        updated_task = Entry.get()
        if updated_task != "":
            tasks[index] = (updated_task, tasks[index][1])  
            updateListBox()
            Entry.delete(0, "end")
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")

def trackTask():
    try:
        index = lb.curselection()[0]
        task_name, task_status = tasks[index]
        if task_status:
            status = "The task has been successfully completed"
        else:
            status = "The task is not been completed yet"
        messagebox.showinfo("Task Status", f"Task '{task_name}' is {status}.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to track.")

def toggleTask(event):
    try:
        index = lb.nearest(event.y)  
        if lb.bbox(index):  
            tasks[index] = (tasks[index][0], not tasks[index][1]) 
            updateListBox()
    except IndexError:
        pass

def updateListBox():
    lb.delete(0, END)
    for task, completed in tasks:
        if completed:
            lb.insert(END, f'\u2713 {task}')  
        else:
            lb.insert(END, f'\u2610 {task}') 

frame = Frame(my_tdl)
frame.pack(pady=10)
button_frame = Frame(my_tdl)
button_frame.pack(pady=20)

lb = Listbox( frame,width=50,height=8,font=('Verdana', 18),bd=0,fg='black',highlightthickness=0, selectbackground='orange',activestyle="none",)
lb.pack(side=LEFT, fill=BOTH)

updateListBox()

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)
lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

Entry = Entry(my_tdl,font=('Verdana', 20))
Entry.pack(pady=20)

lb.bind("<Button-1>", toggleTask)


addTask_button = Button(button_frame,text='Add the Task',font=('Verdana 12'),bg='yellow',padx=20,pady=10,command=newTask)
addTask_button.pack(fill=BOTH, expand=True, side=LEFT)

updateTask_button = Button(button_frame,text='Update the Task',font=('Verdana 12'),bg='pink',padx=20,pady=10,command=updateTask)
updateTask_button.pack(fill=BOTH, expand=True, side=LEFT)

trackTask_button = Button(button_frame,text='Track the  Task',font=('Verdana 12'),bg='red',padx=20,pady=10,command=trackTask)
trackTask_button.pack(fill=BOTH, expand=True, side=LEFT)

my_tdl.mainloop()
