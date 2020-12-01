from tkinter import *
import sys, os

def restartProgram():
    print("Restarting")
    gameOverMenu.destroy()
    os.system("python3 snakeGame.py")

def menuWindow():
    gameOverMenu.destroy()
    os.system("python3 menu.py")

def resumeProgram():
    gameOverMenu.destroy()
    
    
def exitProgram():
    gameOverMenu.destroy()
    os._exit(0)

def saveGame():
    print("Saved")

def leaderWindow():
    print("Leaderbaords")

h = 600
w = 400

gameOverMenu = Tk()
gameOverMenu.title("Snek")

bgImage = PhotoImage(file="gameoverbg.png")

canvas = Canvas(gameOverMenu, height=h, width=w)
canvas.pack()

bgLabel = Label(canvas, image=bgImage)
bgLabel.pack()


mainMenuButton = Button(gameOverMenu, text="Main Menu", bg='black', fg='white', height=4, width=20, command= menuWindow)
mainMenuButton.place(x=105, y=115)

restartButton = Button(gameOverMenu, text="Restart", bg='black', fg='white', height=4, width=20, command= restartProgram)
restartButton.place(x=105, y=215)

leaderButton = Button(gameOverMenu, text="Leaderboards", bg='black', fg='white', height=4, width=20, command= leaderWindow)
leaderButton.place(x=105, y=315)

exitButton = Button(gameOverMenu, text="Exit", bg='black', fg='white', height=4, width=20, command= exitProgram)
exitButton.place(x=105, y=415)






gameOverMenu.mainloop()
