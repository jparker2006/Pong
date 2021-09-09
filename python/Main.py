import pygame
import random
import sys
from pygame.locals import *
from Paddle import Paddle
from Ball import Ball
pygame.init()

resolution = (800,600)
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

        self.rect2 = pygame.Rect(100, 100, 100, 110)

    def handleEvents(self):
        for event in pygame.event.get():
            if QUIT == event.type:
                sys.exit()
            elif pygame.KEYDOWN == event.type:
                keys = pygame.key.get_pressed()
                if keys[K_SPACE]:
                    self.Ball.start()
                elif keys[K_ESCAPE]:
                    sys.exit()
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

            # basic collision detection example
            point = pygame.mouse.get_pos()
            collide = self.rect2.collidepoint(point)
            color = (255, 0, 0) if collide else (255, 255, 255)
            pygame.draw.rect(self.screen, color, self.rect2)

            self.Ball.draw(self.screen)
            self.PaddleA.draw(self.screen)
            self.PaddleB.draw(self.screen)

            self.clock.tick(60) # regulate FPS
            pygame.display.flip()

if "__main__" == __name__:
    MainGame().run()
