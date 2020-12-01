from tkinter import *
import sys, os

def menuWindow():
    bossWindow.destroy()
    os.system("python3 menu.py")

h = 600
w = 400

bossWindow = Tk()
bossWindow.title("Snek")

bgImage = PhotoImage(file="boss.png")

canvas = Canvas(bossWindow, height=h, width=w)
canvas.pack()

bgLabel = Label(canvas, image=bgImage)
bgLabel.pack()


mainMenuButton = Button(bossWindow, text="Main Menu", bg='#e0b522', fg='white', height=2, width=20, command= menuWindow)
mainMenuButton.place(x=530, y=620)


bossWindow.mainloop()
