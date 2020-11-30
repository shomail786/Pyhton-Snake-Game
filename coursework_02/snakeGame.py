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

canvas = Canvas(window, width=1280, height=720)
background = canvas.create_image((0,0), image = bgImage, anchor = "nw")
canvas.pack()


snake = []
snakeSize = 15
snake.append(canvas.create_rectangle(snakeSize,snakeSize, snakeSize * 2, snakeSize * 2, fill="white" ))


score = 0
txt = "Score:" + str(score)

scoreText = canvas.create_text( width/2 , 20 , fill="white" , font="Helvetica 18", text=txt)

canvas.bind("<Left>", leftKey) 
canvas.bind("<Right>", rightKey)
canvas.bind("<Up>", upKey)
canvas.bind("<Down>", downKey)
canvas.bind("<Escape>", escKey)
canvas.focus_set()

direction = "right"




window.mainloop()

