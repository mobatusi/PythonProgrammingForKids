## Creating the game canvas
from tkinter import *
import random
import time


## Creating the ball class
class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color) # x and y coordinates for top-left corner and xy coordinates for the bottom-right corner
        self.canvas.move(self.id, 245, 100)     # move oval to the middle of the canvas
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]  # set object variable x to 0
        self.y = -3 # set object variable y t0 -3 to speed up the ball
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id) # get the paddle's coordinates
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)    # 0 says don't move horizontally, -1 says move 1 pixel up the screen
        pos = self.canvas.coords(self.id)
        # print(self.canvas.coords(self.id))
        if pos[0] <= 0:
            self.x = 3
        if pos[1] <= 0:     # if you hit the top of the screen, stop subtracting one from the vertical position, and stop moving
            self.y = 1
        if pos[2] >= self.canvas_width:
            self.x = -3
        if pos[3] >= self.canvas_height:        # if the bottom of the ball is greater than or equal to the variable canvas_height, set it back to -1
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -3


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.started = False
        self.canvas.bind_all('<Button-1>', self.start_game)
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def turn_left(self,evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2

    def start_game(self,evt):
        self.started = True

    def draw(self):
        self.canvas.move(self.id, self.x ,0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

tk = Tk()
tk.title("Game")    # window title
tk.resizable(0,0)   # size of the window cannot be changed either horizontally or vertically
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width =500, height=400, bd=0, highlightthickness=0)
canvas.pack()       # Tells the canvas to size itself according to the width and height parameters given in the preceding line
tk.update()         # tells tkinter to initialize itself for the animation in our game

paddle = Paddle(canvas,'blue')
ball = Ball(canvas, paddle, 'red')
game_over_text = canvas.create_text(250,200, text = 'GAME OVER', \
                                    state = 'hidden')
# tk.mainloop()       # Keeps graphics window open
while 1:
    if ball.hit_bottom == False and paddle.started == True:
        ball.draw()
        paddle.draw()
    if ball.hit_bottom == True:
        time.sleep(1)
        canvas.itemconfig(game_over_text, state = 'normal')
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)