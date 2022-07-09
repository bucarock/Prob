import pygame
import random
import time

t = time.time()
pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

dis = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Snake")

game_over = False
snake_block = 10
snake_speed = 30
font_style = pygame.font.SysFont(None, 30)
x1 = 300
y1 = 400

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

foodx = round(random.randrange(0, 800 - snake_block))
foody = round(random.randrange(0, 500 - snake_block))
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10

    if x1 >= 800 or x1 < 0 or y1 >= 600 or y1 < 0:
        game_over = True


    x1 += x1_change
    y1 += y1_change
    dis.fill(white)

    pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
    pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
    pygame.display.update()

    if x1 == foodx and y1 == foody:
        print("Вкусно)")




    pygame.draw.rect(dis, blue, [x1, y1, 10, 10])
    pygame.display.update()

    clock.tick(30)

pygame = quit()
quit()
