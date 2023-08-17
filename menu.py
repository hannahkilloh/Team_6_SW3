import pygame
import sys
from models.buttons import Button, ImageOnScreen
import game


# if __name__ == '__main__': # need to run main function after this


pygame.init()

screen = pygame.display.set_mode((1000, 900))
pygame.display.set_caption("Chess Battle")

BG = pygame.image.load("assets/images/menu_background.png").convert()
BG.set_alpha(400)
screen.blit(BG, (0, 0))
# BG2 = pygame.image.load("assets/images/background_b_queen.png").convert()
# BG2.set_alpha(128)
# screen.blit(BG2, (450, 0))


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font('assets/fonts/JetBrainsMono-Bold.ttf', 50)  # add size variable to settings file


def history():
    while True:
        history_mouse_pos = pygame.mouse.get_pos()

        screen.fill("black")

        history_text = get_font(45).render(
            "This is the history of moves screen.", True, "Black")
        history_rect = history_text.get_rect(center=(500, 350))
        screen.blit(history_text, history_rect)

        history_back = Button(image=None, pos=(500, 450),
                              text_input="BACK", font=get_font(75), base_color="light pink", hovering_color="white")

        history_back.change_color(history_mouse_pos)
        history_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if history_back.check_for_input(history_mouse_pos):
                    screen.fill('black')
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        screen.copy()

        menu_mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(60).render("", True, "blue")
        menu_rect = menu_text.get_rect(center=(500, 450))

        game_logo = ImageOnScreen(image=pygame.image.load("assets/images/game_logo_very_small.png"), pos=(500, 100))

        play_button = Button(image=pygame.image.load("assets/images/blank_button_long.png"), pos=(500, 350),
                             text_input="Play Chess", font=get_font(75), base_color="blue", hovering_color='#7BFCFC')
        history_button = Button(image=pygame.image.load("assets/images/blank_button_long.png"), pos=(500, 500),
                                text_input="Games History", font=get_font(75), base_color="blue", hovering_color='#7BFCFC')
        quit_button = Button(image=pygame.image.load("assets/images/blank_button_long.png"), pos=(500, 650),
                             text_input="Quit", font=get_font(75), base_color="blue", hovering_color='#7BFCFC')

        screen.blit(menu_text, menu_rect)

        for logo in [game_logo]:
            logo.update(screen)

        for button in [play_button, history_button, quit_button]:
            button.change_color(menu_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.check_for_input(menu_mouse_pos):
                    game.play_game()
                    pygame.quit()
                    sys.exit()
                if history_button.check_for_input(menu_mouse_pos):
                    history()
                if quit_button.check_for_input(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
