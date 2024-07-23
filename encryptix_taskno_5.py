from tkinter import *
contact_book = Tk() 
contact_book.geometry('500x500') 
contact_book.config(bg='lightblue')
contact_book.resizable(0, 0)
contact_book.title("Contact Book")

user_name = StringVar() 
phone_number = StringVar() 
email_address = StringVar() 

frame = Frame(contact_book, bg='gray') 
frame.pack(pady=5)

frame1 = Frame(contact_book, bg='gray')
frame1.pack(pady=5)

frame2 = Frame(contact_book, bg='gray')
frame2.pack(pady=5)

Label(frame, text='Name', font='Verdana 10 bold').pack(side=LEFT) 
Entry(frame, textvariable=user_name, width=40).pack(pady=5) 

Label(frame1, text='Phone No.', font='Verdana 10 bold').pack(side=LEFT) 
Entry(frame1, textvariable=phone_number, width=25).pack(pady=5, padx=10, side=LEFT) 

Label(frame1, text='Email id.', font='Verdana 10 bold').pack(side=LEFT) 
Entry(frame1, textvariable=email_address, width=40).pack(pady=5, padx=5, side=LEFT) 

Label(frame2, text='Address', font='Verdana 10 bold').pack(side=LEFT) 
address = Text(frame2, width=37, height=10, bg='white') 
address.pack(pady=5)


scroll_bar = Scrollbar(contact_book, orient=VERTICAL)
scroll_bar.pack(side=RIGHT, fill=Y)

select = Listbox(contact_book, yscrollcommand=scroll_bar.set, height=14, width=60) 
scroll_bar.config(command=select.yview)
select.pack(side=RIGHT, fill=BOTH)


def add_entry():
    if user_name.get() and phone_number.get() and address.get("1.0", END).strip():
       entry = f"{user_name.get()} | {phone_number.get()} | {email_address.get()} | {address.get('1.0', END).strip()}"
       select.insert(END, entry)


def view_entry():
    selected = select.curselection()
    if selected:
       entry = select.get(selected)
       name, number, email, addr = entry.split(" | ")
       user_name.set(name)
       phone_number.set(number)
       email_address.set(email)
       address.delete("1.0", END)
       address.insert(END, addr)
       
def messagebox(title, message, box_type="info"):
    
    if box_type == "info":
        messagebox.showinfo(title, message)
    elif box_type == "warning":
        messagebox.showwarning(title, message)
    elif box_type == "error":
        messagebox.showerror(title, message)
    else:
        raise ValueError("Invalid message box type")

def search_fields():
    search_term = user_name.get().strip().lower()  
    found = False
    for index in range(select.size()):
        entry = select.get(index)
        if search_term in entry.lower():  
            select.selection_clear(0, END) 
            select.selection_set(index) 
            select.activate(index)  
            select.see(index)  
            messagebox("Found", f"Found '{entry}'", "info")
            found = True
            break  

    if not found:
        messagebox("Not Found", f"Could not find '{search_term}'", "warning")

def update_entry():
    selected = select.curselection()
    if selected:
        index = selected[0]
        if user_name.get() and phone_number.get() and address.get("1.0", END).strip():
           entry = f"{user_name.get()} | {phone_number.get()} | {email_address.get()} | {address.get('1.0', END).strip()}"
           select.delete(index)  
           select.insert(index, entry)  


def delete_entry():
    selected = select.curselection()
    if selected:
       index = selected[0]
       select.delete(index)


Button(contact_book, text="Add", font="Verdana 10 bold",bg='blue', command=add_entry).place(x=40, y=250) 
Button(contact_book, text="View", font=" Verdana 10 bold ",bg='green', command=view_entry).place(x=40, y=300) 
Button(contact_book, text="Search", font="Verdana 10 bold ",bg='orange', command=search_fields).place(x=40, y=350) 
Button(contact_book, text="Update", font="Verdana 10  bold" ,bg='yellow', command=update_entry).place(x=40, y=390) 
Button(contact_book, text="Delete", font="Verdana 10 bold", bg='light green', command=delete_entry).place(x=30, y=430) 

contact_book.mainloop()
