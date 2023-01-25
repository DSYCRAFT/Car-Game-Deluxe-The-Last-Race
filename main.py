import pygame
from pygame.locals import *
pygame.init()

# Windows dimention
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Road parameters
ROAD_W = 500
ROADMARK_W = 10

# Set windows size
screen = pygame.display.set_mode( SIZE )

# Title
pygame.display.set_caption("Car Game Deluxe: The Last Race")

# Background color
screen.fill((49, 185, 52))

# Icon
ICON = pygame.image.load("icon.png")
pygame.display.set_icon(ICON)

# Draw the road
pygame.draw.rect(screen, (31, 31, 31), (SCREEN_WIDTH/2 - ROAD_W/2, 0, ROAD_W, SCREEN_HEIGHT))

# Draw the roadmark
pygame.draw.rect(screen, (255, 240, 60), (SCREEN_WIDTH/2 - ROADMARK_W/2, 0, ROADMARK_W, SCREEN_HEIGHT))

# Draw the white lines
pygame.draw.rect(screen, (255, 255, 255), (SCREEN_WIDTH/2 - ROAD_W/2 + ROADMARK_W * 2, 0, ROADMARK_W, SCREEN_HEIGHT))

# Draw the white lines 2
pygame.draw.rect(screen, (255, 255, 255), (SCREEN_WIDTH/2 + ROAD_W/2 - ROADMARK_W * 3, 0, ROADMARK_W, SCREEN_HEIGHT))

# Update changes
pygame.display.update()

# Load car player image
car_player = pygame.image.load("player.png")
car_player_loc = car_player.get_rect()
car_player_loc.center = SCREEN_WIDTH/2.9 + ROAD_W/2, SCREEN_HEIGHT*0.9

# Load bad car player image
bad_car = pygame.image.load("bad.png")
bad_car_loc = bad_car.get_rect()
bad_car_loc.center = SCREEN_WIDTH/2.9 + ROAD_W/19, SCREEN_HEIGHT/6

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    # Draw player
    screen.blit(car_player, car_player_loc)

    # Draw player
    screen.blit(bad_car, bad_car_loc)

    # Update the app
    pygame.display.update()