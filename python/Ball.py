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

        if (self.nXPos <= 0 or self.nXPos >= resolution[0]): # score game here
            print("scorer")
            #self.nXPos =  resolution[0] / 2
            #self.nYPos = resolution[1] / 2
            #nRandXVelo = random.randint(-6, 6)
            #while 0 == nRandXVelo:
                #nRandXVelo = random.randint(-6, 6)
            #self.dXVel = nRandXVelo
            #self.dYVel = random.randint(-3, 3)

        if (self.nYPos <= 15 or self.nYPos >= resolution[1] - 15): #bounce off walls
            if (self.dYVel > 0):
                self.dYVel = -random.randint(1, 5)
                if (self.dXVel < 0):
                    self.dXVel = -random.randint(1, 5)
                else:
                    self.dXVel = random.randint(1, 5)
            else:
                self.dYVel = random.randint(1, 5)

    def GetYPos(self):
        return self.nYPos;
    def GetXPos(self):
        return self.nXPos;

    def HitPaddle(self):
        self.dXVel *= -1
        if (self.dXVel < 0):
            self.dXVel -= random.random()
        else:
            self.dXVel += random.random()
        self.dYVel = random.randint(-3, 3)
        #self.dYVel = random.randint(2, 4)
