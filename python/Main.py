import pygame
import random
import sys
from pygame.locals import *
from Paddle import Paddle
from Ball import Ball
pygame.init()

# weird thing first hit after game start doesnt detect collision

resolution = (600,400)
c_white = (255, 255, 255)
c_black = (0, 0, 0)

class MainGame():
    def __init__(self):
        pygame.init()
        self.setTitle = pygame.display.set_caption('Pong') # set window title
        self.screen = pygame.display.set_mode(resolution) # set window resolution
        self.clock = pygame.time.Clock() # set fps clock

        self.Ball = Ball()
        self.PaddleA = Paddle(10) # W and A
        self.PaddleB = Paddle(resolution[0] - 40) # keyup and keydown

    def handleEvents(self):
        for event in pygame.event.get():
            if QUIT == event.type:
                sys.exit()
            # probably let user on paddle 2 move with mouse
            # improve paddle movement with while timer w counter
            elif pygame.KEYDOWN == event.type:
                keys = pygame.key.get_pressed()
                if keys[K_ESCAPE]:
                    self.PauseGame()
                elif keys[K_w]:
                    self.PaddleA.Move(True)
                elif keys[K_s]:
                    self.PaddleA.Move(False)
                elif keys[K_UP]:
                    self.PaddleB.Move(True)
                elif keys[K_DOWN]:
                    self.PaddleB.Move(False)
                else:
                    print("unknown keystroke")

    def run(self):
        while True:
            self.handleEvents()
            self.Ball.update()

            self.screen.fill(c_black)

            self.Ball.draw(self.screen)
            self.PaddleA.draw(self.screen)
            self.PaddleB.draw(self.screen)

            if (40 == self.Ball.GetXPos()) :
                self.Ball.HitPaddle()
            if (550 == self.Ball.GetXPos()) :
                self.Ball.HitPaddle()

            self.clock.tick(60) # regulate FPS
            pygame.display.flip()

    def PauseGame(self):
        print("paused")
        # write game pausing here

if "__main__" == __name__:
    MainGame().run()
