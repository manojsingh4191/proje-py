import pygame
import time
import random
from pygame.locals import *
SIZE=40
class snake :
    def __init__(self,parent_screen,length):
            self.parent_screen=parent_screen
            self.block= pygame.image. load("adam.jpg").convert()
            self.length=length
            self.x=[40]*length
            self.y=[40]*length
            self.direction='down'
    def draw(self):
        self.parent_screen.fill((210,210,255))
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
        pygame.display.flip()

    def move_up (self):
        self.direction='up'
    def move_down (self):
        self.direction='down'
    def move_right (self):
        self.direction='right'
    def move_left (self):
        self.direction='left'

    def walk(self):
        for i in range(self.length-1,0,-1):
            self.x[i]=self.x[i-1]
            self.y[i]=self.y[i-1]
        if self.direction == 'up':
            self.y[0]-=SIZE
        elif self.direction == 'down':
            self.y[0]+=SIZE
        elif self.direction == 'right':
            self.x[0]+=SIZE
        elif self.direction == 'left':
            self.x[0]-=SIZE
        self.draw()

class Apple:
    def __init__(self,parent_screen):
        self.parent_screen=parent_screen
        self.image= pygame.image.load("manoj.jpg").convert()
        self.x=300
        self.y=100
    def draw(self):
        self.parent_screen.blit(self.image,(self.x,self.y))
        pygame.display.flip()


class Game :
    def __init__(self) :
        pygame.init()
        self.surface=pygame.display.set_mode((1000,600))
        self.snake=snake(self.surface,3)
        self.Apple=Apple(self.surface)
        self.Apple.draw()
        self.snake.draw()
    def play(self):
        self.snake.walk()
        self.Apple.draw()
        
    def run(self):
        running=True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key ==K_ESCAPE:
                        running=False

                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key ==K_DOWN:
                        self.snake.move_down()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                elif event.type==QUIT:
                    running=False
            
            self.play()
            time.sleep(0.11)

if __name__=="__main__":
    game =Game()
    game.run()


    #colour
    # wight=(255,255,255)
    # red=(255,25,3)
    # green=(40,255,68)
    # blue=(40,50,255)

    #screan 
    # surface=pygame.display.set_mode((1000,500))
    # surface.fill((123,44,65))
    # block= pygame.image. load("manoj.jpg").convert()
    # block_x=100
    # block_y=100
    # surface.blit(block,(block_x,block_y))
    # pygame.display.flip()
    
#runear 
    # running=True
    # while running:
    #     for event in pygame.event.get():
    #         if event.type == KEYDOWN:
    #             if event.key ==K_ESCAPE:
    #                 running=False
    #             #key
    #             if event.key == K_UP:
    #                 block_y=block_y-10
    #                 draw_block()
    #             if event.key ==K_DOWN:
    #                 block_y=block_y+10
    #                 draw_block()
    #             if event.key == K_LEFT:
    #                 block_x=block_x-10
    #                 draw_block()
    #             if event.key == K_RIGHT:
    #                 block_x=block_x+10
    #                 draw_block()

    #         elif event.type==QUIT:
    #             running=False
