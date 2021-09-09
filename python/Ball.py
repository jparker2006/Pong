import pygame
import random

resolution = (800,600)
c_white = (255, 255, 255)

class Ball:
    # xPos, yPos, xVelo, yVelo, ballsize (constructor)
    def __init__(self, xPos =  resolution[0] / 2, yPos = resolution[1] / 2, xVel = 0, yVel = 0, rad = 15):
        self.nXPos = xPos
        self.nYPos = yPos
        self.dXVel = xVel
        self.dYVel = yVel
        self.nRadius = rad
        self.bStarted = False
        self.type = "Ball"

    def draw(self, surface):
        pygame.draw.circle(surface, c_white, (self.nXPos, self.nYPos), self.nRadius)

    def update(self):
        self.nXPos += self.dXVel
        self.nYPos += self.dYVel

        if (self.nXPos <= 15 or self.nXPos >= resolution[0] - 15): # score
            self.nXPos =  resolution[0] / 2
            self.nYPos = resolution[1] / 2

            nRandXVel = 0
            nRandYVel = 0

            while nRandXVel == 0 and nRandYVel == 0:   # cant be static
                nRandXVel = random.randint(-6, 6)
                nRandYVel = random.randint(-7, 7)

            self.dXVel = nRandXVel
            self.dYVel = nRandYVel

        if (self.nYPos <= 15 or self.nYPos >= resolution[1] - 15): #bounce off walls
            if (self.dYVel > 0):
                self.dYVel = -random.randint(2, 6)
            else:
                self.dYVel = random.randint(2, 6)

    def start(self):
        if self.bStarted:
            return
        self.dXVel = 3
        self.dYVel = 2
        self.bStarted = True
