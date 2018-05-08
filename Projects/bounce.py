"""
This is a game with a bouncing ball and a paddle. The ball will fly around the screen, and the player will bounce it
off the paddle. If the ball hits the bottom of the screen, the game comes to an end.

"""

## Creating the game canvas
from Tkinter import *
import random
import time


## Creating the ball class
class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color) # x and y coordinates for top-left corner and xy coordinates for the bottom-right corner
        self.canvas.move(self.id, 245, 100)     # move oval to the middle of the canvas
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]  # set object variable x to 0
        self.y = -3 # set object variable y t0 -3 to speed up the ball
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

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
            self.y = -1

tk = Tk()
tk.title("Game")    # window title
tk.resizable(0,0)   # size of the window cannot be changed either horizontally or vertically
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width =500, height=400, bd=0, highlightthickness=0)
canvas.pack()       # Tells the canvas to size itself according to the width and height parameters given in the preceding line
tk.update()         # tells tkinter to initialize itself for the animation in our game

ball = Ball(canvas, 'red')

# tk.mainloop()       # Keeps graphics window open
while 1:
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)