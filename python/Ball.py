import pygame, random

resolution = (600,400)
c_pyYellow = (255,211,67)

class Ball:
    # x position, y position, x velocity, y velocity, ballsize
    def __init__(self, xPos =  resolution[0] / 2, yPos = resolution[1] / 2, xVel = 3, yVel = 0, rad = 12):
        self.nXPos = xPos
        self.nYPos = yPos
        self.dXVel = xVel
        self.dYVel = yVel
        self.nRadius = rad
        self.nPaddleAScore = 0
        self.nPaddleBScore = 0
        self.type = "Ball"

    def draw(self, surface):
        pygame.draw.circle(surface, c_pyYellow, (self.nXPos, self.nYPos), self.nRadius)

    def update(self):
        self.nXPos += self.dXVel
        self.nYPos += self.dYVel

        if (self.nXPos <= 0): # Paddle A / Left side loses point
            self.nXPos =  resolution[0] / 2
            self.nYPos = resolution[1] / 2
            self.dXVel = -3
            self.nPaddleBScore += 1
        elif (self.nXPos >= resolution[0]): # Paddle B / Right side loses point
            self.nXPos =  resolution[0] / 2
            self.nYPos = resolution[1] / 2
            self.dXVel = 3
            self.nPaddleAScore += 1

        if (self.nYPos <= 15 or self.nYPos >= resolution[1] - 15): # bounce off walls
            if (self.nYPos <= 11):
                self.nYPos = 15
            if (self.nYPos >= resolution[1] - 11):
                self.nYPos = resolution[1] - 15

            if (self.dYVel > 0):
                self.dYVel = -random.randint(1, 5)
            else:
                self.dYVel = random.randint(1, 5)

            if (self.dXVel < 0):
                self.dXVel = -random.randint(3, 5)
            else:
                self.dXVel = random.randint(3, 5)

    def GetYPos(self):
        return self.nYPos;
    def GetXPos(self):
        return self.nXPos;

    def HitPaddle(self):
        self.dXVel *= -1
        if (self.dXVel < 0):
            self.dXVel -= random.random()
            if (self.dXVel < -6): # cap speed
                self.dXVel = -6
        else:
            self.dXVel += random.random()
            if (self.dXVel > 6):
                self.dXVel = 6
        self.dYVel = random.randint(-3, 3)
