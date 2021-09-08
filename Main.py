import pygame, sys, random
from pygame.locals import *
pygame.init()

resolution = (500,500)
white = (255, 255, 255)
black = (0, 0, 0)

class Ball:
    # xPos, yPos, xVelo, yVelo, ballsize (constructor)
    def __init__(self, xPos =  resolution[0] / 2, yPos = resolution[1] / 2, xVel = 0, yVel = 3, rad = 50):
        self.x = xPos
        self.y = yPos
        self.dx = xVel
        self.dy = yVel
        self.radius = rad
        self.type = "ball"
    def draw(self, surface):
        pygame.draw.circle(surface, black, (self.x, self.y), self.radius)
    def update(self):
        self.x += self.dx
        self.y += self.dy
        if (self.x <= 0 or self.x >= resolution[0]): #bounce off walls
            self.dx *= -1
        if (self.y <= 50 or self.y >= resolution[1] - 50):
            self.dy *= -1

class MainGame():
    def __init__(self):
        pygame.init()
        self.setTitle = pygame.display.set_caption('Dragon Jumper')
        self.screen = pygame.display.set_mode(resolution)
        self.clock = pygame.time.Clock()
        self.gameObjects = []
        self.gameObjects.append(Ball())

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif (event.type == pygame.KEYDOWN) or (event.type == pygame.MOUSEBUTTONDOWN):
                print("PRESS")

    def run(self):
        while True:
            self.handleEvents()

            for gameObj in self.gameObjects:
                gameObj.update()

            self.screen.fill(white)

            for gameObj in self.gameObjects:
                gameObj.draw(self.screen)

            self.clock.tick(60) #regulate FPS
            pygame.display.flip()

MainGame().run()



#add an image template

#tom = pygame.image.load('images/tom_standing.png').convert_alpha()
#tomX = 10
#tomY = 40
#WINDOW.blit(tom, (tomX, tomY))
