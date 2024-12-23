import pygame #It helps to crate graphics
import numpy as np # It helps to make complex calculation with python
import sys # It's usefull to control part of opertaive system

# starting pygame
pygame.init()

# Defining the screen size
height = 700
width = 700

num_cells_x = 100
num_cells_y = 100

# Creating my screen
screen = pygame.display.set_mode((width,height))

running = True

screen_color = (69, 77, 89)

while running:
    
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(screen_color)

    # Drawing the board.
    for y in range(0, num_cells_y):
        for x in range(0, num_cells_x):
            
            poly = []
            
    # refreshing the screen
    pygame.display.flip()

pygame.quit()