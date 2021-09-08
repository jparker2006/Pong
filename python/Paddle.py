import pygame

resolution = (800,600)
c_white = (255, 255, 255)

class Paddle:
    def __init__(self, xPos, yPos = resolution[1] / 2 - 55):
        self.nXPos = xPos
        self.nYPos = yPos
        self.bOnKey = False
        self.type = "Paddle"
    def draw(self, surface):
        pygame.draw.rect(surface, c_white, pygame.Rect(self.nXPos, self.nYPos, 30, 110))
    def Move(self, bUpOrDown): # True is up, False is down
        if bUpOrDown:
            self.nYPos -= 8
            if self.nYPos < 0:
                self.nYPos = 0
        else:
            self.nYPos += 8
            if self.nYPos > 490:
                self.nYPos = 490
