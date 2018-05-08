"""
This is a game with a bouncing ball and a paddle. The ball will fly around the screen, and the player will bounce it
off the paddle. If the ball hits the bottom of the screen, the game comes to an end.

"""

# Creating the game canvas

from Tkinter import *
import random
import time

tk = Tk()
tk.title("Game")    # window title
tk.resizable(0,0)   # size of the window cannot be changed either horizontally or vertically
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width =500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

tk.mainloop()       # Keeps graphics window open
