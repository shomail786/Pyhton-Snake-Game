# Game Resolution: 1280 X 720

from tkinter import *
import random, time, sys, os

def gameOverWindow():
    window.destroy()
    os.system("python3 gameOverMenu.py")

def pauseWindow():
    os.system("python3 pauseMenu.py")




def setWindowDimensions(w,h):
    window = Tk()
    window.title("Snake Game")
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    return window


    



width = 1280
height = 720


window = setWindowDimensions(width, height)

bgImage = PhotoImage(file="gamebg.png")
pauseImage = PhotoImage(width = 40, height = 40, file="pause.png")


window.mainloop()

