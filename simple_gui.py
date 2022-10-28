from tkinter import *

count = 0
def submit():
    name = entry.get()
    print("Hi "+ name)
    global count
    count += 1
    print(count)

def delete():
    entry.delete(0, END)
    print("Deleted Everything lol")

def backspace():
    entry.delete(len(entry.get())-1,END)

window = Tk()

entry = Entry(window,
              font = ('arial',50),
              fg = 'Light Green',
              bg = 'Black')
entry.pack(side = LEFT)

submit_button = Button(window, text = "Submit",command = submit, relief=RAISED, bd = 10)
submit_button.pack(side = RIGHT)

delete_button = Button(window, text = "Delete",command = delete, relief=RAISED, bd = 10)
delete_button.pack(side = RIGHT)

backspace_button = Button(window, text = "Backspace",command = backspace, relief=RAISED, bd = 10)
backspace_button.pack(side = RIGHT)


window.mainloop()


