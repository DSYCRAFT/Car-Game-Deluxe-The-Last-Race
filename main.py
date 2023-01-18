import pygame
from pygame.locals import *
pygame.init()

# Windows dimention
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Set windows size
screen = pygame.display.set_mode( SIZE )

# Title
pygame.display.set_caption("Car Game Deluxe: The Last Race")

# Background color
screen.fill((49, 185, 52))

# Icon
ICON = pygame.image.load("sprites/icon.png")
pygame.display.set_icon(ICON)

# Update changes
pygame.display.update()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

