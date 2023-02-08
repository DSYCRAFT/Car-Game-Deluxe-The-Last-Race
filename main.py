import pygame
from pygame.locals import *
pygame.init()
import random

# Windows dimention
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Road parameters
ROAD_W = 500
ROADMARK_W = 10

# Lanes limitation
RIGHT_LANE = SCREEN_WIDTH/2 + ROAD_W/4
LEFT_LANE = SCREEN_WIDTH/2 - ROAD_W/4

# Set windows size
screen = pygame.display.set_mode( SIZE )

# Title
pygame.display.set_caption("Car Game Deluxe: The Last Race")

# Background color
screen.fill((49, 185, 52))

# Icon
ICON = pygame.image.load("icon.png")
pygame.display.set_icon(ICON)

# Enemy speed
speed = 1

# Came over font
go_font = pygame.font.Font("font.ttf", 64)
go_x = 200
go_y = 300

# Game over funcion
def game_over(x, y):
    go_text = go_font.render("GAME OVER", True, (125, 125, 125))
    screen.blit( go_text, (x, y))

# Update changes
pygame.display.update()

# Load car player image
car_player = pygame.image.load("player.png")
car_player_loc = car_player.get_rect()
car_player_loc.center = RIGHT_LANE, SCREEN_HEIGHT*0.9

# Load bad car player image
bad_car = pygame.image.load("bad.png")
bad_car_loc = bad_car.get_rect()
bad_car_loc.center = LEFT_LANE, SCREEN_HEIGHT/6

# Game loop
running = True
counter = 0
while running:
    
    counter += 1

    # Increase game difficulty
    if counter == 5000:
        speed += 0.15
        counter = 0
        print("LEVEL UP!", speed)

   # Enemy car movement
    bad_car_loc[1] += 1

    # Enemy car appears again
    if bad_car_loc.y > SCREEN_HEIGHT:
        bad_car_loc.y = -200

        # Enemy car appears again randomly
        if random.randint(0, 1) == 0:
            bad_car_loc.center = RIGHT_LANE, -200

        else:
             bad_car_loc.center = LEFT_LANE, -200

    # End game logic
    if car_player_loc[0] == bad_car_loc[0] and bad_car_loc[1] > car_player_loc[1] - 128:
        game_over(go_x, go_y)
        #break

  
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

            if event.key in [K_a, K_LEFT]:
                car_player_loc = car_player_loc.move(-ROAD_W/2, 0)

            if event.key in [K_d, K_RIGHT]:
                car_player_loc = car_player_loc.move(+ROAD_W/2, 0)

             
    # Draw the road
    pygame.draw.rect(screen, (31, 31, 31), (SCREEN_WIDTH/2 - ROAD_W/2, 0, ROAD_W, SCREEN_HEIGHT))

    # Draw the roadmark
    pygame.draw.rect(screen, (255, 240, 60), (SCREEN_WIDTH/2 - ROADMARK_W/2, 0, ROADMARK_W, SCREEN_HEIGHT))

    # Draw the white lines
    pygame.draw.rect(screen, (255, 255, 255), (SCREEN_WIDTH/2 - ROAD_W/2 + ROADMARK_W * 2, 0, ROADMARK_W, SCREEN_HEIGHT))

    # Draw the white lines 2
    pygame.draw.rect(screen, (255, 255, 255), (SCREEN_WIDTH/2 + ROAD_W/2 - ROADMARK_W * 3, 0, ROADMARK_W, SCREEN_HEIGHT))

    # Draw player
    screen.blit(car_player, car_player_loc)

    # Draw player
    screen.blit(bad_car, bad_car_loc)

    # Update the app
    pygame.display.update()