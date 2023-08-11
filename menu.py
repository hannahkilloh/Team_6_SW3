import pygame
import sys
from models.buttons import Button

pygame.init()

screen = pygame.display.set_mode((1000, 900))
pygame.display.set_caption("Welcome Menu")

BG = pygame.image.load("assets/images/b_king.png").convert()
BG.set_alpha(128)
screen.blit(BG, (-550, 0))
BG2 = pygame.image.load("assets/images/b_queen.png").convert()
BG2.set_alpha(128)
screen.blit(BG2, (450, 0))


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font('freesansbold.ttf', 40)


def play():
    while True:
        play_mouse_pos = pygame.mouse.get_pos()

        screen.fill("black")

        play_text = get_font(45).render(
            "This is the PLAY screen.", True, "White")
        play_rect = play_text.get_rect(center=(500, 450))
        screen.blit(play_text, play_rect)

        play_back = Button(image=None, pos=(500, 450),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        play_back.change_color(play_mouse_pos)
        play_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_back.check_for_input(play_mouse_pos):
                    main_menu()

        pygame.display.update()


def options():
    while True:
        options_mouse_pos = pygame.mouse.get_pos()

        screen.fill("white")

        options_text = get_font(45).render(
            "This is the OPTIONS screen.", True, "Black")
        options_rect = options_text.get_rect(center=(500, 350))
        screen.blit(options_text, options_rect)

        options_back = Button(image=None, pos=(500, 450),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="black")

        options_back.change_color(options_mouse_pos)
        options_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if options_back.check_for_input(options_mouse_pos):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        screen.copy()

        menu_mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(100).render("", True, "light pink")
        menu_rect = menu_text.get_rect(center=(500, 450))

        play_button = Button(image=pygame.image.load("assets/images/play_rect.png"), pos=(500, 250),
                             text_input="PLAY CHESS", font=get_font(75), base_color="light pink", hovering_color="White")
        options_button = Button(image=pygame.image.load("assets/images/play_rect.png"), pos=(500, 400),
                                text_input="GAMES HISTORY", font=get_font(75), base_color="light pink", hovering_color="White")
        quit_button = Button(image=pygame.image.load("assets/images/play_rect.png"), pos=(500, 550),
                             text_input="QUIT", font=get_font(75), base_color="light pink", hovering_color="White")

        screen.blit(menu_text, menu_rect)

        for button in [play_button, options_button, quit_button]:
            button.change_color(menu_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.check_for_input(menu_mouse_pos):
                    play()
                if options_button.check_for_input(menu_mouse_pos):
                    options()
                if quit_button.check_for_input(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
