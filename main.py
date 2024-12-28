from tkinter import *

win = Tk()
win.title("Age App")
win.geometry("500x500")
frame = Frame(master=win, height=200, width=360, bg="blue")

lbl1 = Label(frame, text="Name", bg="yellow", width=12)
lbl2 = Label(frame, text="Age", bg="yellow", width=12)

name_entry = Entry(frame)
age_entry = Entry(frame)

def display():
    name = name_entry.get()
    age = age_entry.get()
    if name and age:
        textbox.delete("1.0", END)  
        greet = f"Hey {name},\n"
        message = f"Your age is {age}. Thanks for the information!"
        textbox.insert(END, greet)
        textbox.insert(END, message)
    else:
        textbox.delete("1.0", END) 
        textbox.insert(END, "Please enter both Name and Age!")

textbox = Text(win, bg="gray", fg="black", height=10, width=50)
btn = Button(text="Save", command=display, bg="green")
frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=80)
age_entry.place(x=150, y=80)
btn.place(x=130, y=210)
textbox.place(x=20, y=250)

win.mainloop()
