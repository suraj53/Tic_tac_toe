import tkinter
from tkinter import messagebox      # this is for messagebox i.e alert box(library file)
from tkinter import ttk


ActivePlayer = 1
p1 = []                  # this is space use for player 1
p2 = []                  # this is space use for player 2

root = tkinter.Tk()
root.title("tic tac toy :player 1")

bu1 = ttk.Button(root, text=' ')                                    # this is use for define the number of buttons (from 1 to 9)
bu1.grid(row=0, column=0, sticky='snew', ipadx=10, ipady=10)
bu1.config(command=lambda: ButtonClick(1))

bu2 = ttk.Button(root, text='')
bu2.grid(row=0, column=1, sticky='snew', ipadx=40, ipady=40)
bu2.config(command=lambda: ButtonClick(2))

bu3 = ttk.Button(root, text='')
bu3.grid(row=0, column=2, sticky='snew', ipadx=40, ipady=40)
bu3.config(command=lambda: ButtonClick(3))

bu4 = ttk.Button(root, text='')
bu4.grid(row=1, column=0, sticky='snew', ipadx=40, ipady=40)
bu4.config(command=lambda: ButtonClick(4))

bu5 = ttk.Button(root, text='')
bu5.grid(row=1, column=1, sticky='snew', ipadx=40, ipady=40)
bu5.config(command=lambda: ButtonClick(5))

bu6 = ttk.Button(root, text='')
bu6.grid(row=1, column=2, sticky='snew', ipadx=40, ipady=40)
bu6.config(command=lambda: ButtonClick(6))

bu7 = ttk.Button(root, text='')
bu7.grid(row=2, column=0, sticky='snew', ipadx=40, ipady=40)
bu7.config(command=lambda: ButtonClick(7))

bu8 = ttk.Button(root, text='')
bu8.grid(row=2, column=1, sticky='snew', ipadx=40, ipady=40)
bu8.config(command=lambda: ButtonClick(8))

bu9 = ttk.Button(root, text='')
bu9.grid(row=2, column=2, sticky='snew', ipadx=40, ipady=40)
bu9.config(command=lambda: ButtonClick(9))


def ButtonClick(id):                               # this is use for click id (i.e if we select button then x or 0 is printed
    global p1
    global p2
    global ActivePlayer
    if (ActivePlayer == 1):
        SetLayout(id, "X")
        p1.append(id)
        root.title("tic tac toy:player 2")
        ActivePlayer = 2
        print("p1:{}".format(p1))
    elif (ActivePlayer == 2):
        SetLayout(id, "0")
        p2.append(id)
        root.title("tic tac toy:player 1")
        ActivePlayer = 1
        print("p2:{}".format(p2))

    CheckWiner()


def SetLayout(id, PlayerSymbol):   # this function is use for button's id
    if id == 1:
        bu1.config(text=PlayerSymbol)
        bu1.state(['disabled'])
    elif id == 2:
        bu2.config(text=PlayerSymbol)
        bu2.state(['disabled'])
    elif id == 3:
        bu3.config(text=PlayerSymbol)
        bu3.state(['disabled'])
    elif id == 4:
        bu4.config(text=PlayerSymbol)
        bu4.state(['disabled'])
    elif id == 5:
        bu5.config(text=PlayerSymbol)
        bu5.state(['disabled'])
    elif id == 6:
        bu6.config(text=PlayerSymbol)
        bu6.state(['disabled'])
    elif id == 7:
        bu7.config(text=PlayerSymbol)
        bu7.state(['disabled'])
    elif id == 8:
        bu8.config(text=PlayerSymbol)
        bu8.state(['disabled'])
    elif id == 9:
        bu9.config(text=PlayerSymbol)
        bu9.state(['disabled'])


def CheckWiner():                         # this function is for check that who is the winer
    winer = -1
    if (1 in p1) and (2 in p1) and (3 in p1):
        winer = 1
    if (1 in p2) and (2 in p2) and (3 in p2):
        winer = 2

    if (4 in p1) and (5 in p1) and (6 in p1):
        winer = 1

    if (4 in p2) and (5 in p2) and (6 in p2):
        winer = 2

    if (7 in p1) and (8 in p1) and (9 in p1):
        winer = 1
    if (7 in p2) and (8 in p2) and (9 in p2):
        winer = 2


    if (1 in p1) and (4 in p1) and (7 in p1):
        winer = 1

    if (1 in p2) and (4 in p2) and (7 in p2):
        winer = 2


    if (2 in p1) and (5 in p1) and (8 in p1):
        winer = 1
    if (2 in p2) and (5 in p2) and (8 in p2):
        winer = 2


    if (3 in p1) and (6 in p1) and (9 in p1):
        winer = 1

    if (3 in p2) and (6 in p2) and (9 in p2):
        winer = 2

    if (1 in p1) and (5 in p1) and (9 in p1):
        winer = 1

    if (1 in p2) and (5 in p2) and (9 in p2):
        winer = 2



    if (3 in p1) and (5 in p1) and (7 in p1):
        winer = 1


    if (3 in p2) and (5 in p2) and (7 in p2):
        winer = 1

    if winer == 1:
        messagebox.showinfo(title="congratulations.", message="player 1 is the winner")

    elif winer == 2:
        messagebox.showinfo(title="congratulations.", message="player 2 is the winner")

root.mainloop()