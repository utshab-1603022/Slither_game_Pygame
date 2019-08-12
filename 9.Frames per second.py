import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Slither')

gameExit = False

x = 300
y = 300
x_change = 0
y_change = 0

clock = pygame.time.Clock()


while not gameExit:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -2   #if change is not given, holding the keys doesn't make any work 
            if event.key == pygame.K_RIGHT:
                x_change = 2
            if event.key == pygame.K_UP:
                y_change -= 2
            if event.key == pygame.K_DOWN:
                y_change += 2
    x += x_change
    y += y_change
            
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [x,y,10,100])
    pygame.draw.rect(gameDisplay, red, [x,y,10,10])

    pygame.display.update()

    clock.tick(100)    #fps is 100. Instead of changing this, x,y change is recommended


pygame.quit()
quit()
