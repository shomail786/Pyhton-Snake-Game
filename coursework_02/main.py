from tkinter import *
import sys, os, random, time
from tkinter import messagebox

def loadFunction():
    
    def menuWindow():
        loadMenu.destroy()
        mMenu()
                
    def exitProgram():
        loadMenu.destroy()
        os._exit(0)

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

    loadMenu = Tk()
    loadMenu.title("Snek")


    canvas = Canvas(loadMenu, bg='#e0b522', height=h, width=w)
    canvas.pack()

    
    titleLabel =Label(loadMenu, text="~LOAD~", font="Helevtica 48", bg='#e0b522', fg='white')
    titleLabel.place(x=60, y=30)
    
    nameLabel =Label(loadMenu, text="Enter filename", font="Helvetica 22", bg='#e0b522', fg='white')
    nameLabel.place(x=100, y=145)

    fileText = Entry(loadMenu, bg="white")
    fileText.place(x=95, y=200)

    submitButton = Button(loadMenu, text="Load", bg='#e0b522', fg='white', height=1, width=4, command= loadGameProg)
    submitButton.place(x=270, y=195)

    mainMenuButton = Button(loadMenu, text="Main Menu", bg='#e0b522', fg='white', height=3, width=20, command= menuWindow)
    mainMenuButton.place(x=105, y=260)

    exitButton = Button(loadMenu, text="Exit", bg='#e0b522', fg='white', height=3, width=20, command= exitProgram)
    exitButton.place(x=105, y=330)


def saveFunction():
     
    def menuWindow():
        saveMenu.destroy()
        mMenu()
                
    def exitProgram():
        saveMenu.destroy()
        os._exit(0)

    def saveGameProg():
        global score
        scoreString = str(score)
        fileString = fileText.get()
        saveFile = open(fileString, 'w')
        saveFile.write(scoreString)
        saveFile.close()

    h = 450
    w = 400

    saveMenu = Tk()
    saveMenu.title("Snek")


    canvas = Canvas(saveMenu, bg='#e0b522', height=h, width=w)
    canvas.pack()

    titleLabel =Label(saveMenu, text="~SAVE~", font="Helevtica 48", bg='#e0b522', fg='white')
    titleLabel.place(x=60, y=30)
    
    nameLabel =Label(saveMenu, text="Enter filename", font="Helvetica 22", bg='#e0b522', fg='white')
    nameLabel.place(x=100, y=145)

    fileText = Entry(saveMenu, bg="white")
    fileText.place(x=95, y=200)

    submitButton = Button(saveMenu, text="Save", bg='#e0b522', fg='white', height=1, width=4, command= saveGameProg)
    submitButton.place(x=270, y=195)

    mainMenuButton = Button(saveMenu, text="Main Menu", bg='#e0b522', fg='white', height=3, width=20, command= menuWindow)
    mainMenuButton.place(x=105, y=260)

    exitButton = Button(saveMenu, text="Exit", bg='#e0b522', fg='white', height=3, width=20, command= exitProgram)
    exitButton.place(x=105, y=330)


def leaderboardFunction():
    
    def menuWindow():
        leaderWindow.destroy()
        mMenu()

    h = 720
    w = 1280

    leaderWindow = Tk()
    leaderWindow.title("Snek")

    bgImage = PhotoImage(file="leaderboardbg.png")

    canvas = Canvas(leaderWindow, height=h, width=w)
    canvas.pack()

    background = canvas.create_image((0,0), image = bgImage, anchor = "nw")

    scores = []

    leaderboard = open("leaderboard.txt", "r")
    for line in leaderboard:
        scores.append(line.strip("\n").split(" "))

    for i in range(len(scores)):
        scores[i][1] = int(scores[i][1])

    scores.sort(key=lambda x: x[1], reverse=True)

    txt = "1: %s: %s" % (scores[0][0], str(scores[0][1]))
    canvas.create_text(650, 250, fill="white", font="Helvetica 32 bold", text=txt)

    txt = "2: %s: %s" % (scores[1][0], str(scores[1][1]))
    canvas.create_text(650, 300, fill="white", font="Helvetica 32 bold", text=txt)

    txt = "3: %s: %s" % (scores[2][0], str(scores[2][1]))
    canvas.create_text(650, 350, fill="white", font="Helvetica 32 bold", text=txt)

    txt = "4: %s: %s" % (scores[3][0], str(scores[3][1]))
    canvas.create_text(650, 400, fill="white", font="Helvetica 32 bold", text=txt)

    txt = "5: %s: %s" % (scores[4][0], str(scores[4][1]))
    canvas.create_text(650, 450, fill="white", font="Helvetica 32 bold", text=txt)

    

    mainMenuButton = Button(leaderWindow, text="Main Menu", bg='#e0b522', fg='white', height=2, width=20, command= menuWindow)
    mainMenuButton.place(x=545, y=620)


    leaderWindow.mainloop()


def gameFunction():

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

    def bossWindow():
        window.destroy()
        bWindow()

    def gameOverWindow():
        window.destroy()
        gMenu()
    
    
    
    def pauseWindow(): 
        if messagebox.askyesno("Paused", "Would you like to resume?"):
            pass

        else:
            window.destroy()
            pMenu()

    def pauseButton():
        btnPause = Button(window, bg="#e0b522", image=pauseImage, width="40", height="40", command= lambda: pauseWindow())
        btnPause.place(x=45,y=45)

    def placeFood():
        global food, foodX, foodY
        food = canvas.create_rectangle(0,0, snakeSize, snakeSize, fill="steel blue")
        foodX = random.randint(0,width-snakeSize)
        foodY = random.randint(0, height-snakeSize)
        canvas.move(food, foodX, foodY)

    def bossKey(event):
        bossWindow()

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

    

    def setWindowDimensions(w,h):
        window = Tk()
        window.title("Snake Game")
        ws = window.winfo_screenwidth()
        hs = window.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        return window

    def moveFood():
        global food, foodX, foodY
        canvas.move(food, (foodX*(-1)), (foodY*(-1)))
        foodX = random.randint(0,width-snakeSize)
        foodY = random.randint(0,height-snakeSize)
        canvas.move(food, foodX, foodY)

    def overlapping(a,b):
        if a[0] < b[2] and a[2] > b[0] and a[1] < b[3] and a[3] > b[1]:
            return True
        return False
        
    def growSnake():
        lastElement = len(snake)-1
        lastElementPos = canvas.coords(snake[lastElement])
        snake.append(canvas.create_rectangle(0,0, snakeSize,snakeSize,fill="#FDF3F3"))
        if (direction == "left"):
            canvas.coords(snake[lastElement+1],lastElementPos[0]+snakeSize, lastElementPos[1],lastElementPos[2]+snakeSize,lastElementPos[3])
        
        elif (direction == "right"):
            canvas.coords(snake[lastElement+1],lastElementPos[0]-snakeSize, lastElementPos[1],lastElementPos[2]-snakeSize,lastElementPos[3])

        elif (direction == "up"):
            canvas.coords(snake[lastElement+1],lastElementPos[0], lastElementPos[1]+snakeSize,lastElementPos[2],lastElementPos[3]+snakeSize)

        else:
            canvas.coords(snake[lastElement+1],lastElementPos[0], lastElementPos[1]-snakeSize,lastElementPos[2],lastElementPos[3]-snakeSize)

        global score
        global speed
        score += 10
        speed -= 1
        txt = "Score:" + str(score)
        canvas.itemconfigure(scoreText, text=txt)

    def moveSnake():
        canvas.pack()
        positions = []
        positions.append(canvas.coords(snake[0]))
        if positions[0][0] < 0:
            canvas.coords(snake[0],width,positions[0][1],width-snakeSize,positions[0][3])
        
        elif positions[0][2] > width:
            canvas.coords(snake[0],0-snakeSize, positions[0][1],0,positions[0][3])
        
        elif positions[0][3] > height:
            canvas.coords(snake[0],positions[0][0],0 - snakeSize,positions[0][2],0)

        elif positions[0][1] < 0:
            canvas.coords(snake[0],positions[0][0],height,positions[0][2],height-snakeSize)

        positions.clear()
        positions.append(canvas.coords(snake[0]))

        if direction == "left":
            canvas.move(snake[0], -snakeSize,0)
        
        elif direction == "right":
            canvas.move(snake[0], snakeSize,0)

        elif direction == "up":
            canvas.move(snake[0], 0,-snakeSize)

        elif direction == "down":
            canvas.move(snake[0], 0,snakeSize)
        sHeadPos = canvas.coords(snake[0])
        foodPos = canvas.coords(food)
        
        if overlapping(sHeadPos, foodPos):
            moveFood()
            growSnake()
        
        for i in range(1, len(snake)):
            if overlapping(sHeadPos, canvas.coords(snake[i])):
                gameOver = True
                gameOverWindow()
        
        for i in range(1, len(snake)):
            positions.append(canvas.coords(snake[i]))
        for i in range(len(snake)-1):
            canvas.coords(snake[i+1],positions[i][0], positions[i][1],positions[i][2],positions[i][3])
        
        if 'gameOver' not in locals():
            global speed
            window.after(speed, moveSnake)
                


    width = 1280
    height = 720


    window = setWindowDimensions(width, height)

    bgImage = PhotoImage(file="gamebg.png")
    pauseImage = PhotoImage(width = 40, height = 40, file="pause.png")

    canvas = Canvas(window, width=1280, height=720)
    background = canvas.create_image((0,0), image = bgImage, anchor = "nw")
    canvas.pack()


    snake = []
    global snakeSize
    snakeSize = 15
    snake.append(canvas.create_rectangle(snakeSize,snakeSize, snakeSize * 2, snakeSize * 2, fill="white" ))


    
    txt = "Score:" + str(score)

    scoreText = canvas.create_text( width/2 , 20 , fill="white" , font="Helvetica 18", text=txt)
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

    pauseMenu = Tk()
    pauseMenu.title("Snek")

    global pause
    pauseBgImage = PhotoImage(file="pausebg.gif")
    
    canvas = Canvas(pauseMenu, height=h, width=w)


    canvas.pack()


    bgPause = Label(pauseMenu, image=pauseBgImage)
    bgPause.place(x=0,y=0)


    mainMenuButton = Button(pauseMenu, text="Main Menu", bg='#e0b522', fg='white', height=2, width=20, command= menuWindow)
    mainMenuButton.place(x=105, y=175)

    saveButton = Button(pauseMenu, text="Save", bg='#e0b522', fg='white', height=2, width=20, command= saveGame)
    saveButton.place(x=105, y=240)

    leaderButton = Button(pauseMenu, text="Leaderboards", bg='#e0b522', fg='white', height=2, width=20, command= leaderWindow)
    leaderButton.place(x=105, y=305)

    restartButton = Button(pauseMenu, text="Restart", bg='#e0b522', fg='white', height=2, width=20, command= restartProgram)
    restartButton.place(x=105, y=370)

    exitButton = Button(pauseMenu, text="Exit", bg='#e0b522', fg='white', height=2, width=20, command= exitProgram)
    exitButton.place(x=105, y=435)



    pauseMenu.mainloop()


def cWindow():
     
    def menuWindow():
        controlWindow.destroy()
        mMenu()

    def wasdControls():
        global arrows
        arrows = False

    def arrowControls():
        global arrows
        arrows = True

    h = 600
    w = 400

    controlWindow = Tk()
    controlWindow.title("Snek")

    bgImage = PhotoImage(file="changecontrols.png")

    canvas = Canvas(controlWindow, height=h, width=w)
    canvas.pack()

    bgLabel = Label(canvas, image=bgImage)
    bgLabel.pack()


    mainMenuButton = Button(controlWindow, text="Main Menu", bg='#e0b522', fg='white', height=2, width=20, command= menuWindow)
    mainMenuButton.place(x=545, y=620)

    wasdButton = Button(controlWindow, text="WASD", bg='#e0b522', fg='white', height=2, width=10, command= wasdControls)
    wasdButton.place(x=810, y=510)

    arrowButton = Button(controlWindow, text='Arrow Keys', bg='#e0b522', fg='white', height=2, width=10, command= arrowControls)
    arrowButton.place(x=810, y=270)

    

    controlWindow.mainloop()


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
        print("Leaderbaords")

    def saveLeaderBoard():
        global score
        scoreString = str(score)
        nameString = nameText.get()
        leaderboardFile = open("leaderboard.txt", 'a')
        leaderboardFile.write(nameString + " " + scoreString + '\n')
        leaderboardFile.close()

    h = 600
    w = 400

    gameOverMenu = Tk()
    gameOverMenu.title("Snek")

    bgImage = PhotoImage(file="gameoverbg.png")

    canvas = Canvas(gameOverMenu, height=h, width=w)
    canvas.pack()

    bgLabel = Label(canvas, image=bgImage)
    bgLabel.pack()

    nameLabel =Label(gameOverMenu, text="Enter Name", font="Helvtica", bg="white")
    nameLabel.place(x=150, y=115)

    nameText = Entry(gameOverMenu, bg="white",)
    nameText.place(x=95, y=160)

    submitButton = Button(gameOverMenu, text="Submit", bg='#e0b522', fg='white', height=1, width=4, command= saveLeaderBoard)
    submitButton.place(x=270, y=155)

    mainMenuButton = Button(gameOverMenu, text="Main Menu", bg='#e0b522', fg='white', height=3, width=20, command= menuWindow)
    mainMenuButton.place(x=105, y=230)

    restartButton = Button(gameOverMenu, text="Restart", bg='#e0b522', fg='white', height=3, width=20, command= restartProgram)
    restartButton.place(x=105, y=305)

    leaderButton = Button(gameOverMenu, text="Leaderboards", bg='#e0b522', fg='white', height=3, width=20, command= leaderWindow)
    leaderButton.place(x=105, y=380)

    exitButton = Button(gameOverMenu, text="Exit", bg='#e0b522', fg='white', height=3, width=20, command= exitProgram)
    exitButton.place(x=105, y=455)






    gameOverMenu.mainloop()


def iWindow():
    
    def menuWindow():
        instructionWindow.destroy()
        mMenu()

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

    canvas.bind("<b>", bossKey)

    mainMenu.mainloop()


def bWindow():
    def menuWindow():
        bossWindow.destroy()
        mMenu()

    h = 600
    w = 400

    bossWindow = Tk()
    bossWindow.title("Snek")

    bgImage = PhotoImage(file="boss.png")

    canvas = Canvas(bossWindow, height=h, width=w)
    canvas.pack()

    bgLabel = Label(canvas, image=bgImage)
    bgLabel.pack()


    mainMenuButton = Button(bossWindow, text="Main Menu", bg='#FFFFFF', fg='black', height=2, width=20, command= menuWindow)
    mainMenuButton.place(x=545, y=620)


    bossWindow.mainloop()




pause = True
direction = "right"
snakeSize = 15
score = 0
speed = 70
arrows = True
mMenu()