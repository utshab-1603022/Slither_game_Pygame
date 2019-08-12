import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Slither')

clock = pygame.time.Clock()

block_size = 20     #new: change from 10 to 20
FPS = 10


font = pygame.font.SysFont(None, 25)

def snake(block_size, snakeList):
    for XnY in snakeList:
        pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],block_size,block_size])

def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2,display_height/2])

def gameLoop():
    gameExit = False
    gameOver = False
    
    x = display_width/2
    y = display_height/2
    x_change = 0
    y_change = 0

    snakeList = []  
    snakeLength = 10

    randAppleX = round(random.randrange(0, display_width - block_size))#/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height - block_size))#/10.0)*10.0
    
    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over, press C to play again or Q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:   #new:makes over/quit if we hit c/q during game
                    gameOver = False
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0        #avoids diagonal movement
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = block_size
                    x_change = 0

        if x>=display_width or x<0 or y>=display_height or y<0:
            #gameExit = True
            gameOver = True
                    
        x += x_change
        y += y_change
                
        gameDisplay.fill(white)
        AppleThickness = 30
        pygame.draw.rect(gameDisplay, red, [randAppleX,randAppleY, AppleThickness, AppleThickness])

        
        snakeHead = []
        snakeHead.append(x)
        snakeHead.append(y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:   
            del snakeList[0]
        for eachSegment in snakeList[:-1]:   #[:-1] means elements upto last
            if eachSegment == snakeHead:
                gaveOver = True
        
        snake(block_size, snakeList) 
        pygame.display.update()
##alt+3 
##        if x >= randAppleX and x <= randAppleX + AppleThickness:
##            if y >= randAppleY and y <= randAppleY + AppleThickness:
##                randAppleX = round(random.randrange(0, display_width - block_size))#/10.0)*10.0
##                randAppleY = round(random.randrange(0, display_height - block_size))#/10.0)*10.0
##                snakeLength += 1
            
        
        clock.tick(FPS)    #fps is 100. Instead of changing this, x,y change is recommended

    pygame.quit()
    quit()

gameLoop()
