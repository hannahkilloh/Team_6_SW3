import pygame
import sys
from Team_6_SW3.models.settings import Settings
from Team_6_SW3.models.buttons import Button, ImageOnScreen
import game


def set_background():
    BG = pygame.image.load("assets/images/menu_background.png").convert()
    BG.set_alpha(400)
    settings.win.blit(BG, (0, 0))


if __name__ == '__main__':
    pygame.init()

    settings = Settings()
    pygame.display.set_caption("Chess Battle")
    set_background()


    def history():
        while True:
            history_mouse_pos = pygame.mouse.get_pos()

            settings.win.fill("black")

            history_text = settings.get_font().render(
                "This is the history of moves screen.", True, "white")
            history_rect = history_text.get_rect(center=(500, 350))
            settings.win.blit(history_text, history_rect)

            history_back = Button(image=None, pos=(500, 450), text_input="BACK", font=settings.get_font(),
                                  base_color="blue", hovering_color="#7BFCFC", settings=settings)

            history_back.change_color(history_mouse_pos)
            history_back.update(settings.win)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if history_back.check_for_input(history_mouse_pos):
                        settings.win.fill('black')
                        main_menu()

            scaled_win = pygame.transform.smoothscale(settings.win, settings.screen_.get_size())
            settings.screen_.blit(scaled_win, (0, 0))
            pygame.display.flip()


    def main_menu():
        while True:
            set_background()

            menu_mouse_pos = pygame.mouse.get_pos()

            game_logo = ImageOnScreen(image=pygame.image.load("assets/images/game_logo_very_small.png").convert_alpha(),
                                      pos=(500, 100))

            play_button = Button(image=pygame.image.load("assets/images/blank_button_long.png").convert_alpha(),
                                 pos=(500, 350), text_input="Play Chess", font=settings.get_font(), base_color="blue",
                                 hovering_color='#7BFCFC', settings=settings)
            history_button = Button(image=pygame.image.load("assets/images/blank_button_long.png").convert_alpha(),
                                    pos=(500, 500), text_input="Games History", font=settings.get_font(),
                                    base_color="blue", hovering_color='#7BFCFC', settings=settings)
            quit_button = Button(image=pygame.image.load("assets/images/blank_button_long.png").convert_alpha(),
                                 pos=(500, 650), text_input="Quit", font=settings.get_font(), base_color="blue",
                                 hovering_color='#7BFCFC', settings=settings)
            game_logo.update(settings.win)

            for button in [play_button, history_button, quit_button]:
                button.change_color(menu_mouse_pos)
                button.update(settings.win)

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

            scaled_win = pygame.transform.smoothscale(settings.win, settings.screen_.get_size())
            settings.screen_.blit(scaled_win, (0, 0))
            pygame.display.flip()


    main_menu()
