import pygame
import time
import random

pygame.init()

# defining colors
green = (45, 168, 21)  # snake
black = (0, 0, 0)  # bachground
red = (255, 0, 0)  # text
orange = (255, 165, 0)  # food
width, height = 600, 400

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Snake Game")

clock = pygame.time.Clock()

snake_size = 10
snake_speed = 15

massage_font = pygame.font.SysFont("futura-bold", 28)
score_font = pygame.font.SysFont("futura-bold", 22)


def print_score(score):
    txt = score_font.render("Score is : " + str(score), True, red)
    game_display.blit(txt, [0, 0])


def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(
            game_display, green, [pixel[0], pixel[1], snake_size, snake_size]
        )


def run_game():
    game_over = False
    game_close = False

    # start position :
    x = width / 2
    y = height / 2

    # default vars:
    x_speed = 0
    y_speed = 0
    snake_pixels = []
    snake_len = 1

    target_x = round(random.randrange(width - snake_size) / 10.0) *10
    target_y = round(random.randrange(height - snake_size) / 10.0) *10
    
    #the game loop:
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_size
                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size
        if x >= width or x < 0 or y <= height or y < 0: #if if got at screen edges
            game_close = True

        #the movement
        x += x_speed    
        y += y_speed  

        game_display.fill(black)
        pygame.draw.rect(game_display, orange, [target_x,target_y, snake_size, snake_size])  

