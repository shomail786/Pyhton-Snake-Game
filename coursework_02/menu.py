from tkinter import *
import sys, os



h = 720
w = 1280

mainMenu = Tk()
mainMenu.title("Main Menu ")

bgImage = PhotoImage(file="menubg.png")

canvas = Canvas(mainMenu, height=h, width=w)
canvas.pack()

bgLabel = Label(canvas, image=bgImage)
bgLabel.pack()




mainMenu.mainloop()
