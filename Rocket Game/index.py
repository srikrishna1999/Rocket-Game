import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("monitor")
icon = pygame.image.load("code.png")
pygame.display.set_icon(icon)
playerImg = pygame.image.load("setup.png")
playerX = 370
playerY = 480
bulletImg = pygame.image.load("bullet.png")
ufoImg = pygame.image.load("ufo.png")
ufoX = random.randint(25,725)
ufoY = 70
background = pygame.image.load("background.png")
bullet_state = "ready"
font = pygame.font.Font("freesansbold.ttf", 32)
def ufo(x, y):
    screen.blit(ufoImg,(x,y))

def player(x, y):
    screen.blit(playerImg, (x, y))


def bullet(x, y):
    global bullet_state
    bullet_state = "shooting"
    screen.blit(bulletImg, (x, y))
points = 0
def score(x, y):
    score = font.render("Score : " + str(points),True,(255,255,255))
    screen.blit(score, (x, y))

bulX = 0
bulY = 0
running = True
r = 10
g = 200
b = 155
change = 0
ans = 0
c = 1
hit = False
while running:
    screen.fill((r, g, b))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change = -2
            if event.key == pygame.K_RIGHT:
                change = 2
            if event.key == pygame.K_SPACE:
                bulX = playerX + 15
                bulY = playerY + 15
                hit = False
                bullet(bulX,bulY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                change = 0
    #bulletX += change
    if bullet_state == "shooting":
        bullet(bulX,bulY)
        bulY = bulY - 5
    if c<5.0:
        c = c + 0.0005

    if playerX < 25:
        playerX = 25
    elif playerX > 710:
        playerX = 710
    if bulX > ufoX and bulX < ufoX + 40:
        if bulY > ufoY and bulY < ufoY + 20:
            if hit == False:
                points = points + 500
                hit = True
                print(points)
            bullet_state = "ready"
    score(20,20)
    if ufoX<725 and ans == 0:
        ufoX = ufoX + c
    else:
        ans = 1
    if ufoX>25 and ans == 1:
        ufoX = ufoX - c
    else:
        ans = 0
    ufo(ufoX,ufoY)
    playerX += change
    player(playerX, playerY)
    pygame.display.update()
