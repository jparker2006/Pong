import pygame, random
from pygame.locals import *
pygame.init()

resolution = (500,500)
# colors
c_white = (255, 255, 255)
c_black = (0, 0, 0)
c_maroon = (176, 48, 96, 1)
# colors end

class Dragon:
    # xPos, yPos, xVelo, yVelo, ballsize (constructor)
    def __init__(self, xPos =  resolution[0] / 2, yPos = resolution[1] / 2, xVel = 0, yVel = 4.5, rad = 30):
        self.nXPos = xPos
        self.nYPos = yPos
        self.dXVel = xVel
        self.dYVel = yVel
        self.nRadius = rad
        self.type = "dragon"
    def draw(self, surface):
        pygame.draw.circle(surface, c_black, (self.nXPos, self.nYPos), self.nRadius)
    def update(self):
        self.nXPos += self.dXVel
        self.nYPos += self.dYVel
        if (self.nXPos <= 30 or self.nXPos >= resolution[0] - 30): #bounce off walls
            self.dXVel *= -1
        if (self.nYPos <= 30 or self.nYPos >= resolution[1] - 30):
            self.dYVel *= -1
    def jump(self):
        self.dYVel *= -1

class MainGame():
    def __init__(self):
        pygame.init()
        self.setTitle = pygame.display.set_caption('Dragon Jumper')
        self.screen = pygame.display.set_mode(resolution)
        self.clock = pygame.time.Clock()
        self.Dragon = Dragon()

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.Dragon.jump()
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[K_UP] or keys[K_SPACE] or keys[K_w]:
                    self.Dragon.jump()
                elif keys[K_ESCAPE]:
                    pygame.quit()

    def run(self):
        while True:
            self.handleEvents()
            self.Dragon.update()

            self.screen.fill(c_maroon)

            self.Dragon.draw(self.screen)

            self.clock.tick(60) #regulate FPS
            pygame.display.flip()


MainGame().run()



#add an image template

#tom = pygame.image.load('images/tom_standing.png').convert_alpha()
#tomX = 10
#tomY = 40
#WINDOW.blit(tom, (tomX, tomY))
