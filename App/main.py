import pygame #It helps to crate graphics
import numpy as np # It helps to make complex calculation with python
import sys # It's usefull to control part of opertaive system

# starting pygame
pygame.init()

# Estas variables definirán el tamaño de la pantalla
height = 700
width = 700

# Creating my screen
screen = pygame.display.set_mode((height,width))

running = True

while running:
    
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    num_cells_x = 100
    num_cells_y = 100
    # Drawing the board.
    for y in range(0, num_cells_y):
        for x in range(0, num_cells_x):
            
            poly = []
            
    # refreshing the screen
    pygame.display.flip()

pygame.quit()