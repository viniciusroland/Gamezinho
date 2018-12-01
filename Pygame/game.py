import pygame
import random

pygame.init()

rock = pygame.image.load('Game/rock_reduzida2.png')

walkRight = [pygame.image.load('Game/R1.png'), pygame.image.load('Game/R2.png'), pygame.image.load('Game/R3.png'), pygame.image.load('Game/R4.png'), pygame.image.load('Game/R5.png'), pygame.image.load('Game/R6.png'), pygame.image.load('Game/R7.png'), pygame.image.load('Game/R8.png'), pygame.image.load('Game/R9.png')]

walkLeft = [pygame.image.load('Game/L1.png'), pygame.image.load('Game/L2.png'), pygame.image.load('Game/L3.png'), pygame.image.load('Game/L4.png'), pygame.image.load('Game/L5.png'), pygame.image.load('Game/L6.png'), pygame.image.load('Game/L7.png'), pygame.image.load('Game/L8.png'), pygame.image.load('Game/L9.png')]

bg = pygame.image.load('Game/bg.jpg') 

char = pygame.image.load('Game/standing.png')

w_win = 800
h_win = 450
win = pygame.display.set_mode((w_win, h_win))

pygame.display.set_caption("Gamezinho")
clock = pygame.time.Clock()

isJump = False

x = 50
y = 360
w = 64
h = 64
vel = 15
left = False
right = False
walkCount = 0
jumpCount = 10
run = True
x_rock = 700
y_rock = 380
vel_rock = 10
pontuacao = 0



def calcula_pontos():
    global pontuacao
    if(x == x_rock and y < y_rock):
        pontuacao += 1
    
    print('Minha pontuacao: %s' % pontuacao)



def draw():
    global vel_rock
    global x_rock
    if x_rock < 0:
        vel_rock = random.randint(10, 40)
        x_rock = w_win
    x_rock -= vel_rock
    global walkCount
    win.blit(bg, (0, 0))
    win.blit(rock, (x_rock, y_rock))
    
    
    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//3], (x, y))
        walkCount += 1

    elif right:
        win.blit(walkRight[walkCount//3], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))

    pygame.display.update()

while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        left = True
        right = False
        x = x - vel
    elif keys[pygame.K_RIGHT]:
        left = False
        right = True
        x = x + vel
    else:
        left = False
        right = False
        walkCount = 0

    if not(isJump):

        if keys[pygame.K_SPACE]:
            right = False
            left = False
            walkCount = 0
            isJump = True

    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    if(x > w_win):
        x = 0
    if(x < 0):
        x = w_win

    if(y > h_win):
        y = 0
    if(y < 0):
        y = h_win
    
    draw()    
    calcula_pontos()

pygame.quit()

