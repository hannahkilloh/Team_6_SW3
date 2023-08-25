import pygame
import sys
from models.settings import Settings
from models.buttons import Button, ImageOnScreen
import game
import json


def set_background():
    BG = pygame.image.load("assets/images/menu_background.png").convert()
    BG.set_alpha(400)
    settings.win.blit(BG, (0, 0))


game_logo = ImageOnScreen(
    image=pygame.image.load("assets/images/chess_battle_logo_MAIN.png").convert_alpha(), pos=(500, 150))

if __name__ == '__main__':
    pygame.init()

    settings = Settings()
    pygame.display.set_caption("Chess Battle")
    set_background()

# Winning screen to be displayed at the end of game with options to go to main menu, play a new game/
    # or go to games history
    def winning_screen():
        while True:
            set_background()

            menu_mouse_pos = pygame.mouse.get_pos()

            new_game_button = Button(image=pygame.image.load("assets/images/blank_button_long.png").convert_alpha(),
                                     pos=(500, 350), text_input="New Game", font=settings.get_font(),
                                     base_color="blue",
                                     hovering_color='#7BFCFC', settings=settings)
            history_button = Button(image=pygame.image.load("assets/images/blank_button_long.png").convert_alpha(),
                                    pos=(500, 500), text_input="Games History", font=settings.get_font(),
                                    base_color="blue", hovering_color='#7BFCFC', settings=settings)
            quit_button = Button(image=pygame.image.load("assets/images/blank_button_long.png").convert_alpha(),
                                 pos=(500, 650), text_input="Quit", font=settings.get_font(), base_color="blue",
                                 hovering_color='#7BFCFC', settings=settings)
            game_logo.update(settings.win)

            for button in [new_game_button, history_button, quit_button]:
                button.change_color(menu_mouse_pos)
                button.update(settings.win)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if new_game_button.check_for_input(menu_mouse_pos):
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


    def history():
        while True:
            set_background()

            history_mouse_pos = pygame.mouse.get_pos()

            game_logo.update(settings.win)

            history_back = Button(image=pygame.image.load("assets/images/very_short_button.png").convert_alpha(),
                                  pos=(500, 825), text_input="BACK", font=settings.get_font(),
                                  base_color="blue", hovering_color="#7BFCFC", settings=settings)

            history_back.change_color(history_mouse_pos)
            history_back.update(settings.win)

            history_box_image = ImageOnScreen(
                image=pygame.image.load("assets/images/chess_history_table.png").convert_alpha(), pos=(500, 525))
            history_box_image.update(settings.win)

            # Load game history data from moves.json file
            with open("moves.json", "r") as json_file:
                game_history_data = json.load(json_file)

            # Initial font and position settings for json file entries
            font = pygame.font.Font('assets/fonts/JetBrainsMono-Bold.ttf', 20)
            y_position = 455  # y axis

            # Display only the 4 most recent games in on the Games history screen
            num_entries_to_display = 4
            start_index = max(len(game_history_data) - num_entries_to_display, 0)

            entries = []
            i = 0
            for key, value in game_history_data.items():
                if i >= start_index:
                    entries.append((key, value))
                i += 1

            entries.reverse()
            for entry in entries:
                # draw timestamp
                history_text = font.render(entry[0], True, "blue")
                history_rect = history_text.get_rect(center=(250, y_position))
                settings.win.blit(history_text, history_rect)

                # draw white moves
                white_string = ""
                for move in entry[1]["white"]:
                    pass

                white_moves = font.render(white_string, True, "blue")
                white_rect = white_moves.get_rect(center=(350, y_position))
                settings.win.blit(white_moves, white_rect)

                # draw black moves
                black_string = ""
                for move in entry[1]["black"]:
                    pass

                black_moves = font.render(black_string, True, "blue")
                black_rect = black_moves.get_rect(center=(350, y_position))
                settings.win.blit(black_moves, black_rect)

                y_position += 70

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
