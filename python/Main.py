import pygame, random, sys
from pygame.locals import *
from Paddle import Paddle
from Ball import Ball
pygame.init()

resolution = (600,400)
c_pyYellow = (255,211,67)
c_green = (8,255,8)
c_red = (255, 6, 8)

class MainGame():
    def __init__(self):
        self.setTitle = pygame.display.set_caption('Pong') # set window title
        self.screen = pygame.display.set_mode(resolution) # set window resolution
        self.clock = pygame.time.Clock() # set fps clock

        self.Ball = Ball()
        self.PaddleA = Paddle(10) # W and A
        self.PaddleB = Paddle(resolution[0] - 30) # keyup and keydown

        self.font = pygame.font.SysFont('cambriacambriamath', 48)
        self.scoreboard = self.font.render("0 | 0", True, c_red)
        self.scoreFrame = self.scoreboard.get_rect()
        self.scoreFrame.center = (resolution[0] // 2, 30)

    def handleEvents(self):
        for event in pygame.event.get():
            if QUIT == event.type:
                sys.exit()
            elif pygame.KEYDOWN == event.type:
                keys = pygame.key.get_pressed()
                if keys[K_w]:
                    self.PaddleA.Move(True)
                elif keys[K_s]:
                    self.PaddleA.Move(False)
                elif keys[K_UP]:
                    self.PaddleB.Move(True)
                elif keys[K_DOWN]:
                    self.PaddleB.Move(False)

    def run(self):
        bGameStarted = True
        while True:
            self.handleEvents()
            self.screen.fill(c_green)

            self.Ball.draw(self.screen)
            self.PaddleA.draw(self.screen)
            self.PaddleB.draw(self.screen)

            self.Ball.update()

            # collision detection
            if (self.Ball.GetXPos() >= 40 and self.Ball.GetXPos() <= 47): # have to give the pixels room for error
                if (self.Ball.GetYPos() >= self.PaddleA.GetYPos() - 25 and self.Ball.GetYPos() <= self.PaddleA.GetYPos() + 115):
                    self.Ball.HitPaddle()
            if (self.Ball.GetXPos() >= 550 and self.Ball.GetXPos() <= 557):
                if (self.Ball.GetYPos() >= self.PaddleB.GetYPos() - 25 and self.Ball.GetYPos() <= self.PaddleB.GetYPos() + 115):
                    self.Ball.HitPaddle()

            self.scoreboard = self.font.render((str)(self.Ball.nPaddleAScore) + " | " + (str)(self.Ball.nPaddleBScore), True, c_red)
            self.screen.blit(self.scoreboard, self.scoreFrame)

            self.clock.tick(60) # regulate FPS
            pygame.display.flip()

if "__main__" == __name__:
    MainGame().run()
