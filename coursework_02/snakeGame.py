# Game Resolution: 1280 X 720

from tkinter import *
import random, time, sys, os

def gameOverWindow():
    window.destroy()
    os.system("python3 gameOverMenu.py")

def pauseWindow():
    os.system("python3 pauseMenu.py")









def placeFood():
    global food, foodX, foodY
    food = canvas.create_rectangle(0,0, snakeSize, snakeSize, fill="steel blue")
    foodX = random.randint(0,width-snakeSize)
    foodY = random.randint(0, height-snakeSize)
    canvas.move(food, foodX, foodY)

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
    
    score += 10
    
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
        window.after(50, moveSnake)


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



pauseButton()
placeFood()
moveSnake()
window.mainloop()

