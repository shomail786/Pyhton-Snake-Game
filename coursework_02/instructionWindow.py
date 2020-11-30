from tkinter import *
import sys, os

def menuWindow():
    instructionWindow.destroy()
    os.system("python3 menu.py")

h = 600
w = 400

instructionWindow = Tk()
instructionWindow.title("Snek")

bgImage = PhotoImage(file="instructions.png")

canvas = Canvas(instructionWindow, height=h, width=w)
canvas.pack()

bgLabel = Label(canvas, image=bgImage)
bgLabel.pack()


mainMenuButton = Button(instructionWindow, text="Main Menu", bg='#e0b522', fg='white', height=2, width=20, command= menuWindow)
mainMenuButton.place(x=530, y=620)


instructionWindow.mainloop()
