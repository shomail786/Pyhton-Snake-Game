# Recommended Resolution: 1280x720
# All images are my own

# Imports all needed libraries
from tkinter import *
import sys
import os
import random
import time
from tkinter import messagebox

'''Function used to load the score from a previous saved game file'''


def loadFunction():

    def menuWindow():
        loadMenu.destroy()
        mMenu()

    def exitProgram():
        loadMenu.destroy()
        os._exit(0)

    # Takes user entered filename from input box and opens the file. Sets the
    # score to the score in the file.
    def loadGameProg():
        global score
        fileString = fileText.get()
        loadFile = open(fileString, 'r')
        scoreString = loadFile.read()
        print(scoreString)
        loadFile.close()
        score = int(scoreString)
        loadMenu.destroy()
        gameFunction()

    h = 450
    w = 400
    # Initialises Tkinter window
    loadMenu = Tk()
    loadMenu.title("Snek")

    # Creates canvas object, and places labels and buttons
    canvas = Canvas(loadMenu, bg='#e0b522', height=h, width=w)
    canvas.pack()

    titleLabel = Label(
        loadMenu,
        text="~LOAD~",
        font="Helevtica 48",
        bg='#e0b522',
        fg='white')
    titleLabel.place(x=60, y=30)

    nameLabel = Label(
        loadMenu,
        text="Enter filename",
        font="Helvetica 22",
        bg='#e0b522',
        fg='white')
    nameLabel.place(x=100, y=145)

    fileText = Entry(loadMenu, bg="white")
    fileText.place(x=95, y=200)

    submitButton = Button(
        loadMenu,
        text="Load",
        bg='#e0b522',
        fg='white',
        height=1,
        width=4,
        command=loadGameProg)
    submitButton.place(x=270, y=195)

    mainMenuButton = Button(
        loadMenu,
        text="Main Menu",
        bg='#e0b522',
        fg='white',
        height=3,
        width=20,
        command=menuWindow)
    mainMenuButton.place(x=105, y=260)

    exitButton = Button(
        loadMenu,
        text="Exit",
        bg='#e0b522',
        fg='white',
        height=3,
        width=20,
        command=exitProgram)
    exitButton.place(x=105, y=330)


'''Function used to save game to user specified file'''


def saveFunction():

    def menuWindow():
        saveMenu.destroy()
        mMenu()

    def exitProgram():
        saveMenu.destroy()
        os._exit(0)
    # Takes user entered filename from input box and saves the score to the
    # user's specified filename.

    def saveGameProg():
        global score
        scoreString = str(score)
        fileString = fileText.get()
        saveFile = open(fileString, 'w')
        saveFile.write(scoreString)
        saveFile.close()

    h = 450
    w = 400

    # Initialises Tkinter window, canvas and any labels and buttons
    saveMenu = Tk()
    saveMenu.title("Snek")

    canvas = Canvas(saveMenu, bg='#e0b522', height=h, width=w)
    canvas.pack()

    titleLabel = Label(
        saveMenu,
        text="~SAVE~",
        font="Helevtica 48",
        bg='#e0b522',
        fg='white')
    titleLabel.place(x=60, y=30)

    nameLabel = Label(
        saveMenu,
        text="Enter filename",
        font="Helvetica 22",
        bg='#e0b522',
        fg='white')
    nameLabel.place(x=100, y=145)

    fileText = Entry(saveMenu, bg="white")
    fileText.place(x=95, y=200)

    submitButton = Button(
        saveMenu,
        text="Save",
        bg='#e0b522',
        fg='white',
        height=1,
        width=4,
        command=saveGameProg)
    submitButton.place(x=270, y=195)

    mainMenuButton = Button(
        saveMenu,
        text="Main Menu",
        bg='#e0b522',
        fg='white',
        height=3,
        width=20,
        command=menuWindow)
    mainMenuButton.place(x=105, y=260)

    exitButton = Button(
        saveMenu,
        text="Exit",
        bg='#e0b522',
        fg='white',
        height=3,
        width=20,
        command=exitProgram)
    exitButton.place(x=105, y=330)


'''Used to display 5 top scores sorted in decsending order'''


def leaderboardFunction():

    def menuWindow():
        leaderWindow.destroy()
        mMenu()

    h = 720
    w = 1280
    # Initialises Tkinter window, canvas and any labels and buttons
    leaderWindow = Tk()
    leaderWindow.title("Snek")

    bgImage = PhotoImage(file="leaderboardbg.png")

    canvas = Canvas(leaderWindow, height=h, width=w)
    canvas.pack()

    background = canvas.create_image((0, 0), image=bgImage, anchor="nw")

    # Creates list to store scores collected from score file
    scores = []

    # Opens leaderboard file and loads scores and name into score list
    leaderboard = open("leaderboard.txt", "r")
    for line in leaderboard:
        scores.append(line.strip("\n").split(" "))

    for i in range(len(scores)):
        scores[i][1] = int(scores[i][1])

    # Sorts list by key of second value(Score), in descending order
    scores.sort(key=lambda x: x[1], reverse=True)

    # Displays scores on leaderboard page
    txt = "1: %s: %s" % (scores[0][0], str(scores[0][1]))
    canvas.create_text(
        650,
        250,
        fill="white",
        font="Helvetica 32 bold",
        text=txt)

    txt = "2: %s: %s" % (scores[1][0], str(scores[1][1]))
    canvas.create_text(
        650,
        300,
        fill="white",
        font="Helvetica 32 bold",
        text=txt)

    txt = "3: %s: %s" % (scores[2][0], str(scores[2][1]))
    canvas.create_text(
        650,
        350,
        fill="white",
        font="Helvetica 32 bold",
        text=txt)

    txt = "4: %s: %s" % (scores[3][0], str(scores[3][1]))
    canvas.create_text(
        650,
        400,
        fill="white",
        font="Helvetica 32 bold",
        text=txt)

    txt = "5: %s: %s" % (scores[4][0], str(scores[4][1]))
    canvas.create_text(
        650,
        450,
        fill="white",
        font="Helvetica 32 bold",
        text=txt)

    mainMenuButton = Button(
        leaderWindow,
        text="Main Menu",
        bg='#e0b522',
        fg='white',
        height=2,
        width=20,
        command=menuWindow)
    mainMenuButton.place(x=545, y=620)

    leaderWindow.mainloop()


'''Main function used to run snek game'''


def gameFunction():

    # Define functions to used arrow keys and wasd keys to control movement of
    # the snake
    def leftKey(event):
        global direction
        direction = "left"

    def rightKey(event):
        global direction
        direction = "right"

    def upKey(event):
        global direction
        direction = "up"

    def downKey(event):
        global direction
        direction = "down"

    def aKey(event):
        global direction
        direction = "left"

    def dKey(event):
        global direction
        direction = "right"

    def wKey(event):
        global direction
        direction = "up"

    def sKey(event):
        global direction
        direction = "down"

    # Opens boss window
    def bossWindow():
        window.destroy()
        bWindow()

    # Opens game over window
    def gameOverWindow():
        window.destroy()
        gMenu()

    # Opens pause menu
    def pauseWindow():
        if messagebox.askyesno("Paused", "Would you like to resume?"):
            pass

        else:
            window.destroy()
            pMenu()

    # Creates pause buttons
    def pauseButton():
        btnPause = Button(
            window,
            bg="#e0b522",
            image=pauseImage,
            width="40",
            height="40",
            command=lambda: pauseWindow())
        btnPause.place(x=45, y=45)

    # Creates and places food onto canvas at random coordinates
    def placeFood():
        global food, foodX, foodY
        food = canvas.create_rectangle(0, 0, snakeSize, snakeSize, fill="red")
        foodX = random.randint(0, width - snakeSize)
        foodY = random.randint(0, height - snakeSize)
        canvas.move(food, foodX, foodY)

    def bossKey(event):
        bossWindow()

    # Defines functions for increase speed, decrease speed and increase score
    # cheats
    def slowKey(event):
        global speed
        if speed < 85:
            speed += 1
        else:
            speed = 85

    def fastKey(event):
        global speed
        if speed > 5:
            speed -= 1
        else:
            speed = 6

    def scoreCheatKey(event):
        global score
        score += 100
        print(score)
        txt = "Score:" + str(score)
        canvas.itemconfigure(scoreText, text=txt)

    def escKey(event):
        pauseWindow()

    def setWindowDimensions(w, h):
        window = Tk()
        window.title("Snake Game")
        ws = window.winfo_screenwidth()
        hs = window.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        return window

    def moveFood():
        global food, foodX, foodY
        canvas.move(food, (foodX * (-1)), (foodY * (-1)))
        foodX = random.randint(0, width - snakeSize)
        foodY = random.randint(0, height - snakeSize)
        canvas.move(food, foodX, foodY)

    # Function to see if snake is colliding with itself
    def overlapping(a, b):
        if a[0] < b[2] and a[2] > b[0] and a[1] < b[3] and a[3] > b[1]:
            return True
        return False

    # Function used increaase snake size
    def growSnake():

        # Depending on direction, the snake increases either x1,x2,y1,y2
        # coordinates
        lastElement = len(snake) - 1
        lastElementPos = canvas.coords(snake[lastElement])
        snake.append(
            canvas.create_rectangle(
                0,
                0,
                snakeSize,
                snakeSize,
                fill="#FDF3F3"))
        if (direction == "left"):
            canvas.coords(snake[lastElement + 1],
                          lastElementPos[0] + snakeSize,
                          lastElementPos[1],
                          lastElementPos[2] + snakeSize,
                          lastElementPos[3])

        elif (direction == "right"):
            canvas.coords(snake[lastElement + 1],
                          lastElementPos[0] - snakeSize,
                          lastElementPos[1],
                          lastElementPos[2] - snakeSize,
                          lastElementPos[3])

        elif (direction == "up"):
            canvas.coords(snake[lastElement + 1],
                          lastElementPos[0],
                          lastElementPos[1] + snakeSize,
                          lastElementPos[2],
                          lastElementPos[3] + snakeSize)

        else:
            canvas.coords(snake[lastElement + 1],
                          lastElementPos[0],
                          lastElementPos[1] - snakeSize,
                          lastElementPos[2],
                          lastElementPos[3] - snakeSize)

        global score
        global speed

        # Increases score and increases speed as the snake grows
        score += 10
        speed -= 2
        txt = "Score:" + str(score)
        canvas.itemconfigure(scoreText, text=txt)

    # Used to move the snake across the canvas depending on user input
    def moveSnake():
        canvas.pack()
        positions = []
        positions.append(canvas.coords(snake[0]))
        if positions[0][0] < 0:
            canvas.coords(
                snake[0],
                width,
                positions[0][1],
                width - snakeSize,
                positions[0][3])

        elif positions[0][2] > width:
            canvas.coords(
                snake[0],
                0 - snakeSize,
                positions[0][1],
                0,
                positions[0][3])

        elif positions[0][3] > height:
            canvas.coords(
                snake[0],
                positions[0][0],
                0 - snakeSize,
                positions[0][2],
                0)

        elif positions[0][1] < 0:
            canvas.coords(
                snake[0],
                positions[0][0],
                height,
                positions[0][2],
                height - snakeSize)

        positions.clear()
        positions.append(canvas.coords(snake[0]))

        if direction == "left":
            canvas.move(snake[0], -snakeSize, 0)

        elif direction == "right":
            canvas.move(snake[0], snakeSize, 0)

        elif direction == "up":
            canvas.move(snake[0], 0, -snakeSize)

        elif direction == "down":
            canvas.move(snake[0], 0, snakeSize)
        sHeadPos = canvas.coords(snake[0])
        foodPos = canvas.coords(food)

        # Checks for collisions and increases snake size
        if overlapping(sHeadPos, foodPos):
            moveFood()
            growSnake()

        # Ends game if snake collides with its own body
        for i in range(1, len(snake)):
            if overlapping(sHeadPos, canvas.coords(snake[i])):
                gameOver = True
                gameOverWindow()

        for i in range(1, len(snake)):
            positions.append(canvas.coords(snake[i]))
        for i in range(len(snake) - 1):
            canvas.coords(snake[i + 1],
                          positions[i][0],
                          positions[i][1],
                          positions[i][2],
                          positions[i][3])

        # Increases speed if game is not finished
        if 'gameOver' not in locals():
            global speed
            window.after(speed, moveSnake)

    width = 1280
    height = 720

    # Initialises Tkinter window, canvas and any labels and buttons and
    # background image
    window = setWindowDimensions(width, height)

    bgImage = PhotoImage(file="gamebg.png")
    pauseImage = PhotoImage(width=40, height=40, file="pause.png")

    canvas = Canvas(window, width=1280, height=720)
    background = canvas.create_image((0, 0), image=bgImage, anchor="nw")
    canvas.pack()

    # Creates snake object and sets size to 15
    snake = []
    global snakeSize
    snakeSize = 15
    snake.append(
        canvas.create_rectangle(
            snakeSize,
            snakeSize,
            snakeSize * 2,
            snakeSize * 2,
            fill="#cfffe5"))

    txt = "Score:" + str(score)

    scoreText = canvas.create_text(
        width / 2,
        20,
        fill="white",
        font="Helvetica 18",
        text=txt)

    # Binds either arrow keys or wasd to the movement of the snake, depending
    # on the control scheme set by the user
    global arrows
    if arrows == True:
        canvas.bind("<Left>", leftKey)
        canvas.bind("<Right>", rightKey)
        canvas.bind("<Up>", upKey)
        canvas.bind("<Down>", downKey)

    else:
        canvas.bind("<a>", aKey)
        canvas.bind("<d>", dKey)
        canvas.bind("<w>", wKey)
        canvas.bind("<s>", sKey)

    # Binds boss key and cheat keys
    canvas.bind("<Escape>", escKey)
    canvas.bind("<b>", bossKey)
    canvas.bind("<j>", slowKey)
    canvas.bind("<k>", fastKey)
    canvas.bind("<l>", scoreCheatKey)
    canvas.focus_set()

    pauseButton()
    placeFood()
    moveSnake()
    window.mainloop()


'''Function used to initialise and display the pause menu'''


def pMenu():
    def restartProgram():
        print("Restarting")
        pauseMenu.destroy()
        global score
        global speed
        score = 0
        speed = 70
        gameFunction()

    def menuWindow():
        pauseMenu.destroy()
        mMenu()

    def exitProgram():
        pauseMenu.destroy()
        os._exit(0)

    def saveGame():
        pauseMenu.destroy()
        saveFunction()

    def leaderWindow():
        pauseMenu.destroy()
        leaderboardFunction()

    h = 600
    w = 400

    # Initialises Tkinter window, canvas and any labels and buttons and images
    pauseMenu = Tk()
    pauseMenu.title("Snek")

    global pause
    pauseBgImage = PhotoImage(file="pausebg.gif")

    canvas = Canvas(pauseMenu, height=h, width=w)

    canvas.pack()

    bgPause = Label(pauseMenu, image=pauseBgImage)
    bgPause.place(x=0, y=0)

    mainMenuButton = Button(
        pauseMenu,
        text="Main Menu",
        bg='#e0b522',
        fg='white',
        height=2,
        width=20,
        command=menuWindow)
    mainMenuButton.place(x=105, y=175)

    saveButton = Button(
        pauseMenu,
        text="Save",
        bg='#e0b522',
        fg='white',
        height=2,
        width=20,
        command=saveGame)
    saveButton.place(x=105, y=240)

    leaderButton = Button(
        pauseMenu,
        text="Leaderboards",
        bg='#e0b522',
        fg='white',
        height=2,
        width=20,
        command=leaderWindow)
    leaderButton.place(x=105, y=305)

    restartButton = Button(
        pauseMenu,
        text="Restart",
        bg='#e0b522',
        fg='white',
        height=2,
        width=20,
        command=restartProgram)
    restartButton.place(x=105, y=370)

    exitButton = Button(
        pauseMenu,
        text="Exit",
        bg='#e0b522',
        fg='white',
        height=2,
        width=20,
        command=exitProgram)
    exitButton.place(x=105, y=435)

    pauseMenu.mainloop()


'''Allows for changing of controls'''


def cWindow():

    def menuWindow():
        controlWindow.destroy()
        mMenu()

    # Set arrows boolean to true or false based on control scheme selected by
    # the user
    def wasdControls():
        global arrows
        arrows = False

    def arrowControls():
        global arrows
        arrows = True

    h = 600
    w = 400

    # Initialises Tkinter window, canvas and any labels and buttons and images
    controlWindow = Tk()
    controlWindow.title("Snek")

    bgImage = PhotoImage(file="changecontrols.png")

    canvas = Canvas(controlWindow, height=h, width=w)
    canvas.pack()

    bgLabel = Label(canvas, image=bgImage)
    bgLabel.pack()

    mainMenuButton = Button(
        controlWindow,
        text="Main Menu",
        bg='#e0b522',
        fg='white',
        height=2,
        width=20,
        command=menuWindow)
    mainMenuButton.place(x=545, y=620)

    wasdButton = Button(
        controlWindow,
        text="WASD",
        bg='#e0b522',
        fg='white',
        height=2,
        width=10,
        command=wasdControls)
    wasdButton.place(x=810, y=510)

    arrowButton = Button(
        controlWindow,
        text='Arrow Keys',
        bg='#e0b522',
        fg='white',
        height=2,
        width=10,
        command=arrowControls)
    arrowButton.place(x=810, y=270)

    controlWindow.mainloop()


'''Function used to initialise and show the game over menu'''


def gMenu():
    def restartProgram():
        print("Restarting")
        gameOverMenu.destroy()
        global score
        global speed
        score = 0
        speed = 70
        gameFunction()

    def menuWindow():
        gameOverMenu.destroy()
        mMenu()

    def resumeProgram():
        gameOverMenu.destroy()

    def exitProgram():
        gameOverMenu.destroy()
        os._exit(0)

    def saveGame():
        gameOverMenu.destroy()
        saveFunction()

    def leaderWindow():
        leaderboardFunction()
    
    # Opens leaderboard file and saves user inputted name and score

    def saveLeaderBoard():
        global score
        scoreString = str(score)
        nameString = nameText.get()
        leaderboardFile = open("leaderboard.txt", 'a')
        leaderboardFile.write(nameString + " " + scoreString + '\n')
        leaderboardFile.close()

    h = 600
    w = 400

    # Initialises Tkinter window, canvas and any labels and buttons and images
    gameOverMenu = Tk()
    gameOverMenu.title("Snek")

    bgImage = PhotoImage(file="gameoverbg.png")

    canvas = Canvas(gameOverMenu, height=h, width=w)
    canvas.pack()

    bgLabel = Label(canvas, image=bgImage)
    bgLabel.pack()

    nameLabel = Label(
        gameOverMenu,
        text="Enter Name",
        font="Helvtica",
        bg="white")
    nameLabel.place(x=150, y=115)

    nameText = Entry(gameOverMenu, bg="white",)
    nameText.place(x=95, y=160)

    submitButton = Button(
        gameOverMenu,
        text="Submit",
        bg='#e0b522',
        fg='white',
        height=1,
        width=4,
        command=saveLeaderBoard)
    submitButton.place(x=270, y=155)

    mainMenuButton = Button(
        gameOverMenu,
        text="Main Menu",
        bg='#e0b522',
        fg='white',
        height=3,
        width=20,
        command=menuWindow)
    mainMenuButton.place(x=105, y=230)

    restartButton = Button(
        gameOverMenu,
        text="Restart",
        bg='#e0b522',
        fg='white',
        height=3,
        width=20,
        command=restartProgram)
    restartButton.place(x=105, y=305)

    leaderButton = Button(
        gameOverMenu,
        text="Leaderboards",
        bg='#e0b522',
        fg='white',
        height=3,
        width=20,
        command=leaderWindow)
    leaderButton.place(x=105, y=380)

    exitButton = Button(
        gameOverMenu,
        text="Exit",
        bg='#e0b522',
        fg='white',
        height=3,
        width=20,
        command=exitProgram)
    exitButton.place(x=105, y=455)

    gameOverMenu.mainloop()


'''Displays the 'how to play' window'''


def iWindow():

    def menuWindow():
        instructionWindow.destroy()
        mMenu()

    h = 600
    w = 400

    # Initialises Tkinter window, canvas and any labels and buttons and iamges
    instructionWindow = Tk()
    instructionWindow.title("Snek")

    bgImage = PhotoImage(file="instructions.png")

    canvas = Canvas(instructionWindow, height=h, width=w)
    canvas.pack()

    bgLabel = Label(canvas, image=bgImage)
    bgLabel.pack()

    mainMenuButton = Button(
        instructionWindow,
        text="Main Menu",
        bg='#e0b522',
        fg='white',
        height=2,
        width=20,
        command=menuWindow)
    mainMenuButton.place(x=530, y=620)

    instructionWindow.mainloop()


'''Main menu funtion - runs first when program starts, 
   links to different parts of the program'''


def mMenu():
    def gameWindow():
        mainMenu.destroy()
        gameFunction()

    def instructionWindow():
        mainMenu.destroy()
        iWindow()

    def leaderWindow():
        mainMenu.destroy()
        leaderboardFunction()

    def controlsWindow():
        mainMenu.destroy()
        cWindow()

    def loadGame():
        mainMenu.destroy()
        loadFunction()

    def exitProgram():
        os._exit(0)

    def bossKey(event):
        mainMenu.destroy()
        bWindow()

    h = 720
    w = 1280

    # Initialises Tkinter window, canvas and any labels and buttons and images
    mainMenu = Tk()
    mainMenu.title("Main Menu ")

    bgImage = PhotoImage(file="menubg.png")

    canvas = Canvas(mainMenu, height=h, width=w)
    canvas.pack()

    bgLabel = Label(canvas, image=bgImage)
    bgLabel.pack()

    playButton = Button(
        mainMenu,
        text="Play Game",
        bg='#e0b522',
        fg='white',
        height=2,
        width=20,
        command=gameWindow)
    playButton.place(x=547.5, y=310)

    leaderButton = Button(
        mainMenu,
        text="Leaderboards",
        bg='#e0b522',
        fg='white',
        height=2,
        width=20,
        command=leaderWindow)
    leaderButton.place(x=547.5, y=360)

    controlsButton = Button(
        mainMenu,
        text="Change Controls",
        bg='#e0b522',
        fg='white',
        height=2,
        width=20,
        command=controlsWindow)
    controlsButton.place(x=547.5, y=410)

    loadButton = Button(
        mainMenu,
        text="Load Game",
        bg='#e0b522',
        fg='white',
        height=2,
        width=20,
        command=loadGame)
    loadButton.place(x=547.5, y=460)

    insButton = Button(
        mainMenu,
        text="How to Play",
        bg='#e0b522',
        fg='white',
        height=2,
        width=20,
        command=instructionWindow)
    insButton.place(x=547.5, y=510)

    exitButton = Button(
        mainMenu,
        text="Exit",
        bg='#e0b522',
        fg='white',
        height=2,
        width=20,
        command=exitProgram)
    exitButton.place(x=547.5, y=560)

    canvas.bind("<b>", bossKey)

    mainMenu.mainloop()


'''When B key is pressed, this function is called to open the boss window'''


def bWindow():
    def menuWindow():
        bossWindow.destroy()
        mMenu()

    h = 600
    w = 400

    # Initialises Tkinter window, canvas and any labels and buttons and images
    bossWindow = Tk()
    bossWindow.title("Snek")

    bgImage = PhotoImage(file="boss.png")

    canvas = Canvas(bossWindow, height=h, width=w)
    canvas.pack()

    bgLabel = Label(canvas, image=bgImage)
    bgLabel.pack()

    mainMenuButton = Button(
        bossWindow,
        text="Main Menu",
        bg='#FFFFFF',
        fg='black',
        height=2,
        width=20,
        command=menuWindow)
    mainMenuButton.place(x=545, y=620)

    bossWindow.mainloop()

# Stores variables that are in global scope and calls main menu function
pause = True
direction = "right"
snakeSize = 15
score = 0
speed = 70
arrows = True
mMenu()
