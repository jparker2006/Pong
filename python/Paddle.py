import pygame

c_pyYellow = (255,211,67)

class Paddle:
    def __init__(self, xPos, yPos = 150): # y is center of y axis on screen
        self.nXPos = xPos
        self.nYPos = yPos
        self.bOnKey = False
        self.type = "Paddle"

    def draw(self, surface):
        pygame.draw.rect(surface, c_pyYellow, pygame.Rect(self.nXPos, self.nYPos, 20, 90))

    def Move(self, bUpOrDown): # True is up, False is down
        if bUpOrDown:
            self.nYPos -= 45
            if self.nYPos < 0:
                self.nYPos = 0
        else:
            self.nYPos += 45
            if self.nYPos > 310:
                self.nYPos = 310

    def GetYPos(self):
        return self.nYPos
    def GetXPos(self):
        return self.nXPos
