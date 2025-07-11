from tkinter import *
import random

GAME_WIDTH=705
GAME_HEIGHT= 555
CELL_SIZE = 15
BODY_PARTS= 3
SPEED= 100


direction='right'

class Snake:
    def __init__(self):
        self.body_size= BODY_PARTS
        self.coordinates = []
        self.squares = []
        
        for i in range(BODY_PARTS-1,-1,-1):
            self.coordinates.append([i*CELL_SIZE, 0])
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + CELL_SIZE, y+ CELL_SIZE, fill="green", tag="snake")
            self.squares.append(square)
        
        

class Food:
    def __init__(self):
        self.x = random.randint(0, int(GAME_WIDTH / CELL_SIZE)-1) * CELL_SIZE
        self.y = random.randint(0, int(GAME_HEIGHT / CELL_SIZE)-1) * CELL_SIZE
        self.reddot = canvas.create_oval(self.x, self.y, self.x + CELL_SIZE, self.y + CELL_SIZE, fill="red")


score=0
pp= False



def move():
    start.place_forget()

    x,y=snake.coordinates[0]
    
    if direction== 'right':
        x+=CELL_SIZE
    elif direction== 'left':
        x-=CELL_SIZE
    elif direction== 'up':
        y-=CELL_SIZE
    elif direction== 'down':            
        y+=CELL_SIZE   

    if x < 0:
        x= GAME_WIDTH - CELL_SIZE
    if y<0:
        y= GAME_HEIGHT - CELL_SIZE
    if x==GAME_WIDTH:
        x=0
    if y==GAME_HEIGHT:      
        y=0  

    if [x, y] in snake.coordinates:
        over=canvas.create_text(GAME_WIDTH/2, GAME_HEIGHT/2, text="Game Over", fill="red", font=("Arial", 24))
        return
        

    snake.coordinates.insert(0, [x, y])
    
    square = canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill="green", tag="snake")
    snake.squares.insert(0, square) 
    

    if snake.coordinates[0] == [food.x, food.y]:
        canvas.delete(food.reddot)
        global score
        global SPEED
        score += 1
        Score_dis.config(text=f"Score: {score}")
        if SPEED>50:
            SPEED= 100-score

        food.__init__()
    else:
        snake.coordinates.pop()
        canvas.delete(snake.squares[-1])
        snake.squares.pop()
    
    
    

    if pp == True:    
        window.after(SPEED, move)


def up(event):
    global direction
    if direction != 'down':
        direction = 'up'
def down(event):
    global direction
    if direction != 'up':
        direction = 'down'  
def left(event):
    global direction
    if direction != 'right':
        direction = 'left' 
def right(event):
    global direction
    if direction != 'left':
        direction = 'right'

    

    
window= Tk()
window.title("Eat and Grow")
window.geometry("705x600+410+100")
window.resizable(False, False)
window.config(bg="white")

window.bind("<w>", up)
window.bind("<s>", down)
window.bind("<a>", left)
window.bind("<d>", right)





Score_dis= Label(window, text=f"Score: {score}", bg="white", fg="black", font=("Arial", 16))
Score_dis.pack()
canvas=Canvas(window, bg='black' , width=GAME_WIDTH, height=GAME_HEIGHT)
canvas.pack()
start= Label(window, text="Press Space to Start \n Control with AWSD (turn off the capslock if on)", bg="white", fg="black", font=("Arial", 16))
start.place(x=GAME_WIDTH/2, y=GAME_HEIGHT/2, anchor='center')
playpause= Label(window, text="Space: Play/Pause", bg="white", fg="black", font=("Arial", 10))
playpause.place(x= 600, y= 15, anchor='center')



snake= Snake()
food= Food()

window.bind("<space>", lambda event: play())


def play():
    global pp
    pp = not pp
    if pp == True:
        move()




window.mainloop()

