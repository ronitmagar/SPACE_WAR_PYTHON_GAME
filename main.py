import pygame
import math
import random
import time

# INITIALIZE THE PYGAME

pygame.init()

screen = pygame.display.set_mode((900, 600))  # creates screen for display game
background_image = pygame.image.load('backimg.jpg')  # background image
pygame.display.set_caption("SPACE_WARRIORS")
icon = pygame.image.load('ufoimg.png')  # loads image in pygame
pygame.display.set_icon(icon)  # sets the icon

# player
playerimg = pygame.image.load('ufoimg.png')
playerX = 418
playerY = 550
change = 0
SCORE = 0
# alien
alien = pygame.image.load('alien.png')
enemX = random.randint(0, 868)
enemY = random.randint(10, 300)
echangeX = 0.5
enemchangeY = 0

# bullet
bullet = pygame.image.load('bullet.png')
bulletX = 418
bulletY = 550
bullet_change = 1
bullet_state = "initial"


def player(x, y):
    screen.blit(playerimg, (x, y))


def alienenemy(ex, ey):
    screen.blit(alien, (ex, ey))


def bulletfire(bx, by):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (bx, by))


def iscollision(enemX, enemY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemX - bulletX, 2) + math.pow(enemY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False


font = pygame.font.Font('freesansbold.ttf', 25)

textX = 370
textY = 10


def show_score(x1, y1, ):
    scoredisplay = font.render("SCORE :" + str(SCORE), True, (255, 0, 0))

    screen.blit(scoredisplay, (x1, y1))


# creating loop for game

running = True

while running:
    screen.fill((0, 0, 0))  # background
    screen.blit(background_image, (0, 0))
    for event in pygame.event.get():  # this will keep looking for all the events happening in pygame window module
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left pressed")
                change = -0.5

            if event.key == pygame.K_RIGHT:
                print("right pressed")
                change = 0.5
            if event.key == pygame.K_SPACE:
                print("space pressed")
                if bullet_state is "initial":
                    bulletX = playerX
                    bulletfire(bulletX, bulletY)

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_SPACE:
                print("key up")
                change = 0

    playerX = playerX + change

    if playerX >= 868:
        playerX = 868

    if playerX <= 0:
        playerX = 0

    enemX = enemX + echangeX

    if enemX <= 0:
        echangeX = 0.5
        enemY = enemY + 20

    if enemX >= 868:
        echangeX = -0.5
        enemY = enemY + 20

    if bulletY <= 0:
        bulletY = 550
        bullet_state = "initial"

    if bullet_state is "fire":
        bulletfire(bulletX, bulletY)
        bulletY -= bullet_change

    collision = iscollision(enemX, enemY, bulletX, bulletY)
    if collision:
        bulletY = 550
        bullet_state = "initial"
        SCORE += 1
        print(SCORE)
        enemX = random.randint(0, 868)
        enemY = random.randint(10, 300)

    player(playerX, playerY)
    alienenemy(enemX, enemY)
    show_score(textX, textY)
    pygame.display.update()  # window needs to keep updating to display the events
