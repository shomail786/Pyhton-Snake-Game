from tkinter import *
import sys, os



h = 600
w = 400

gameOverMenu = Tk()
gameOverMenu.title("Snek")

bgImage = PhotoImage(file="gameoverbg.png")

canvas = Canvas(gameOverMenu, height=h, width=w)
canvas.pack()

bgLabel = Label(canvas, image=bgImage)
bgLabel.pack()









gameOverMenu.mainloop()
