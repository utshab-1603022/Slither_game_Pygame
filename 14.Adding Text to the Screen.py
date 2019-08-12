import pygame
import time

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Slither')

gameExit = False

x = display_width/2
y = display_height/2
x_change = 0
y_change = 0

clock = pygame.time.Clock()

block_size = 10
FPS = 30

#new
font = pygame.font.SysFont(None, 25)
def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2,display_height/2])

while not gameExit:
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
        gameExit = True
                
    x += x_change
    y += y_change
            
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [x,y,block_size,100])
    pygame.draw.rect(gameDisplay, red, [x,y,block_size,block_size])
    pygame.display.update()
    
    clock.tick(FPS)    #fps is 100. Instead of changing this, x,y change is recommended

#new
message_to_screen("You Lose",red)
pygame.display.update()
time.sleep(2)

pygame.quit()
quit()
