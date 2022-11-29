# Import the library
from tkinter import *
import time
import multiprocessing

# Create an instance of window
win = Tk()

# Set the geometry of the window
win.geometry("350x500")

# Title of the window
win.title("Sunete v1.0.0")

# Lectia 1
label1 = Label(win, text="Lecția 1:")
entry1 = Entry(win)
entry1.insert(0,"8:00:00")
entry2 = Entry(win)
entry2.insert(0,"8:45:00")

# Lectia 2
label2 = Label(win, text="Lecția 2:")
entry3 = Entry(win)
entry3.insert(0,"9:00:00")
entry4 = Entry(win)
entry4.insert(0,"9:45:00")

# Lectia 3
label3 = Label(win, text="Lecția 3:")
entry5 = Entry(win)
entry5.insert(0,"9:55:00")
entry6 = Entry(win)
entry6.insert(0,"10:40:00")


# Lectia 4
label4 = Label(win, text="Lecția 4:")
entry7 = Entry(win)
entry7.insert(0,"11:00:00")
entry8 = Entry(win)
entry8.insert(0,"11:45:00")


# Lectia 5
label5 = Label(win, text="Lecția 5:")
entry9 = Entry(win)
entry9.insert(0,"11:55:00")
entry10 = Entry(win)
entry10.insert(0,"12:40:00")


# Lectia 6
label6 = Label(win, text="Lecția 6:")
entry11 = Entry(win)
entry11.insert(0,"12:50:00")
entry12 = Entry(win)
entry12.insert(0,"13:35:00")


# Lectia 7
label7 = Label(win, text="Lecția 7:")
entry13 = Entry(win)
entry13.insert(0,"13:45:00")
entry14 = Entry(win)
entry14.insert(0,"14:30:00")

# Recreatia
label8 = Label(win, text="La ce recreatie sa cante playlist-ul?")
entry15 = Entry(win)
entry15.insert(0,"3")

# Lectia 1
label1.pack()
entry1.pack()
entry2.pack()

# Lectia 2
label2.pack()
entry3.pack()
entry4.pack()

# Lectia 3
label3.pack()
entry5.pack()
entry6.pack()

# Lectia 4
label4.pack()
entry7.pack()
entry8.pack()

# Lectia 5
label5.pack()
entry9.pack()
entry10.pack()

# Lectia 6
label6.pack()
entry11.pack()
entry12.pack()

# Lectia 7
label7.pack()
entry13.pack()
entry14.pack()

# Recreatia
label8.pack()
entry15.pack()


def startButton():
    entry1.config(state= "disabled")
    entry2.config(state= "disabled")
    entry3.config(state= "disabled")
    entry4.config(state= "disabled")
    entry5.config(state= "disabled")
    entry6.config(state= "disabled")
    entry7.config(state= "disabled")
    entry8.config(state= "disabled")
    entry9.config(state= "disabled")
    entry10.config(state= "disabled")
    entry11.config(state= "disabled")
    entry12.config(state= "disabled")
    entry13.config(state= "disabled")
    entry14.config(state= "disabled")
    replaceButton()

start = Button(win, text= "Start", command=startButton)
start.pack()
start.place(x=160,y=465)

def replaceButton():
    start.place_forget()
    stop = Button(win, text= "Stop", command=stopButton)
    stop.pack()
    stop.place(x=160,y=465)

def stopButton():
    entry1.config(state= "normal")
    entry2.config(state= "normal")
    entry3.config(state= "normal")
    entry4.config(state= "normal")
    entry5.config(state= "normal")
    entry6.config(state= "normal")
    entry7.config(state= "normal")
    entry8.config(state= "normal")
    entry9.config(state= "normal")
    entry10.config(state= "normal")
    entry11.config(state= "normal")
    entry12.config(state= "normal")
    entry13.config(state= "normal")
    entry14.config(state= "normal")
    start = Button(win, text= "Start", command=startButton)
    start.pack()
    start.place(x=160,y=465)


win.mainloop()