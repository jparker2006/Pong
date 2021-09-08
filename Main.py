import pygame, random, sys
from pygame.locals import *
pygame.init()

resolution = (800,600)
# colors
c_white = (255, 255, 255)
c_black = (0, 0, 0)
c_maroon = (176, 48, 96)
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

class MainGame():
    def __init__(self):
        pygame.init()
        self.setTitle = pygame.display.set_caption('Pong')
        self.screen = pygame.display.set_mode(resolution)
        self.clock = pygame.time.Clock()
        self.Ball = Ball()

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[K_SPACE]:
                    self.Ball.start()

    def run(self):
        while True:
            self.handleEvents()
            self.Ball.update()

            self.screen.fill(c_black)

            self.Ball.draw(self.screen)

            self.clock.tick(60) #regulate FPS
            pygame.display.flip()

if __name__ == "__main__":
    MainGame().run()
