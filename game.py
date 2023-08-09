import pygame
from models.settings import Settings
from models.helpers import Board

pygame.init()

pygame.display.set_caption('🐍🐍 Welcome to the Pythonic Chess 🐍🐍')

# can pass in any colours, to set theme up easier
board = Board("white", "black", "pink", "black")

# Main game loop
run = True
while run:
    board.initialise()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
