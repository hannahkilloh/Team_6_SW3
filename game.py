import pygame
from models.settings import Settings
from models.helpers import Board, BoardSettings

pygame.init()
pygame.font.init()
pygame.display.set_caption('🐍🐍 Welcome to the Pythonic Chess 🐍🐍')

# can pass in any colours, to set theme up easier
board_settings = BoardSettings("light grey", "dark grey", "pink", "black", 'freesansbold.ttf')
board = Board(board_settings)

game_state = 'start_menu'
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
