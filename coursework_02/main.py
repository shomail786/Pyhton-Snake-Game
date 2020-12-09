from tkinter import *
import sys, os, random



def gameFunction():

    def bossWindow():
        window.destroy()
        bWindow()

    def gameOverWindow():
        window.destroy()
        gMenu()

    def pauseWindow():
        window.destroy()
        pMenu()


    def pauseButton():
        btnPause = Button(window, bg="#e0b522", image=pauseImage, width="40", height="40", command= pauseWindow)
        btnPause.place(x=45,y=45)

    def placeFood():
        global food, foodX, foodY
        food = canvas.create_rectangle(0,0, snakeSize, snakeSize, fill="steel blue")
        foodX = random.randint(0,width-snakeSize)
        foodY = random.randint(0, height-snakeSize)
        canvas.move(food, foodX, foodY)

    def bossKey(event):
        bossWindow()

        
    
    def escKey(event):
        pauseWindow()

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
    #snakeSize = 15
    snake.append(canvas.create_rectangle(snakeSize,snakeSize, snakeSize * 2, snakeSize * 2, fill="white" ))


    
    txt = "Score:" + str(score)

    scoreText = canvas.create_text( width/2 , 20 , fill="white" , font="Helvetica 18", text=txt)

    canvas.bind("<Left>", leftKey) 
    canvas.bind("<Right>", rightKey)
    canvas.bind("<Up>", upKey)
    canvas.bind("<Down>", downKey)
    canvas.bind("<Escape>", escKey)
    canvas.bind("<b>", bossKey)
    canvas.bind("<j>", slowKey)
    canvas.bind("<k>", fastKey)
    canvas.bind("<n>", smallKey)
    canvas.bind("<m>", bigKey)
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

    def resumeProgram():
        pauseMenu.destroy()
        gameFunction()
        
    def exitProgram():
        pauseMenu.destroy()
        os._exit(0)

    def saveGame():
        print("Saved")

    def leaderWindow():
        print("Leaderbaords")

    h = 600
    w = 400

    pauseMenu = Tk()
    pauseMenu.title("Snek")

    global pause
    pauseBgImage = PhotoImage(file="pausebg.gif")
    
    canvas = Canvas(pauseMenu, bg='#e0b522', height=h, width=w)

    txt = "~PAUSED~" 

    scoreText = canvas.create_text(200,70, fill="white" , font="Helvetica 40", text=txt)
    canvas.pack()


    #bgPause = Label(pauseMenu, image=pauseBgImage)
    #bgPause.pack(x=0,y=0)


    resumeButton = Button(pauseMenu, text="Resume", bg='black', fg='white', height=2, width=20, command= resumeProgram)
    resumeButton.place(x=105, y=110)

    mainMenuButton = Button(pauseMenu, text="Main Menu", bg='black', fg='white', height=2, width=20, command= menuWindow)
    mainMenuButton.place(x=105, y=175)

    saveButton = Button(pauseMenu, text="Save", bg='black', fg='white', height=2, width=20, command= saveGame)
    saveButton.place(x=105, y=240)

    leaderButton = Button(pauseMenu, text="Leaderboards", bg='black', fg='white', height=2, width=20, command= leaderWindow)
    leaderButton.place(x=105, y=305)

    restartButton = Button(pauseMenu, text="Restart", bg='black', fg='white', height=2, width=20, command= restartProgram)
    restartButton.place(x=105, y=370)

    exitButton = Button(pauseMenu, text="Exit", bg='black', fg='white', height=2, width=20, command= exitProgram)
    exitButton.place(x=105, y=435)

    # exitButton = Button(pauseMenu, text="Exit", bg='black', fg='white', height=2, width=20, command= exitProgram)
    # exitButton.place(x=105, y=435)

    # cheatButton = Button(pauseMenu, text="Cheat Code", bg='black', fg='white', height=2, width=20, command= cheatWindow)
    # cheatButton.place(x=105, y=500)

    pauseMenu.mainloop()




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
        print("Saved")

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

    submitButton = Button(gameOverMenu, text="Submit", bg='black', fg='white', height=1, width=4, command= saveLeaderBoard)
    submitButton.place(x=270, y=155)

    mainMenuButton = Button(gameOverMenu, text="Main Menu", bg='black', fg='white', height=3, width=20, command= menuWindow)
    mainMenuButton.place(x=105, y=230)

    restartButton = Button(gameOverMenu, text="Restart", bg='black', fg='white', height=3, width=20, command= restartProgram)
    restartButton.place(x=105, y=305)

    leaderButton = Button(gameOverMenu, text="Leaderboards", bg='black', fg='white', height=3, width=20, command= leaderWindow)
    leaderButton.place(x=105, y=380)

    exitButton = Button(gameOverMenu, text="Exit", bg='black', fg='white', height=3, width=20, command= exitProgram)
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





def mMenu():
    def gameWindow():
        mainMenu.destroy()
        gameFunction()

    def instructionWindow():
        mainMenu.destroy()
        iWindow()

    def leaderWindow():
        print("Leaderbaords")

    def controlsWindow():
        print("Controls")

    def loadGame():
        print("Load Game")

    def exitProgram():
        os._exit(0)

    def bossKey(event):
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

direction = "right"
snakeSize = 15
score = 0
speed = 70
mMenu()