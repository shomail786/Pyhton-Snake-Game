from tkinter import *
import sys, os



h = 600
w = 400

pauseMenu = Tk()
pauseMenu.title("Snek")

bgImage = PhotoImage(file="pausebg.png")

canvas = Canvas(pauseMenu, height=h, width=w)
canvas.pack()

bgLabel = Label(canvas, image=bgImage)
bgLabel.pack()


resumeButton = Button(pauseMenu, text="Resume", bg='black', fg='white', height=3, width=20, command= resumeProgram)
resumeButton.place(x=105, y=110)

mainMenuButton = Button(pauseMenu, text="Main Menu", bg='black', fg='white', height=3, width=20, command= menuWindow)
mainMenuButton.place(x=105, y=185)

saveButton = Button(pauseMenu, text="Save", bg='black', fg='white', height=3, width=20, command= saveGame)
saveButton.place(x=105, y=260)

leaderButton = Button(pauseMenu, text="Leaderboards", bg='black', fg='white', height=3, width=20, command= leaderWindow)
leaderButton.place(x=105, y=335)

restartButton = Button(pauseMenu, text="Restart", bg='black', fg='white', height=3, width=20, command= restartProgram)
restartButton.place(x=105, y=410)

exitButton = Button(pauseMenu, text="Exit", bg='black', fg='white', height=3, width=20, command= exitProgram)
exitButton.place(x=105, y=485)





pauseMenu.mainloop()
