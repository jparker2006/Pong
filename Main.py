# ball should change velo after hitting top/bottom wall or paddle

import pygame, random, sys
from pygame.locals import *
pygame.init()

resolution = (800,600)
# colors
c_white = (255, 255, 255)
c_black = (0, 0, 0)
# colors end

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
        if (self.nXPos <= 15 or self.nXPos >= resolution[0] - 15): #bounce off walls
            self.dXVel *= -1
        if (self.nYPos <= 15 or self.nYPos >= resolution[1] - 15):
            self.dYVel *= -1
    def start(self):
        if self.bStarted:
            return
        self.dXVel = 3
        self.dYVel = 2
        self.bStarted = True

class Paddle:
    def __init__(self, xPos, yPos = resolution[1] / 2 - 55, xVel = 0, yVel = 0):
        self.nXPos = xPos
        self.nYPos = yPos
        self.dXVel = xVel
        self.dYVel = yVel
        self.bOnKey = False
        self.type = "Paddle"
    def draw(self, surface):
        pygame.draw.rect(surface, c_white, pygame.Rect(self.nXPos, self.nYPos, 30, 110))
    def update(self):
        self.nXPos += self.dXVel
        self.nYPos += self.dYVel
    def MoveUp(self):
        self.dYVel -= 1
    def MoveDown(self):
        self.dYVel += 1
    def KeyUp(self):
        self.bOnKey = False

class MainGame():
    def __init__(self):
        pygame.init()
        self.setTitle = pygame.display.set_caption('Pong')
        self.screen = pygame.display.set_mode(resolution)
        self.clock = pygame.time.Clock()
        self.Ball = Ball()
        self.PaddleA = Paddle(10) # W and A
        self.PaddleB = Paddle(resolution[0] - 40) # keyup and keydown

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[K_SPACE]:
                    self.Ball.start()
                elif keys[K_ESCAPE]:
                    sys.exit()
                elif keys[K_w]:
                    self.PaddleA.MoveUp()
                elif keys[K_s]:
                    self.PaddleA.MoveDown()
                elif keys[K_UP]:
                    self.PaddleB.MoveUp()
                elif keys[K_DOWN]:
                    self.PaddleB.MoveDown()

    def run(self):
        while True:
            self.handleEvents()
            self.Ball.update()
            self.PaddleA.update()
            self.PaddleB.update()

            self.screen.fill(c_black)

            self.Ball.draw(self.screen)
            self.PaddleA.draw(self.screen)
            self.PaddleB.draw(self.screen)

            self.clock.tick(60) #regulate FPS
            pygame.display.flip()

if __name__ == "__main__":
    MainGame().run()
