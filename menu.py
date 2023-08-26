import pygame
import sys
from models.settings import Settings
from models.buttons import Button, ImageOnScreen
from models.helpers import get_file_path_from_root
import game
import json

pygame.init()
settings = Settings()
pygame.display.set_caption("Chess Battle!")


def set_background():
    BG = pygame.image.load(get_file_path_from_root("assets/images/menu_background.png")).convert()
    BG.set_alpha(400)
    settings.win.blit(BG, (0, 0))


set_background()

game_logo = ImageOnScreen(
    image=pygame.image.load(get_file_path_from_root("assets/images/chess_battle_logo_MAIN.png")).convert_alpha(),
    pos=(500, 150))

winning_bubble = ImageOnScreen(
    image=pygame.image.load(get_file_path_from_root("assets/images/chess_bot_and_speechbubble.png")).convert_alpha(),
    pos=(500, 500))


# Winning screen to be displayed at the end of game with options to go to main menu, play a new game/
# or go to games history
def winning_screen(winner):
    while True:
        set_background()

        menu_mouse_pos = pygame.mouse.get_pos()

        new_game_button = Button(
            image=pygame.image.load(get_file_path_from_root("assets/images/very_short_button.png")).convert_alpha(),
            pos=(200, 800), text_input="Replay", font=settings.get_font(),
            base_color="blue",
            hovering_color='#7BFCFC', settings=settings)
        main_menu_button = Button(
            image=pygame.image.load(get_file_path_from_root("assets/images/very_short_button.png")).convert_alpha(),
            pos=(500, 800), text_input="Menu", font=settings.get_font(),
            base_color="blue", hovering_color='#7BFCFC', settings=settings)
        quit_button = Button(
            image=pygame.image.load(get_file_path_from_root("assets/images/very_short_button.png")).convert_alpha(),
            pos=(800, 800), text_input="Quit", font=settings.get_font(), base_color="blue",
            hovering_color='#7BFCFC', settings=settings)
        game_logo.update(settings.win)

        winning_bubble.update(settings.win)

        font = pygame.font.Font('assets/fonts/JetBrainsMono-Bold.ttf', 40)
        winner_font = font.render(winner + " Wins!", True, "blue")
        winner_rect = winner_font.get_rect(center=(680, 470))
        settings.win.blit(winner_font, winner_rect)

        for button in [new_game_button, main_menu_button, quit_button]:
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
                if main_menu_button.check_for_input(menu_mouse_pos):
                    main_menu()
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

        # Initial font and position settings for json file entries
        font = pygame.font.Font('assets/fonts/JetBrainsMono-Bold.ttf', 20)
        font_size25 = pygame.font.Font('assets/fonts/JetBrainsMono-Bold.ttf', 25)

        # game_logo.update(settings.win)

        history_back = Button(
            image=pygame.image.load(get_file_path_from_root("assets/images/games_history_back_button.png")).convert_alpha(),
            pos=(500, 850), text_input="BACK", font=font_size25,
            base_color="blue", hovering_color="#7BFCFC", settings=settings)

        history_back.change_color(history_mouse_pos)
        history_back.update(settings.win)

        history_box_image = ImageOnScreen(
            image=pygame.image.load(get_file_path_from_root("assets/images/games_history_top_box.png")).convert_alpha(),
            pos=(500, 190))
        history_box_image.update(settings.win)

        history_box_image_empty = ImageOnScreen(
            image=pygame.image.load(
                get_file_path_from_root("assets/images/games_history_chess_game_notation_box.png")).convert_alpha(), pos=(500, 580))
        history_box_image_empty.update(settings.win)

        # Load game history data from moves.json file
        with open("moves.json", "r") as json_file:
            game_history_data = json.load(json_file)

        # Display only the 4 most recent games in on the Games history screen
        num_entries_to_display = 4
        start_index = max(len(game_history_data) - num_entries_to_display, 0)

        entries = []
        buttons = []
        i = len(game_history_data) - 1  # Start at the end of the index to show most recent game first
        button_index = 0
        for key, value in reversed(game_history_data.items()):
            if i >= start_index:
                entries.append((key, value))
                buttons.append(
                    Button(image=pygame.image.load(
                        get_file_path_from_root("assets/images/chess_history_button.png")).convert_alpha(),
                           pos=(500, 120 + (button_index * 60)), text_input=key, font=font,
                           base_color="blue", hovering_color="#7BFCFC", settings=settings, internal_id=button_index))
                button_index += 1
            i -= 1

        for b in buttons:
            b.update(settings.win)

        # draw moves
        if settings.history_being_shown > -1:
            lines = []
            move_string = ""
            for m in entries[settings.history_being_shown][1]:
                move_string += ">".join(m)
                move_string += ","
                if len(move_string) > 50:
                    lines.append(move_string)
                    move_string = ""
            lines.append(move_string)

            y_pos = 0
            for line in lines:
                moves = font.render(line, True, "blue")
                moves_rect = moves.get_rect(center=(500, 450 + y_pos))
                settings.win.blit(moves, moves_rect)
                y_pos += 30

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if history_back.check_for_input(history_mouse_pos):
                    settings.win.fill('black')
                    main_menu()
                for b in buttons:
                    if b.check_for_input(history_mouse_pos):
                        settings.history_being_shown = b.internal_id

        scaled_win = pygame.transform.smoothscale(settings.win, settings.screen_.get_size())
        settings.screen_.blit(scaled_win, (0, 0))
        pygame.display.flip()


def main_menu():
    while True:
        set_background()

        menu_mouse_pos = pygame.mouse.get_pos()

        play_button = Button(
            image=pygame.image.load(get_file_path_from_root("assets/images/blank_button_long.png")).convert_alpha(),
            pos=(500, 350), text_input="Play Chess", font=settings.get_font(), base_color="blue",
            hovering_color='#7BFCFC', settings=settings)
        history_button = Button(
            image=pygame.image.load(get_file_path_from_root("assets/images/blank_button_long.png")).convert_alpha(),
            pos=(500, 500), text_input="Games History", font=settings.get_font(),
            base_color="blue", hovering_color='#7BFCFC', settings=settings)
        quit_button = Button(
            image=pygame.image.load(get_file_path_from_root("assets/images/blank_button_long.png")).convert_alpha(),
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


if __name__ == '__main__':
    main_menu()
