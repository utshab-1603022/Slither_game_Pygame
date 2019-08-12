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

#attaching snakehead
img = pygame.image.load('SnakeHead.png')


clock = pygame.time.Clock()

block_size = 20
FPS = 10
direction = "right"

smallfont = pygame.font.SysFont("comicsansms", 25)  #changes
mediumfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

def snake(block_size, snakeList):
    if direction == "right":
        head = pygame.transform.rotate(img, 270)
    if direction == "left":
        head = pygame.transform.rotate(img, 90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img, 180)
        
    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))    #img to head
    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],block_size,block_size])
#centering text
def text_objects(text, color, size):  #changes below
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = mediumfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color, y_displace=0, size = "small"):     #parameter added
    #centering text
    textSurf, textRect = text_objects(msg, color, size) #parameter added
    textRect.center = (display_width / 2), (display_height /2) + y_displace
    gameDisplay.blit(textSurf, textRect)

def gameLoop():
    global direction
    gameExit = False
    gameOver = False
    
    x = display_width/2
    y = display_height/2
    x_change = 10
    y_change = 0

    snakeList = []  
    snakeLength = 10

    randAppleX = round(random.randrange(0, display_width - block_size))#/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height - block_size))#/10.0)*10.0
    
    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over",
                              red,
                              y_displace = -50,
                              size = "large")
            message_to_screen("Press C to play again or Q to quit",
                              black,
                              50,
                              size = "medium")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:   #makes over/quit if we hit c/q during game
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
                    direction = "left"
                    x_change = -block_size
                    y_change = 0        #avoids diagonal movement
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
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

        if x > randAppleX and x < randAppleX + AppleThickness or x + block_size > randAppleX and x + block_size < randAppleX + AppleThickness:
            #print("x crossover")
            if y > randAppleY and y < randAppleY + AppleThickness:
                #print("x and y crossover")
                randAppleX = round(random.randrange(0, display_width - block_size))#/10.0)*10.0
                randAppleY = round(random.randrange(0, display_height - block_size))#/10.0)*10.0
                snakeLength += 1
            elif y + block_size > randAppleY and y + block_size < randAppleY + AppleThickness:
                #print("x and y crossover")
                randAppleX = round(random.randrange(0, display_width - block_size))#/10.0)*10.0
                randAppleY = round(random.randrange(0, display_height - block_size))#/10.0)*10.0
                snakeLength += 1
            
        clock.tick(FPS)    #fps is 100. Instead of changing this, x,y change is recommended

    pygame.quit()
    quit()

gameLoop()

