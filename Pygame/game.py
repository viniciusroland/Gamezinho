import pygame
import random

pygame.init()
w_win = 800
h_win = 450
win = pygame.display.set_mode((w_win, h_win))

pygame.display.set_caption("Gamezinho")
clock = pygame.time.Clock()

bg = pygame.image.load('Game/bg.jpg') 

class Player:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vel = 15
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.isJump = False        
        self.walkRight = [pygame.image.load('Game/R1.png'), pygame.image.load('Game/R2.png'), pygame.image.load('Game/R3.png'), pygame.image.load('Game/R4.png'), pygame.image.load('Game/R5.png'), pygame.image.load('Game/R6.png'), pygame.image.load('Game/R7.png'), pygame.image.load('Game/R8.png'), pygame.image.load('Game/R9.png')]
        
        self.walkLeft = [pygame.image.load('Game/L1.png'), pygame.image.load('Game/L2.png'), pygame.image.load('Game/L3.png'), pygame.image.load('Game/L4.png'), pygame.image.load('Game/L5.png'), pygame.image.load('Game/L6.png'), pygame.image.load('Game/L7.png'), pygame.image.load('Game/L8.png'), pygame.image.load('Game/L9.png')]
    
        self.char = pygame.image.load('Game/standing.png')


    def __str__(self):
        return 'Player1'
    
    def drawPlayer(self):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            win.blit(self.walkLeft[self.walkCount//3] , (self.x, self.y))
            self.walkCount += 1

        elif self.right:
            win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.char, (self.x, self.y))

        pygame.display.update()


    def atualizaPos(self, eixo, direcao):
        if eixo == 'x':
            self.x += self.vel * direcao

        if eixo == 'y':
            self.y += self.vel * direcao


class Rock:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = pygame.image.load('Game/rock_reduzida2.png') 
        self.vel_rock = 10 

    def drawRock(self):
        if self.x < 0:
            self.vel_rock = random.randint(10, 40)
            self.x = w_win
        self.x -= self.vel_rock
        win.blit(bg, (0, 0))
        win.blit(self.img, (self.x, self.y))
    
player = Player(50, 360, 64, 64)
rock = Rock(700, 380)
pontuacao = 0
run = True

def calcula_pontos():
    global pontuacao
    if(player.x == rock.x and player.y < rock.y):
        pontuacao += 1
    
    print('Minha pontuacao: %s' % pontuacao)

while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:

        player.left = True
        player.right = False
        player.atualizaPos('x', -1)
    elif keys[pygame.K_RIGHT]:

        player.left = False
        player.right = True
        player.atualizaPos('x', 1)
    else:

        player.left = False
        player.right = False
        player.walkCount = 0

    if not(player.isJump):

        if keys[pygame.K_SPACE]:
            
            player.right = False
            player.left = False
            player.walkCount = 0
            player.isJump = True
    else:
        if player.jumpCount >= -10:
            neg = 1
            if player.jumpCount < 0:
                neg = -1
            player.y -= (player.jumpCount ** 2) * 0.5 * neg
            player.jumpCount -= 1
        else:
            player.isJump = False
            player.jumpCount = 10

    if(player.x > w_win):
        player.x = 0
    if(player.x < 0):
        player.x = w_win

    if(player.y > h_win):
        player.y = 0
    if(player.y < 0):
        player.y = h_win
    
    player.drawPlayer()    
    rock.drawRock()
    calcula_pontos()

pygame.quit()

