from tkinter import *
import sys, os

def gameWindow():
    mainMenu.destroy()
    os.system("python3 snakeGame.py")

def instructionWindow():
    print("How to play")

def leaderWindow():
    print("Leaderbaords")

def controlsWindow():
    print("Controls")

def loadGame():
    print("Load Game")

def exitProgram():
    os._exit(0)

h = 720
w = 1280

mainMenu = Tk()
mainMenu.title("Main Menu ")

bgImage = PhotoImage(file="menubg.png")

canvas = Canvas(mainMenu, height=h, width=w)
canvas.pack()

bgLabel = Label(canvas, image=bgImage)
bgLabel.pack()


playButton = Button(mainMenu, text="Play Game", bg='#e0b522', fg='white', height=2, width=20, command= gameWindow)
playButton.place(x=547.5, y=310)

leaderButton = Button(mainMenu, text="Leaderboards", bg='#e0b522', fg='white', height=2, width=20, command= leaderWindow)
leaderButton.place(x=547.5, y=360)

controlsButton = Button(mainMenu, text="Change Controls", bg='#e0b522', fg='white', height=2, width=20, command= controlsWindow)
controlsButton.place(x=547.5, y=410)

loadButton = Button(mainMenu, text="Load Game", bg='#e0b522', fg='white', height=2, width=20, command= loadGame)
loadButton.place(x=547.5, y=460)

insButton = Button(mainMenu, text="How to Play", bg='#e0b522', fg='white', height=2, width=20, command= instructionWindow)
insButton.place(x=547.5, y=510)

exitButton = Button(mainMenu, text="Exit", bg='#e0b522', fg='white', height=2, width=20, command= exitProgram)
exitButton.place(x=547.5, y=560)

mainMenu.mainloop()
