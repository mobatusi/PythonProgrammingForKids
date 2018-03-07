"""
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/

1.08.15: Added Ball class
"""

import pygame
from random import randint, choice

class Ball:
    def __init__(self,radius,color,xcor,ycor,xvel,yvel):
        self.radius = radius
        self.color = color
        self.xcor = xcor
        self.ycor = ycor
        self.xvel = xvel
        self.yvel = yvel

    def move(self):
        if self.xcor < 0 or self.xcor > 700 - 2*self.radius:
            self.xvel = -self.xvel
        if self.ycor < 0 or self.ycor > 500 - 2*self.radius:
            self.yvel = -self.yvel
        self.xcor += self.xvel
        self.ycor += self.yvel
        pygame.draw.ellipse(screen, self.color,
                            [self.xcor,self.ycor,2*self.radius,2*self.radius])

# Define the colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

ball_list = []

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#create the balls
for i in range(100):
    newball = Ball(randint(10,60), #radius
                   (randint(0,255),#red
                    randint(0,255),#green
                    randint(0,255)),#blue
                   randint(0,650), #x-value
                   randint(0,450), #y-value
                   randint(-5,5),   #x-velocity
                   randint(-5,5))   #y-velocity
    ball_list.append(newball) #add it to the ball list

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

    # --- Game logic should go here

    # --- Drawing code should go here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)

    #move the balls
    for ball in ball_list:
        ball.move()

    #pygame.draw.rect(screen,WHITE,[350,400,75,25])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
