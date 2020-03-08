# This game will be an arena fight game

import pygame
import random
import math
from pygame import mixer

# Initalize pygame so you can use it
pygame.init()
# Creating the screen
screen = pygame.display.set_mode((1000, 600))

class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()
        #adding all the images to sprite array
        self.images = []
        self.images.append(pygame.image.load('GrayMage1.png'))
        self.images.append(pygame.image.load('GrayMage2.png'))
        self.images.append(pygame.image.load('GrayMage3.png'))
        self.images.append(pygame.image.load('GrayMage4.png'))

        self.imagesL = []
        self.imagesL.append(pygame.image.load('GrayMageLeft1.png'))
        self.imagesL.append(pygame.image.load('GrayMageLeft2.png'))
        self.imagesL.append(pygame.image.load('GrayMageLeft3.png'))
        self.imagesL.append(pygame.image.load('GrayMageLeft4.png'))

        #index value to get the image from the array
        #initially it is 0
        self.index = 0
 #now the image that we will display will be the index from the image array
        self.image = self.images[self.index]
        self.imageL = self.imagesL[self.index]
        # creating a rect at position x,y (5,5) of size (48,48) which is the size of sprite
        self.rect = pygame.Rect(400, 480, 48, 48)

    def move(self, xpos, ypos, centre=False):
        if centre:
            self.rect.center = [xpos, ypos]
        else:
            self.rect.topleft = [xpos, ypos]

    def updateMageFace(self):
        x = pygame.mouse.get_pos() # gets the cord of my mouse
        xx = x[0] # gets the x cor of my mouse but y cor = x[1]
        self.index += 1
        if xx < playerx:
            if self.index >= len(self.imagesL):
                self.index = 0
        else:
            if self.index >= len(self.images):
                self.index = 0
        if xx < playerx:
            self.image = self.imagesL[self.index]
        else:
            self.image = self.images[self.index]


my_sprite = MySprite()
my_group = pygame.sprite.Group(my_sprite)
clock = pygame.time.Clock()

# Player values
playerImg = my_group
playerx = 400
playery = 480
playerx_change = 0
playery_change = 0
"""  Use for later
def isCollision(playerx, playerx, bulletx, bullety):
    dist = math.hypot(enemyx - bulletx, enemyy - bullety)
    if dist < 40:
        return True
    else:
        return False
"""
bg = pygame.image.load('MageBg.png')
center = False
running = True
while running:
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:  # .key looks for a key press
                playerx_change = -5
            if event.key == pygame.K_d:
                playerx_change = 5
            if event.key == pygame.K_w:  # .key looks for a key press
                playery_change = -5
            if event.key == pygame.K_s:
                playery_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerx_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                playery_change = 0
    # Player movment

    playerx += playerx_change
    playery += playery_change
    # this created the boundries left and right
    if playerx <= 32:
        playerx = 32
    elif playerx >= 920:
        playerx = 920
    elif playery <= 101:
        playery = 101
    elif playery >= 520:
        playery = 520

    MySprite.move(my_sprite, playerx, playery, center) # line takes in the sprites, x cor, y cor, and the boolean
    MySprite.updateMageFace(my_sprite) # updates the way the sprite is facing
    #my_group.update() # updates the way the sprite is facing but i think mysprite,update is better
    my_group.draw(screen) # draws the sprite on the screen
    pygame.display.update()  # This will up date the screen, you need to update ever loop
    clock.tick(10)

    # Next step, create fire ball then have it shoot at the location of the curser!