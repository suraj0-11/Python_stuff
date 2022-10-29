from tkinter import *
food = ['pizza','burger','fries']

def order():
    if (x.get()==0):
        print("you ordered pizza")
    elif(x.get()==1):
        print("You ordered burger")
    elif(x.get()==2):
        print("You ordered fries")
    else:
        print("Huh?")

window = Tk()

x = IntVar()


for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],
                              fg = 'red',
                              bg = 'white',
                              font = ('Impact',50),
                              variable = x,
                              value = index,
                              relief=RAISED,
                              bd = 10,
                              indicatoron=0,
                              width=15,
                              command=order)
    radiobutton.pack(anchor=W)



window.mainloop()


