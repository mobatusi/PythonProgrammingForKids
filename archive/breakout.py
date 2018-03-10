#breakout.py

import pygame
from pygame.locals import *
from random import randint, choice, randrange
import time

class Bullet:
    def __init__(self,color,xcor,ycor,yvel):
        self.color = color
        self.xcor = xcor
        self.ycor = ycor
        self.yvel = yvel
        self.status = 1 #starts out "on"
        self.rect = pygame.Rect(self.xcor,self.ycor,2,10)

    def move(self,bullet_list):
        #if bullet gets to top edge, disappear and turn 'off'
        if self.ycor < 0:
            self.status = 0
        self.ycor += self.yvel #update position by velocity
        if self.status == 1: #if the bullet is 'on"
            #draw it
            self.rect = pygame.draw.rect(screen, self.color,
                                         [self.xcor,self.ycor,5,20])
        else:
            bullet_list.remove(self)

class AlienBullet:
    def __init__(self,color,xcor,ycor,yvel):
        self.color = color
        self.xcor = xcor
        self.ycor = ycor
        self.yvel = yvel
        self.status = 1 #starts out "on"
        self.rect = pygame.Rect(self.xcor,self.ycor,2,10)

    def move(self,paddle,alien_bullet_list):
        #if bullet gets to bottom edge, disappear and turn 'off'
        if self.ycor > HEIGHT:
            self.status = 0
        self.ycor += self.yvel #update position by velocity
        if self.rect.colliderect(paddle):
            #play explode sound
            explode_sound.play()
            self.status = 0
            lives_obj.decreaseLives()
        if self.status == 1: #if the bullet is 'on"
            #draw it
            self.rect = pygame.draw.rect(screen, self.color,
                                         [self.xcor,self.ycor,5,25])
        else:
            alien_bullet_list.remove(self)


class Paddle:
    def __init__(self,xcor,ycor,height,width,color):
        self.xcor = xcor
        self.ycor = ycor
        self.height = height
        self.width = width
        self.color = color
        self.move = 0 #paddle doesn't move at first
        self.rect = pygame.Rect(self.xcor, self.ycor,self.width,self.height)

    def draw(self):
        self.xcor += self.move
        #don't go off the right side of the screen
        if self.xcor > 700 - self.width: #if the xcor is off the screen
            self.xcor = 700 - self.width #reset the xcor to the right
            self.move = 0               #stop moving
        #don't go off the left side of the screen:
        if self.xcor < 0: #if the xcor is off the screen
            self.xcor = 0 #reset the xcor to the left
            self.move = 0 #stop moving
        self.rect = pygame.draw.rect(screen, self.color,
                                     [self.xcor,self.ycor,self.width,self.height])
        pygame.draw.rect(screen, self.color,
                         [self.xcor + 0.5*self.width - 5,
                          self.ycor - 10,10,10])

class Score:
    def __init__(self,xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.score = 0

    def increaseScore(self,value):
        self.score += value

    def displayScore(self):
        # This is a font we use to draw text on the screen (size 36)
        font = pygame.font.Font(None, 36)
        text = font.render("Score:"+str(self.score), True, GREEN)
        screen.blit(text, [self.xpos, self.ypos])

    def resetScore(self):
        self.score = 0

class Alien(object):
    def __init__(self,xpos,ypos):
        self.status = 1 #aliens start off "alive"
        self.rect = pygame.Rect(xpos,ypos,40,40)
        self.image = pygame.image.load('images/alien.png').convert()
        self.image = pygame.transform.scale(self.image,(40,40))

    def move(self):
        #if group is moving down:
        if down > 0:
            self.rect.y += moveAmount
        #if group is moving left
        elif left:
            self.rect.x -= moveAmount
        #otherwise, move right
        else:
            self.rect.x += moveAmount


    def update(self,bullet_list,alien_list):
        for bullet in bullet_list:
            #if a bullet hits the alien:
            if self.rect.colliderect(bullet):
                #play exploding sound
                explode_sound.play()
                self.status = 0   #alien disappears
                bullet.status = 0 #bullet disappears
                #remove bullet from bullet list
                bullet_list.remove(bullet)
                score.increaseScore(10)

        if self.status == 1: #if the alien is 'alive'
            #draw it
            screen.blit(self.image, [self.rect.x,self.rect.y])


        #This is outside the Alien class
def setAlienField():
    #create field of Aliens:
    alien_list = []
    rows = 5
    cols = 11
    for i in range(rows):
        for j in range(cols):
            alien = Alien(40*j + 100,
                          35*i+50)
            alien_list.append(alien)
    return alien_list

def moveAliens(alien_list):
    #make sure we can access these variables
    global down,left,landed

    #loop through alien list to find left and right
    #edges of alien group
    maxX = 0
    minX = 1000
    for alien in alien_list:
        if alien.rect.x > maxX:
            maxX = alien.rect.x
        if alien.rect.x < minX:
            minX = alien.rect.x
        #check if aliens have landed!
        if alien.rect.y > 420:
            landed = True

    if down > 0:
        down -= 1

    elif left and minX <25:
        left = False
        down = 3

    elif not left and maxX + 90 > WIDTH:
        left = True
        down = 3

    #move the aliens
    for alien in alien_list:
        alien.move()

class Lives:
    def __init__(self,xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.lives = 3

    def decreaseLives(self):
        self.lives -= 1

    def displayLives(self):
        font = pygame.font.Font(None, 36)
        text = font.render("Lives: "+str(self.lives), True, YELLOW)
        screen.blit(text, [self.xpos, self.ypos])

    def resetLives(self):
        self.lives = 3

# Define the colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
YELLOW = (255,255,0)

bullet_list = []
alien_list = []
alien_bullet_list = []

pygame.init()

# Set the width and height of the screen
WIDTH = 700
HEIGHT = 500
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

#alien variables
down = 0
left = True
moveAmount = 10
move_delay = 1
landed = False #if aliens invade!

pygame.display.set_caption("Space Invaders!")

#define sounds:
shoot_sound = pygame.mixer.Sound("images/Laser_Shoot5.ogg")
alien_shoot_sound = pygame.mixer.Sound("images/Laser_Shoot10.ogg")
explode_sound = pygame.mixer.Sound("images/Explosion10.ogg")
end_sound = pygame.mixer.Sound("images/Randomize14.ogg")

# boolean for keeping the game going
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#create the paddle:
paddle = Paddle(randint(50,450),#xcor
                450,#ycor
                20,#height
                50,#width
                GREEN) #color

#create field of aliens
alien_list = setAlienField()

#set next alien move time
next_move_time = time.time() + move_delay

#create the score object
score = Score(150,25)

#create the lives object
lives_obj = Lives(550,25)

#game loop
while not done:
    for event in pygame.event.get(): #Check all the clicks and keystrokes
        if event.type == pygame.QUIT: # If user clicked the X to close the window
            done = True # stop repeating this loop
        if event.type == pygame.KEYDOWN: #if a key is pressed
            if event.key == K_LEFT: #if the left arrow key is pressed
                paddle.move = -5 #the paddle should go left
            if event.key == K_RIGHT: #if the right arrow key is pressed
                paddle.move = 5 #the right paddle should go right
            if event.key == K_SPACE: #the space key will shoot bullets!
                bullet_list.append(Bullet(GREEN,paddle.xcor+0.5*paddle.width,paddle.ycor-20,-2))
                #play laser sound
                shoot_sound.play()
        if event.type == pygame.KEYUP: #if a key is released
            if event.key == K_RIGHT or event.key == K_LEFT: #if it's the LEFT or RIGHT key:
                paddle.move = 0 #stop the paddle

    # set the background color
    screen.fill(BLACK)

    #move the bullet
    for bullet in bullet_list:
        bullet.move(bullet_list)

    #move the paddles
    paddle.draw()

    #display the score
    score.displayScore()

    #if all the aliens are gone:
    if len(alien_list) == 0:
        bullet_list = [] #clear the bullets
        #create new field of aliens
        alien_list = setAlienField()
        #display the Next Level text
        font = pygame.font.Font(None, 72)
        text = font.render("NEXT LEVEL", True, GREEN)
        screen.blit(text, [100 ,300])
        pygame.display.update()
        #pause for next "level"
        time.sleep(3)

    #update move delay by remaining aliens
    move_delay = len(alien_list)/55.0

    #move aliens after delay
    if time.time() > next_move_time:
        next_move_time = time.time() + move_delay
        moveAliens(alien_list)

    #display the aliens
    for alien in alien_list:
        if alien.status == 0:
            alien_list.remove(alien)
        else:
            #randomly shoot AlienBullet
            if randint(0,10000) < 5:
                #play shooting sound
                alien_shoot_sound.play()
                #create alien bullet
                alienBullet = AlienBullet(WHITE,alien.rect.x+10,alien.rect.y+10,2)
                #add the bullet to the list
                alien_bullet_list.append(alienBullet)
            #update alien
            alien.update(bullet_list,alien_list)


    #move the alien bullets
    for abullet in alien_bullet_list:
        if abullet.status == 0:
            alien_bullet_list.remove(abullet)
        else:
            abullet.move(paddle,alien_bullet_list)

    #display the lives object
    lives_obj.displayLives()

    #The game ends if the lives run out:
    if lives_obj.lives == 0 or landed:
        #play end sound
        end_sound.play()
        #keep the loop going
        waiting = True
        #display the Game Over text
        font = pygame.font.Font(None, 36)
        text = font.render("GAME OVER. PLAY AGAIN? Y/N ", True, GREEN)
        #keep going util player gives an answer
        while waiting:
            #blit the prompt image on the main surface
            screen.blit(text, [100 ,300])
            pygame.display.update()
            #get an game events
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    #if the user hit N the want to play again
                    if event.key == K_n:
                        done = True
                        waiting = False
                        break
                    #if the user hit Y the want to play again
                    if event.key == K_y :
                        lives_obj.resetLives()
                        #create new field of aliens
                        alien_list = setAlienField()
                        alien_bullet_list = []
                        waiting = False
                        playing = True
                        break

    # update the screen
    pygame.display.flip()

    # limit the speed to 60 frames per second
    clock.tick(60)

# quit pygame
pygame.quit()