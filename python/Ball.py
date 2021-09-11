import pygame
import random

resolution = (600,400)
c_white = (255, 255, 255)

class Ball:
    # x position, y position, x velocity, y velocity, ballsize
    def __init__(self, xPos =  resolution[0] / 2, yPos = resolution[1] / 2, xVel = 3, yVel = 0, rad = 12):
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

        if (self.nXPos <= 12 or self.nXPos >= resolution[0] - 12): # score game here
            self.nXPos =  resolution[0] / 2
            self.nYPos = resolution[1] / 2
            nRandXVelo = random.randint(-5, 5)
            while 0 == nRandXVelo:
                nRandXVelo = random.randint(-5, 5)
            self.dXVel = nRandXVelo
            self.dYVel = random.randint(-6, 6)

        if (self.nYPos <= 12 or self.nYPos >= resolution[1] - 12): #bounce off walls
            if (self.dYVel > 0):
                self.dYVel = -random.randint(2, 6)
            else:
                self.dYVel = random.randint(2, 6)

    def GetYPos(self):
        return self.nYPos;
    def GetXPos(self):
        return self.nXPos;

    def HitPaddle(self):
        self.dXVel *= -1
